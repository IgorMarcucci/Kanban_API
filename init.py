from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://username:password@localhost:5432/your_database"
db = SQLAlchemy(app)

from app import routes

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)