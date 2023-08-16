"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Characters, Planets, Favorites
#from models import Person

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

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

#INICIO ENDPOINTS
# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

#  [GET] /people Get a list of all the people in the database -done
@app.route('/people', methods=['GET'])
def get_characters():

    all_people = Characters.query.all()
    result = list(map(lambda item: item.serialize(), all_people))
    return jsonify(result), 200  



# [GET] /people/<int:people_id> Get a one single people information -done
@app.route('/people/<int:character_id>', methods=['GET'])
def get_character(character_id):

    character = Characters.query.filter_by(id=character_id).first()    
    return jsonify(character.serialize()), 200  

# [GET] /planets Get a list of all the planets in the database -done
@app.route('/planets', methods=['GET'])
def get_planets():

    planets = Planets.query.all()
    result = list(map(lambda item: item.serialize(), planets))
    return jsonify(result), 200  


# [GET] /planets/<int:planet_id> Get one single planet information -done
@app.route('/planets/<int:planet_id>', methods=['GET'])
def get_planet(planet_id):

    planet = Planets.query.filter_by(id=planet_id).first()    
    return jsonify(planet.serialize()), 200  


#[GET] /users Get a list of all the blog post users -done
@app.route('/users', methods=['GET'])
def get_users():

    all_users = User.query.all()
    result = list(map(lambda item: item.serialize(), all_users))
    return jsonify(result), 200  

# [GET] /users/favorites Get all the favorites that belong to the current user.


# [POST] /favorite/planet/<int:planet_id> Add a new favorite planet to the current user with the planet id = planet_id.
# [POST] /favorite/people/<int:people_id> Add new favorite people to the current user with the people id = people_id.
# [DELETE] /favorite/planet/<int:planet_id> Delete favorite planet with the id = planet_id.
# [DELETE] /favorite/people/<int:people_id> Delete favorite people with the id = people_id.








#FIN ENDPOINTS
# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
