"""Import data"""

#  MANAGEMENT ENVIRONMENT --------------------------------
import os
import yaml
import pandas as pd
import datapackage
from sklearn.utils import resample


# CONFIG_FILE = os.path.join(os.path.dirname(__file__), "config.yaml")
# COLUMNS_NAMES = os.path.join(os.path.dirname(__file__), "columns_name.txt")
CONFIG_FILE = os.path.join(
    os.path.dirname(__file__), "..", "configuration", "config.yaml"
)
COLUMNS_NAMES = os.path.join(
    os.path.dirname(__file__), "..", "configuration", "columns_name.txt"
)


def import_yaml_config(file_path: str = CONFIG_FILE):
    """Read the yaml file"""
    with open(file_path, "r", encoding="utf-8") as file:
        return yaml.safe_load(file)


def import_data(path_raw_bank_data: str) -> pd.DataFrame:
    """Load, balance data \
    and returns it as a pandas DataFrame"""

    # Load Data Package into storage
    package = datapackage.Package(path_raw_bank_data)

    # Load only tabular data
    resources = package.resources
    df_bank = pd.read_csv(resources[1].descriptor["path"])

    with open(COLUMNS_NAMES, "r") as f:
        content = f.read()

    cols_name = list(content.split(","))
    df_bank.columns = cols_name

    df_bank.deposit = df_bank.deposit.map({1: "no", 2: "yes"})

    # Separate the data into minority and majority classes
    df_majority = df_bank[df_bank["deposit"] == "no"]
    df_minority = df_bank[df_bank["deposit"] == "yes"]

    # Reduce the size of the majority class
    df_majority_downsampled = resample(
        df_majority, replace=False, n_samples=len(df_minority), random_state=42
    )

    # Concatenate the two rebalanced classes
    df_downsampled = pd.concat([df_majority_downsampled, df_minority])

    # Shuffle the rebalanced data
    df_downsampled = df_downsampled.sample(frac=1, random_state=42)

    return df_downsampled
