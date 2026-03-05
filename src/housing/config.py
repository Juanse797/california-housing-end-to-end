from pathlib import Path

# Raíz del repo (…/Ml_pytorch_aurelio)
PROJECT_ROOT = Path(__file__).resolve().parents[2]

# Carpeta data del proyecto
DATA_DIR = PROJECT_ROOT / "data"

# Donde guardas el housing
HOUSING_DIR = DATA_DIR / "housing"