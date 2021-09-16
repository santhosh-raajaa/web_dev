from flask import Blueprint,url_for,render_template,request,flash

auth=Blueprint('auth',__name__)

@auth.route('/login',methods=["GET",'POST'])	
def login():

	return render_template('login.html',bool="login")

@auth.route('/logout',methods=["GET",'POST'])
def logout():
	return render_template("login.html",bool="logout")

@auth.route('/signup',methods=["GET",'POST'])
def signup():
	if request.method == 'POST':

		email=request.form.get('email')
		user=request.form.get('user')
		password1=request.form.get('password1')
		password2=request.form.get('password2')
		if len(email)<4:
			flash("Too short to be an email id",category="err")
			
		elif len(user)<3:
			flash("Must be greater than 2 charac",category="err")

			
		elif len(password1)<5:
			flash("Too short ,try something strong",category="err")

			
		elif password1!=password2:
			flash("passwords does't match",category="err")

			

		else:
			flash(f"Data can be used for creating accts",category="succ")

			#database input
	return render_template("sign_up.html")

@auth.route('/tips',methods=["GET",'POST'])
def tips():
	return "Close and go back"
	