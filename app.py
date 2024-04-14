# Import Flask and Create Instance of the Flask Object
from flask import Flask, render_template
app = Flask(__name__, template_folder="templates", static_folder="static")




# User Defined Content
def contentSS():
    _content_buld_ss = ""

    # Add main build
    _content_buld_ss += "<main><div>Hello World! I'm using Flask.</div></main>"

    # Add styles
    _content_buld_ss += "<style></style>"

    return _content_buld_ss




# Function that returns content. App Route decorator to map URL route to function
@app.route("/")
def home():
    # # Call Method to Build Content
    # return contentSS()

    return render_template("index.html")

# Call File Using Python3 command
if __name__=='__main__':
    app.run(debug=True)
    