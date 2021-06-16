from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Imgdetails(db.Model):
    slno = db.Column(db.Integer, primary_key=True)
    fileName = db.Column(db.String(80), unique=True, nullable=False)
    imgData = db.Column(db.String(), nullable=False)
    time = db.Column(db.String(20), nullable=True)