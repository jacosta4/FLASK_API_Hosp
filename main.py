from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


class Welcome(Resource):
    def get(self):
        return {"data": "Welcome to this API"}

    def post(self):
        return {"data": "Posted"}


api.add_resource(Welcome, "/welcome")

if __name__ == '__main__':
    app.run(debug=True)
