import pickle
import os.path


class TextFeaturizer:
    # Text featurization
    def featurization(self, column_name):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        pkl_filename = f"{base_dir}/model/tfidf_model.pkl"
        with open(pkl_filename, 'rb') as file:
            tfidf = pickle.load(file)

        pkl_filename = f"{base_dir}/model/tsvd_model.pkl"
        with open(pkl_filename, 'rb') as file:
            tsvd = pickle.load(file)

        self[f'{column_name}'] = tsvd.transform(tfidf.transform(self[f'{column_name}']))

        return self
