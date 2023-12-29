from ejemplo7 import db, Persona, app

with app.app_context():
    #Genera la tabla
    db.create_all()

    #Se insertan datos

    persona1 = Persona("Antonio",34)
    persona2 = Persona("Omar",24)

    db.session.add_all([persona1,persona2])
    db.session.commit()

    persona3 = Persona("María",20)
    db.session.add(persona3)
    db.session.commit() #SIEMPRE HAY QUE HACER COMMIT AL INSERTAR O AJUSTAR ALGO EN LA BD

    personas = Persona.query.all()
    print("Consultar todas las personas")
    print(personas)

    #busquedas concretas por el valores de columnas
    filtro1 = Persona.query.filter_by(nombre="Antonio")
    print("Filtro por nombre = Antonio")
    print(filtro1.all())

    #Busquedas por elementos, por la columna identificador
    #seleccion1 = Persona.query.get(2) #legacy
    seleccion1 = db.session.get(Persona, 2)
    print("Busqueda por id 2")
    print(seleccion1)

    #Actualizar datos
    #persona = Persona.query.get(1) #legacy
    persona = db.session.get(Persona, 1)
    persona.edad = 45
    db.session.add(persona)
    db.session.commit()

    #Eliminar registros

    #persona_borrar = Persona.query.get(3) #legacy
    persona_borrar = db.session.get(Persona, 3)
    db.session.delete(persona_borrar)
    db.session.commit()
    print("Hemos borrado esta persona: {}".format(persona_borrar))

    personas = Persona.query.all()
    print("Todas las personas")
    print(personas)
