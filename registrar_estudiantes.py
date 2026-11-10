
from modelos import Estudiante
from conexiones import session


def crear_estudiante(nombre, correo):

    sesion = session()

    if not nombre.strip():
        print("El nombre no puede estar vacío.")
        sesion.close()
        return

    if not correo.strip():
        print("El correo no puede estar vacío.")
        sesion.close()
        return

    estudiante = sesion.query(Estudiante).filter(
        Estudiante.correo == correo.strip()
    ).first()

    if estudiante:
        print("Ese correo ya está registrado.")
        sesion.close()
        return

    nuevo = Estudiante(
        nombre=nombre.strip(),
        correo=correo.strip()
    )

    sesion.add(nuevo)
    sesion.commit()

    print("Estudiante registrado correctamente.")

    sesion.close()


def listar_estudiantes():

    sesion = session()

    estudiantes = sesion.query(Estudiante).all()

    if not estudiantes:
        print("No hay estudiantes registrados.")

    for estudiante in estudiantes:
        print(estudiante)

    sesion.close()
