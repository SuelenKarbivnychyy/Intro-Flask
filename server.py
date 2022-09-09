"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Home page."""

    return""" "<!doctype html><html>Hi! This is the home page.</html>"<p>  
    <a href="/hello"> Click me to go to Complimentes Main page.</a></p> <p>
    <a href="/insult"> Or click me to go to Insults Main page.</a> </p> """#I added this line as "Make the /hello Route Easier to Access"

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
          <input type="submit" value="Submit">
          <p>
          <label for="select-complimet">Choose one compliment</label>          
          <select name="compliment" id="select-compliment">
            <option value="pretty">Pretty</option>
            <option value="fantastic">Fantastic</option>
            <option value="amazing">Amazing</option>
            <option value="sweet">Sweet</option>
          </p>  
          </select> 
        </form>
      </body>
    </html>
    """


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    # compliment = choice(AWESOMENESS)
    compliment = request.args.get("compliment") #added this code to Allow Users to Choose Their Compliments
  

    return f"""
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {player}! I think you're {compliment}!
        <p><a href="/">Click me to go to Home page</a></p>
      </body>
    </html>
    """

# this code down for insult page

@app.route('/insult')
def say_hello_insult():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>        
        <h1>Hi There!</h1>  
        <form action="/diss">
          What's your name? <input type="text" name="person">
          <input type="submit" value="Submit">
          <p>
          <label for="select-insult">Choose one insult</label>
          <select name="insult" id="select-insult">
            <option value="nuts">Nuts</option>
            <option value="crazy">Crazy</option>
            <option value="idiot">Idiot</option>
            <option value="mad">Mad</option> 
          </p>
          </select>  
        </form>
      </body>
    </html>
    """

@app.route('/diss')
def insults_person():

    player = request.args.get("person")

    insult = request.args.get("insult")

    return f"""
    <!doctype html>
    <html>
      <head>
        <title>A Insult</title>
      </head>
      <body>
        Hi, {player}! I think you're {insult}!
        <p><a href="/">Click me to go to Home page</a></p>
      </body>
    </html>
    """

if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
