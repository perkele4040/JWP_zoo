from flask import Flask, render_template, url_for, request
from dbinit import db, db_reload
from dbconnector import DBConnector
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import check_password_hash, generate_password_hash



perform_db_reload = True
auth = HTTPBasicAuth()
app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///zoo.db'
db.init_app(app)


@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')


@app.route('/animals', methods=['GET'])
@auth.login_required()
def get_animals_details():
    return render_template('animals.html', animals=db_connector.get_animals(), user=auth.current_user())


@app.route('/back/edit-animal', methods=['PUT'])
def edit_animal_back():
    return db_connector.edit_animal_db(request.get_data(as_text=True),
                                       request.headers.get('ID'), request.headers.get('SEL'))


@app.route('/back/add-animal', methods=['POST'])
def add_animal_back():
    return db_connector.add_animal_db(request.headers.get('NM'), request.headers.get('SP'), request.headers.get('ENC'))


@app.route('/back/remove-animal', methods=['DELETE'])
def remove_animal_back():
    return db_connector.remove_animal_db(request.headers.get('ID'))


@app.route('/enclosures', methods=['GET'])
@auth.login_required()
def get_enclosures_details():
    return render_template('enclosures.html', enclosures=db_connector.get_enclosures(), user=auth.current_user())


@app.route('/back/edit-enclosure', methods=['PUT'])
def edit_enclosure_back():
    return db_connector.edit_enclosure_db(request.get_data(as_text=True),
                                          request.headers.get('ID'), request.headers.get('SEL'))


@app.route('/back/add-enclosure', methods=['POST'])
def add_enclosure_back():
    return db_connector.add_enclosure_db(request.headers.get('LC'), request.headers.get('INH'))


@app.route('/back/remove-enclosure', methods=['DELETE'])
def remove_enclosure_back():
    return db_connector.remove_enclosure_db(request.headers.get('ID'))


@app.route('/employees', methods=['GET'])
@auth.login_required()
def get_employees_details():
    return render_template('employees.html', employees=db_connector.get_employees(), user=auth.current_user())


@app.route('/back/edit-employee', methods=['PUT'])
def edit_employee_back():
    return db_connector.edit_employee_db(request.get_data(as_text=True),
                                         request.headers.get('ID'), request.headers.get('SEL'))


@app.route('/back/add-employee', methods=['POST'])
def add_employee_back():
    return db_connector.add_employee_db(request.headers.get('FN'), request.headers.get('LN'))


@app.route('/back/remove-employee', methods=['DELETE'])
def remove_employee_back():
    return db_connector.remove_employee_db(request.headers.get('ID'))


@auth.verify_password
def verify_password(username, password):
    if db_connector.authenticate(username, password):
        return True


@app.route('/login', methods=['GET'])
@auth.login_required
def get_login_page():
    return render_template('login.html', user=auth.current_user())


if perform_db_reload:
    db_reload(app.app_context())
    print('DB restored to default state')
db_connector = DBConnector(db)
app.run(host='127.0.0.1', port=443)
