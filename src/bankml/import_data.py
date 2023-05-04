"""Import data"""

#  MANAGEMENT ENVIRONMENT --------------------------------
import yaml
import pandas as pd


# CONFIG_FILE = os.path.join(os.path.dirname(__file__), "config.yaml")
CONFIG_FILE = "configuration/config.yaml"


def import_yaml_config(file_path: str = CONFIG_FILE):
    """Read the yaml file"""
    with open(file_path, "r", encoding="utf-8") as file:
        return yaml.safe_load(file)


def import_data(bank_dataset_path: str) -> pd.DataFrame:
    """Read data \
    and returns it as a pandas DataFrame"""

    # Read data
    bank_dataset = pd.read_csv(bank_dataset_path)

    # Return the pandas DataFrame
    return bank_dataset
