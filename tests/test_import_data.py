#  MANAGEMENT ENVIRONMENT --------------------------------
import unittest
import pandas as pd
from bankml.import_data import import_data


# TESTS  -------------------------------
class TestDownloadData(unittest.TestCase):

    def setUp(self):
        # PARAMETERS  -------------------------------
        # self.config = import_yaml_config()
        # path_raw_bank_data = self.config["path"]["data_url"]

        # define a valid and an invalid url for the tests
        self.url_valide = "https://datahub.io/machine-learning/bank-marketing/datapackage.json"
        self.url_invalide = "https://www.google.com/404"

    def test_type(self):
        # test if the function returns an object of type pandas.DataFrame
        df = import_data(self.url_valide)
        self.assertIsInstance(df, pd.DataFrame)

    def test_exception(self):
        # test if the function raises an exception if the url is invalid
        with self.assertRaises(Exception):
            import_data(self.url_invalide)

    def test_shape(self):
        # test if the dataframe has the right number of columns
        df = import_data(self.url_valide)
        self.assertEqual(df.shape[1], 17)


if __name__ == "__main__":
    unittest.main()
