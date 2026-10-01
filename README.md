# wmongo-mcp: Model Context Protocol Server for WMongo

`wmongo-mcp` is an official **Model Context Protocol (MCP)** server built on top of **FastMCP** that equips AI agents with tools to architect, validate, scaffold, and generate code for **WMongo** (Synchronous & Asynchronous MongoDB engine for Python).

## Key Technologies & Libraries

- **[MCP Protocol](https://modelcontextprotocol.io/)**: Open standard connecting AI models to external tools and context.
- **[FastMCP](https://github.com/jlowin/fastmcp)**: Python framework for fast MCP server implementation.
- **[WMongo](file:///home/william.rodriguez/Documents/w_libraries/w_libraries/wmongo)**: MongoDB client with multi-collection management, forensic audit trails, and Pydantic validation.
- **[Pydantic v2](https://docs.pydantic.dev/)**: Data schema validation and Python AST inspection.
- **[Pytest](https://docs.pytest.org/)**: Modern Python testing framework.
- **[Pytest-Cov](https://pytest-cov.readthedocs.io/)**: Code coverage measurement for pytest.
- **[Docker](https://www.docker.com/)**: Containerized test execution environment.

---

## MCP Tools Exposed

1. **`validate_model_schema(model_code: str)`**: Validates Pydantic document models for WMongo compatibility.
2. **`search_wmongo_pattern(query: str)`**: Searches the official wisrovi SUITE catalog for WMongo architectural patterns.
3. **`deploy_wmongo_scaffolding(target_dir: str, project_name: str, scaffold_type: str)`**: Deploys project scaffolding with repository, config, models, and tests.
4. **`get_wmongo_architect_blueprints()`**: Returns code reference and blueprints for WMongo features.
5. **`get_wmongo_architect_manual()`**: Returns the comprehensive WMongo architecting manual.
6. **`generate_wmongo_crud(model_code: str)`**: Automatically generates repository CRUD class for Pydantic models.

---

## Running Unit Tests & Coverage

### Local Pytest Execution

```bash
# Install editable package
pip install -e .

# Run pytest test suite
PYTHONPATH=src pytest tests/

# Calculate code coverage
./scripts/run_coverage.sh
```

### Docker Containerized Test Execution

```bash
./scripts/run_tests_docker.sh
```

---

*Part of the wisrovi SUITE ecosystem.*