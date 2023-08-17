from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

  
    
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String, nullable=False)
    email=db.Column(db.String, nullable=False)
    password=db.Column(db.String, nullable=False)
    favpla= db.relationship('FavoritePlanets', backref='user', lazy=True) 
    favcha= db.relationship('FavoriteCharacters', backref='user', lazy=True) 

    def __repr__(self):
        return '<User %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "user_name":self.user_name
            # do not serialize the password, its a security breach  
        }

class Characters(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    character_name = db.Column(db.String, nullable=False)
    character_gender = db.Column(db.String, nullable=False)
    character_height = db.Column(db.String, nullable=False)
    character_mass = db.Column(db.String, nullable=False)
    character_hair_color = db.Column(db.String, nullable=False)
    character_skin_color = db.Column(db.String, nullable=False)
    character_eye_color = db.Column(db.String, nullable=False)
    character_birth_year = db.Column(db.String, nullable=False)
    character_home_world = db.Column(db.String, nullable=False)
    favs= db.relationship('FavoriteCharacters', backref='characters', lazy=True)   

    def __repr__(self):
        return '<Characters %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "character_name": self.character_name,
            "character_gender":self.character_gender,
            "character_height":self.character_height,
            "character_mass":self.character_mass,
            "character_hair_color":self.character_hair_color,
            "character_skin_color":self.character_skin_color,
            "character_eye_color":self.character_eye_color,
            "character_birth_year":self.character_birth_year,
            "character_home_world":self.character_home_world

            # do not serialize the password, its a security breach  
        }

class Planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    planet_name = db.Column(db.String, nullable=False)
    rotation_period = db.Column(db.Integer, nullable=False)
    orbital_period = db.Column(db.Integer, nullable=False)
    diameter = db.Column(db.Integer, nullable=False)
    climate = db.Column(db.String, nullable=False)
    gravity = db.Column(db.Integer, nullable=False)
    terrain = db.Column(db.String, nullable=False)
    favs= db.relationship('FavoritePlanets', backref='planets', lazy=True)   
    
    def __repr__(self):
        return '<Planets %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "planet_name": self.planet_name,
            "rotation_period":self.rotation_period,
            "orbital_period": self.orbital_period,
            "diameter": self.diameter,
            "climate": self.climate,
            "gravity": self.gravity,
            "terrain": self.terrain
            
            # do not serialize the password, its a security breach  
        }

class FavoritePlanets(db.Model):
    id = db.Column(db.Integer, primary_key=True)    
    related_user = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    favorite_planets = db.Column(db.Integer, db.ForeignKey('planets.id'), nullable=False)

    def __repr__(self):
        return '<FavoritePlanets %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "Related_User": self.related_user,
            "Favorite_Planets": self.favorite_planets            
            
            # do not serialize the password, its a security breach  
        }
    
class FavoriteCharacters(db.Model):
    id = db.Column(db.Integer, primary_key=True)    
    related_user = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    favorite_characters = db.Column(db.Integer, db.ForeignKey('characters.id'), nullable=False)    

    def __repr__(self):
        return '<FavoriteCharacters %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "Related_User": self.related_user,
            "Favorite_Characters":self.favorite_characters,
      
            
            # do not serialize the password, its a security breach  
        }
    
    