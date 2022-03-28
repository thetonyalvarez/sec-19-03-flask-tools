from flask import Flask, request, render_template, redirect, session, flash, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey

app = Flask(__name__)

app.config['SECRET_KEY'] = "very-cool"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

RESPONSES = ""

@app.route("/")
def show_home():
	"""Survey homepage."""

	return render_template('start_survey.html',
	survey=survey
	)

@app.route("/start", methods=["POST"])
def start_survey():
	"""Clear RESPONSES list"""

	# Using Session method to store answers
	session[RESPONSES] = []
	return redirect("/questions/0")


@app.route("/questions")
def show_question_form():
	return render_template('questions.html')

@app.route("/questions/<int:qIndex>")
def show_question(qIndex):
	"""Show question."""
	responses = session.get(RESPONSES)

	if (responses is None):
		flash("Please click on the button to start the survey.")
		return redirect("/")

	# if a user attempts to skip a question by manually entering a url:
	if len(responses) == len(survey.questions):
		return redirect("/survey-complete")

	if len(responses) != qIndex:
		flash("Please answer the question to move forward.")
		return redirect(f"/questions/{len(responses)}")

	question = survey.questions[qIndex]

	return render_template("questions.html",
	question = question,
	question_id = qIndex
	)

@app.route("/answer", methods=['POST'])
def handle_answer():
	
	# get choice from question
	choice = request.form['choice']
	
	# append answer to RESPONSES list
	responses = session[RESPONSES]
	responses.append(choice)
	session[RESPONSES] = responses

	if (len(responses) == len(survey.questions)):
		return redirect("/survey-complete")

	# redirect to question template
	return redirect(f"/questions/{len(responses)}")

@app.route("/survey-complete")
def end_survey():
	# raise
	return render_template("survey-complete.html")