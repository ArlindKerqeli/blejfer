from flask import Blueprint, render_template, request
 

mod_sell = Blueprint('sell', __name__,url_prefix='/sell')


@mod_sell.route('/', methods=['GET'])
def index():
    ''' Renders the App index page.
    :return:
    '''
    return render_template('mod_sell/index.html')

@mod_sell.route('/my-list', methods=['GET'])
def my_list():
    ''' Renders the App index page.
    :return:
    '''
    return "my list"

