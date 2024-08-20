from flask import Flask, request
from flask_restful import Api, Resource, reqparse, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class MovieModel(db.Model):
    name = db.Column(db.String(80), primary_key=True)
    rate = db.Column(db.Integer)
    ranking = db.Column(db.Integer)

video_put_args = reqparse.RequestParser()
video_put_args.add_argument('name', type=str, help='Name of the video', required=True)
video_put_args.add_argument('rate', type=int, help='Rate of the video', required=True)
video_put_args.add_argument('ranking', type=int, help='Ranking of the video', required=True)

resource_fields = {
    'name': fields.String,
    'rate': fields.Integer,
    'ranking': fields.Integer
}

class MovieResource(Resource):
    @marshal_with(resource_fields)
    def get(self, name):
        movie = MovieModel.query.filter_by(name=name).first()
        if not movie:
            return {'message': 'Movie not found'}, 404
        return movie

    @marshal_with(resource_fields)
    def put(self, name):
        args = video_put_args.parse_args()
        movie = MovieModel.query.filter_by(name=name).first()
        if movie:
            return {'message': 'Movie already exists'}, 409
        new_movie = MovieModel(name=name, rate=args['rate'], ranking=args['ranking'])
        db.session.add(new_movie)
        db.session.commit()
        return new_movie, 201

api.add_resource(MovieResource, '/movie/<string:name>')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)