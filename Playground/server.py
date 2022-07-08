from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def boxes():
    return render_template('index.html', num = 3, color = "blue")

@app.route('/play/<int:num>')
def multiply(num):
    return render_template('index.html', num = num, color ="blue") 

@app.route('/play/<int:num>/<string:color>')
def choose_color(num, color):
    return render_template('index.html', num = num, color = color)

if __name__=="__main__":
    app.run(debug=True)