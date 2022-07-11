from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = '12345'

#display route
@app.route('/')
def hello_world():
    name = 'Patrick'
    return render_template('index.html', name = name)

#Action route
@app.route('/process_info', methods=['POST'])
def process_info():
    #request.form request info from the html page/webpage
    print(f"You have now purchased a new {request.form['item']}")

    # credit_card_number = request.form['credit_card_number']
    #session is a dictionary
    session['ccn'] = str(request.form['credit_card_number'])[-4:]
    #not what you want to do 
    # return render_template('index.html')
    #what you want to do below...
    return redirect('/tracking_info')

@app.route('/tracking_info')
def tracking_info():
    # print('Your credit card number is')
    # print(session['ccn'])

    # if session['ccn']: will give key error

    if 'ccn' not in session:
        return redirect('/')

    return render_template('tracking.html')

if __name__==("__main__"):
    app.run(debug=True)