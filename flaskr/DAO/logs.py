# TODO REFACTOR AS DISCUSSED VENKAT
from flaskr.models import db, Logs, Users, Aircrafts,  Ratings


def createLog(**kwargs):
    newLog = Logs()
    if kwargs.get('sic_time'):
       newLog.sic_time = kwargs.get('sic_time')
    if kwargs.get('total_time'):
        newLog.total_time = kwargs.get('total_time')
    if kwargs.get('pic_time'):
        newLog.get('pic_time')
    if kwargs.get('date'):
        newLog.date = kwargs.get('date')
    if kwargs.get('night_time'):
        newLog.night_time = kwargs.get('night_time')
    if kwargs.get('day_time'):
        newLog.day_time = kwargs.get('day_time')
    if kwargs.get('xc_time'):
        newLog.xc_time = kwargs.get('xc_time')
    if kwargs.get('dual_received'):
        newLog.dual_received = kwargs.get('dual_received')
    if kwargs.get('dual_given'):
        newLog.dual_given = kwargs.get('dual_given')
    if kwargs.get('actual_instrument'):
        newLog.actual_instrument = kwargs.get('actual_instrument')
    if kwargs.get('simulated_instrument'):
        newLog.simulated_instrument = kwargs.get('simulated_instrument')
    if kwargs.get('departure'):
        newLog.departure = kwargs.get('departure')
    if kwargs.get('destination'):
        newLog.destination = kwargs.get('destination')
    if kwargs.get('via'):
        newLog.via = kwargs.get('via')
    if kwargs.get('day_landings'):
        newLog.day_landings = kwargs.get('day_landings')
    if kwargs.get('night_landings'):
        newLog.night_landings = kwargs.get('night_landings')
    if kwargs.get('num_instrument_approaches'):
        newLog.num_instrument_approaches = kwargs.get('num_instrument_approaches')
    if kwargs.get('remarks'):
        newLog.remarks = kwargs.get('remarks')
    if kwargs.get('user_id'):
        newLog.user_id = kwargs.get('user_id')
    if kwargs.get('aircraft_id'):
        newLog.aircraft_id = kwargs.get('aircraft_id')
    if kwargs.get('created'):
        newLog.created = kwargs.get('created')
    if kwargs.get('updated'):
        newLog.updated = kwargs.get('updated')

    db.session.add(newLog)
    db.session.commit()


def updateLogs(id, **kwargs):
    if kwargs.get('sic_time'):
        db.session.query(Logs).get(id).sic_time = kwargs.get('sic_time')
    if kwargs.get('total_time'):
        db.session.query(Logs).get(id).total_time = kwargs.get('total_time')
    if kwargs.get('pic_time'):
        db.session.query(Logs).get(id).pic_time = kwargs.get('pic_time')
    if kwargs.get('date'):
        db.session.query(Logs).get(id).date = kwargs.get('date')
    if kwargs.get('night_time'):
        db.session.query(Logs).get(id).night_time = kwargs.get('night_time')
    if kwargs.get('day_time'):
        db.session.query(Logs).get(id).day_time = kwargs.get('day_time')
    if kwargs.get('xc_time'):
        db.session.query(Logs).get(id).xc_time = kwargs.get('xc_time')
    if kwargs.get('dual_received'):
        db.session.query(Logs).get(id).dual_received = kwargs.get('dual_received')
    if kwargs.get('dual_given'):
        db.session.query(Logs).get(id).dual_given = kwargs.get('dual_given')
    if kwargs.get('actual_instrument'):
        db.session.query(Logs).get(id).actual_instrument = kwargs.get('actual_instrument')
    if kwargs.get('simulated_instrument'):
        db.session.query(Logs).get(id).simulated_instrument = kwargs.get('simulated_instrument')
    if kwargs.get('departure'):
        db.session.query(Logs).get(id).departure = kwargs.get('departure')
    if kwargs.get('destination'):
        db.session.query(Logs).get(id).destination = kwargs.get('destination')
    if kwargs.get('via'):
        db.session.query(Logs).get(id).via = kwargs.get('via')
    if kwargs.get('day_landings'):
        db.session.query(Logs).get(id).day_landings = kwargs.get('day_landings')
    if kwargs.get('night_landings'):
        db.session.query(Logs).get(id).night_landings = kwargs.get('night_landings')
    if kwargs.get('num_instrument_approaches'):
        db.session.query(Logs).get(id).num_instrument_approaches = kwargs.get('num_instrument_approaches')
    if kwargs.get('remarks'):
        db.session.query(Logs).get(id).remarks = kwargs.get('remarks')
    if kwargs.get('user_id'):
        db.session.query(Logs).get(id).user_id = kwargs.get('user_id')
    if kwargs.get('aircraft_id'):
        db.session.query(Logs).get(id).aircraft_id = kwargs.get('aircraft_id')
    if kwargs.get('created'):
        db.session.query(Logs).get(id).created = kwargs.get('created')
    if kwargs.get('updated'):
        db.session.query(Logs).get(id).updated = kwargs.get('updated')
    db.session.commit()


def findLogsById(id):
    obj = db.session.query(Logs).get(id)
    print(obj)
    print(vars(obj))
    return obj

def findLogsByUserId(id):
    obj = db.session.query(Logs).filter(Logs.user_id == id)
    return obj

def findAllLogs():
    obj = db.session.query(Logs).all()
    return obj


def deleteLog(id):
    obj = db.session.query(Logs).get(id)
    db.session.delete(obj)
    db.session.commit()
