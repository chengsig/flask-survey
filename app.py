from flask import Flask, request, render_template, session, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension

from surveys import satisfaction_survey

app = Flask(__name__)
app.config["SECRET_KEY"] = "oh-so-secret"

debug = DebugToolbarExtension(app)


@app.route("/")
def view_survey():

    
    return render_template(
        'survey-intro.html',
        survey_title=satisfaction_survey.title,
        survey_instructions=satisfaction_survey.instructions)

@app.route("/question/<int:question_num>", methods=["POST"])
def view_question(question_num):

    # if question_num == 0:
    #     session['answers'] = []
    # elif question_num >= len(satisfaction_survey.questions):
    #     return redirect('/thanks')
    # else:
    #     answers = session['answers']
    #     answers.append(request.form.get("answer_input"))
    #     session['answers'] = answers

    if question_num >= len(satisfaction_survey.questions):
         return redirect('/thanks')

    if question_num == 0:
        session['answers'] = []
    else:
        answers = session['answers']
        answers.append(request.form.get("answer_input"))
        session['answers'] = answers

    next_question = question_num + 1

    the_question = satisfaction_survey.questions[question_num].question

    question_choices = satisfaction_survey.questions[question_num].choices

    return render_template('question.html', next_question = next_question, the_question=the_question, question_choices = question_choices )

@app.route('/thanks')
def say_thanks():
    return render_template("thanks.html")