from flask import Flask, jsonify, render_template, request
import requests

app = Flask(__name__)
app.static_folder = 'static'

def get_random_jeopardy_question():
    url = "https://jservice.io/api/random"
    response = requests.get(url)
    if response.status_code == 200:
        question = response.json()[0]
        return question
    else:
        return None

@app.route("/", methods=["GET"])
def jeopardy_game():
    question = get_random_jeopardy_question()
    user_answer = ""
    result = ""

    return render_template("index.html", question=question, user_answer=user_answer, result=result)

@app.route("/check_answer", methods=["POST"])
def check_answer():
    data = request.json

    user_answer = data.get("answer", "").strip().lower()
    correct_answer = data.get("correct_answer", "").strip().lower()

    if user_answer == correct_answer:
        result = "Good job! Correct"
    else:
        result = "Try again"

    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True)