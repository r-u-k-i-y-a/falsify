import pickle
import os.path
import numpy as np
from falsify_app.Utilities import Utilities


class Classifier:
    def classify(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        pkl_filename = f"{base_dir}/model/catboost_model.pkl"
        with open(pkl_filename, 'rb') as file:
            cat = pickle.load(file)

        prediction = cat.predict(self)
        probability = np.max(cat.predict_proba(self))

        return Utilities.prediction_stats(prediction, probability)
