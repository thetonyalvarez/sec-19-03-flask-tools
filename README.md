## TODO

### FS Two: Multiple Surveys
Make your system able to handle more than one survey — we’ve provided a second survey in surveys.py, and provided a dictionary mapping a survey “code” to the survey object.

Add a page that lets the user pick the survey they want to fill out: it should list the available surveys. It should then take you to the start page you made earlier, except for this survey.

You’ll need to figure out a good way to keep track of the survey the user is filling out as they move through the system.

### FS Three: Allow Comments for Some Questions
The personality quiz survey uses a new feature of the surveys: one of its questions is marked as allowing comments. For this question, you should show the radio buttons of the choices, as usual, but also a multiline text box where the visitor can enter a comment.

You should keep track of the textual comments as well as the radio-button choices. Figure out a good data structure to keep track of these things.

### FS Four: Much Nicer Thanks Page
Remake your “thanks!” page that is shown at the end of the survey—instead of just saying “thanks”, it should list each question and the provided answer (including any comments), like this:

Do you like pretzels? Yes
Are you hungry? No
Do you like burritos, and, if so, what is your favorite kind? Yes Carnitas

### FS Five: Prevent Re-Submission
We don’t want users to submit a survey more than once.

Of course, you could put something in the session that says they’ve completed that survey, and check for that, but the cookies that support the session typically only last as long as the browser is running — a user who quits their browser could re-answer the survey.

Figure out a way you could prevent a site visitor from re-filling-out a survey using cookies.

### FS Six: Lots of Other Ideas
Finish all of these? Want more challenges over the weeeknd? Here are lots of potential ideas to polish this:

add Bootstrap to your site
allow users to skip a question
allow users to go back to a previously-answered question on the survey and change their answer
ambitious, weekend project: make a web interface to allow users to create surveys through the web (you can mutate the surveys object to append a newly-designed survey to it)
