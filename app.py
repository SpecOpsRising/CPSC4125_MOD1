from flask import Flask, render_template    # import the Flask class from the flask module
import requests                  # import the requests module to make HTTP requests
import logging                   # import the logging module to log error messages
app = Flask(__name__)       # create an instance of the Flask class/Create an app instance

URL = "https://xckd.com/info.0.json"
req = requests.get(url = URL)
Data = req.json()

@app.route('/')             # use the route() decorator to define a URL Route, in this case home '/'
def home():
    try:
        URL = "https://xckd.com/info.0.json"
        response = requests.get(url = URL)
        if (response.status_code != 200):
            raise ValueError(f"Error connecting to XKCD please try again later")
        Data = response.json()
        return render_template('index.html', data=Data)
    except ValueError as e:
        logging.error(f"ValueError with Home Page : {e}")
        return render_template('errorPage.html', errorMessage = e)

@app.route('/album')
def album():
    try:
        URL = "https://xckd.com/info.0.json"
        response = requests.get(url = URL)
        if (response.status_code != 200):
            raise ValueError(f"Error connecting to XKCD please try again later")
        Data = response.json()
        return render_template('Album.html', data=Data)
    except ValueError as e:
        logging.error(f"ValueError with Album Page : {e}")
        return render_template('errorPage.html', errorMessage = e)

@app.route('/selectComic/<comicNum>') # Second route with path parameter (part of the URL) called comicNum
def selectComic(comicNum):
    try:
        logging.debug(f"Select Comic URL with value : {comicNum}")  # log the value of comicNum
        if not comicNum.isdigit():
            raise ValueError(f"The requested comic number should be an integer. Received : {comicNum} instead")
        int(comicNum)
        if(int(comicNum) > 3000):
            raise ValueError(f"No comic available for number {comicNum}. Please try a number less than 3001")
        URL = "https://xckd.com/"+ comicNum +"/info.0.json"
        response = requests.get(url = URL)
        print(response.status_code)
        if (response.status_code != 200):
            raise ValueError(f"Error connecting to XKCD please try again later")
        Data = response.json()
        return render_template('selectComic.html', data=Data)
    except ValueError as e:
        logging.error(f"ValueError with Comic Select : {e}")
        return render_template('errorPage.html', errorMessage = e)
    except Exception as e:
        logging.error(f"Exception with Comic Select : {e}")  # log the error message
        return render_template('errorPage.html', errorMessage = e)
    # if(comicNum.isdigit() and int(comicNum) <= 3000):
    #     URL = "https://xckd.com/"+ comicNum +"/info.0.json"
    #     print(URL)
    #     req = requests.get(url = URL)
    #     Data = req.json()
    #     return render_template('selectComic.html', data=Data)
    # else:
    #     return render_template('errorPage.html')


if __name__ == '__main__':
    app.run(debug = True)               # call the run() method of the app object to run the server on the local development machine