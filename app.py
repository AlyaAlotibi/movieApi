import os
from flask import (Flask, request,
 abort, jsonify,render_template)
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate 
from models import *
from auth.auth import *
def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  #CORS(app, resources={r"*/api/*" : {origins: '*'}} نحدد ريسورس
  CORS(app)
  setup_db(app)
  
  @app.after_request
  def after_request(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'GET, POST, PATCH, DELETE, OPTION')
        return response
  @app.route('/')
  def home():
    return render_template('pages/index.html')
  @app.route('/movies')
  @requires_auth('get:movies')
  def movies(payload):
    try:
      data=Movies.query.order_by(Movies.id).all()
      print(data)
      return jsonify({
            'success': True,
             'Movies': [movie.format() for movie in data]
        })
    except:
      abort(401)
  
  @app.route('/actors')
  @requires_auth('get:actors')
  def actors(payload):
    try:
      data=Actors.query.order_by(Actors.id).all()
      return jsonify({
            'success': True,
             'Actors': [actors.format() for actors in data]
        })
    except:
      abort(401)
  @app.route('/movies_create', methods=['POST'])
  @requires_auth('post:movies')
  def create_movie(payload):
        body = request.get_json()
        title = body.get('title')
        release_date =body.get('release_date')
        type = body.get('type')
        image_link = body.get('image_link')
        link = body.get('link')
        if title is None:
            abort(400)
        try:
            new_movie=Movies(title=title,type=type,release_date=release_date,image_link=image_link,link=link)
            new_movie.insert()
            return jsonify({
                'success': True,
                'created': new_movie.title,
            })
        except:
            abort(401)
  @app.route('/actors_create', methods=['POST'])
  @requires_auth('post:actors')
  def create_actor(payload):
        body = request.get_json()
        name = body.get('name')
        print(name)
        image_link = body.get('image_link')
        print(image_link)
        gender = body.get('gender')
        print(gender)
        movie_id = body.get('movie_id')
        print(movie_id)
        if name is None:
            abort(400)
        try:
            new_actor=Actors(name=name,gender=gender,image_link=image_link,movie_id=movie_id)
            new_actor.insert()
            return jsonify({
                'success': True,
                'created': new_actor.name,
            })
        except:
            abort(401)
  @app.route('/movies/<int:movies_id>',methods=['PATCH'])
  @requires_auth('patch:movies')
  def edit_movies(payload,movies_id):
    movie=Movies.query.filter(Movies.id==movies_id).one_or_none()
    if movie is None:
      abort(404)
    try:
      body=request.get_json()
      movie.title=body['title']
      movie.release_date=body['release_date']
      movie.type=body['type']
      movie.image_link=body['image_link']
      movie.link=body['link']
      Movies.update(movie)
      return jsonify({"success": True,
             "Movies": [movies.format() for movies in Movies.query.all()]}),200

    except:
      abort(401)

  @app.route('/actors/<int:actor_id>', methods=['PATCH'])
  @requires_auth('patch:actors')
  def edit_actors(payload, actor_id):
    actor=Actors.query.filter(Actors.id==actor_id).one_or_none()
    if actor is None:
      abort(404)
    try:
      body=request.get_json()
      actor.name=body['name']
      actor.gender=body['gender']
      actor.image_link=body['image_link']
      actor.movie_id=body['movie_id']
      Actors.update(actor)
      return jsonify({"success": True,
             "Actors": [actor.format() for actor in Actors.query.all()]}),200

    except:
      abort(401) 
  @app.route('/movies/<int:movies_id>',methods=['DELETE'])
  @requires_auth('delete:movies')
  def delete_movies(payload,movies_id):
    removed_movie=Movies.query.filter(Movies.id==movies_id).one_or_none()
    if removed_movie is None:
      abort(404)
    try:
      Movies.delete(removed_movie)
      return jsonify({"success": True, "delete": movies_id})
    except:
      abort(401)
  @app.route('/actors/<int:actor_id>', methods=['DELETE'])
  @requires_auth('delete:actors')
  def delete_actors(payload, actor_id):
    removed_actor=Actors.query.filter(Actors.id==actor_id).one_or_none()
    if removed_actor is None:
      abort(404)
    try:
      Actors.delete(removed_actor)
      return jsonify({"success": True, "delete": actor_id})
    except:
      abort(401) 
  # Error Handling
  @app.errorhandler(422)
  def unprocessable(error):
    return jsonify({
        "success": False,
        "error": 422,
        "message": "unprocessable"
    }), 422
  @app.errorhandler(404)
  def not_found(error):
    return jsonify({
                    "success": False,
                    "error": 404,
                    "message": "resource not found"
                    }), 404
  @app.errorhandler(401)
  def Unauthorized(error):
    return jsonify({
                    "success": False,
                    "error": 401,
                    "message": "Unauthorized"
                    }), 401

  return app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)