from flask import *
#from flask_sqlalchemy import SQLAlchemy
#import os


app = Flask(__name__)

@app.route("/details",methods=['GET'])


def hello():

    return  jsonify ({"Empid": "21"})

    

if __name__ =='__main__':

    app.run(debug=True)