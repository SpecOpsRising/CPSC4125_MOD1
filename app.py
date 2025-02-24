from flask import Flask, render_template    # import the Flask class from the flask module
import requests                  # import the requests module to make HTTP requests
import logging                   # import the logging module to log error messages
app = Flask(__name__)       # create an instance of the Flask class/Create an app instance

@app.route('/')             #Home route that allows you access to the home page and lets you link to the other pages of the website
def home():
    try:
        return render_template('index.html')
    except ValueError as e:
        logging.error(f"ValueError with Home Page : {e}")
        return render_template('errorPage.html', errorMessage = e)

@app.route('/breeds')
def breeds():
    try:
        URL = "https://dogapi.dog/api/v2/breeds" #This project uses the Dog API to get information about dog breeds
        response = requests.get(url = URL)
        if (response.status_code != 200):
            raise ValueError(f"Error connecting to Dog API please try again later")
        return render_template('breeds.html', data=response.json())
    except ValueError as e:
        logging.error(f"ValueError with Breed List Page : {e}")
        return render_template('errorPage.html', errorMessage = e)

@app.route('/selectedBreed/<id>') #Allows you to choose a breed from the breeds data given by the Dog API. Nav button defaults to the first breed.
def selectBreed(id):
    try:
        logging.debug(f"Select Breed URL with value : {id}")
        if (id == None or id == ""):
            raise ValueError(f"The requested breed id is not valid, please choose from the available list. Inputed id: {id}")
        URL = "https://dogapi.dog/api/v2/breeds/"+ id
        response = requests.get(url = URL)
        if (response.status_code != 200):
            raise ValueError(f"Error connecting to Dog API please try again later")
        return render_template('selectedBreed.html', data=response.json())
    except ValueError as e:
        logging.error(f"ValueError with Breed Select : {e}")
        return render_template('errorPage.html', errorMessage = e)
    except Exception as e:
        logging.error(f"Exception with Breed Select : {e}")
        return render_template('errorPage.html', errorMessage = e)
    
@app.route('/facts/<limit>')
def facts(limit):
    try:
        logging.debug(f"Facts URL with value : {limit}")
        if limit.isdigit() == False:
            raise ValueError(f"The input is not a number please input a number. Recieved: {limit}")
        URL = "https://dogapi.dog/api/v2/facts?limit=" + limit
        response = requests.get(url = URL)
        if (response.status_code != 200):
            raise ValueError(f"Error connecting to Dog API please try again later")
        return render_template('facts.html', data=response.json())
    except ValueError as e:
        logging.error(f"ValueError with Facts Page : {e}")
        return render_template('errorPage.html', errorMessage = e)
    except Exception as e:
        logging.error(f"Exception with Facts Page : {e}")
        return render_template('errorPage.html', errorMessage = e)


if __name__ == '__main__':
    app.run(debug = True)               # call the run() method of the app object to run the server on the local development machine