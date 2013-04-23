from flask import *
import judogame

app = Flask(__name__)

@app.route("/")
def main():
	if not 'username' in session:
		return render_template('login.html')
	else:
		return render_template('index.html')
					
			
@app.route("/login", methods=['POST'])
def login():
    session['username'] = request.form['username']
    return redirect(url_for('main'))
    
    
@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('main'))

def showChoices():
	return """
		<button type="Throw">Throw</button>
	"""
	
def showCurrentGame():
	pass
	
def showHistory():
	pass
    
if __name__ == "__main__":
	app.secret_key = "swordfish"
	app.run(debug = True)