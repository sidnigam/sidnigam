from flask import Flask, render_template
import requests
import random

app = Flask(__name__)

@app.route("/")
def index():
    age = random.randint(1,10)
    gender = "male"
    return render_template('index2.html', age = age, gender = gender)


@app.route("/<name>")
def guesser(name):
    age_url = f"https://api.agify.io?name={name}"
    gender_url = f"https://api.genderize.io?name={name}"
    response = requests.get(gender_url)
    gender = response.json()["gender"]
    response = requests.get(age_url)
    age = response.json()["age"]
    return render_template('index2.html', name = name, age = age, gender = gender)


if __name__ == '__main__':
    app.run(debug=True)
