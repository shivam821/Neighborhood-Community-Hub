from flask import Flask, render_template, request, flash, redirect, url_for
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Ensure you have a secret key for sessions

@app.route('/')
@app.route('/landingPage')
def landingPage():
    return render_template('main/landingPage.html')

@app.route('/loginPage', methods=['GET', 'POST'])
def loginPage():
    if request.method == 'POST':
        userEmail = request.form.get('email')
        userPassword = request.form.get('password')
        try:
            with sqlite3.connect('database.db') as connection:
                cursor = connection.cursor()
                selectUserdata = '''
                SELECT password FROM Users WHERE email = ?;
                '''
                cursor.execute(selectUserdata, (userEmail,))
                result = cursor.fetchone()  # Corrected this line to use cursor.fetchone()
                if result:
                    dbPassword = result[0]
                    if userPassword == dbPassword:
                        return 'Login Successfully'
                    else:
                        flash('Incorrect Password')
                else:
                    flash('Email not found')
            return redirect(url_for('loginPage'))
        except Exception as e:
            flash(f'Error occurred: {e}')
            return redirect(url_for('loginPage'))
    return render_template('authentication/loginPage.html')

@app.route('/signupPage', methods=['GET', 'POST'])
def signupPage():
    if request.method == 'POST':
        userEmail = request.form.get('email')
        userUsername = request.form.get('username')
        userPassword = request.form.get('password')
        userCPassword = request.form.get('password1')

        if userPassword != userCPassword:
            flash('Passwords do not match.')
            return redirect(url_for('signupPage'))

        try:
            with sqlite3.connect('database.db') as connection:
                cursor = connection.cursor()
                insertUserdata = '''
                INSERT INTO Users(email, username, password) VALUES(?,?,?);
                '''
                userSignup_data = (userEmail, userUsername, userPassword)
                cursor.execute(insertUserdata, userSignup_data)
                connection.commit()
                flash('Account Created')
                return redirect(url_for('loginPage'))
        except Exception as e:
            flash(f'Error occurred: {e}')
            return redirect(url_for('signupPage'))

    return render_template('authentication/signupPage.html')

if __name__ == '__main__':
    app.run(debug=True)