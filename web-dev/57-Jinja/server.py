from flask import Flask, render_template
import random
import datetime

app = Flask(__name__)

@app.route("/")

def index():
    random_num = random.randint(1,10)
    current_year = datetime.datetime.now().year
    return render_template('index2.html', rand=random_num, current_year=current_year)

if __name__ == '__main__':
    app.run(debug=True)