from flask import Flask, render_template    # import the Flask class from the flask module
import requests                  # import the requests module to make HTTP requests
app = Flask(__name__)       # create an instance of the Flask class/Create an app instance

URL = "https://xckd.com/info.0.json"
req = requests.get(url = URL)
Data = req.json()

@app.route('/')             # use the route() decorator to define a URL Route, in this case home '/'
def home():
    return render_template('index.html')

@app.route('/album')  # Second route with path parameter (part of the URL) called who
def album():
    return render_template('album.html', data=Data)

if __name__ == '__main__':
    app.run(debug = True)               # call the run() method of the app object to run the server on the local development machine