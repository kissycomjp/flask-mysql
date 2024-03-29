import pymysql
#from db_config import mysql
from flask import jsonify
from flask import flash, request
from werkzeug import generate_password_hash, check_password_hash

from flaskext.mysql import MySQL
import os


from flask import Flask

app = Flask(__name__)

mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = os.environ['db_username']
app.config['MYSQL_DATABASE_PASSWORD'] = os.environ['db_password']
app.config['MYSQL_DATABASE_DB'] = os.environ['db_name']
app.config['MYSQL_DATABASE_HOST'] = os.environ['ipaddress']
mysql.init_app(app)


@app.route('/')
def index():
	return "Hello, world!"

@app.route('/add', methods=['POST'])
def add_user():
	try:
		_json = request.json
		_name = _json['name']
		_email = _json['email']
		_password = _json['pwd']
		# validate the received values
		if _name and _email and _password and request.method == 'POST':
			#do not save password as a plain text
			_hashed_password = generate_password_hash(_password)
			# save edits
			sql = "INSERT INTO tbl_user(user_name, user_email, user_password) VALUES(%s, %s, %s)"
			data = (_name, _email, _hashed_password,)
			conn = mysql.connect()
			cursor = conn.cursor()
			cursor.execute(sql, data)
			conn.commit()
			resp = jsonify('User added successfully!')
			resp.status_code = 200
			return resp
		else:
			return not_found()
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()
		
@app.route('/users')
def users():
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * FROM tbl_user")
		rows = cursor.fetchall()
		resp = jsonify(rows)
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()
		
@app.route('/user', methods=['POST'])
def user():
	try:
		_json = request.json
		_user_id = _json['user_id']
		# validate the received values
		if _user_id and request.method == 'POST':
			conn = mysql.connect()
			cursor = conn.cursor(pymysql.cursors.DictCursor)
			cursor.execute("SELECT * FROM tbl_user WHERE user_id=%s",_user_id)
			row = cursor.fetchone()
			resp = jsonify(row)
			resp.status_code = 200
			return resp
		else:
			return not_found()	
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()

@app.route('/update', methods=['POST'])
def update_user():
	try:
		_json = request.json
		_id = _json['user_id']
		_name = _json['name']
		_email = _json['email']
		_password = _json['pwd']		
		# validate the received values
		if _name and _email and _password and _id and request.method == 'POST':
			#do not save password as a plain text
			_hashed_password = generate_password_hash(_password)
			# save edits
			sql = "UPDATE tbl_user SET user_name=%s, user_email=%s, user_password=%s WHERE user_id=%s"
			data = (_name, _email, _hashed_password, _id,)
			conn = mysql.connect()
			cursor = conn.cursor()
			cursor.execute(sql, data)
			conn.commit()
			resp = jsonify('User updated successfully!')
			resp.status_code = 200
			return resp
		else:
			return not_found()
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()
		
@app.route('/delete', methods=['POST'])
def delete_user():
	try:
		_json = request.json
		_user_id = _json['user_id']
		# validate the received values
		if _user_id and request.method == 'POST':
			conn = mysql.connect()
			cursor = conn.cursor()
			cursor.execute("DELETE FROM tbl_user WHERE user_id=%s", _user_id)
			conn.commit()
			resp = jsonify('User deleted successfully!')
			resp.status_code = 200
			return resp
		else:
			return not_found()
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()
		
@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp
		
if __name__ == "__main__":
    #app.run()
    #app.run(host='0.0.0.0', port=80, debug=True)
    app.run(host='0.0.0.0', port=8080, debug=True, threaded=True)
