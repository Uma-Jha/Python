from flask import Flask, render_template
app = Flask(__name__)    
                         
@app.route('/')         
def hello_world():
	return render_template('index.html')  
@app.route('/projects')
def myProjects():
	return render_template('projects.html')
@app.route('/about')
def aboutMe():
	return render_template('aboutMe.html')
app.run(debug=True) 