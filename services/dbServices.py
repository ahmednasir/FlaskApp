from sqlalchemy import create_engine,and_,or_,update,Table
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session


def connect():
    try:
        db = "Test"
        host = "127.0.0.1"
        username = "root"
        password = ""
        engine = create_engine("mysql+pymysql://"+username+":"+password+"@"+host+"/"+db,pool_size=20, max_overflow=0)
        print("Connected")
        if engine:
            base = automap_base()
            base.prepare(engine, reflect=True)
            session = Session(engine)
            model = base.classes.InfoTable
            return engine, model, session

        return False, False, False
    except Exception as ex:
        print(ex)
        return False, False, False