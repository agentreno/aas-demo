from flask import Flask, redirect, request
app = Flask(__name__)

posts = []

@app.route("/")
def index():
   # Render the main page
   output = """
      <link rel="stylesheet" href="/static/site.css">
      <h1>Shoddy Incorporated Message Board</h1>
      <h2>POSTS</h2>
      <div>
         <form action='sendmsg' method='post'>
            <input type='text' name='msg' autofocus>
            <input type='submit' value='Submit'>
         </form>
         <form action='refresh'>
            <input type='hidden' name='next' value='/'>
            <input type='submit' value='Refresh'>
         </form>
      </div>
   """
   for post in posts:
      output += "<p>" + post + "</p>"
   return output

@app.route("/sendmsg", methods=["POST"])
def post():
   # Add message to the list of posts and go back to the main page
   posts.append(request.form["msg"])
   return redirect("/")

@app.route("/refresh")
def refresh():
   nexturl = request.args.get("next").lower()
   return redirect(nexturl)

if __name__ == "__main__":
   app.run(debug=True)
