#  MANAGEMENT ENVIRONMENT --------------------------------
import os

# get the absolute path of the configuration file and variable names
CONFIG_FILE = os.path.join(
    os.path.dirname(__file__), "config.yaml"
)
COLUMNS_NAMES = os.path.join(
    os.path.dirname(__file__), "columns_name.txt"
)
