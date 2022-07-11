from flask import Flask, render_template, request, redirect 
app = Flask(__name__)

#display route
@app.route('/')
def hello_world():
    name = 'Patrick'
    return render_template('index.html', name = name)

#Action route
@app.route('/process_info', methods=['POST'])
def process_info():
    print(request.form['first_name'])
    #not what you want to do 
    return redirect('/tracking_info')

@app.route('/tracking_info')
def tracking_info():
    return render_template('tracking.html')

if __name__==("__main__"):
    app.run(debug=True)