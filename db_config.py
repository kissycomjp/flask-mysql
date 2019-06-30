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
