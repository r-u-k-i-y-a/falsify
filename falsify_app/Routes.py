from flask import request, render_template, redirect, url_for
from falsify_app import app
import pandas as pd
from falsify_app.Runner import Runner


# Test method to verify the status of API
@app.route("/falsify/health", methods=['GET', 'POST'])
def health():
    # Return functioning response
    return 'Falsify is Alive!'


@app.route("/falsify/index", methods=['GET', 'POST'])
def index():
    # Return functioning response
    return render_template('index.html')


@app.route("/falsify/predict", methods=['POST'])
def predict():
    user_rating = request.form['user-rating']
    user_review_count = request.form['user-review-count']
    review_content = request.form['review-content']
    restaurant_rating = request.form['restaurant-rating']
    restaurant_review_count = request.form['restaurant-review-count']

    # Create array from data received
    data = {
        'reviewContent': [review_content],
        'rating': [user_rating],
        'reviewCount': [user_review_count],
        'restaurantRating': [restaurant_rating],
        'restaurantReviewsCount': [restaurant_review_count]
    }

    # Create DataFrame from array and get results
    df = Runner.classify_review(pd.DataFrame(data))

    return redirect(url_for('index', data=df))
