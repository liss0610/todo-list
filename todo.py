from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # Renderiza index.html

if __name__ == '__main__':
    app.run(debug=True)


# agregrar crear tareas

from flask import request, redirect, url_for

@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create_todo():
    if request.method == 'POST':
        title = request.form['title']
        desc = request.form['desc']
        
        # Crear nueva tarea asociada al usuario actual
        todo = Todo(
            created_by=g.user.id,
            title=title,
            desc=desc
        )
        # Guardar en la base de datos
        db.session.add(todo)
        db.session.commit()
        
        # Redirigir a la lista de tareas
        return redirect(url_for('todo.list_todos'))
    
    return render_template('todo/create.html')


# EDITAR TAREAS

@bp.route('/edit/<int:id>', methods=('GET', 'POST'))
@login_required
def edit_todo(id):
    # Obtener la tarea desde la base de datos
    todo = Todo.query.get_or_404(id)
    
    # Validar que el usuario actual es el creador de la tarea
    if todo.created_by != g.user.id:
        return redirect(url_for('todo.list_todos'))

    if request.method == 'POST':
        todo.title = request.form['title']
        todo.desc = request.form['desc']
        todo.state = 'state' in request.form  # Checkbox para estado completado
        
        # Guardar cambios
        db.session.commit()
        return redirect(url_for('todo.list_todos'))

    return render_template('todo/edit.html', todo=todo)

# añadiremos una ruta para eliminar tareas

@bp.route('/delete/<int:id>', methods=('POST',))
@login_required
def delete_todo(id):
    # Obtener la tarea desde la base de datos
    todo = Todo.query.get_or_404(id)
    
    # Validar que el usuario actual es el creador de la tarea
    if todo.created_by != g.user.id:
        return redirect(url_for('todo.list_todos'))

    # Eliminar la tarea
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('todo.list_todos'))

# confirmacion de elminacion en mensaje tempporal

from flask import flash

@bp.route('/delete/<int:id>', methods=('POST',))
@login_required
def delete_todo(id):
    todo = Todo.query.get_or_404(id)
    if todo.created_by != g.user.id:
        return redirect(url_for('todo.list_todos'))

    db.session.delete(todo)
    db.session.commit()
    flash('La tarea fue eliminada correctamente.')
    return redirect(url_for('todo.list_todos'))
