from falsify_app.TextProcessor import TextProcessor
from falsify_app.TextFeaturizer import TextFeaturizer
from falsify_app.Classifier import Classifier


# This class manages the execution procedure
class Runner:

    @staticmethod
    def classify_review(data):
        # Execute reprocessing techniques
        data = TextProcessor.tokenize_string_column(data, 'reviewContent')
        data = TextProcessor.clean_string_column(data, 'reviewContent')
        data = TextFeaturizer.featurization(data, 'reviewContent')
        data = Classifier.classify(data)

        # Return output
        return data
