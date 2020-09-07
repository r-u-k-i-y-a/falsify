import pickle
import os.path


# This class manages text featurization
class TextFeaturizer:
    # Text featurization
    def featurization(self, column_name):
        # Load pre trained TF-IDF vector generator model
        base_dir = os.path.dirname(os.path.abspath(__file__))
        pkl_filename = f"{base_dir}/model/tfidf_model.pkl"
        with open(pkl_filename, 'rb') as file:
            tfidf = pickle.load(file)

        # Load pre trained TSVD model
        pkl_filename = f"{base_dir}/model/tsvd_model.pkl"
        with open(pkl_filename, 'rb') as file:
            tsvd = pickle.load(file)

        # Generate features for specified column
        self[f'{column_name}'] = tsvd.transform(tfidf.transform(self[f'{column_name}']))

        # return output
        return self
