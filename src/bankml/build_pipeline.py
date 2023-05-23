"""This file contains some pipeline to preprocess the data"""

#  MANAGEMENT ENVIRONMENT --------------------------------
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from bankml.import_data import import_data


def pipeline_fit_transform_data_bank() -> Pipeline:
    """Creation of a pipeline to pre-process training data"""

    # config = import_yaml_config()
    # path_raw_bank_data = config["path"]["data_url"]

    df = import_data()

    # test_fraction = config["model"]["test_fraction"]
    test_fraction = 0.3

    train, _ = train_test_split(
        df, test_size=test_fraction, stratify=df["deposit"], random_state=42
    )

    train = train.drop("deposit", axis="columns")

    # Select columns of type object or str
    colonnes_object = train.select_dtypes(include=["object"]).columns.tolist()

    # Select columns of type int or float
    colonnes_int = train.select_dtypes(include=["float",
                                                "int"]).columns.tolist()

    numeric_transformer = Pipeline(
        steps=[("imputer", SimpleImputer(strategy="mean")),
               ("scaler", MinMaxScaler())]
    )

    categorical_transformer = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="most_frequent",
                                      fill_value="missing")),
            ("onehot", OneHotEncoder(handle_unknown="ignore")),
        ]
    )

    preprocessor = ColumnTransformer(
        transformers=[
            ("num", numeric_transformer, colonnes_int),
            ("cat", categorical_transformer, colonnes_object),
        ],
        remainder="passthrough",
    )

    preprocessing_pipeline = Pipeline([("preprocessor", preprocessor)])

    preprocessing_pipeline.fit_transform(train)

    return preprocessing_pipeline


def pipeline_ml_train_bank(df, ml_model) -> Pipeline:
    """Creation of a pipeline to pre-process data
    and use a machine learning model"""

    # We check if df is empty with the empty method
    if df.empty:
        raise ValueError("df is empty")

    # Select columns of type object or str
    colonnes_object = df.select_dtypes(include=["object"]).columns.tolist()

    # Select columns of type int or float
    colonnes_int = df.select_dtypes(include=["int", "float"]).columns.tolist()

    numeric_transformer = Pipeline(
        steps=[("imputer", SimpleImputer(strategy="mean")),
               ("scaler", MinMaxScaler())]
    )

    categorical_transformer = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="most_frequent",
                                      fill_value="missing")),
            ("onehot", OneHotEncoder(handle_unknown="ignore")),
        ]
    )

    preprocessor = ColumnTransformer(
        transformers=[
            ("num", numeric_transformer, colonnes_int),
            ("cat", categorical_transformer, colonnes_object),
        ],
        remainder="passthrough",
    )

    pipeline_ml = Pipeline([("preprocessor", preprocessor),
                            ("classifier", ml_model)])

    return pipeline_ml
