from flask import Flask, render_template, request
from wtforms import Form, FloatField, validators
from compute import compute

app = Flask(__name__)

# Model
    # Here Q and R will be the two numbers coming in from the user
class InputForm(Form):
    q = FloatField(validators=[validators.InputRequired()])
    r = FloatField(validators=[validators.InputRequired()])

# View
@app.route('/hw1', methods=['GET', 'POST']) #app.route displays the path that is used to get to the file and also it contains the methods of how the file will be proccessed 
def index():
    form = InputForm(request.form) 
    if request.method == 'POST' and form.validate(): 
        q = form.q.data #The number inputed from the user is saved here 
        r = form.r.data #The number inputed from the user is saved here 
        
        s = compute(q,r) #compute is a funciton from a seperate file 
        return render_template("view_output.html", form=form, s=s) #Outputs the the html file with the inputed and computed information  
    else:
        return render_template("view_input.html", form=form) #Outputs to the screen the initial html file requesting the input values fromt the user

if __name__ == '__main__': #This is the entry point 
    app.run(debug=True)
