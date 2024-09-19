from datetime import datetime
from models import  db, Docente, Alumnos, Aula, DocenteAula, Materias, MateriaAlumno,AlumnoAula,MateriaAlumno
from flask import blueprints, jsonify, request

router = blueprints.Blueprint('router', __name__)

# Rutas de Docentes
@router.route('/docentes', methods=['GET'])
def get_docente():
    try:
        docente = Docente.query.all()
        return jsonify([d.serialize() for d in docente]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@router.route('/docente', methods=['POST'])
def search_docente():
    try:
        data = request.json
        docente = Docente.query.get(data['id'])
        if docente is None:
            return jsonify("Docente no encontrado"), 404
        return jsonify(docente.serialize()), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    
@router.route('/docentes', methods=['POST'])
def post_docente():
    try:
        data = request.json
        docente = Docente(name=data['name'])
        db.session.add(docente)
        db.session.commit()
        return jsonify("Docente creado"), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    
@router.route('/docente' , methods=['PUT'])
def put_docente():
    try:
        data = request.json
        docente = Docente.query.get(data['id'])
        if docente is None:
            return jsonify("Docente no encontrado"), 404
        docente.name = data['name']
        db.session.commit()
        return jsonify("Docente actualizado"), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    
@router.route('/docente' , methods=['DELETE'])
def delete_docente():
    try:
        data = request.json
        docente = Docente.query.get(data['id'])
        if docente is None:
            return jsonify("Docente no encontrado"), 404
        db.session.delete(docente)
        db.session.commit()
        return jsonify("Docente eliminado"), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    
# Rutas de Alumnos
@router.route('/alumnos', methods=['GET'])
def get_alumnos():
    try:
        alumnos = Alumnos.query.all()
        return jsonify([a.serialize() for a in alumnos]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@router.route('/alumno', methods=['POST'])
def search_alumno():
    try:
        data = request.json
        alumno = Alumnos.query.get(data['id'])
        if alumno is None:
            return jsonify("Alumno no encontrado"), 404
        return jsonify(alumno.serialize()), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@router.route('/alumnos', methods=['POST'])
def post_alumno():
    try:
        data = request.json
        print(data)
        alumno = Alumnos(name=data['name'], curp=data['curp'], N_Control=data['nControl'])
        db.session.add(alumno)
        db.session.commit()
        return jsonify("Alumno creado"), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@router.route('/alumno' , methods=['PUT'])
def put_alumno():
    try:
        data = request.json
        alumno = Alumnos.query.get(data['id'])
        if alumno is None:
            return jsonify("Alumno no encontrado"), 404
        alumno.name = data['name']
        alumno.curp = data['curp']
        alumno.N_Control = data['nControl']
        db.session.commit()
        return jsonify("Alumno actualizado"), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    
@router.route('/alumno' , methods=['DELETE'])
def delete_alumno():
    try:
        data = request.json
        alumno = Alumnos.query.get(data['id'])
        if alumno is None:
            return jsonify("Alumno no encontrado"), 404
        db.session.delete(alumno)
        db.session.commit()
        return jsonify("Alumno eliminado"), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Rutas de Aulas
@router.route('/aulas', methods=['GET'])
def get_aulas():
    try:
        aulas = Aula.query.all()
        return jsonify([a.serialize() for a in aulas]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@router.route('/aula', methods=['POST'])
def search_aula():
    try:
        data = request.json
        aula = Aula.query.get(data['id'])
        if aula is None:
            return jsonify("Aula no encontrada"), 404
        return jsonify(aula.serialize()), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@router.route('/aulas', methods=['POST'])
def post_aula():
    try:
        data = request.json
        print(data['N_Aula'])
        aula = Aula(N_Aula=data['N_Aula'])
        db.session.add(aula)
        db.session.commit()
        return jsonify("Aula creada"), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@router.route('/aula' , methods=['PUT'])
def put_aula():
    try:
        data = request.json
        aula = Aula.query.get(data['id'])
        if aula is None:
            return jsonify("Aula no encontrada"), 404
        aula.N_Aula = data['N_Aula']
        db.session.commit()
        return jsonify("Aula actualizada"), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@router.route('/aula' , methods=['DELETE'])
def delete_aula():
    try:
        data = request.json
        aula = Aula.query.get(data['id'])
        if aula is None:
            return jsonify("Aula no encontrada"), 404
        db.session.delete(aula)
        db.session.commit()
        return jsonify("Aula eliminada"), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Rutas de DocenteAula
@router.route('/docenteaulas', methods=['GET'])
def get_docenteaulas():
    try:
        docenteaulas = DocenteAula.query.all()
        return jsonify([da.serialize() for da in docenteaulas]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@router.route('/docenteaula', methods=['POST'])
def search_docenteaula():
    try:
        data = request.json
        docenteaula = DocenteAula.query.get(data['id'])
        if docenteaula is None:
            return jsonify("DocenteAula no encontrada"), 404
        return jsonify(docenteaula.serialize()), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@router.route('/docenteaulas', methods=['POST'])
def post_docenteaula():
    try:
        data = request.json
        print(data)
        docenteaula = DocenteAula(id_Docente=data['id_Docente'], id_Aula=data['id_Aula'], id_Materia=data['id_Materia'])
        db.session.add(docenteaula)
        db.session.commit()
        return jsonify("DocenteAula creada"), 200
    except Exception as e:
        print(e)
        return jsonify({'error': str(e)}), 400

@router.route('/docenteaula' , methods=['PUT'])
def put_docenteaula():
    try:
        data = request.json
        docenteaula = DocenteAula.query.get(data['id'])
        if docenteaula is None:
            return jsonify("DocenteAula no encontrada"), 404
        docenteaula.id_Docente = data['id_Docente']
        docenteaula.id_Aula = data['id_Aula']
        docenteaula.id_Materia = data['id_Materia']
        db.session.commit()
        return jsonify("DocenteAula actualizada"), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    
@router.route('/docenteaula' , methods=['DELETE'])
def delete_docenteaula():
    try:
        data = request.json
        docenteaula = DocenteAula.query.get(data['id'])
        if docenteaula is None:
            return jsonify("DocenteAula no encontrada"), 404
        db.session.delete(docenteaula)
        db.session.commit()
        return jsonify("DocenteAula eliminada"), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Rutas de Materias
@router.route('/materias', methods=['GET'])
def get_materias():
    try:
        materias = Materias.query.all()
        return jsonify([m.serialize() for m in materias]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@router.route('/materia', methods=['POST'])
def search_materia():
    try:
        data = request.json
        materia = Materias.query.get(data['id'])
        if materia is None:
            return jsonify("Materia no encontrada"), 404
        return jsonify(materia.serialize()), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@router.route('/materias', methods=['POST'])
def post_materia():
    try:
        data = request.json
        materia = Materias(name=data['name'])
        db.session.add(materia)
        db.session.commit()
        return jsonify("Materia creada"), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    
@router.route('/materia' , methods=['PUT'])
def put_materia():
    try:
        data = request.json
        materia = Materias.query.get(data['id'])
        if materia is None:
            return jsonify("Materia no encontrada"), 404
        materia.name = data['name']
        db.session.commit()
        return jsonify("Materia actualizada"), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@router.route('/materia' , methods=['DELETE'])
def delete_materia():
    try:
        data = request.json
        materia = Materias.query.get(data['id'])
        if materia is None:
            return jsonify("Materia no encontrada"), 404
        db.session.delete(materia)
        db.session.commit()
        return jsonify("Materia eliminada"), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Rutas de MateriaAlumno
@router.route('/MateriaAlumnos', methods=['GET'])
def get_MateriaAlumnos():
    try:
        MateriaAlumnos = MateriaAlumno.query.all()
        return jsonify([am.serialize() for am in MateriaAlumnos]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@router.route('/MateriaAlumno', methods=['POST'])
def search_MateriaAlumno():
    try:
        data = request.json
        MateriaAlumno = MateriaAlumno.query.get(data['id'])
        if MateriaAlumno is None:
            return jsonify("MateriaAlumno no encontrada"), 404
        return jsonify(MateriaAlumno.serialize()), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@router.route('/MateriaAlumnos', methods=['POST'])
def post_MateriaAlumno():
    try:
        data = request.json
        MateriaAlumno = MateriaAlumno(id_alumno=data['id_alumno'], id_materia=data['id_materia'])
        db.session.add(MateriaAlumno)
        db.session.commit()
        return jsonify("MateriaAlumno creada"), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    
@router.route('/MateriaAlumno' , methods=['PUT'])
def put_MateriaAlumno():
    try:
        data = request.json
        MateriaAlumno = MateriaAlumno.query.get(data['id'])
        if MateriaAlumno is None:
            return jsonify("MateriaAlumno no encontrada"), 404
        MateriaAlumno.id_alumno = data['id_alumno']
        MateriaAlumno.id_materia = data['id_materia']
        db.session.commit()
        return jsonify("MateriaAlumno actualizada"), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@router.route('/MateriaAlumno' , methods=['DELETE'])
def delete_MateriaAlumno():
    try:
        data = request.json
        MateriaAlumno = MateriaAlumno.query.get(data['id'])
        if MateriaAlumno is None:
            return jsonify("MateriaAlumno no encontrada"), 404
        db.session.delete(MateriaAlumno)
        db.session.commit()
        return jsonify("MateriaAlumno eliminada"), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Rutas de AulumnoAula

@router.route('/alumnoaulas', methods=['GET'])
def get_alumnoaulas():
    try:
        alumnoaulas = AlumnoAula.query.all()
        return jsonify([aa.serialize() for aa in alumnoaulas]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@router.route('/alumnoaula', methods=['POST'])
def search_alumnoaula():
    try:
        data = request.json
        alumnoaula = AlumnoAula.query.get(data['id'])
        if alumnoaula is None:
            return jsonify("AlumnoAula no encontrada"), 404
        return jsonify(alumnoaula.serialize()), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@router.route('/alumnoaulas', methods=['POST'])
def post_alumnoaula():
    try:
        data = request.json
        alumnoaula = AlumnoAula(id_alumnoo=data['id_Alumno'], id_Aula=data['id_Aula'])
        db.session.add(alumnoaula)
        db.session.commit()
        return jsonify("AlumnoAula creada"), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    
@router.route('/alumnoaula' , methods=['PUT'])
def put_alumnoaula():
    try:
        data = request.json
        alumnoaula = AlumnoAula.query.get(data['id'])
        if alumnoaula is None:
            return jsonify("AlumnoAula no encontrada"), 404
        alumnoaula.id_alumnoo = data['id_Alumno']
        alumnoaula.id_Aula = data['id_Aula']
        db.session.commit()
        return jsonify("AlumnoAula actualizada"), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    
@router.route('/alumnoaula' , methods=['DELETE'])
def delete_alumnoaula():
    try:
        data = request.json
        alumnoaula = AlumnoAula.query.get(data['id'])
        if alumnoaula is None:
            return jsonify("AlumnoAula no encontrada"), 404
        db.session.delete(alumnoaula)
        db.session.commit()
        return jsonify("AlumnoAula eliminada"), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400


