# imports
from falsify_app import app

# Specify IP address and port for Flask to run
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
