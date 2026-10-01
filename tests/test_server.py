"""Unit tests for wmongo-mcp server tools."""

import os
import shutil
import tempfile
from wmongo_mcp.server import (
    validate_model_schema,
    search_wmongo_pattern,
    deploy_wmongo_scaffolding,
    get_wmongo_architect_blueprints,
    get_wmongo_architect_manual,
    generate_wmongo_crud,
)


def test_validate_model_schema():
    valid_code = """
from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    id: Optional[int] = None
    username: str
"""
    result = validate_model_schema(valid_code)
    assert "✅ Model looks good" in result


def test_search_wmongo_pattern():
    res = search_wmongo_pattern("forensic")
    assert "Enterprise Forensic Audit Log" in res


def test_get_wmongo_architect_blueprints():
    res = get_wmongo_architect_blueprints()
    assert "WMONGO EXPERT BLUEPRINTS" in res


def test_get_wmongo_architect_manual():
    res = get_wmongo_architect_manual()
    assert "WMONGO ARCHITECT MANUAL" in res


def test_deploy_wmongo_scaffolding():
    temp_dir = tempfile.mkdtemp()
    try:
        res = deploy_wmongo_scaffolding(target_dir=temp_dir, project_name="test_proj")
        assert "Success" in res
        assert os.path.exists(os.path.join(temp_dir, "config", "settings.py"))
        assert os.path.exists(os.path.join(temp_dir, "models", "user.py"))
    finally:
        shutil.rmtree(temp_dir)


def test_generate_wmongo_crud():
    code = """
from pydantic import BaseModel

class Product(BaseModel):
    name: str
    price: float
"""
    res = generate_wmongo_crud(code)
    assert "class ProductRepository" in res
