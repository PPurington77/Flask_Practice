# Pre-req
```
pip install pipenv
```
# Check List
- create a folder/directory for your assignment
- navigate into that folder
- create you virtual env
```
    pipenv install flask
```
- `WARNING` check for the files 'pipfile and 'pipfile.lock'
    - If you don't see these you need to fix it right away
- launch the virtual environment
```
pipenv shell
```
- create a server.py file
```py
from flask import Flask, render_template, request, redirect   
app = Flask(__name__)    
@app.route('/')         

#THIS WILL MOVE IN THE FUTURE

def hello_world():
    return 'Hello World!'  

#END OF MOVING AREA
if __name__=="__main__":   different module    
    app.run(debug=True)    # Run the app in debug mode.
```
