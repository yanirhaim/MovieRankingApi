# Import necessary modules from Flask and related extensions
from flask import Flask, request
from flask_restful import Api, Resource, reqparse, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask app and Flask-RESTful API
app = Flask(__name__)
api = Api(app)

# Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

# Define MovieModel class for database schema
class MovieModel(db.Model):
    name = db.Column(db.String(80), primary_key=True)
    rate = db.Column(db.Integer)
    ranking = db.Column(db.Integer)

# Set up request parser for PUT requests
video_put_args = reqparse.RequestParser()
video_put_args.add_argument('name', type=str, help='Name of the video', required=True)
video_put_args.add_argument('rate', type=int, help='Rate of the video', required=True)
video_put_args.add_argument('ranking', type=int, help='Ranking of the video', required=True)

# Define resource fields for marshalling
resource_fields = {
    'name': fields.String,
    'rate': fields.Integer,
    'ranking': fields.Integer
}

# Define MovieResource class to handle GET and PUT requests
class MovieResource(Resource):
    @marshal_with(resource_fields)
    def get(self, name):
        # Retrieve movie by name
        movie = MovieModel.query.filter_by(name=name).first()
        if not movie:
            return {'message': 'Movie not found'}, 404
        return movie

    @marshal_with(resource_fields)
    def put(self, name):
        # Parse arguments from request
        args = video_put_args.parse_args()
        # Check if movie already exists
        movie = MovieModel.query.filter_by(name=name).first()
        if movie:
            return {'message': 'Movie already exists'}, 409
        # Create new movie
        new_movie = MovieModel(name=name, rate=args['rate'], ranking=args['ranking'])
        db.session.add(new_movie)
        db.session.commit()
        return new_movie, 201

# Add MovieResource to API with route
api.add_resource(MovieResource, '/movie/<string:name>')

# Run the application
if __name__ == '__main__':
    # Create database tables
    with app.app_context():
        db.create_all()
    # Start the Flask development server
    app.run(debug=True)