#!/usr/bin/env python3
"""
Generate MCP modules for every Falcon API service collection not already
hand-covered, driven by FalconPy's endpoint metadata.

Noise filtered out:
  - operations already wrapped by hand-crafted modules
  - legacy/superseded collections (detects -> alerts, iocs -> ioc)
  - analytics aggregate_* / Aggregates rollups
  - deprecated lower-version duplicates (keep highest V# per base name in a collection)

Emits:
  - falcon_mcp/modules/gen_<collection>.py        (one module per collection)
  - falcon_mcp/common/api_scopes_generated.py      (op -> scope hints)

Generated tools are generic: expanded query params + a `body` dict for write
bodies, with descriptions taken from the API docs. Read/write/destructive
annotations come from HTTP method + name heuristics (bias: only mark READ when
confident, so nothing mutating leaks into read-only mode).
"""

import importlib
import inspect
import keyword
import pathlib
import pkgutil
import re

import falconpy._endpoint as EP

MODULES_DIR = pathlib.Path(__file__).resolve().parent.parent / "falcon_mcp" / "modules"
COMMON_DIR = pathlib.Path(__file__).resolve().parent.parent / "falcon_mcp" / "common"

# Collections we deliberately skip (legacy/superseded or pure plumbing).
SKIP_COLLECTIONS = {"detects", "iocs", "oauth2"}

# Best-effort console scope labels per collection (error-hint enrichment only).
COLLECTION_SCOPE = {
    "aspm": "ASPM",
    "cspm_registration": "CSPM registration",
    "cloud_policies": "Cloud Security Policies",
    "cloud_security": "Cloud security",
    "cloud_security_assets": "Cloud Security API Assets",
    "cloud_security_detections": "Cloud Security API Detections",
    "cloud_security_compliance": "Cloud Security API Assets",
    "cloud_connect_aws": "AWS accounts",
    "cloud_aws_registration": "Cloud Security AWS Registration",
    "cloud_azure_registration": "Cloud Security Azure Registration",
    "cloud_google_cloud_registration": "Cloud Security Google Cloud Registration",
    "cloud_oci_registration": "Cloud Security OCI Registration",
    "cloud_snapshots": "Snapshot",
    "d4c_registration": "D4C registration",
    "data_protection_configuration": "Data Protection",
    "falcon_container": "Falcon Container Image",
    "container_images": "Falcon Container Image",
    "container_image_compliance": "Cloud Security API Assets",
    "container_vulnerabilities": "Falcon Container Image",
    "container_detections": "Cloud Security API Detections",
    "container_packages": "Falcon Container Image",
    "container_alerts": "Alerts",
    "image_assessment_policies": "Falcon Container Image",
    "admission_control_policies": "Kubernetes Protection",
    "kubernetes_protection": "Kubernetes Protection",
    "kubernetes_container_compliance": "Kubernetes Protection",
    "unidentified_containers": "Kubernetes Protection",
    "drift_indicators": "Falcon Container Image",
    "exposure_management": "Assets",
    "spotlight_vulnerabilities": "Vulnerabilities",
    "spotlight_evaluation_logic": "Vulnerabilities",
    "spotlight_vulnerability_metadata": "Risk Platform - Risk",
    "configuration_assessment": "Configuration Assessment",
    "configuration_assessment_evaluation_logic": "Configuration Assessment",
    "discover": "Assets",
    "intel": "Falcon Intelligence",
    "intelligence_feeds": "Falcon Indicator Graph",
    "intelligence_indicator_graph": "Falcon Indicator Graph",
    "identity_protection": "Identity Protection GraphQL",
    "it_automation": "Falcon for IT",
    "recon": "Monitoring rules (Falcon Intelligence Recon)",
    "saas_security": "Falcon Shield",
    "falcon_complete_dashboard": "Falcon Complete Dashboard",
    "sensor_download": "Sensor Download",
    "sensor_usage": "Sensor Usage",
    "spotlight": "Vulnerabilities",
    "user_management": "User Management",
    "mssp": "Flight Control",
    "ngsiem": "NGSIEM",
    "real_time_response": "Real time response",
    "real_time_response_admin": "Real time response (admin)",
    "real_time_response_audit": "Real time response",
    "hosts": "Hosts",
    "host_group": "Host Groups",
    "host_migration": "Host Migration",
    "certificate_based_exclusions": "Certificate Based Exclusions",
    "ioc": "IOC Management",
    "ioa_exclusions": "IOA Exclusions",
    "ml_exclusions": "Machine Learning Exclusions",
    "quarantine": "Quarantined Files",
    "custom_storage": "Custom Storage",
    "foundry_logscale": "App Logs",
    "faas_execution": "Foundry Function",
    "api_integrations": "API integrations",
    "workflows": "Workflow",
    "correlation_rules": "Correlation Rules",
    "correlation_rules_admin": "Correlation Rules",
    "message_center": "Message Center",
    "sample_uploads": "Sample Uploads",
    "downloads": "Tools Download",
    "mobile_enrollment": "Mobile enrollment",
    "device_content": "Device Content",
    "delivery_settings": "Channel File",
    "deployments": "Deployment Coordinator",
    "quick_scan": "Quick Scan",
    "quick_scan_pro": "QuickScan Pro",
    "serverless_exports": "Falcon Container Image",
    "cao_hunting": "CAO Hunting",
    "device_control_policies": "Device Control Policies",
    "firewall_management": "Firewall Management",
    "firewall_policies": "Firewall Management",
    "prevention_policies": "Prevention Policies",
    "sensor_update_policies": "Sensor update policies",
    "response_policies": "Response Policies",
    "content_update_policies": "Content Update",
    "installation_tokens": "Installation Tokens",
    "scheduled_reports": "Scheduled Reports",
    "tailored_intelligence": "Tailored Intelligence",
    "threatgraph": "Threatgraph",
    "alerts": "Alerts",
    "incidents": "Incidents",
    "event_streams": "Event streams",
    "fdr": "Falcon Data Replicator",
    "zero_trust_assessment": "Zero Trust Assessment",
}

# Verbs that signal an irreversible or high-impact mutation. Kept broad on
# purpose: anything matching is tagged ``destructive`` and is gated behind
# FALCON_MCP_ALLOW_DESTRUCTIVE.
DESTRUCTIVE_RE = re.compile(
    r"(?i)(delete|remove|purge|uninstall|revoke|deprovision|destroy|"
    r"contain|isolate|kill|terminate|quarantine|reset|restart|reboot|shutdown|"
    r"wipe|disable|block|expire|rotate|regenerate|cancel|detonate|execute|"
    r"invoke|perform|trigger|run|scan|drain|evict|suppress|dismiss|clawback|"
    r"release|clear|drop|prune|deactivate|unassign|unlink|detach|clean)"
)
# Verbs we are confident are non-destructive writes (create/modify style). Only
# operations matching this allowlist are tagged ``write``; everything else that
# isn't clearly a read falls through to ``destructive`` (fail-safe).
WRITE_NAME_RE = re.compile(
    r"(?i)(create|update|upsert|add|set|assign|grant|import|save|register|"
    r"enable|attach|tag|comment|refresh|install|upload|modify|patch|post|put|"
    r"new|edit|configure|connect|provision|validate|verify|preview|submit|"
    r"schedule|start|enroll|notify|send|approve|apply|launch|init|generate|"
    r"build|copy|clone|duplicate|combine|merge|link|associate|entitle|"
    r"acknowledge|assess|signal|increment|reveal|change)"
)
READ_NAME_RE = re.compile(r"(?i)^(get|query|read|combined|list|lookup|retrieve|download|preview|aggregate)")
READ_SUBSTR_RE = re.compile(r"(?i)(_get_|_query|queries_|combined_)")
AGGREGATE_RE = re.compile(r"(?i)(^|_)aggregate|Aggregates")
VERSION_SUFFIX_RE = re.compile(r"(V\d+|_v\d+)$")


def camel_to_snake(name: str) -> str:
    s = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", name)
    s = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1_\2", s)
    s = s.replace("-", "_").replace(".", "_")
    s = re.sub(r"_+", "_", s)
    return s.lower().strip("_")


def base_name(op: str) -> str:
    return VERSION_SUFFIX_RE.sub("", op)


def version_num(op: str) -> int:
    m = re.search(r"[vV](\d+)$", op)
    return int(m.group(1)) if m else 1


def classify(op: str, method: str) -> str:
    """Classify an operation as read / write / destructive.

    Fail-safe by design: HTTP GET is treated as read-only (per HTTP semantics);
    DELETE and any destructive-verb match are destructive; clearly non-GET reads
    (POST-based query/search ops) are read; confidently safe write verbs are
    write; and ANYTHING ELSE falls through to destructive so an unrecognized
    mutating op can never escape the destructive gate by being mislabeled write.
    """
    # GET is read-only per HTTP spec — safe even if the name contains a verb
    # that also appears in the destructive list (e.g. "release notes").
    if method == "GET":
        return "read"
    if method == "DELETE" or DESTRUCTIVE_RE.search(op):
        return "destructive"
    # Non-GET reads: POST-backed query/search/combined operations.
    if READ_NAME_RE.search(op) or READ_SUBSTR_RE.search(op):
        return "read"
    if WRITE_NAME_RE.search(op):
        return "write"
    # Unknown mutating verb -> treat as destructive (fail-safe).
    return "destructive"


def py_type(t: str) -> str:
    return {"integer": "int", "boolean": "bool", "number": "float", "array": "list[str]"}.get(t, "str")


def clean_desc(s: str, cap: int | None = None) -> str:
    s = re.sub(r"\s+", " ", (s or "").strip())
    s = s.replace("\\", "").replace('"', "'")
    if cap is not None and len(s) > cap:
        s = s[:cap].rstrip() + "..."
    return s


def safe_ident(name: str) -> str:
    n = re.sub(r"[^0-9a-zA-Z_]", "_", name)
    if not n or n[0].isdigit():
        n = "p_" + n
    if keyword.iskeyword(n):
        n = n + "_"
    return n


def collect_endpoints():
    out = {}
    pp = pathlib.Path(EP.__file__).parent
    for mod in pkgutil.iter_modules([str(pp)]):
        if mod.name.startswith("_") and not mod.name.startswith("__"):
            m = importlib.import_module(f"falconpy._endpoint.{mod.name}")
            for attr in dir(m):
                if attr.endswith("_endpoints") and isinstance(getattr(m, attr), list):
                    coll = mod.name.lstrip("_")
                    for ep in getattr(m, attr):
                        if isinstance(ep, (list, tuple)) and len(ep) >= 3 and ep[0]:
                            out.setdefault(coll, {})[ep[0]] = ep
    return out


def falconpy_field_mapping() -> dict[str, list[str]]:
    """Extract FalconPy's hardcoded path-token substitution table.

    FalconPy's Uber client only substitutes ``{token}`` path segments for
    operations present in the ``field_mapping`` dict inside
    ``falconpy._util._uber.scrub_target``. For those ops the path values are read
    from TOP-LEVEL kwargs (by the mapped field name) — NOT from ``parameters=``.
    We parse that dict statically so the generator can (a) emit the right
    top-level path args for supported ops and (b) skip ops whose path tokens
    FalconPy can't fill (which would otherwise produce broken URLs).
    """
    try:
        from falconpy._util import _uber  # noqa: WPS433 (local import by design)

        src = inspect.getsource(_uber.scrub_target)
    except Exception:  # noqa: BLE001
        return {}
    try:
        start = src.index("field_mapping = {")
        end = src.index("}", start)
    except ValueError:
        return {}
    region = src[start:end + 1]
    mapping: dict[str, list[str]] = {}
    for m in re.finditer(r'"([A-Za-z0-9_]+)":\s*\[([^\]]*)\]', region):
        mapping[m.group(1)] = re.findall(r'"([^"]+)"', m.group(2))
    return mapping


FIELD_MAPPING = falconpy_field_mapping()
# Ops whose path substitution FalconPy resolves conditionally / unreliably; skip
# to avoid emitting tools that build malformed request URLs.
PATH_SKIP_OPS = {"GetSearchStatusV1"}
PATH_TOKEN_RE = re.compile(r"\{[^}]+\}")


def used_operations() -> set:
    used = set()
    for f in MODULES_DIR.glob("*.py"):
        if f.name.startswith("gen_"):
            continue
        t = f.read_text()
        used |= set(re.findall(r'operation\s*=\s*["\']([A-Za-z0-9_]+)["\']', t))
        used |= set(re.findall(r'command(?:_for)?\(\s*["\']([A-Za-z0-9_]+)["\']', t))
    return used


def hand_tool_names() -> set:
    """Collect tool names registered by hand-crafted (non-gen) modules, without the
    ``falcon_`` prefix, so generated tools that would collide get disambiguated."""
    import asyncio
    import os
    from unittest.mock import MagicMock

    from mcp.server.fastmcp import FastMCP

    os.environ["FALCON_MCP_READONLY"] = "false"
    os.environ["FALCON_MCP_ALLOW_DESTRUCTIVE"] = "true"
    names, dummy = set(), MagicMock()
    for f in MODULES_DIR.glob("*.py"):
        if f.stem.startswith("gen_") or f.stem in ("__init__", "base"):
            continue
        m = importlib.import_module(f"falcon_mcp.modules.{f.stem}")
        for attr in dir(m):
            if attr.endswith("Module") and attr != "BaseModule":
                try:
                    s = FastMCP("seed")
                    getattr(m, attr)(dummy).register_tools(s)
                    for t in asyncio.run(s.list_tools()):
                        names.add(t.name[7:] if t.name.startswith("falcon_") else t.name)
                except Exception:
                    pass
    return names


def scope_for(coll: str, kind: str) -> str:
    label = COLLECTION_SCOPE.get(coll) or " ".join(w.capitalize() for w in coll.split("_"))
    perm = "read" if kind == "read" else "write"
    return f"{label}:{perm}"


def build_method(ep, kind: str) -> tuple[str, str, str]:
    """Return (tool_name, method_source, operation_id).

    On a skip, returns ("__SKIP__", reason, operation_id) so the caller can log
    why an operation was omitted instead of silently emitting a broken tool.
    """
    op, method, route = ep[0], ep[1], ep[2]
    desc = clean_desc(ep[3] if len(ep) > 3 and isinstance(ep[3], str) else op)
    params = ep[5] if len(ep) > 5 and isinstance(ep[5], list) else []
    qparams = [p for p in params if isinstance(p, dict) and p.get("in") == "query"]
    body_param = next((p for p in params if isinstance(p, dict) and p.get("in") == "body"), None)
    has_body = body_param is not None
    body_required = bool(body_param and body_param.get("required"))
    has_formdata = any(isinstance(p, dict) and p.get("in") == "formData" for p in params)
    path_params = [p for p in params if isinstance(p, dict) and p.get("in") == "path"]
    needs_path = bool(path_params) or bool(PATH_TOKEN_RE.search(route or ""))

    # formData (file upload / multipart) bodies aren't expressible through the
    # generic query/body call shape — skip rather than emit a broken tool.
    if has_formdata:
        return "__SKIP__", "formData/multipart body not supported by generic wrapper", op

    path_fields: list[str] = []
    if needs_path:
        if op in PATH_SKIP_OPS:
            return "__SKIP__", "path substitution is conditional in FalconPy", op
        if op not in FIELD_MAPPING:
            return "__SKIP__", "path token has no FalconPy field_mapping entry", op
        path_fields = FIELD_MAPPING[op]

    tool = camel_to_snake(op)
    seen, path_lines, req_lines, opt_lines, qp_map, pp_map = set(), [], [], [], [], []

    # Path parameters first — always required, always plain str.
    for fld in path_fields:
        py = safe_ident(fld)
        if py in seen:
            continue
        seen.add(py)
        path_lines.append(
            f'        {py}: str = Field(description="`{fld}` path parameter (required)."),'
        )
        pp_map.append((fld, py))

    for p in qparams:
        api = p.get("name")
        if not api or api in seen:
            continue
        seen.add(api)
        py = safe_ident(api)
        typ = py_type(p.get("type", "string"))
        pdesc = clean_desc(p.get("description", "")) or f"`{api}` query parameter."
        if p.get("required"):
            req_lines.append(f'        {py}: {typ} = Field(description="{pdesc}"),')
        else:
            opt_lines.append(f'        {py}: {typ} | None = Field(default=None, description="{pdesc}"),')
        qp_map.append((api, py))

    # Required params (no default) must precede optional ones in the signature.
    # A required body therefore goes in the required group; an optional body
    # goes after the optional query params (but before member_cid).
    sig = list(path_lines) + list(req_lines)
    if has_body and body_required:
        sig.append(
            f'        body: dict = Field('
            f'description="Request JSON body for `{op}` per the CrowdStrike API schema (required)."),'
        )
    sig += list(opt_lines)
    if has_body and not body_required:
        sig.append(
            f'        body: dict | None = Field(default=None, '
            f'description="Request JSON body for `{op}` per the CrowdStrike API schema."),'
        )
    sig.append('        member_cid: str | None = Field(default=None, description="Optional child CID for MSSP scoping."),')

    qp_dict = "{" + ", ".join(f'"{api}": {py}' for api, py in qp_map) + "}" if qp_map else "None"
    pp_arg = ("path_params={" + ", ".join(f'"{fld}": {py}' for fld, py in pp_map) + "}, ") if pp_map else ""
    body_arg = "body_params=body, " if has_body else ""
    src = (
        f"    def {tool}(\n        self,\n" + "\n".join(sig) + "\n    ) -> list[dict] | dict:\n"
        f'        """{desc}"""\n'
        f'        return self._call(operation="{op}", query_params={qp_dict}, {pp_arg}{body_arg}'
        f'error_message="{op} failed", member_cid=member_cid)\n'
    )
    return tool, src, op


def main():
    endpoints = collect_endpoints()
    used = used_operations()
    global_tool_names = hand_tool_names()  # seed so generated tools never shadow hand-crafted ones
    scope_map = {}
    gen_count = mod_count = 0
    generated_files = []
    skipped = []  # (operation_id, reason) for ops we deliberately did not emit

    for coll in sorted(endpoints):
        if coll in SKIP_COLLECTIONS:
            continue
        ops = endpoints[coll]
        # version-dedup: keep highest V# per base name across the whole collection
        best = {}
        for op in ops:
            b = base_name(op)
            if b not in best or version_num(op) > version_num(best[b]):
                best[b] = op
        keep = set(best.values())

        candidates = []
        for op, ep in ops.items():
            if op not in keep or op in used:
                continue
            if AGGREGATE_RE.search(op):
                continue
            candidates.append(ep)
        if not candidates:
            continue

        methods, anns = [], {"read": [], "write": [], "destructive": []}
        for ep in sorted(candidates, key=lambda e: e[0]):
            kind = classify(ep[0], ep[1])
            tool, src, op = build_method(ep, kind)
            if tool == "__SKIP__":
                # src holds the human-readable reason on a skip
                skipped.append((op, src))
                continue
            if tool in global_tool_names:
                tool2 = f"{tool}_{coll}"[:60]
                src = src.replace(f"    def {tool}(", f"    def {tool2}(", 1)
                tool = tool2
            if tool in global_tool_names:
                continue
            global_tool_names.add(tool)
            methods.append(src)
            anns[kind].append(tool)
            scope_map[op] = [scope_for(coll, kind)]
            gen_count += 1

        cls = "Gen" + "".join(w.capitalize() for w in coll.split("_")) + "Module"
        reg = ["    def register_tools(self, server: FastMCP) -> None:"]
        for kind, annconst in (("read", None), ("write", "WRITE_ANNOTATIONS"), ("destructive", "DESTRUCTIVE_ANNOTATIONS")):
            for tool in anns[kind]:
                if annconst:
                    reg.append(f"        self._add_tool(server=server, method=self.{tool}, name=\"{tool}\", annotations={annconst})")
                else:
                    reg.append(f"        self._add_tool(server=server, method=self.{tool}, name=\"{tool}\")")
        reg.append("\n    def register_resources(self, server: FastMCP) -> None:\n        pass\n")

        header = (
            '"""AUTO-GENERATED FileVantage-style module — do not hand-edit; regenerate via\n'
            'scripts/generate_falcon_modules.py. Wraps the CrowdStrike Falcon '
            f'`{coll}` API service collection."""\n\n'
            "from mcp.server import FastMCP\n"
            "from mcp.types import ToolAnnotations\n"
            "from pydantic import Field\n\n"
            "from falcon_mcp.common.generated_base import GeneratedModuleBase\n\n"
            "WRITE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=False, "
            "idempotentHint=False, openWorldHint=True)\n"
            "DESTRUCTIVE_ANNOTATIONS = ToolAnnotations(readOnlyHint=False, destructiveHint=True, "
            "idempotentHint=True, openWorldHint=True)\n\n\n"
            f"class {cls}(GeneratedModuleBase):\n"
            f'    """Generated tools for the Falcon `{coll}` collection."""\n\n'
        )
        body = header + "\n".join(reg) + "\n" + "\n".join(methods)
        path = MODULES_DIR / f"gen_{coll}.py"
        path.write_text(body)
        generated_files.append(path.name)
        mod_count += 1

    # scope file
    lines = ['"""AUTO-GENERATED scope hints — regenerate via scripts/generate_falcon_modules.py."""\n',
             "GENERATED_SCOPE_REQUIREMENTS = {"]
    for op in sorted(scope_map):
        lines.append(f'    "{op}": {scope_map[op]!r},')
    lines.append("}\n")
    (COMMON_DIR / "api_scopes_generated.py").write_text("\n".join(lines))

    print(f"Generated {mod_count} modules, {gen_count} tools, {len(scope_map)} scope entries.")
    print("Files:", ", ".join(sorted(generated_files)))

    if skipped:
        reasons: dict[str, int] = {}
        for _op, reason in skipped:
            reasons[reason] = reasons.get(reason, 0) + 1
        print(f"\nSkipped {len(skipped)} operations (no safe generic wrapper):")
        for reason in sorted(reasons):
            print(f"  {reasons[reason]:4d}  {reason}")


if __name__ == "__main__":
    main()
