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
  #app.run(host ='0.0.0.0')
  # For flask running in Heroku
  # Bind to PORT if defined, otherwise default to 5000.
  port = int(os.environ.get('PORT', 5000))
  app.run(host='0.0.0.0', port=port)