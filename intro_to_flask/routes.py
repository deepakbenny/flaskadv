from intro_to_flask import app
from flask import render_template, request, flash
from forms import ContactForm
from flask.ext.mail import Message, Mail
 
mail = Mail()

@app.route('/')
def home():
	return render_template('home.html')
	
@app.route('/about')
def about():
	return render_template('about.html')
	
@app.route('/contact', methods=['GET', 'POST'])

#Story behind long code in contact
#if the idiot user fails to enter all the Fields
#then we are gonna tell the idiot to enter it again

def contact():
  form = ContactForm()

  if request.method == 'POST':
  	if form.validate() == False:
  		flash('Retry')
  		return render_template('contact.html',form=form)
  	else:
  		return 'Posted'
  elif request.method == 'GET':	
  	return render_template('contact.html',form = form)