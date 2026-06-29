"""
Module registry for Falcon MCP Server

This module provides a registry of available modules for the Falcon MCP server.
"""

from __future__ import annotations

import importlib
import os
import pkgutil
from typing import TYPE_CHECKING

from falcon_mcp.common.logging import get_logger

if TYPE_CHECKING:
    from falcon_mcp.modules.base import BaseModule

logger = get_logger(__name__)

# This will be populated by the discovery process
AVAILABLE_MODULES: dict[str, type[BaseModule]] = {}

# Prefix used by the auto-generated module layer (scripts/generate_falcon_modules.py).
GENERATED_PREFIX = "gen_"


def _generated_enabled() -> bool:
    """Whether the auto-generated ``gen_*`` modules should be loaded.

    The generated layer adds hundreds of thin API wrappers. It is opt-in so the
    default server exposes only the curated, hand-written tools. Enable it by
    setting FALCON_MCP_ENABLE_GENERATED to a truthy value (1/true/yes/on).
    """
    return os.environ.get("FALCON_MCP_ENABLE_GENERATED", "").strip().lower() in (
        "1",
        "true",
        "yes",
        "on",
    )


def discover_modules() -> None:
    """Discover available modules by scanning the modules directory."""
    # Get the path to the modules directory
    current_dir = os.path.dirname(__file__)
    modules_path = os.path.join(current_dir, "modules")

    generated_enabled = _generated_enabled()

    # Scan for module files
    for _, name, is_pkg in pkgutil.iter_modules([modules_path]):
        if is_pkg or name == "base":  # Skip base.py and packages
            continue
        # Generated modules are opt-in to keep the default tool surface curated.
        if name.startswith(GENERATED_PREFIX) and not generated_enabled:
            logger.debug("Skipping generated module (opt-in): %s", name)
            continue

        try:
            module = importlib.import_module(f"falcon_mcp.modules.{name}")
        except Exception as exc:
            # A broken module must not take down discovery for the rest.
            logger.error("Failed to import module %s: %s", name, exc)
            continue

        # Look for *Module classes
        for attr_name in dir(module):
            if attr_name.endswith("Module") and attr_name != "BaseModule":
                # Get the class
                module_class = getattr(module, attr_name)
                # Register it
                module_name = attr_name.lower().replace("module", "")
                AVAILABLE_MODULES[module_name] = module_class
                logger.debug("Discovered module: %s", module_name)


def get_available_modules() -> dict[str, type[BaseModule]]:
    """Get available modules dict, discovering if needed (lazy loading).

    Returns:
        Dict mapping module names to module classes
    """
    if not AVAILABLE_MODULES:
        logger.debug("No modules discovered yet, performing lazy discovery")
        discover_modules()
    return AVAILABLE_MODULES


def get_module_names() -> list[str]:
    """Get the names of all registered modules, discovering if needed (lazy loading).

    Returns:
        List of module names
    """
    return list(get_available_modules().keys())
