from app import db
from app.model.classes import Classes

# get all classes
def get_all_classes():
    return Classes.query.all()

# get classes by id 
def get_classes_by_id(id):
    return Classes.query.get(id)

# create new class
def create_class(name, course_id):
    new_class = Classes(
        name = name,
        course_id = course_id
    )
    db.session.add(new_class)   # Aggiunge l'oggetto alla sessione del database
    db.session.commit()           # Esegue il commit per salvare la nuova riga nel database
    return new_class

# update class
def update_class(id, name=None):
    the_class = Classes.query.get(id)
    if not the_class:
        return None
    
    if name is not None:
        the_class.name = name
        
    db.session.commit()
    return the_class

# delete class
def delete_class(id):
    the_class = Classes.query.get(id)
    if not the_class:
        return None
    
    db.session.delete(the_class)
    db.session.commit()
    return the_class     
