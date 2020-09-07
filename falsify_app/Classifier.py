import pickle
import os.path
import numpy as np
from falsify_app.Utilities import Utilities


# This class manages classification tasks
class Classifier:

    # Main classifier method
    def classify(self):
        # Read pre trained catboost classification model
        base_dir = os.path.dirname(os.path.abspath(__file__))
        pkl_filename = f"{base_dir}/model/catboost_model.pkl"
        with open(pkl_filename, 'rb') as file:
            cat = pickle.load(file)

        # Calculate prediction and probability separately
        prediction = cat.predict(self)
        probability = np.max(cat.predict_proba(self))

        # return output
        return Utilities.prediction_stats(prediction, probability)
