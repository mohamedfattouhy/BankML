#  MANAGEMENT ENVIRONMENT --------------------------------
import unittest
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from bankml.import_data import import_yaml_config, import_data
from bankml.build_pipeline import (
    pipeline_fit_transform_data_bank,
    pipeline_ml_train_bank,
)


# TESTS  -------------------------------
class TestBuildPipeline(unittest.TestCase):

    def setUp(self):
        # PARAMETERS  -------------------------------
        self.config = import_yaml_config()
        self.path_raw_bank_data = self.config["path"]["data_url"]

        # Load df
        self.df = import_data(self.path_raw_bank_data)

    def test_type(self):
        # test if the functions returns an object of type Pipeline
        pipe1 = pipeline_ml_train_bank(df=self.df,
                                       ml_model=RandomForestClassifier())
        self.assertIsInstance(pipe1, Pipeline)
        pipe2 = pipeline_fit_transform_data_bank()
        self.assertIsInstance(pipe2, Pipeline)

    def test_exception_value(self):
        with self.assertRaises(Exception):
            # train is empty
            pipeline_ml_train_bank(pd.DataFrame(),
                                   ml_model=RandomForestClassifier())
        with self.assertRaises(TypeError):
            # ml_model is not filled in
            pipeline_ml_train_bank(self.df)


if __name__ == "__main__":
    unittest.main()
