from flask import Blueprint, render_template, request
 

mod_buy = Blueprint('buy', __name__,url_prefix='/buy')


@mod_buy.route('/', methods=['GET'])
def index():
    ''' Renders the App index page.
    :return:
    '''
    return render_template('mod_buy/index.html')

@mod_buy.route('/my-list', methods=['GET'])
def my_list():
    ''' Renders the App index page.
    :return:
    '''
    return "my list"

