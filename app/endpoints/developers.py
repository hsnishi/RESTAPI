from flask_restful import Resource, reqparse, fields, marshal_with, abort
from models.developer import DeveloperModel
from db import db

resource_fields = {
    'name' : fields.String,
    'gender' : fields.String,
    'age' : fields.Integer,
    'hobby' : fields.String,
    'date_of_birth' : fields.String
}

resource_fields_get = {
    'id' : fields.Integer,
    'name' : fields.String,
    'gender' : fields.String,
    'age' : fields.Integer,
    'hobby' : fields.String,
    'date_of_birth' : fields.String
}

class Developers(Resource):
    """
    Class used to implement the GET and POST
    methods that does not receive data by URL
    """

    @marshal_with(resource_fields_get)
    def get(self):
        """
        Gets all developers from the data base

        Return:
            Returns all the information of all developers
        """
        developers = DeveloperModel.query.all()

        return developers
    
    @marshal_with(resource_fields)
    def post(self):
        """
        Adds new developers to the database
        """
        developer_post_args = reqparse.RequestParser()
        developer_post_args.add_argument("name", type=str, help="Name of the developer", required=True)
        developer_post_args.add_argument("gender", type=str, help="Gender of the developer", required=True)
        developer_post_args.add_argument("age", type=int, help="Name of the developer", required=True)
        developer_post_args.add_argument("hobby", type=str, help="Name of the developer", required=True)
        developer_post_args.add_argument("date_of_birth", type=str, help="Name of the developer", required=True)
        
        args = developer_post_args.parse_args()

        developer = DeveloperModel( name = args["name"], gender = args["gender"], age = args["age"], hobby= args["hobby"], date_of_birth = args["date_of_birth"])
        db.session.add(developer)
        db.session.commit()

        return developer,201

class Developer(Resource):
    """
    Class used to implement the GET, PUT and DELETE
    methods that receive information by the URL
    """
    @marshal_with(resource_fields_get)
    def get(self, dev_id_or_query=None):
        """
        Gets the developers from the database based on id or query
        
        Args:
            dev_id_or_query -- Querystring or ID of the developer

        Return:
            Returns the developers that satify the conditions
        """
        if dev_id_or_query[0] == '?':
            pass
        else:
            result = DeveloperModel.query.filter_by(id = int(dev_id_or_query)).first()

            if not result:
                abort(404, message = "Developer not found")
        
        return result

    @marshal_with(resource_fields_get)
    def put(self, dev_id_or_query):
        """
        Updates the information about a specific developer

        Args:
            dev_id_or_query -- ID of the developer thats the info needs to be updated

        Return:
            Returns all the information updated
        """
        developer_put_args = reqparse.RequestParser()
        developer_put_args.add_argument("name", type=str, help="Name of the developer", required=False)
        developer_put_args.add_argument("gender", type=str, help="Gender of the developer", required=False)
        developer_put_args.add_argument("age", type=int, help="Name of the developer", required=False)
        developer_put_args.add_argument("hobby", type=str, help="Name of the developer", required=False)
        developer_put_args.add_argument("date_of_birth", type=str, help="Name of the developer", required=False)

        args = developer_put_args.parse_args()

        result = DeveloperModel.query.filter_by(id = int(dev_id_or_query)).first()
        if not result:
            abort(400, message = "Developer not found, cannot update")

        if args["name"] != None:
            result.name = args["name"]
        
        if args["gender"] != None:
            result.gender = args["gender"]
        
        if args["age"] != None:
            result.age = args["age"]
        
        if args["hobby"] != None:
            result.hobby = args["hobby"]
        
        if args["date_of_birth"] != None:
            result.date_of_birth = args["date_of_birth"]

        db.session.commit()
        
        return result

    def delete(self, dev_id_or_query):
        """
        Deletes the developer from the database based on the id

        Args:
            dev_id_or_query -- ID of the developer that will be deleted

        Return:
            Returns the success or error code
        """
        result = DeveloperModel.query.filter_by(id = int(dev_id_or_query)).first()
        if not result:
            abort(400, message = "Developer ID does not exist, cannot delete")
        
        db.session.delete(result)
        db.session.commit()

        return '', 204