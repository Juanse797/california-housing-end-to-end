from pathlib import Path

# Raíz del repo (…/Ml_pytorch_aurelio)
PROJECT_ROOT = Path(__file__).resolve().parents[2]

# Carpeta data del proyecto
DATA_DIR = PROJECT_ROOT / "data"

# Aquí definimos la "identidad" del dataset
HOUSING_PATH = DATA_DIR / "housing_raw"
HOUSING_CSV = HOUSING_PATH / "housing.csv"

# Aqui definimos la ruta del split
SPLIT_DIR = DATA_DIR / "interim"

# Aqui definimos la ruta del csv preprocesado
PREPROCESSED_DIR = DATA_DIR / "processed"