from __future__ import annotations

from pathlib import Path
import tarfile
import urllib.request

import pandas as pd
 
from housing.config import HOUSING_DIR


HOUSING_URL = "https://github.com/ageron/data/raw/main/housing.tgz"


def load_housing_data(data_dir: Path | str = HOUSING_DIR) -> pd.DataFrame:
    """
    Descarga (si no existe) y carga el dataset Housing como DataFrame.
    Guarda:
      - housing.tgz en data_dir
      - el CSV extraído en data_dir/housing/housing.csv
    """
    data_dir = Path(data_dir)
    tarball_path = data_dir / "housing.tgz"
    csv_path = data_dir / "housing" / "housing.csv"

    if not tarball_path.is_file():
        data_dir.mkdir(parents=True, exist_ok=True)

        urllib.request.urlretrieve(HOUSING_URL, tarball_path)

        with tarfile.open(tarball_path) as tar:
            tar.extractall(path=data_dir, filter="data")

    # Si ya estaba descargado pero no extraído por alguna razón, asegúralo:
    if not csv_path.exists():
        with tarfile.open(tarball_path) as tar:
            tar.extractall(path=data_dir, filter="data")

    return pd.read_csv(csv_path)

if __name__ == "__main__":
    load_housing_data()