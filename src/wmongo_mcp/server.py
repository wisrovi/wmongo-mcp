"""wmongo-mcp: Model Context Protocol server for WMongo architecting and code generation."""

import argparse
import ast
import json
import logging
import os
import sys
from functools import lru_cache

from mcp.server.fastmcp import FastMCP

from wmongo_mcp.catalog import PatternsCatalog
from wmongo_mcp.templates import TemplateGenerator

# Setup logging strictly to stderr to avoid breaking MCP protocol
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s", stream=sys.stderr)
logger = logging.getLogger(__name__)

# Create primary FastMCP Server instance
mcp = FastMCP("wmongo-mcp-server")


@lru_cache(maxsize=1)
def get_catalog() -> PatternsCatalog:
    """Return shared patterns catalog instance."""
    return PatternsCatalog()


def _is_pydantic_model(cls: ast.ClassDef) -> bool:
    """Return True if class inherits from BaseModel or ForensicModel."""
    return any(
        isinstance(b, ast.Name) and b.id in ("BaseModel", "ForensicModel")
        for b in cls.bases
    )


@mcp.tool()
def validate_model_schema(model_code: str) -> str:
    """Validate a Pydantic model definition for WMongo MongoDB compatibility."""
    try:
        tree = ast.parse(model_code)
        issues = []
        warnings = []

        classes = [n for n in ast.walk(tree) if isinstance(n, ast.ClassDef)]
        model_classes = [c for c in classes if _is_pydantic_model(c)]

        if not model_classes:
            issues.append("No Pydantic BaseModel or ForensicModel subclass found.")

        result = "Valid Model Validation Result:\n"
        if issues:
            result += "Issues:\n" + "\n".join(f"  ❌ {i}" for i in issues) + "\n"
        if warnings:
            result += "Warnings:\n" + "\n".join(f"  ⚠️ {w}" for w in warnings) + "\n"
        if not issues and not warnings:
            result += "✅ Model looks good for WMongo collection storage!"
        return result

    except SyntaxError as e:
        return f"❌ Syntax Error in model code: {e}"
    except Exception as e:
        return f"❌ Validation Error: {type(e).__name__}: {e}"


@mcp.tool()
def search_wmongo_pattern(query: str) -> str:
    """Search for production-ready WMongo architectural patterns."""
    results = get_catalog().search(query)
    if not results:
        return f"No pattern matching '{query}' was found in WMongo catalog."

    response = "Found production-ready architectural patterns in wisrovi SUITE:\n\n"
    for p in results:
        response += f"🚀 [{p['origin']}] {p['name']}\n"
        response += f"   - Feature: {p['feature']}\n"
        response += f"   - Module: {p['module']}\n"
        response += f"   - Description: {p['description']}\n\n"
    return response


@mcp.tool()
def deploy_wmongo_scaffolding(
    target_dir: str,
    project_name: str = "wmongo_project",
    scaffold_type: str = "standard",
) -> str:
    """Deploys a professional WMongo project structure following wisrovi standards."""
    try:
        if not os.path.isabs(target_dir):
            return "Error: target_dir must be an absolute path."

        for folder in TemplateGenerator.get_folders(scaffold_type):
            os.makedirs(os.path.join(target_dir, folder), exist_ok=True)

        blueprints = TemplateGenerator.get_files_blueprint(scaffold_type, project_name)
        for rel_path, content in blueprints.items():
            full_path = os.path.join(target_dir, rel_path)
            os.makedirs(os.path.dirname(full_path), exist_ok=True)
            with open(full_path, "w", encoding="utf-8") as f:
                f.write(content)

        return f"Success: WMongo architecture '{project_name}' deployed at {target_dir}"
    except Exception as e:
        return f"Error deploying scaffolding: {str(e)}"


@mcp.tool()
def get_wmongo_architect_blueprints() -> str:
    """Complete reference with multi-table, forensic, and CRUD examples for WMongo."""
    multi_table_code = (
        "from typing import Optional\n"
        "from wmongo import ForensicModel, WMongo\n\n"
        "class User(ForensicModel):\n"
        "    id: Optional[int] = None\n"
        "    username: str\n"
        "    email: str\n\n"
        "class Order(ForensicModel):\n"
        "    id: Optional[int] = None\n"
        "    total: float\n\n"
        "# Multi-table registration with ghost table forensic auditing\n"
        "app = WMongo(models=[User, Order], database='my_db', forensic=True)\n"
        "inserted_user = app.user.insert(User(username='alice', email='alice@example.com'))\n"
    )

    async_code = (
        "import asyncio\n"
        "from wmongo import WMongoAsync\n\n"
        "async def main():\n"
        "    async with WMongoAsync(database='mydb') as wm:\n"
        "        doc_id = await wm.insert('users', {'name': 'Alice', 'age': 30})\n"
        "        users = await wm.find('users', {'age': {'$gte': 20}})\n"
    )

    return (
        "WMONGO EXPERT BLUEPRINTS (COMPLETE REFERENCE)\n\n"
        "=== 1. MULTI-COLLECTION & FORENSIC AUDIT LOG ===\n" + multi_table_code + "\n"
        "=== 2. ASYNC MONGODB OPERATIONS ===\n" + async_code
    )


@mcp.tool()
def get_wmongo_architect_manual() -> str:
    """Expert manual for building high-performance MongoDB systems with WMongo."""
    manual_text = (
        "WMONGO ARCHITECT MANUAL (ADVANCED)\n"
        "--- PROJECT STRUCTURE RULES (MANDATORY) ---\n"
        "1. CONFIG: Centralize MongoDB settings in `config/settings.py`.\n"
        "2. MODELS: Inherit from `ForensicModel` or `BaseModel` in `models/` directory.\n"
        "3. MULTI-TABLE: Register models via `WMongo(models=[...], forensic=True)` for automatic `_forensic_audit_log` audit trails.\n"
        "4. ASYNC: Use `WMongoAsync` for non-blocking FastAPI and Motor applications.\n\n"
        "Generated by WMongo MCP by wisrovi"
    )
    return manual_text


@mcp.tool()
def generate_wmongo_crud(model_code: str) -> str:
    """Generate repository CRUD wrapper code for a Pydantic model definition."""
    try:
        tree = ast.parse(model_code)
        classes = [n.name for n in ast.walk(tree) if isinstance(n, ast.ClassDef) and _is_pydantic_model(n)]
        if not classes:
            return "# Error: No Pydantic model found in provided code."

        model_name = classes[0]
        repo_name = f"{model_name}Repository"

        code = (
            f"from typing import List, Optional\n"
            f"from wmongo import WMongo, ForensicModel\n\n"
            f"class {repo_name}:\n"
            f"    def __init__(self, database: str = 'app_db', uri: str = 'mongodb://localhost:27017'):\n"
            f"        self.db = WMongo(model={model_name}, database=database, uri=uri, forensic=True)\n\n"
            f"    def create(self, item: {model_name}) -> str:\n"
            f"        return self.db.insert(item.dict())\n\n"
            f"    def find(self, query: dict) -> List[dict]:\n"
            f"        return self.db.find(query)\n\n"
            f"    def update(self, query: dict, update_values: dict) -> int:\n"
            f"        return self.db.update(query, update_values)\n\n"
            f"    def delete(self, query: dict) -> int:\n"
            f"        return self.db.delete(query)\n"
        )
        return code
    except Exception as e:
        return f"# Generation error: {e}"


def run_stdio():
    """Run MCP server in stdio mode."""
    mcp.run(transport="stdio")


def main():
    """Main CLI entrypoint for wmongo-mcp server."""
    parser = argparse.ArgumentParser(description="wmongo-mcp: WMongo Architect MCP Server")
    parser.add_argument("command", nargs="?", default="run", choices=["run", "help"])
    args = parser.parse_args()

    if args.command == "run":
        run_stdio()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
