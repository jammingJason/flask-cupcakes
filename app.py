"""Flask app for Cupcakes"""

from flask import Flask, request, jsonify, render_template
from models import db, connect_db, Cupcake

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)


@app.route('/')
def get_all_cupcakes():
    return render_template('index.html')


@app.route('/api/cupcakes')
def get_cupcakes():
    all_cupcakes = [cupcake.serialize() for cupcake in Cupcake.query.all()]
    return jsonify(cupcakes=all_cupcakes)


@app.route('/api/cupcakes/<id>')
def get_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)
    return jsonify(cupcake=cupcake.serialize())


@app.route('/api/cupcakes', methods=['POST'])
def add_cupcakes():
    flavor = request.json['flavor']
    size = request.json['size']
    rating = request.json['rating']
    image = request.json['image']
    new_cupcake = Cupcake(flavor=flavor,
                          size=size,
                          rating=rating,
                          image=image)
    db.session.add(new_cupcake)
    db.session.commit()
    return (jsonify(cupcake=new_cupcake.serialize()), 201)


@app.route('/api/cupcakes/<id>', methods=['PATCH'])
def update_cupcakes(id):
    cupcake = Cupcake.query.get_or_404(id)
    cupcake_flavor = request.json.get('flavor', cupcake.flavor)
    cupcake_size = request.json.get('size', cupcake.size)
    cupcake_rating = request.json.get('rating', cupcake.rating)
    cupcake_image = request.json.get('image', cupcake.image)
    cc = Cupcake(id=id, flavor=cupcake_flavor, size=cupcake_size,
                 rating=cupcake_rating, image=cupcake_image)
    db.session.merge(cc)
    db.session.commit()
    return jsonify(cupcake=cupcake.serialize())


@app.route('/api/cupcakes/<id>', methods=['DELETE'])
def delete_cupcake(id):
    # db.session.filter_by(id=id).delete()
    cc = Cupcake.query.get_or_404(id)
    db.session.delete(cc)
    db.session.commit()
    return jsonify(message="Deleted item #"+id)
