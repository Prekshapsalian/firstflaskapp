#first to import flask flask is class
from flask import Flask, render_template
#create  an instance/obj of the class
app= Flask(__name__)
#route decorator to tell flask what url should trigger our function
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/about')
def about():
    return render_template('about.html')

if __name__=='__main__':
    app.run(debug=True)#run the code it will automatically reload the server when code changes
# shift ! basic code will be displayed