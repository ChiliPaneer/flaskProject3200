#TODO REFACTOR AS DISCUSSED VENKAT
from flaskr.models import db, Logs, Users, Aircrafts, CategoryEnum, CertificateEnum, Ratings

def createLogs(params):
    newLog = Logs(params)
    db.session.add(newLog)
    db.session.commit()

def updateLogs():
    return -1


def findLogsById(id):
    obj = db.session.query(Logs).get(id)
    return obj


def findAllLogs():
    obj = db.session.query(Logs).all()
    return obj

def deleteLogs(id):
    obj = db.session.query.get(id)
    db.session.delete(obj)
    db.session.commit()

