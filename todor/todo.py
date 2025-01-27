# Importando Blueprint
from flask import Blueprint
# Creando instancia
bp = Blueprint('todo', __name__, url_prefix='/todo')
#Creado ruta y función
@bp.route('/list')
def index():
    return "Lista de tareas"
@bp.route('/create')
def create():
    return "Crear una tarea"
