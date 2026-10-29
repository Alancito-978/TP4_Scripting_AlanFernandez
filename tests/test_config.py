import unittest
from pathlib import Path

import yaml


PROJECT_ROOT = Path(__file__).resolve().parent.parent
COMPOSE_FILE = PROJECT_ROOT / "docker" / "docker-compose.yml"


class TestDockerComposeConfig(unittest.TestCase):

    def test_compose_file_exists(self):
        """Verifica que exista el archivo de Docker Compose."""
        self.assertTrue(
            COMPOSE_FILE.is_file(),
            f"No se encontró el archivo: {COMPOSE_FILE}"
        )

    def test_compose_yaml_is_valid(self):
        """Verifica que el archivo tenga una sintaxis YAML válida."""
        with COMPOSE_FILE.open("r", encoding="utf-8") as file:
            config = yaml.safe_load(file)

        self.assertIsInstance(config, dict)
        self.assertIn("services", config)
        self.assertIn("web_server", config["services"])
        self.assertIn("log_analyzer", config["services"])


if __name__ == "__main__":
    unittest.main()
