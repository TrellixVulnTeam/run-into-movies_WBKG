from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
def firstpage():
    return render_template('firstpage.html')

@app.route('/signup/')
def signup():
    return render_template('signup.html')

@app.route('/index/')
def index():
    return render_template('index.html')

if __name__=='__main__':
    app.run(debug=True)
