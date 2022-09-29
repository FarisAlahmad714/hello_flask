from flask import Flask ,  render_template

app = Flask(__name__)    

@app.route('/')          
def hello_world():
    return 'Hello World!'  

@app.route('/dojo')          
def dojo():
    return 'Dojo!'      

@app.route('/hello/<banana>')
def hello(banana):
    return f"Hello{banana}"

@app.route('/repeat/<int:num>/<string:banana>')  #will allow us to pass in any string value in url and int:num will return the string times the value given in url ex /repeat/faris/23 
def repeat(banana, num):
    return f"Hello{banana * num }"

# @app.errorhandler(404)
# def page_not_found(e):
#     return render_template("404.html")

if __name__=="__main__":    
    app.run(debug=True)    #