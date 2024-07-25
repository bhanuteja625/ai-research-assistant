from flask import Flask, request, render_template, session, redirect, url_for
from researcher import Researcher  # Make sure the Researcher class has to_dict and from_dict methods
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Make sure to change this to a truly secret key in production

@app.before_request
def initialize_session():
    researcher = Researcher()
    session["researcher"] = researcher.to_dict()
    session["user"] = ["Hey AI assistant!"]
    session["apprentice"] = ["Hello. How can I help you?"]

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'researcher' in session:
        researcher_dict = session['researcher']
        research_apprentice = Researcher.from_dict(researcher_dict)

    if request.method == 'POST':
        research_query_input = request.form.get('research_query')
        robowiz_output = research_apprentice.research(research_query_input)
        session["user"].append(research_query_input)
        session["apprentice"].append(robowiz_output)

        session['researcher'] = research_apprentice.to_dict()

    return render_template('index.html', conversation=zip(session['user'], session['apprentice']))

if __name__ == '__main__':
    app.run(debug=True)
