from pathlib import Path

DIR = Path("_manufacturing/_inventory")

FILE_NAME = DIR / "data/_inventory.json"
LOG_FILE = DIR / "logs/_inventory.log"

REQUIRED_FIELDS = ("name", "quantity", "reorder_level", "supplier")