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
from models import db, User, Characters, Planets, FavoriteCharacters, FavoritePlanets
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

# [GET] /users/favorites Get all the favorites that belong to the current user. -done

@app.route('/users/favorites/<int:user_id>', methods=['GET'])
def get_favorites(user_id):

    user_fav_pla = FavoritePlanets.query.filter_by(related_user=user_id).all()
    result_pla = list(map(lambda item: item.serialize(), user_fav_pla))

    user_fav_cha = FavoriteCharacters.query.filter_by(related_user=user_id).all()
    result_cha = list(map(lambda item: item.serialize(), user_fav_cha))

    combined_result = result_pla + result_cha
    
    return jsonify(combined_result), 200



# [POST] /favorite/planet/<int:planet_id> Add a new favorite planet to the current user with the planet id = planet_id. - done
@app.route('/favorite/planet/<int:planet_id>', methods=['POST'])
def create_favorite_planet(planet_id):

    new_fav_pla = request.get_json()

    planet = Planets.query.get(planet_id)
    if planet is None:
        return jsonify({"message": "Planet not found"}), 404
    
    new_pla = FavoritePlanets(
        related_user=new_fav_pla["Related_User"],
        favorite_planets=planet_id  
    )
    db.session.add(new_pla)
    db.session.commit()

    response_body = {
        "message": "Se crea nuevo planeta favorito"
    }
    
    return jsonify(response_body), 200


# [POST] /favorite/people/<int:people_id> Add new favorite people to the current user with the people id = people_id. -done
@app.route('/favorite/people/<int:people_id>', methods=['POST'])
def create_favorite_character(people_id):

    new_fav_cha = request.get_json()

    character = Characters.query.get(people_id)
    if character is None:
        return jsonify({"message": "Character not found"}), 404
    
    new_cha = FavoriteCharacters(
        related_user=new_fav_cha["Related_User"],
        favorite_characters=people_id  
    )
    db.session.add(new_cha)
    db.session.commit()

    response_body = {
        "message": "Se crea nuevo personaje favorito"
    }
    
    return jsonify(response_body), 200



# [DELETE] /favorite/planet/<int:planet_id> Delete favorite planet with the id = planet_id.

@app.route('/favorite/people/<int:people_id>', methods=['DELETE'])
def delete_favorite_character(people_id):

    # new_fav_cha = request.get_json()

    # character = Characters.query.get(people_id)
    # if character is None:
    #     return jsonify({"message": "Character not found"}), 404
    
    # new_cha = FavoriteCharacters(
    #     related_user=new_fav_cha["Related_User"],
    #     favorite_characters=people_id  
    # )
    # db.session.add(new_cha)
    # db.session.commit()

    response_body = {
        "message": "Se borra personaje favorito"
    }
    
    return jsonify(response_body), 200



# [DELETE] /favorite/people/<int:people_id> Delete favorite people with the id = people_id.








#FIN ENDPOINTS
# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
