from flask import Flask, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import UniqueConstraint
from dataclasses import dataclass
import requests

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:1234@db/main'
CORS(app)

db = SQLAlchemy(app)

@dataclass #We add @dataclass so the class is JSON serializable
class Product(db.Model):
    #If we dont inicialize the variables we wont be able to visualize it
    id: int
    title: str
    image: str

    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    title = db.Column(db.String(200))
    image = db.Column(db.String(200))

@dataclass
class ProductUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    product_id = db.Column(db.Integer)

    UniqueConstraint('user_id', 'product_id', name='user_product_unique')

@app.route('/api/products')
def index():
    return jsonify(Product.query.all())

@app.route('/api/products/<int:id>/like', methods=['POST'])
def like(id):
    req = requests.get('http://host.docker.internal:8000/api/user')
    return jsonify(req.json())

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')