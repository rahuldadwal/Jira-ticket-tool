Assignment 2: Jira task application

To run the application we need to apply some changes first:

In file: test.py

1: we need to add jira domain in {"server": "https://your-domain.atlassian.net"} to make connection with jira
 
2: we need to add email and api token in "basic_auth=("example@gmail.com", "jira_token")" to authenticate jira application

To run application:

-	run "python test.py" in Powershell or terminal

A message in shell informs you that application is Running on "http://127.0.0.1:5000/"
Copy the given link in shell "http://127.0.0.1:5000/" and paste it on browser this will run the application

On web page:

Add Project name or Project KEY, Title, Description of the issue to be created
If issue is new it will create a issue on jira
If issue title is already existing it will throw error "Already Exist"

