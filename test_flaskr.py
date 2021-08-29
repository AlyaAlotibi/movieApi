import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from app import *
from models import *
def create_headers(token):
            return {
             "Content-Type": "application/json",
             "Authorization": f"Bearer {token}",
                }
MOVIE_PRODUCER=os.environ['MOVIE_PRODUCER']
MOVIE_ASSISTANT=os.environ['MOVIE_ASSISTANT']
MOVIE_DIRECTOR=os.environ['MOVIE_DIRECTOR']
#database_name = "movie_test"
#database_path = "postgres://{}:{}@{}/{}".format('postgres', '123','localhost:5432', database_name)
database_path = os.environ['DATABASE_URL']
if database_path.startswith("postgres://"):
    database_path = database_path.replace("postgres://", "postgresql://", 1)
class MovieTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client()
        setup_db(self.app)

        self.new_movie = {
            'title': 'add_Movie_test1',
            'type': 'Action',
            'image_link': 'https://s3-us-west-2.amazonaws.com/flx-editorial-wordpress/wp-content/uploads/2019/09/01093013/Endgame-Lead-1.jpg',
            'link':'https://editorial.rottentomatoes.com/article/highest-grossing-movies-all-time/',
            'release_date':'August 23, 2021',
        }
        
        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    def tearDown(self):
            """Executed after reach test"""
            pass
    def test_get_movies(self):
            response = self.client.get("/movies",
            headers=create_headers(MOVIE_ASSISTANT))
            data = response.get_json()
            
            self.assertEqual(response.status_code, 200)
            self.assertEqual(data['success'], True)
    def test_get_movies_invalid_token(self):
                response = self.client.get(
                    "/movies",
                headers=create_headers("mm")
                        )
                data = response.get_json()

                self.assertEqual(response.status_code, 401)
    def test_get_actors(self):
                response = self.client.get("/actors",
                headers=create_headers(MOVIE_ASSISTANT))
                data = response.get_json()
                self.assertEqual(response.status_code, 200)
                self.assertEqual(data['success'], True)
    def test_get_actors_invalid_token(self):
                    response = self.client.get(
                    "/actors",
                    headers=create_headers("unauth")
                        )
                    data = response.get_json()

                    self.assertEqual(response.status_code,401)
    def test_add_new_movie(self):
        response = self.client.post(
            "/movies_create",
            headers=create_headers(MOVIE_PRODUCER),
            json=self.new_movie,
        )
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
    def test_add_new_movie_unauth(self):
        response = self.client.post(
            "/movies_create",
            headers=create_headers(MOVIE_ASSISTANT),
            json=self.new_movie,
        )
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 403)
    def test_add_new_actor(self):
        response = self.client.post(
            "/actors_create",
            headers=create_headers(MOVIE_PRODUCER),
            json={
               "name": "test add actors8",
                "gender": "Male",
                "image_link":"https://s3-us-west-2.amazonaws.com/flx-editorial-wordpress/wp-content/uploads/2019/09/01093013/Endgame-Lead-1.jpg",
                "movie_id":4
                
            },
        )
        self.assertEqual(response.status_code, 200)
    def test_add_new_actor_with_unath_token(self):
        response = self.client.post(
            "/actors_create",
            headers=create_headers(MOVIE_ASSISTANT),
            json={
                "name": "JemyDoe",
                "gender": "Male",
                "image_link":"https://s3-us-west-2.amazonaws.com/flx-editorial-wordpress/wp-content/uploads/2019/09/01093013/Endgame-Lead-1.jpg",
                "movie_id":4
                
            },
        )
        self.assertEqual(response.status_code,403)
    def test_delete_existing_movie(self):
        Movies(id=88, title="Titaniac", type="Romance",release_date="August 23, 1970",image_link= 'https://s3-us-west-2.amazonaws.com/flx-editorial-wordpress/wp-content/uploads/2019/09/01093013/Endgame-Lead-1.jpg',
            link='https://editorial.rottentomatoes.com/article/highest-grossing-movies-all-time/').insert()
        response = self.client.delete(
            "/movies/88",
            headers=create_headers(MOVIE_PRODUCER),
        )

        self.assertEqual(response.status_code, 200)

    def test_delete_unauth(self):
        response = self.client.delete(
            "/movies/14",
            headers=create_headers(MOVIE_ASSISTANT),
        )

        self.assertEqual(response.status_code,403)
        

    def test_delete_existing_actor(self):   
        Actors(id=88, name="Alyaa", gender="Female",movie_id=4,image_link="https://s3-us-west-2.amazonaws.com/flx-editorial-wordpress/wp-content/uploads/2019/09/01093013/Endgame-Lead-1.jpg").insert()   
        response = self.client.delete(
            "/actors/88",
            headers=create_headers(MOVIE_PRODUCER),
        )
      
        self.assertEqual(response.status_code, 200)
        

    def test_delete_unauth_token(self):
        response = self.client.delete(
            "/actors/3",
            headers=create_headers(MOVIE_ASSISTANT),
        )

        self.assertEqual(response.status_code,403)
    def test_update_movie(self):
        Movies(id=92, title="Titanic", type="Romance",release_date="August 23, 1970",image_link= 'https://s3-us-west-2.amazonaws.com/flx-editorial-wordpress/wp-content/uploads/2019/09/01093013/Endgame-Lead-1.jpg',
            link='https://editorial.rottentomatoes.com/article/highest-grossing-movies-all-time/').insert()
        response = self.client.patch(
            "/movies/92",
            headers=create_headers(MOVIE_PRODUCER),
            json={"title": "edit ",'type': 'Action',
            'image_link': 'https://s3-us-west-2.amazonaws.com/flx-editorial-wordpress/wp-content/uploads/2019/09/01093013/Endgame-Lead-1.jpg',
            'link':'https://editorial.rottentomatoes.com/article/highest-grossing-movies-all-time/',
            'release_date':'August 23, 2021'},
        )
        test_movie = Movies.query.get(92)
        self.assertEqual(response.status_code, 200)
        test_movie.delete()
    def test_patch_movie_unauthorized(self):
        response = self.client.patch(
            "/movies/17",
            headers=create_headers(MOVIE_ASSISTANT),
            json={"title": "Th",'type': 'Action',
            'image_link': 'https://s3-us-west-2.amazonaws.com/flx-editorial-wordpress/wp-content/uploads/2019/09/01093013/Endgame-Lead-1.jpg',
            'link':'https://editorial.rottentomatoes.com/article/highest-grossing-movies-all-time/',
            'release_date':'August 23, 2021'},
        )
        self.assertEqual(response.status_code, 403)
    def test_update_actor(self):
        Actors(id=92, name="Alya", gender="Female",movie_id=4,image_link="https://s3-us-west-2.amazonaws.com/flx-editorial-wordpress/wp-content/uploads/2019/09/01093013/Endgame-Lead-1.jpg").insert()
        response = self.client.patch(
            "/actors/92",
            headers=create_headers(MOVIE_PRODUCER),
            json={
                "name": "edit A",
                "gender": "Male",
                "image_link":"https://s3-us-west-2.amazonaws.com/flx-editorial-wordpress/wp-content/uploads/2019/09/01093013/Endgame-Lead-1.jpg"
                
            },
        )
        
        test_actor = Actors.query.get(92)
        self.assertEqual(response.status_code, 200)

        test_actor.delete()
    def test_update_actor_unauth(self):
        Actors(id=93, name="Alya", gender="Female",movie_id=4,image_link="https://s3-us-west-2.amazonaws.com/flx-editorial-wordpress/wp-content/uploads/2019/09/01093013/Endgame-Lead-1.jpg").insert()
        response = self.client.patch(
            "/actors/93",
            headers=create_headers(MOVIE_ASSISTANT),
            json={
                "name": "edit A unauth",
                "gender": "Male",
                "image_link":"https://s3-us-west-2.amazonaws.com/flx-editorial-wordpress/wp-content/uploads/2019/09/01093013/Endgame-Lead-1.jpg"
                
            },
        )
       
        test_actor = Actors.query.get(93)
        self.assertEqual(response.status_code, 403)
        
        test_actor.delete()
if __name__ == "__main__":
    unittest.main()