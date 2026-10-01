"""Unit tests for wmongo-mcp catalog."""

from wmongo_mcp.catalog import PatternsCatalog


def test_catalog_search():
    catalog = PatternsCatalog()
    results = catalog.search("forensic")
    assert len(results) > 0
    assert any("Forensic" in p["name"] or "forensic" in p["feature"].lower() for p in results)


def test_catalog_all_patterns():
    catalog = PatternsCatalog()
    results = catalog.search("wmongo")
    assert len(results) > 0
