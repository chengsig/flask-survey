from flask import Flask, request, render_template, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey

app = Flask(__name__)
app.config["SECRET_KEY"] = "oh-so-secret"

debug = DebugToolbarExtension(app)


@app.route("/")
def view_survey():

    return render_template('survey-intro.html', survey_title=satisfaction_survey.title,survey_instructions=satisfaction_survey.instructions)