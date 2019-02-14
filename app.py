from flask import Flask, request, render_template, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey

app = Flask(__name__)
app.config["SECRET_KEY"] = "oh-so-secret"

debug = DebugToolbarExtension(app)


@app.route("/")
def view_survey():

    
    return render_template('survey-intro.html', survey_title=satisfaction_survey.title,survey_instructions=satisfaction_survey.instructions)

@app.route("/question/<int:question_num>", methods=["POST"])
def view_question(question_num):
    next_question = question_num + 1

    the_question = satisfaction_survey.questions[question_num].question

    question_choices = satisfaction_survey.questions[question_num].choices

    if question_num > 0:
        answers = session['answers']
        answers.append(request.form.get("answer_input"))
        session['answers'] = answers
    else:
        session['answers'] = []


    return render_template('question.html', next_question = next_question, the_question=the_question, question_choices = question_choices )
