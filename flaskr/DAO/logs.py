# TODO REFACTOR AS DISCUSSED VENKAT
from flaskr.models import db, Logs, Users, Aircrafts, CategoryEnum, CertificateEnum, Ratings


def createLogs(**kwargs):
    newLog = Logs(
        sic_time = kwargs.get('sic_time', None),
        total_time=kwargs.get('total_time', None),
        pic_time=kwargs.get('pic_time', None),
        date=kwargs.get('date', None),
        night_time=kwargs.get('night_time', None),
        day_time=kwargs.get('day_time', None),
        xc_time=kwargs.get('xc_time', None),
        dual_received=kwargs.get('dual_received', None),
        dual_given=kwargs.get('dual_given', None),
        actual_instrument=kwargs.get('actual_instrument', None),
        simulated_instrument=kwargs.get('simulated_instrument', None),
        departure=kwargs.get('departure', None),
        destination=kwargs.get('destination', None),
        via=kwargs.get('via', None),
        day_landings=kwargs.get('day_landings', None),
        night_landings=kwargs.get('night_landings', None),
        num_instrument_approaches=kwargs.get('num_instrument_approaches', None),
        remarks=kwargs.get('remarks', None),
        user_id=kwargs.get('user_id', None),
        aircraft_id=kwargs.get('aircraft_id', None),
        created=kwargs.get('created', None),
        updated=kwargs.get('updated', None)
    )
    db.session.add(newLog)
    db.session.commit()


def updateLogs(id, **kwargs):
    if(kwargs.get('sic_time', None)):
        db.session.get(id).sic_time = kwargs.get('sic_time')
    if(kwargs.get('total_time', None)):
        db.session.get(id).total_time = kwargs.get('total_time')
    if(kwargs.get('pic_time', None)):
        db.session.get(id).pic_time = kwargs.get('pic_time')
    if(kwargs.get('date', None)):
        db.session.get(id).date = kwargs.get('date')
    if(kwargs.get('night_time', None)):
        db.session.get(id).night_time = kwargs.get('night_time')
    if(kwargs.get('day_time', None)):
        db.session.get(id).day_time = kwargs.get('day_time')
    if(kwargs.get('xc_time', None)):
        db.session.get(id).xc_time = kwargs.get('xc_time')
    if(kwargs.get('dual_received', None)):
        db.session.get(id).dual_received = kwargs.get('dual_received')
    if(kwargs.get('dual_given', None)):
        db.session.get(id).dual_given = kwargs.get('dual_given')
    if(kwargs.get('actual_instrument', None)):
        db.session.get(id).actual_instrument = kwargs.get('actual_instrument')
    if(kwargs.get('simulated_instrument', None)):
        db.session.get(id).simulated_instrument = kwargs.get('simulated_instrument')
    if(kwargs.get('departure', None)):
        db.session.get(id).departure = kwargs.get('departure')
    if(kwargs.get('destination', None)):
        db.session.get(id).destination = kwargs.get('destination')
    if(kwargs.get('via', None)):
        db.session.get(id).via = kwargs.get('via')
    if(kwargs.get('day_landings', None)):
        db.session.get(id).day_landings = kwargs.get('day_landings')
    if(kwargs.get('night_landings', None)):
        db.session.get(id).night_landings = kwargs.get('night_landings')
    if(kwargs.get('num_instrument_approaches', None)):
        db.session.get(id).num_instrument_approaches = kwargs.get('num_instrument_approaches')
    if(kwargs.get('remarks', None)):
        db.session.get(id).remarks = kwargs.get('remarks')
    if(kwargs.get('user_id', None)):
        db.session.get(id).user_id = kwargs.get('user_id')
    if(kwargs.get('aircraft_id', None)):
        db.session.get(id).aircraft_id = kwargs.get('aircraft_id')
    if(kwargs.get('created', None)):
        db.session.get(id).created = kwargs.get('created')
    if(kwargs.get('updated', None)):
        db.session.get(id).updated = kwargs.get('updated')
    db.session.commit()


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
