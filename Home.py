
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def home():

    return render_template('index.html')

@app.route('/lobby')

def about():
      
      return render_template('skills.html')

@app.route('/Land')


def lands():

    return render_template('Lands.html')

if __name__ == '__main__':
        app.run(debug=True)

