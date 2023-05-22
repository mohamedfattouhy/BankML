"""
Prediction of whether or not a deposit will be created in a
a bank after a marketing campaign.
"""

#  MANAGEMENT ENVIRONMENT --------------------------------

import sys
from sklearn.model_selection import train_test_split
from bankml.import_data import import_yaml_config, import_data
from bankml.train_evaluate import random_forest_bank


# PARAMETERS  -------------------------------

config = import_yaml_config()
path_raw_bank_data = config["path"]["data_url"]

# Test size
TEST_FRACTION = config["model"]["test_fraction"]

# Number of trees as command line argument
N_TREES = float(sys.argv[1]) if len(sys.argv) == 2 else 0

# Load data and split train/test ----------------------------
df_bank = import_data(path_raw_bank_data)

# We split our dataset into a training part and a test part
# Let's take arbitrarily 25% of the dataset for testing and 75% for learning.
train, test = train_test_split(
    df_bank,
    test_size=TEST_FRACTION,
    random_state=42,
    stratify=df_bank["deposit"]
)


train.to_parquet("train.parquet")


def main():
    random_forest_bank(train, test, NTREES=N_TREES)


# MODELISATION: RANDOM FOREST ----------------------------
if __name__ == '__main__':
    main()

# To run the main file on cmd line use: python main.py or
# use the argument N_TREES (integer > 0) like that: python main.py <N_TREES>
