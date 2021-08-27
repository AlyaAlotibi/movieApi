import os
from flask import (Flask, request,
 abort, jsonify)
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
  migrate=Migrate(app,db)
  @app.after_request
  def after_request(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'GET, POST, PATCH, DELETE, OPTION')
        return response
  @app.route('/')
  def index():
    return jsonify({
            'success': True,
            'message': 'Welcome to Alna Movies websit',

        })
  @app.route('/movies')
  @requires_auth('get:movies')
  def movies(payload):
    pass
  
  @app.route('/actors')
  @requires_auth('get:actors')
  def actors(payload):
    pass
  @app.route('/movies/create', methods=['POST'])
  @requires_auth('post:movies')
  def api_create_movie(payload):
    pass
  @app.route('/actors/create', methods=['POST'])
  @requires_auth('post:actors')
  def add_actor(payload):
    pass
  @app.route('/movies/<int:movies_id>',methods=['PATCH'])
  @requires_auth('patch:movies')
  def edit_movies(payload,movies_id):
    pass 

  @app.route('/actors/<int:actor_id>', methods=['PATCH'])
  @requires_auth('patch:actors')
  def edit_actors(payload, actor_id):
    pass 
  @app.route('/movies/<int:movies_id>',methods=['DELETE'])
  @requires_auth('delete:movies')
  def delete_movies(payload,movies_id):
    pass 
  app.route('/actors/<int:actor_id>', methods=['DELETE'])
  @requires_auth('delete:actors')
  def delete_actors(payload, actor_id):
    pass 
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

APP = create_app()

if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8080, debug=True)