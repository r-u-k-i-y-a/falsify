# This class contains utility functions
class Utilities:

    # Function to pretty print final string
    def prediction_stats(value, probability):

        probability = probability * 100

        if value == 0:
            return f"The review is truthful with {probability:.3g}% confidence!"
        else:
            return f"The review is fake with {probability:.3g}% confidence!"
