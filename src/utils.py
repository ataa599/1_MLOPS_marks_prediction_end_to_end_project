import os
import sys
import pickle
from src.exception import CustomException
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV

def save_object(file_path, obj):
    """
    Save a Python object to a file using pickle serialization.
    Creates the directory if it does not exist.
    """
    try:
        dir_path = os.path.dirname(file_path)

        # Create directory if it doesn't exist
        os.makedirs(dir_path, exist_ok=True)

        # Save object to file in binary format
        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        # Raise custom exception for error handling
        raise CustomException(e, sys)
    

def evaluate_models(X_train, y_train, X_test, y_test, models, param):
    """
    Evaluate multiple models using GridSearchCV for hyperparameter tuning.
    Returns a report dictionary with model names and their test R2 scores.
    """
    try:
        report = {}

        # Iterate over all models
        for i in range(len(list(models))):
            model = list(models.values())[i]
            para = param[list(models.keys())[i]]

            # Perform grid search for best hyperparameters
            gs = GridSearchCV(model, para, cv=3)
            gs.fit(X_train, y_train)

            # Set best parameters and retrain model
            model.set_params(**gs.best_params_)
            model.fit(X_train, y_train)

            # Predict on train and test sets
            y_train_pred = model.predict(X_train)
            y_test_pred = model.predict(X_test)

            # Calculate R2 scores
            train_model_score = r2_score(y_train, y_train_pred)
            test_model_score = r2_score(y_test, y_test_pred)

            # Store test score in report
            report[list(models.keys())[i]] = test_model_score

        return report

    except Exception as e:
        # Raise custom exception for error handling
        raise CustomException(e, sys)
    

def load_object(file_path):
    """
    Load a Python object from a pickle file.
    """
    try:
        # Open file and load object
        with open(file_path, "rb") as file_obj:
            return pickle.load(file_obj)
    except Exception as e:
        # Raise custom exception for error handling
        raise CustomException(e, sys)