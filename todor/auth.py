# Importando Blueprint
from flask import Blueprint, render_template
from . import models

# Creando instancia
bp = Blueprint('auth', __name__, url_prefix='/auth')

#Creado ruta y función
@bp.route('/register')
def register():
    return render_template('auth/register.html')

@bp.route('/login')
def login():
    return render_template('auth/login.html')
