from flask import Flask, render_template, redirect, url_for, request
# create instance of flask class
app = Flask("__main__") # name of application's module

# route decorator
# always write a function after decorator
# these routes are what we call endpoints
@app.route('/hello')
def hello():
    # """ like this vv
    # allows for more readable strings
    # without breaking indentation rules
    # can return plain html to be rendered on the page
    # we can also do inline styling
    # displaying a simple html msg,
    # what if I want to render a whole html page/template?
    return """
        <div style="background-color: black">
            <h1 style="color: pink; padding: 20px">Marina was here!</h1>
        </div>
        """

@app.route('/goodbye')
def goodbye():
    return """
        <div style="background-color: orange">
            <h1 style="color: teal">goodbye cruel world :(</h1>
        </div>
        """

# we can use flask.render_template
# to render an html page (like index.html).
# path to template has to be ./templates/<filename>.html
@app.route('/rendertemp')
def renderhtml():
   return render_template('index.html')

# what if I want to render variables?
# placeholder <name>
# any path that is not defined will go here...
# this is an empty route.
@app.route('/<name>')
def name(name):
   # pass the given name to the {{name}} variable in html.
   # {{}} is jinja notation, basically plugging python code
   # into html for example.
   return render_template('name.html', name=name)
   
# if given no path
# prevent 404 msgs
@app.route('/')
def myredir():
   return render_template('redirect.html')
   
# HTTP Methods
# POST <--
# GET  <-- most common requests
# HEAD - same as GET, but does not have response body.
# ex: GET /users: return list of users
#     HEAD /users: makes same request, does not return list (aka body)
# if method is not specified, assumes GET by default.

@app.route('/login', methods=['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('success', name=user))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success', name=user))

@app.route('/success/<name>')
def success(name):
   return f'welcome {name}!!!'
   
if __name__ == "__main__":
  app.run(debug=True) 

# Debugger is great, detects changes in the code
# as the server runs..

# 1st way to run file:
# set FLASK_APP=app.py
# 1st way to debug:
# set FLASK_APP=development
# in linux use 'export' instead of'set' (this is an env variable)

# 2nd way to run and debug:
# if __name__ == "__main__":
#   app.run(debug=True)

# run command:
# like any python file:
# python app.py