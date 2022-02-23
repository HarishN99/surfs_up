# #import dependencies
# import datetime as dt
# import numpy as np
# import pandas as pd
# import sqlalchemy
# from sqlalchemy.ext.automap import automap_base
# from sqlalchemy.orm import Session
# from sqlalchemy import create_engine, func
# from flask import Flask, jsonify

from flask import Flask

# engine = create_engine("sqlite:///hawaii.sqlite")

# Base = automap_base()
# Base.prepare(engine, reflect=True)
# Measurement = Base.classes.measurement
# Station = Base.classes.station

# session = Session(engine)

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world'

# def welcome():
#     return(
#     '''
#     Welcome to the Climate Analysis API!
#     Available Routes:
#     /api/v1.0/precipitation
#     /api/v1.0/stations
#     /api/v1.0/tobs
#     /api/v1.0/temp/start/end
#     ''')


# # export FLASK_APP=app.py

# # flask run 