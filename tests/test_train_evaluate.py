#  MANAGEMENT ENVIRONMENT --------------------------------
import unittest
import pandas as pd
from bankml.train_evaluate import random_forest_bank
from sklearn.model_selection import train_test_split
from bankml.import_data import import_yaml_config, import_data


# TESTS  -------------------------------
class TestTrainerModel(unittest.TestCase):

    def setUp(self):
        # PARAMETERS  -------------------------------
        self.config = import_yaml_config()
        self.path_raw_bank_data = self.config["path"]["data_url"]

        # self.TEST_FRACTION = 0.3
        self.TEST_FRACTION = self.config["model"]["test_fraction"]

        # url to load data from
        # self.url = "https://datahub.io/machine-learning/bank-marketing/datapackage.json"
        self.url = self.config["path"]["data_url"]

        # Load data and split train/test ----------------------------
        self.df_bank = import_data(self.url)
        self.train, self.test = train_test_split(
            self.df_bank,
            test_size=self.TEST_FRACTION,
            random_state=42,
            stratify=self.df_bank["deposit"],
        )

        # train and test dataframes (reduce size to go faster)
        self.train = self.train.sample(frac=0.05, random_state=42)
        self.test = self.test.sample(frac=0.05, random_state=42)

    def test_value_n_tree(self):
        # test if the function throws an exception if
        # the value is not correct or of the wrong type
        with self.assertRaises(ValueError):
            random_forest_bank(self.train, self.test, NTREES=-1)
        with self.assertRaises(ValueError):
            random_forest_bank(self.train, self.test, NTREES=-0.1)
        with self.assertRaises(TypeError):
            random_forest_bank(self.train, self.test, NTREES="1")

    def test_exception_value(self):
        with self.assertRaises(KeyError):
            # train is empty
            random_forest_bank(pd.DataFrame(), self.test, NTREES=1)
        with self.assertRaises(KeyError):
            # test is empty
            random_forest_bank(self.train, pd.DataFrame(), NTREES=1)
        with self.assertRaises(KeyError):
            # train does not have the column 'deposit' (target)
            random_forest_bank(self.train.drop("deposit", axis=1),
                               self.test, NTREES=1)
        with self.assertRaises(KeyError):
            # test does not have the column 'deposit' (target)
            random_forest_bank(self.train, self.test.drop("deposit", axis=1),
                               NTREES=1)


if __name__ == "__main__":
    unittest.main()
