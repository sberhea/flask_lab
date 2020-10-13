"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic']

DISS = [
    'awful', 'horrible', 'not-so-great']

@app.route('/')
def start_here():
    """Home page."""

    return """
    <!doctype html>
    <html>
    <p>Hi! This is the home page.</p>
    <a href="/hello"> Hello page </a>
    </html>
    """


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          What's your name? <input type="text" name="person">
          </br>
          <label for=compliments">Choose a Compliment:</label>
        <select name = "compliments" id = "compliments">
          <option value="awesome">Awesome</option>
          <option value="terrific">Terrific</option>
          <option value="fantastic">Fantastic</option>
        </select>
        <input type="submit" value="Submit">
        </form>
        <button><a href="/diss">Want a diss instead?</a></button>
      </body>
    </html>
    """

@app.route('/diss')
def diss_person():
  """Diss user"""
  # player = request.args.get("person")
  
  diss = choice(DISS)

  return """
  <!doctype html>
  <html>
    <head>
      <title>A Diss</title>
    </head>
    <body>
      Hi, I think you're {}!
    </body>
  </html>
  """.format(diss)

@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    compliment = request.args.get("compliments")

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {}! I think you're {}!
      </body>
    </html>
    """.format(player, compliment)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
