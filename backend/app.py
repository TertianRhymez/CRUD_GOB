from flask import Flask
from conexion import db
from flask_migrate import Migrate
from flask_cors import CORS
from router import router
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://:@(localdb)\mssqllocaldb/crudprueba?driver=ODBC+Driver+17+for+SQL+Server'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

app.register_blueprint(router)

migrate = Migrate(app, db)

CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})


with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)