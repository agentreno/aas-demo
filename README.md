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
  * Check you have git, a text editor and Python installed
  * Clone the repo to your local machine
  * Run the flask web app and confirm that the Hello World page is displayed (python app.py)
  * Add a new route at /message which displays a message of your choice

2. Vulnerability review
  * Look at the source code for the web application (app.py) - can you see any 
    security problems?
  * Find 3 vulnerabilities and confirm the answers with the trainer, ask for 
    hints if needed!
  * Open the web application and try to exploit these vulnerabilities
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

5. Monitoring
  * Add log output to identify an attempt to add a script tag to messages
  * Send the log output to Loggly
