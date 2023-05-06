"""We train and test our prediction model"""

#  MANAGEMENT ENVIRONMENT --------------------------------
import sys
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    ConfusionMatrixDisplay,
    #  confusion_matrix
)
from sklearn.model_selection import GridSearchCV
from .build_pipeline import pipeline_ml_train_bank
# from joblib import dump


def random_forest_bank(train, test, NTREES: int = 0) -> None:
    """Random forest training for the prediction of
       a deposit or not in the bank """

    X_train = train.drop("deposit", axis="columns")
    y_train = train["deposit"]

    pipeline_rdmf_train = pipeline_ml_train_bank(X_train,
                                                 RandomForestClassifier())

    if NTREES:
        try:
            n_trees = int(NTREES)
            if (NTREES < 0) or (n_trees == 0):
                raise ValueError("The 'n_estimators' parameter of "
                                 "RandomForestClassifier must be an int "
                                 "in the range [1, inf). Got {} instead."
                                 .format(NTREES))
        except ValueError as e:
            print("Error:", e)
            sys.exit(1)

        print()
        print(f"You have chosen a number of trees equal to {n_trees}")
        print()
        print("Model being optimized...")

        param_trees = {"classifier__n_estimators": [n_trees]}

        # Create a GridSearchCV object to perform the search
        grid_search = GridSearchCV(pipeline_rdmf_train,
                                   param_grid=param_trees,
                                   cv=5)

        # Train the research grid on the training data
        grid_search.fit(X_train, y_train)

    else:
        print()
        print(
            "The (finally) selected model will be "
            "determined by a research grid"
        )
        print()
        print("Model being optimized...")

        # Define the hyperparameters to be tested
        param_grid = {
            # Number of trees in the random forest
            "classifier__n_estimators": [10, 25, 50],
            # Maximum depth of each tree
            "classifier__max_depth": [None, 5, 10],
            # Minimum number of observations required
            # to split an internal node
            "classifier__min_samples_split": [2, 5, 10],
            # Minimum number of observations required to be a leaf
            "classifier__min_samples_leaf": [1, 2, 4],
        }

        # Create a GridSearchCV object to perform the search
        grid_search = GridSearchCV(pipeline_rdmf_train,
                                   param_grid=param_grid,
                                   cv=5)

        # Train the research grid on the training data
        grid_search.fit(X_train, y_train)

    print()
    print("="*15, "DONE", "="*15)

    optimal_n_trees = grid_search.best_params_['classifier__n_estimators']

    if NTREES:
        print()
        print("Number of trees chosen:", optimal_n_trees)
        print("Cross-validation score:",
              str(round(grid_search.best_score_*100, 1))+'%')
        print()

    else:
        print()
        print("Number of trees retained:", optimal_n_trees)
        print("Best cross-validation score:",
              str(round(grid_search.best_score_*100, 1))+'%')
        print()

    X_test = test.drop("deposit", axis="columns")
    y_test = test["deposit"]

    y_pred = grid_search.best_estimator_.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)

    # print()
    # score_test = grid_search.score(X_test, y_test)
    # print("Score test", score_test)

    print("==" * 20)
    print(
        f"{round(accuracy*100, 1)}% of correct answers on test data"
    )
    print("==" * 20)

    # print()
    # print("confusion matrix")
    # print()
    # print(confusion_matrix(y_test, y_pred, labels=["no", "yes"]))

    # Save the best model
    # dump(grid_search.best_estimator_, "model/random_forest_bank.joblib")

    cfs_matrix = ConfusionMatrixDisplay.from_estimator(
        grid_search.best_estimator_,
        X_test,
        y_test,
        labels=["no", "yes"],
        display_labels=["No", "Yes"],
        cmap=plt.cm.Blues,
        normalize="true",
    )

    cfs_matrix.ax_.set_title("Normalized confusion matrix")

    # plt.savefig("static/confusion_matrix_rdmf_bank.png")
    # print(cfs_matrix.confusion_matrix)

    plt.show()
