"""WMongo Architectural Patterns Catalog."""

from typing import Dict, List, Optional


class PatternsCatalog:
    """Catalog of production-ready patterns for WMongo document database architectures."""

    PATTERNS = [
        {
            "id": "wmongo-crud",
            "name": "Synchronous WMongo Repository",
            "feature": "CRUD & Models",
            "module": "wmongo.wmongo",
            "description": "Standard repository pattern wrapping WMongo with Pydantic model validation and Redis notification/caching support.",
            "origin": "wisrovi SUITE",
        },
        {
            "id": "wmongo-async",
            "name": "Async MongoDB Operations",
            "feature": "Async / Motor Integration",
            "module": "wmongo.wmongo_async",
            "description": "Motor-powered async MongoDB client (WMongoAsync) for high-throughput non-blocking applications.",
            "origin": "wisrovi SUITE",
        },
        {
            "id": "multi-table-management",
            "name": "Multi-Collection Registry & Management",
            "feature": "Multi-Collection Registry",
            "module": "wmongo",
            "description": "Register multiple Pydantic models with WMongo(models=[User, Order]) with dictionary indexing app[User] and dynamic attribute access app.user.",
            "origin": "wisrovi SUITE",
        },
        {
            "id": "forensic-ghost-audit",
            "name": "Enterprise Forensic Audit Log",
            "feature": "Audit & Forensic Security",
            "module": "wmongo",
            "description": "ForensicModel and WMongo(forensic=True) for automatic ghost collection audit logging (_forensic_audit_log) across INSERT, UPDATE, and DELETE operations.",
            "origin": "wisrovi SUITE",
        },
        {
            "id": "n-level-nested-crud",
            "name": "N-Level Nested JSON CRUD",
            "feature": "Nested Documents & Dotted Path Matching",
            "module": "wmongo",
            "description": "Deep nested JSON document CRUD with dotted path query matching (e.g. company.department.manager.city).",
            "origin": "wisrovi SUITE",
        },
        {
            "id": "redis-notifications",
            "name": "Real-time Change Notifications via Redis",
            "feature": "Notifications & Change Streams",
            "module": "wmongo.wmongo",
            "description": "Real-time Redis pub/sub change notification broadcasting for insert, update, and delete actions.",
            "origin": "wisrovi SUITE",
        },
        {
            "id": "field-encryption",
            "name": "Fernet Data Encryption / Decryption",
            "feature": "Security & Encryption",
            "module": "wmongo.wmongo",
            "description": "Fernet symmetric encryption and decryption helpers for sensitive field storage.",
            "origin": "wisrovi SUITE",
        },
    ]

    def search(self, query: str) -> List[Dict[str, str]]:
        """Search patterns matching query string across name, feature, or description."""
        q = query.lower()
        results = []
        for p in self.PATTERNS:
            if q in p["name"].lower() or q in p["feature"].lower() or q in p["description"].lower():
                results.append(p)
        return results
