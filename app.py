from flask import Flask, render_template, request
import requests

app = Flask(__name__)
app.static_folder = 'static'

# Function to get a random Jeopardy question
def get_random_jeopardy_question():
    url = "https://jservice.io/api/random"
    response = requests.get(url)
    if response.status_code == 200:
        question = response.json()[0]
        return question
    else:
        return None

@app.route("/", methods=["GET", "POST"])
def jeopardy_game():
    question = get_random_jeopardy_question()
    user_answer = ""
    result = ""
    #category = question.category.title.upper()

    if request.method == "POST":
        user_answer = request.form.get("answer", "").strip().lower()
        correct_answer = request.form.get("correct_answer", "").strip().lower()

        if user_answer == correct_answer:
            result = "Correct!"

    return render_template("index.html", question=question, user_answer=user_answer, result=result)

@app.route("/new_question", methods=["GET", "POST"])
def new_question():
    question = get_random_jeopardy_question()
    return render_template("index.html", question=question, user_answer="", result="")

if __name__ == "__main__":
    app.run(debug=True)

# from flask import Flask, render_template, request
# import requests
#
# app = Flask(__name__)
#
# # Function to get a random Jeopardy question
# def get_random_jeopardy_question():
#     url = "https://jservice.io/api/random"
#     response = requests.get(url)
#     if response.status_code == 200:
#         question = response.json()[0]
#         return question
#     else:
#         return None
#
# @app.route("/", methods=["GET", "POST"])
# def jeopardy_game():
#     question = get_random_jeopardy_question()
#     user_answer = ""
#     result = ""
#
#     if request.method == "POST":
#         user_answer = request.form.get("answer", "").strip().lower()
#         correct_answer = request.form.get("correct_answer", "").strip().lower()
#
#         if user_answer == correct_answer:
#             result = "Correct!"
#
#     return render_template("index.html", question=question, user_answer=user_answer, result=result)
#
# @app.route("/new_question", methods=["GET", "POST"])
# def new_question():
#     question = get_random_jeopardy_question()
#     return render_template("index.html", question=question, user_answer="", result="")
#
# if __name__ == "__main__":
#     app.run(debug=True)

# from flask import Flask, render_template, request
# import requests
#
# app = Flask(__name__)
#
# # Function to get a random Jeopardy question
# def get_random_jeopardy_question():
#     url = "https://jservice.io/api/random"
#     response = requests.get(url)
#     if response.status_code == 200:
#         question = response.json()[0]
#         return question
#     else:
#         return None
#
# @app.route("/", methods=["GET", "POST"])
# def jeopardy_game():
#     question = get_random_jeopardy_question()
#     user_answer = ""
#     result = ""
#
#     if request.method == "POST":
#         user_answer = request.form.get("answer", "").strip().lower()
#         correct_answer = question["answer"].strip().lower()
#
#         if user_answer == correct_answer:
#             result = "Correct!"
#         else:
#             result = "Sorry, the correct answer is: {}".format(correct_answer)
#
#     return render_template("index.html", question=question, user_answer=user_answer, result=result)
#
# if __name__ == "__main__":
#     app.run(debug=True)