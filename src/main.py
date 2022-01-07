from random import randrange
from flask import Flask, render_template, redirect, url_for, request
import os

app = Flask(__name__)
#jokes = open("file/jokes.txt", "r").readlines()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/badJoke',methods = ['GET'])
def bad_joke():

    f = open("file/jokes.txt", "r")
    jokes = f.readlines()

    line = randrange(0, len(jokes))

    f.close()
    return render_template('badJoke.html', joke=jokes[line])


if __name__ == "__main__":

  #app.run(host ='0.0.0.0')
  # For flask running in Heroku
  # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)