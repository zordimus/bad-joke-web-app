import mysql.connector
import json

from random import randrange
from flask import Flask
app = Flask(__name__)

@app.route('/')
def bad_joke():

    f = open("file/jokes.txt", "r")
    jokes = f.readlines()

    line = randrange(0, len(jokes))
    print("***BAD JOKE IS***")
    print(jokes[line])
    print("*****")

    return '<p>*** BAD JOKE ***</p>' + jokes[line] + '<p>****************</p>'

if __name__ == "__main__":
  app.run(host ='0.0.0.0')    