from conexion import db
from datetime import datetime

class Docente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    create_at = db.Column(db.DateTime, default=datetime.utcnow)
    update_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'create_at': self.create_at,
            'update_at': self.update_at
        }
    

class Alumnos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    curp = db.Column(db.String(255), unique=True)
    N_Control = db.Column(db.String(255), unique=True)
    create_at = db.Column(db.DateTime, default=datetime.utcnow)
    update_at = db.Column(db.DateTime, default=datetime.utcnow)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'curp': self.curp,
            'N_Control': self.N_Control,
            'create_at': self.create_at,
            'update_at': self.update_at
        }
    
class Aula(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    N_Aula = db.Column(db.String(255))
    create_at = db.Column(db.DateTime, default=datetime.utcnow)
    update_at = db.Column(db.DateTime, default=datetime.utcnow)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.N_Aula,
            'create_at': self.create_at,
            'update_at': self.update_at
        }
   

class DocenteAula(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_Docente = db.Column(db.Integer, db.ForeignKey('docente.id'))
    id_Aula = db.Column(db.Integer, db.ForeignKey('aula.id'))
    id_Materia = db.Column(db.Integer, db.ForeignKey('materias.id'))
    create_at = db.Column(db.DateTime, default=datetime.utcnow)
    update_at = db.Column(db.DateTime, default=datetime.utcnow)

    def serialize(self):
        return {
            'id': self.id,
            'id_Docente': self.id_Docente,
            'id_Aula': self.id_Aula,
            'id_Materia': self.id_Materia,
            'create_at': self.create_at,
            'update_at': self.update_at
        }

class AlumnoAula(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_alumnoo = db.Column(db.Integer, db.ForeignKey('alumnos.id'))
    id_Aula = db.Column(db.Integer, db.ForeignKey('aula.id'))
    create_at = db.Column(db.DateTime, default=datetime.utcnow)
    update_at = db.Column(db.DateTime, default=datetime.utcnow)

    def serialize(self):
        return {
            'id': self.id,
            'id_alumnoo': self.id_alumnoo,
            'id_Aula': self.id_Aula,
            'create_at': self.create_at,
            'update_at': self.update_at
        }
    

class Materias(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    create_at = db.Column(db.DateTime, default=datetime.utcnow)
    update_at = db.Column(db.DateTime, default=datetime.utcnow)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'create_at': self.create_at,
            'update_at': self.update_at
        }

class MateriaAlumno(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_alumno = db.Column(db.Integer, db.ForeignKey('alumnos.id'))
    id_materia = db.Column(db.Integer, db.ForeignKey('materias.id'))
    promedio = db.Column(db.DECIMAL(2, 1))

    def serialize(self):
        return {
            'id': self.id,
            'id_alumno': self.id_alumno,
            'id_materia': self.id_materia,
            'promedio': self.promedio
        }