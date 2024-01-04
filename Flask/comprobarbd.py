from ejemplo7 import db, Persona, app

with app.app_context():

    #persona = Persona.query.get(1) #Legacy
    persona = db.session.get(Persona,1)
    persona.color = "Verde"
    db.session.add(persona)
    db.session.commit()

    personas = Persona.query.all()
    print(persona)