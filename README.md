Aims
====
Be able to build and read a basic web application

Understand some web application vulnerabilities and learn how to fix them

Learn how to deploy web applications to dedicated hardware, IaaS, PaaS and
use SaaS.

Introduction
============

In this exercise, you will find 3 vulnerabilities in a sample web application,
demonstrate how to exploit them, and fix them. When this is done, you will
deploy the app to:

* A Raspberry Pi
* An IaaS solution (Amazon Web Services - AWS EC2)
* A PaaS solution (Heroku)

You will then use Loggly to provide basic audit and monitoring.

Method
======
1. App familiarisation and Flask/Python recap
  * Check you have git, a text editor, Python and pip installed.
  * Clone the repo to your local machine.
  * From the project folder, install the dependencies: `sudo pip install
    -r requirements.txt`
  * Run the flask web app and confirm that the Hello World page is displayed:
    `python app.py`
  * Add a new route at /message which displays a message of your choice.
    Look at the code in app.py and re-use fragments of the code to
    achieve this. You could also try the
    [Flask documentation](http://flask.pocoo.org/docs/0.10/quickstart/)

2. Vulnerability review
  * Look at the source code for the web application (app.py) - can you see any
    security problems?
  * Find 3 vulnerabilities and confirm the answers with the trainer, ask for
    hints if needed! You might get some ideas from the
    [OWASP Top 10](https://www.owasp.org/index.php/Top_10_2013-Top_10)
  * Open the web application and try to exploit these vulnerabilities.
  * Demonstrate exploitation of each vulnerability to the trainer, again ask
    for hints if needed!

3. Vulnerability mitigation
  * Make changes to the source code to fix the vulnerabilities
  * Test the exploits from earlier to show they no longer work
  * Show your changes to the trainer

4. Deployment
  * Deploy your code to a Raspberry Pi
  * Deploy your code to an AWS EC2 instance
  * Deploy your code to Heroku
    * You'll need to have a [Heroku account](https://signup.heroku.com/) and
      have the [Heroku toolbelt]
      (https://devcenter.heroku.com/articles/heroku-command) installed.
    * Follow this
      [guide](https://community.nitrous.io/tutorials/deploying-a-flask-application-to-heroku)
      bearing in mind that:
        * You already have a git repo but may not have committed all of
          your changes.
        * There is already a requirements.txt file but you need the
          gunicorn dependency.
    * Alternatively, if you're having trouble or didn't implement all of
      the security patches, create an app with `heroku create` and push
      a prepared branch to Heroku with `git checkout -b heroku
      origin/heroku` and `git push heroku heroku:master`. These commands
      check out patched code, Heroku deployment files (mainly the
      Procfile which tells Heroku how to run the app) and pushes the
      local 'heroku' branch to the remote 'master' branch.

5. Monitoring
  * Add log output to identify an attempt to add a script tag to messages
  * Send the log output to Loggly

Extra Credit
============
Add more unit tests to tests.py to detect these vulnerabilities. Then
add a git pre-commit hook that runs these tests and prevents a commit
with a scary message to the developer if any tests fail.
