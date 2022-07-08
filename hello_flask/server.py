from flask import Flask, render_template # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return render_template('index.html', phrase = 'hello', times = 5)

@app.route('/dojo')
def dojo():
    return 'dojo'

@app.route('/hello/<string:name>')
def hello(name):
    print("Hello " + name)
    return "Hello " + name

@app.route('/repeat/<int:number>/<string:name>')
def route(number, name):
    return f"{number * name}"

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

