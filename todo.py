import sqlite3
from bottle import redirect, route, run, template, request, validate,  error


@route('/')
def todo_list():

    connection = sqlite3.connect('todo.db')
    cursor = connection.cursor()
    cursor.execute("SELECT id, task FROM todo WHERE status LIKE '1';")
    result = cursor.fetchall()
    cursor.close()

    return template('index', rows=result)


@route('/new', method='GET')
def new_item():

    if request.GET.get('save', '').strip():

        new = request.GET.get('task', '').strip()
        connection = sqlite3.connect('todo.db')
        cursor = connection.cursor()

        cursor.execute("INSERT INTO todo (task,status) VALUES (?,?)", (new, 1))
        new_id = cursor.lastrowid

        connection.commit()
        cursor.close()

        redirect('/')

    else:
        return template('new_task.tpl')


@route('/edit/:no', method='GET')
@validate(no=int)
def edit_item(no):

    if request.GET.get('save', '').strip():
        edit = request.GET.get('task', '').strip()
        status = request.GET.get('status', '').strip()

        if status == 'open':
            status = 1
        else:
            status = 0

        connection = sqlite3.connect('todo.db')
        cursor = connection.cursor()
        cursor.execute("UPDATE todo SET task = ?, status = ? WHERE id LIKE ?", (edit, status, no))
        connection.commit()

        redirect('/')

    else:
        connection = sqlite3.connect('todo.db')
        cursor = connection.cursor()
        cursor.execute("SELECT task FROM todo WHERE id LIKE ?", (str(no)))
        cur_data = cursor.fetchone()

        return template('edit_task', old=cur_data, no=no)


if __name__ == '__main__':
    run()
