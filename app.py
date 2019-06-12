from flask import Flask, render_template
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS
from sendmail import sendMail

#from flask_jwt import JWT, jwt_required
#from security import authenticate,identity


app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})
api = Api(app)
# CORS(app)

@app.route('/')
#@app.cross_origin()
def home():
    return render_template('index.html')
    

#@app.cross_origin()
class DataSet(Resource):

    def post(self):
        parser = reqparse.RequestParser()
        print("printing Parser")
        print(parser)
        

        parser.add_argument('data',
            type=dict,
            required = False,
            help = "Object Data Not Found"
        )
        parser.add_argument('sender_id',
            type=str,
            required = False,
            help = "sender_id Data Not Found"
        )
        parser.add_argument('sender_pass',
            type=str,
            required = False,
            help = "sender_pass Data Not Found"
        )
        parser.add_argument('target_id',
            type=str,
            required = False,
            help = "target_id Data Not Found"
        )
        

        request_data = parser.parse_args()


        # print("Request Data")
        # print(request_data)
        print("Request Data str")
        print(str(request_data["data"]))
        subject = "This is JSON data"
        if sendMail(request_data['sender_id'],request_data['sender_pass'],request_data['target_id'],subject,str(request_data['data'])):
            print(str(request_data))
            return request_data,200
        else:
            return {'Message':"Failed"},404
        

        




api.add_resource(DataSet,'/DataSet')
if __name__ == '__main__':
    app.run(port=5000)




