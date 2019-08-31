from flask import Flask, render_template  
app = Flask(__name__) 

print(__name__)

@app.route('/')          
def index():
    return render_template("checker.html", num1=8, num2= 8) 



@app.route('/<x>')          
def hello_2(x):
    return render_template("checker.html", phrase="hello", num1=int(x), num2= 8) 


@app.route('/<x>/<y>')          
def hello_3(x,y):
    return render_template("checker.html", phrase="hello", num1=int(x), num2= int(y)) 




# @app.route('/<x>/<y>/')          
# def hello_3(xxx,zz):
#     return render_template("checker.html", phrase="hello", times=int(x), times=int(y)) 



if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.


