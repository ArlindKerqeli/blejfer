from flask import Blueprint, render_template, request
 

mod_contact = Blueprint('contact', __name__,url_prefix='/contact')


@mod_contact.route('/', methods=['GET'])
def index():
    ''' Renders the App index page.
    :return:
    '''
    return render_template('mod_contact/index.html')



