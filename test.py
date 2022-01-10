from flask import Flask, render_template, request, flash
from jira import JIRA

app = Flask(__name__)

app.secret_key = "abc"

options = {"server": "https://your-domain.atlassian.net"}                   #Changes should be done here
jira = JIRA(options, basic_auth=("email", "api_token"))                     #and here

#
#mongodb app configurations and connections will be written here
#
#

@app.route("/", methods=["GET", "POST"])
def form():

    error = None

    if request.method == "POST":
        print("Executing")
        
        project = request.form.get("projectid")
        title = request.form.get("title")
        description = request.form.get("description")
        
        jql = "(Summary ~ '{}')".format(title)
        a = jira.search_issues(jql)

        if len(a) > 0:
            print('Error')
            flash("Already Exist")
        else:
            create_request(project, title, description, jira)
            print ('raised')
            flash("Successfully Raised")
    return render_template("form.html")

def create_request(project, title, description, jira):
    issue_dict = {
            "project": project,
            'issuetype': {
                "name": "Task"
            },
            "summary": title,
            "description": description
        }
    jira.create_issue(fields=issue_dict)
    return('Ticket Raised!')

#
# we can write mongo db queries here
#
# 

if __name__ == "__main__":
    app.run(debug=True)