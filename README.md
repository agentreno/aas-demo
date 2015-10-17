Aims
====
Be able to build and read a basic web application
Understand some web application vulnerabilities and learn how to fix them
Learn how to deploy a web application to:
   1. Dedicated hardware
   2. Infrastructure as a Service (IaaS) e.g. Amazon Web Services (AWS)
   3. Platform as a Service (PaaS) e.g. Heroku
Use software as a service (SaaS) to enhance the application:
   1. Set up monitoring SaaS using Loggly

Method
======
1. App familiarisation and Flask/Python recap
  * Clone the repository and install dependencies
  * Start the app and view in a browser
  * Add a new route with a simple message
2. Vulnerability review
  * Review the app and source and find 3 vulnerabilities
  * Demonstrate exploitation of those vulnerabilities
  * Mitigate them
3. Deployment
  * Upload the app to dedicated hardware (e.g. Raspberry Pi) and run the app
  * Upload the app to an EC2 instance on AWS and run the app
  * Upload the app to Heroku
4. Monitoring
  * Add log output to identify an attempt to add a script tag to messages
  * Send the log output to Loggly
