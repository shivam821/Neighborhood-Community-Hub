from flask import Flask,render_template
  
app = Flask(__name__) #creating the Flask class object   
 
@app.route('/') 
@app.route('/landingPage') 
def landingPage():
    return render_template('main/landingPage.html')

@app.route('/loginPage') 
def loginPage():
    return render_template('authentication/loginPage.html')

@app.route('/signupPage') 
def signupPage():
    return render_template('authentication/signupPage.html')


  
if __name__ =='__main__':  
    app.run(debug = True)  