import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, People, Planet


app = Flask(__name__)
app.url_map.strict_slashes = False


db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)


@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code


@app.route('/')
def sitemap():
    return generate_sitemap(app)


@app.route('/user', methods=['GET'])
def get_user():
    users = User.query.all()
    results = [user.serialize() for user in users]
    response_body = {"message": "ok",
                     "total_records": len(results),
                     "results": results}
    return jsonify(response_body), 200


@app.route('/user', methods=['POST'])
def create_user():
    request_body = request.get_json()
    user = User(email = request_body['email'],
                password = request_body['password'],
                is_active = request_body['is_active'])
    db.session.add(user)
    db.session.commit()
    return jsonify(request_body), 200


@app.route('/people', methods=['GET'])
def get_people():
    people = People.query.all()
    results = [character.serialize() for character in people]
    response_body = {"message": "ok",
                     "total_records": len(results),
                     "results": results}
    return jsonify(response_body), 200


@app.route('/people/<int:people_id>', methods=['GET'])
def get_people_by_id(people_id):
    people = db.get_or_404(People, people_id)
    result = people.serialize()
    response_body = {"message": "ok",
                     "result": result}
    return jsonify(response_body), 200


@app.route('/planet', methods=['GET'])
def get_planet():
    planets = Planet.query.all()
    results = [planet.serialize() for planet in planets]
    response_body = {"message": "ok",
                     "total_records": len(results),
                     "results": results}
    return jsonify(response_body), 200


@app.route('/planet/<int:planet_id>', methods=['GET'])
def get_planet_by_id(planet_id):
    planet = db.get_or_404(Planet, planet_id)
    result = planet.serialize()
    response_body = {"message": "ok",
                     "result": result}
    return jsonify(response_body), 200


if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
