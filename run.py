# Import flask app
from falsify_app import app

# Flask run configs
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
