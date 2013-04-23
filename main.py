from flask import *
import judogame

app = Flask(__name__)

def isLogin():
	return 'username' in session

@app.route("/")
def main():
	if not isLogin():
		return render_template('login.html')
	else:
		return render_template('index.html')
					
			
@app.route("/login", methods=['POST'])
def login():
    session['username'] = request.form['username']
    return redirect(url_for('main'))
    
    
@app.route("/logout")
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('main'))

@app.route("/move/strike")
def moveStrike():
	return move("strike")

@app.route("/move/throw")
def moveThrow():
	return move("throw")
	
@app.route("/move/block")
def moveBlock():
	return move("block")
	
def move(selectedMove):
	if not isLogin():
		return redirect(url_for('main'))
	else:
		return """You selected %s""" % selectedMove
	
def showCurrentGame():
	pass
	
def showHistory():
	pass
    
if __name__ == "__main__":
	app.secret_key = "swordfish"
	app.run(debug = True)