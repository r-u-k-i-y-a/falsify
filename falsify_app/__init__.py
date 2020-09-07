# Python package initialization file
# Imports
from flask import Flask

# Create flask object
app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'

# Routes file imported after initializing flask to avoid cyclic import crash
from falsify_app import Routes
