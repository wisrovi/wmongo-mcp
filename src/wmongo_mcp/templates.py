"""Code template generators for WMongo project scaffolding."""

from typing import Dict, List


class TemplateGenerator:
    """Provides file scaffolding blueprints for WMongo architectures."""

    @staticmethod
    def get_folders(scaffold_type: str = "standard") -> List[str]:
        """Return folder structure for project deployment."""
        if scaffold_type == "api_service":
            return ["config", "models", "repositories", "routers", "tests"]
        return ["config", "models", "repositories", "tests"]

    @staticmethod
    def get_files_blueprint(scaffold_type: str = "standard", project_name: str = "wmongo_project") -> Dict[str, str]:
        """Return dict of relative file paths to file contents."""
        settings_py = (
            "from dataclasses import dataclass\n"
            "import os\n\n"
            "@dataclass\n"
            "class DatabaseSettings:\n"
            "    uri: str = os.getenv('MONGO_URI', 'mongodb://localhost:27017')\n"
            "    database: str = os.getenv('MONGO_DB', 'app_db')\n"
            "    username: str = os.getenv('MONGO_USER', None)\n"
            "    password: str = os.getenv('MONGO_PASS', None)\n"
            "    forensic: bool = True\n"
        )

        user_model_py = (
            "from typing import Optional\n"
            "from wmongo import ForensicModel\n\n"
            "class User(ForensicModel):\n"
            "    id: Optional[int] = None\n"
            "    username: str\n"
            "    email: str\n"
            "    age: int = 18\n"
        )

        main_py = (
            "from config.settings import DatabaseSettings\n"
            "from models.user import User\n"
            "from wmongo import WMongo\n\n"
            "def main():\n"
            "    settings = DatabaseSettings()\n"
            "    app = WMongo(models=[User], uri=settings.uri, database=settings.database, forensic=settings.forensic)\n"
            "    print(f'Registered collection: {app.user.table_name}')\n"
            "    print(f'Forensic mode: {app.user.forensic}')\n\n"
            "if __name__ == '__main__':\n"
            "    main()\n"
        )

        return {
            "config/__init__.py": "",
            "config/settings.py": settings_py,
            "models/__init__.py": "",
            "models/user.py": user_model_py,
            "repositories/__init__.py": "",
            "tests/__init__.py": "",
            "main.py": main_py,
        }
