from flask import Flask,render_template,request
  
app = Flask(__name__) 
 
@app.route('/') 
@app.route('/landingPage') 
def landingPage():
    return render_template('main/landingPage.html')

@app.route('/loginPage',methods = ['GET','POST']) 
def loginPage():
    if request.method == 'POST' : 
        userEmail = request.form.get('email')
        userPassword = request.form.get('password')
        return f'{userEmail} - {userPassword}'
    return render_template('authentication/loginPage.html')

@app.route('/signupPage',methods = ['GET','POST']) 
def signupPage():
    if request.method == 'POST' : 
        userEmail = request.form.get('email')
        userUsername = request.form.get('username')
        userPassword = request.form.get('password')
        userCPassword = request.form.get('password')
        return f'{userEmail} - {userUsername} - {userPassword} - {userCPassword}'
    return render_template('authentication/signupPage.html')


  
if __name__ =='__main__':  
    app.run(debug = True)  