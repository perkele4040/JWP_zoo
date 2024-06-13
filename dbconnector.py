from dbinit import Animals, Employees, Enclosures, Users
from werkzeug.security import check_password_hash


class DBConnector:
    def __init__(self, db):
        self.db = db

    def get_animals(self):
        return self.db.session.query(Animals).all()

    def edit_animal_db(self, new_value, id, sel):
        a = self.db.session.query(Animals).filter_by(id=id).first()
        if a:
            if sel == 'name':
                a.name = new_value
            elif sel == 'species':
                a.species = new_value
            elif sel == 'enclosure':
                if not self.db.session.query(Enclosures).filter_by(id=new_value).first():
                    return 'This enclosure doesnt exist.'
                a.enclosure = new_value
            else:
                return 'Wrong request!'
            self.db.session.commit()
            return 'Animal update successful!'

    def remove_animal_db(self, id):
        a = self.db.session.query(Animals).filter_by(id=id).first()
        if a:
            self.db.session.delete(a)
            self.db.session.commit()
            return 'Animal removal successful!'
        return 'Something went wrong.'

    def add_animal_db(self, name, species, enclosure):
        a = Animals(name=name, species=species, enclosure=enclosure)
        if not self.db.session.query(Enclosures).filter_by(id=enclosure).first():
            return 'This enclosure doesnt exist.'
        if a:
            self.db.session.add(a)
            self.db.session.commit()
            return 'Animal addition successful!'
        return 'Something went wrong.'

    def get_enclosures(self):
        return self.db.session.query(Enclosures).all()


    def edit_enclosure_db(self, new_value, id, sel):
        e = self.db.session.query(Enclosures).filter_by(id=id).first()
        if e:
            if sel == 'location':
                e.location = new_value
            elif sel == 'inhabitant':
                if not self.db.session.query(Animals).filter_by(id=new_value).first():
                    return 'This animal doesnt exist.'
                e.inhabitant = new_value
            else:
                return 'Wrong request!'
            self.db.session.commit()
            return 'Enclosure update successful!'

    def remove_enclosure_db(self, id):
        a = self.db.session.query(Enclosures).filter_by(id=id).first()
        if a:
            self.db.session.delete(a)
            self.db.session.commit()
            return 'Enclosure removal successful!'
        return 'Something went wrong.'

    def add_enclosure_db(self, location, inhabitant):
        e = Enclosures(location=location, inhabitant=inhabitant)
        if not self.db.session.query(Animals).filter_by(id=inhabitant).first():
            return 'This animal doesnt exist.'
        if e:
            self.db.session.add(e)
            self.db.session.commit()
            return 'Enclosure addition successful!'
        return 'Something went wrong.'

    def get_employees(self):
        return self.db.session.query(Employees).all()

    def edit_employee_db(self, new_value, id, sel):
        e = self.db.session.query(Employees).filter_by(id=id).first()
        if e:
            if sel == 'first':
                e.first_name = new_value
            elif sel == 'last':
                e.last_name = new_value
            else:
                return 'Wrong request!'
            self.db.session.commit()
            return 'Employee update successful!'

    def remove_employee_db(self, id):
        e = self.db.session.query(Employees).filter_by(id=id).first()
        if e:
            self.db.session.delete(e)
            self.db.session.commit()
            return 'Employee removal successful!'
        return 'Something went wrong.'

    def add_employee_db(self, first_name, last_name):
        e = Employees(first_name=first_name, last_name=last_name)
        if e:
            self.db.session.add(e)
            self.db.session.commit()
            return 'Employee addition successful!'
        return 'Something went wrong.'

    def authenticate(self, username, password):
        users = self.get_users()
        for u in users:
            if username == u.email and check_password_hash(u.password, password):
                return True
        return False

    def get_user(self, user_id):
        self.db.session.query(Users).filter_by(id=user_id).first()
        users = self.get_users()
        for u in users:
            if user_id == u.id:
                return u
        return None

    def get_users(self):
        return self.db.session.query(Users).all()
