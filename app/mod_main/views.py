from flask import Blueprint, render_template, request
 

mod_main = Blueprint('main', __name__)


@mod_main.route('/', methods=['GET'])
def index():
    ''' Renders the App index page.
    :return:
    '''
    return render_template('index.html')


@mod_main.route('/signin', methods=['GET', 'POST'])
def signin():
    ''' Logs in the user.
    :return:
    '''
    if request.method == 'POST':  #this block is only entered when the form is submitted
        username = request.form['userid']
       	password = request.form['password']
       	if username =='admin' and password=='admin':
       		return render_template('logged_in.html', username=username,error="")
       	else:
       		return render_template('signin.html', error="Keni shtypur te dhenat Gabim!")
    elif request.method =='GET':
        return render_template('signin.html')

    else:

    	return "Gabim"


