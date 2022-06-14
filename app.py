# Import dependencies
from flask import Flask

# Create a New Flask App Instance
app = Flask(__name__)

# Create Flask Route
@app.route('/')
def hello_world():
    return 'Hello world'

# Run a Flask App
# Windows User must use set FLASK_APP=app.py in Anaconda Powershell before using this command
#export FLASK_APP=app.py
#flask run