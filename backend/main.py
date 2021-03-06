# from app import app

from flask import *
from flask_cors import CORS
import flask_sqlalchemy
import flask_restless
import json

# Create the Flask application and the Flask-SQLAlchemy object
app = Flask(__name__)
CORS(app)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:SWEswe-123@empowering-db.ccanwhd1wsdp.us-east-1.rds.amazonaws.com:3306/empowering_db1'
db = flask_sqlalchemy.SQLAlchemy(app)

# @app.route('/')
# def hello_world():
#     return 'Hello World'

# Define models
class State(db.Model):
	__tablename__ = 'State'
	name = db.Column(db.Unicode, primary_key=True)
	population = db.Column(db.Integer)
	median_hh_income = db.Column(db.Integer)
	dominant_party = db.Column(db.Unicode)
	primary_energy_source_1 = db.Column(db.Unicode)
	primary_energy_source_2 = db.Column(db.Unicode)
	primary_energy_source_3 = db.Column(db.Unicode)

class CongressMember(db.Model):
	__tablename__ = 'CongressMember'
	member_id = db.Column(db.Unicode, primary_key=True)
	first_name = db.Column(db.Unicode)
	last_name = db.Column(db.Unicode)
	date_of_birth = db.Column(db.Unicode)
	party = db.Column(db.Unicode)
	state = db.Column(db.Unicode, db.ForeignKey('State.name'))
	state_rs = db.relationship(State, backref=db.backref('congress_members'))
	state_abr = db.Column(db.Unicode)
	district = db.Column(db.Unicode)
	votes_with_party_pct = db.Column(db.Unicode)
	office = db.Column(db.Unicode)
	twitter_account = db.Column(db.Unicode)
	title = db.Column(db.Unicode)
	facebook_account = db.Column(db.Unicode)
	phone = db.Column(db.Unicode)
	url = db.Column(db.Unicode)
	cspan_id = db.Column(db.Unicode)
	image_url = db.Column(db.Unicode)

class Bills(db.Model):
	__tablename__ = 'Bills'
	bill_id = db.Column(db.Unicode, primary_key=True)
	bill_type = db.Column(db.Unicode)
	title = db.Column(db.Unicode)
	short_title = db.Column(db.Unicode)
	sponsor_id = db.Column(db.Unicode, db.ForeignKey('CongressMember.member_id'))
	sponsor_rs = db.relationship(CongressMember, backref=db.backref('bills_sponsored'))
	introduced_date = db.Column(db.Unicode)
	cosponsors_by_party_R = db.Column(db.Integer)
	cosponsors_by_party_D = db.Column(db.Integer)
	committees = db.Column(db.Unicode)
	active = db.Column(db.Boolean)
	congressdotgov_url = db.Column(db.Unicode)
	govtrack_url = db.Column(db.Unicode)
	house_passage = db.Column(db.Unicode)
	senate_passage = db.Column(db.Unicode)
	summary = db.Column(db.Unicode)
	summary_short = db.Column(db.Unicode)

class Petroleum(db.Model):
	__tablename__ = 'Petroleum'
	state_name = db.Column(db.Unicode, db.ForeignKey('State.name'), primary_key=True)
	state_rs = db.relationship(State, backref=db.backref('petroleum_data'))
	data_1993 = db.Column(db.Integer)
	data_1994 = db.Column(db.Integer)
	data_1995 = db.Column(db.Integer)
	data_1996 = db.Column(db.Integer)
	data_1997 = db.Column(db.Integer)
	data_1998 = db.Column(db.Integer)
	data_1999 = db.Column(db.Integer)
	data_2000 = db.Column(db.Integer)
	data_2001 = db.Column(db.Integer)
	data_2002 = db.Column(db.Integer)
	data_2003 = db.Column(db.Integer)
	data_2004 = db.Column(db.Integer)
	data_2005 = db.Column(db.Integer)
	data_2006 = db.Column(db.Integer)
	data_2007 = db.Column(db.Integer)
	data_2008 = db.Column(db.Integer)
	data_2009 = db.Column(db.Integer)
	data_2010 = db.Column(db.Integer)
	data_2011 = db.Column(db.Integer)
	data_2012 = db.Column(db.Integer)
	data_2013 = db.Column(db.Integer)
	data_2014 = db.Column(db.Integer)
	data_2015 = db.Column(db.Integer)
	data_2016 = db.Column(db.Integer)
	data_2017 = db.Column(db.Integer)

class Biomass(db.Model):
	__tablename__ = 'Biomass'
	state_name = db.Column(db.Unicode, db.ForeignKey('State.name'), primary_key=True)
	state_rs = db.relationship(State, backref=db.backref('biomass_data'))
	data_1993 = db.Column(db.Integer)
	data_1994 = db.Column(db.Integer)
	data_1995 = db.Column(db.Integer)
	data_1996 = db.Column(db.Integer)
	data_1997 = db.Column(db.Integer)
	data_1998 = db.Column(db.Integer)
	data_1999 = db.Column(db.Integer)
	data_2000 = db.Column(db.Integer)
	data_2001 = db.Column(db.Integer)
	data_2002 = db.Column(db.Integer)
	data_2003 = db.Column(db.Integer)
	data_2004 = db.Column(db.Integer)
	data_2005 = db.Column(db.Integer)
	data_2006 = db.Column(db.Integer)
	data_2007 = db.Column(db.Integer)
	data_2008 = db.Column(db.Integer)
	data_2009 = db.Column(db.Integer)
	data_2010 = db.Column(db.Integer)
	data_2011 = db.Column(db.Integer)
	data_2012 = db.Column(db.Integer)
	data_2013 = db.Column(db.Integer)
	data_2014 = db.Column(db.Integer)
	data_2015 = db.Column(db.Integer)
	data_2016 = db.Column(db.Integer)
	data_2017 = db.Column(db.Integer)

class Coal(db.Model):
	__tablename__ = 'Coal'
	state_name = db.Column(db.Unicode, db.ForeignKey('State.name'), primary_key=True)
	state_rs = db.relationship(State, backref=db.backref('coal_data'))
	data_1993 = db.Column(db.Integer)
	data_1994 = db.Column(db.Integer)
	data_1995 = db.Column(db.Integer)
	data_1996 = db.Column(db.Integer)
	data_1997 = db.Column(db.Integer)
	data_1998 = db.Column(db.Integer)
	data_1999 = db.Column(db.Integer)
	data_2000 = db.Column(db.Integer)
	data_2001 = db.Column(db.Integer)
	data_2002 = db.Column(db.Integer)
	data_2003 = db.Column(db.Integer)
	data_2004 = db.Column(db.Integer)
	data_2005 = db.Column(db.Integer)
	data_2006 = db.Column(db.Integer)
	data_2007 = db.Column(db.Integer)
	data_2008 = db.Column(db.Integer)
	data_2009 = db.Column(db.Integer)
	data_2010 = db.Column(db.Integer)
	data_2011 = db.Column(db.Integer)
	data_2012 = db.Column(db.Integer)
	data_2013 = db.Column(db.Integer)
	data_2014 = db.Column(db.Integer)
	data_2015 = db.Column(db.Integer)
	data_2016 = db.Column(db.Integer)
	data_2017 = db.Column(db.Integer)

class Geothermal(db.Model):
	__tablename__ = 'Geothermal'
	state_name = db.Column(db.Unicode, db.ForeignKey('State.name'), primary_key=True)
	state_rs = db.relationship(State, backref=db.backref('geothermal_data'))
	data_1993 = db.Column(db.Integer)
	data_1994 = db.Column(db.Integer)
	data_1995 = db.Column(db.Integer)
	data_1996 = db.Column(db.Integer)
	data_1997 = db.Column(db.Integer)
	data_1998 = db.Column(db.Integer)
	data_1999 = db.Column(db.Integer)
	data_2000 = db.Column(db.Integer)
	data_2001 = db.Column(db.Integer)
	data_2002 = db.Column(db.Integer)
	data_2003 = db.Column(db.Integer)
	data_2004 = db.Column(db.Integer)
	data_2005 = db.Column(db.Integer)
	data_2006 = db.Column(db.Integer)
	data_2007 = db.Column(db.Integer)
	data_2008 = db.Column(db.Integer)
	data_2009 = db.Column(db.Integer)
	data_2010 = db.Column(db.Integer)
	data_2011 = db.Column(db.Integer)
	data_2012 = db.Column(db.Integer)
	data_2013 = db.Column(db.Integer)
	data_2014 = db.Column(db.Integer)
	data_2015 = db.Column(db.Integer)
	data_2016 = db.Column(db.Integer)
	data_2017 = db.Column(db.Integer)

class Hydroelectricity(db.Model):
	__tablename__ = 'Hydroelectricity'
	state_name = db.Column(db.Unicode, db.ForeignKey('State.name'), primary_key=True)
	state_rs = db.relationship(State, backref=db.backref('hydroelectricity_data'))
	data_1993 = db.Column(db.Integer)
	data_1994 = db.Column(db.Integer)
	data_1995 = db.Column(db.Integer)
	data_1996 = db.Column(db.Integer)
	data_1997 = db.Column(db.Integer)
	data_1998 = db.Column(db.Integer)
	data_1999 = db.Column(db.Integer)
	data_2000 = db.Column(db.Integer)
	data_2001 = db.Column(db.Integer)
	data_2002 = db.Column(db.Integer)
	data_2003 = db.Column(db.Integer)
	data_2004 = db.Column(db.Integer)
	data_2005 = db.Column(db.Integer)
	data_2006 = db.Column(db.Integer)
	data_2007 = db.Column(db.Integer)
	data_2008 = db.Column(db.Integer)
	data_2009 = db.Column(db.Integer)
	data_2010 = db.Column(db.Integer)
	data_2011 = db.Column(db.Integer)
	data_2012 = db.Column(db.Integer)
	data_2013 = db.Column(db.Integer)
	data_2014 = db.Column(db.Integer)
	data_2015 = db.Column(db.Integer)
	data_2016 = db.Column(db.Integer)
	data_2017 = db.Column(db.Integer)

class NaturalGas(db.Model):
	__tablename__ = 'NaturalGas'
	state_name = db.Column(db.Unicode, db.ForeignKey('State.name'), primary_key=True)
	state_rs = db.relationship(State, backref=db.backref('naturalgas_data'))
	data_1993 = db.Column(db.Integer)
	data_1994 = db.Column(db.Integer)
	data_1995 = db.Column(db.Integer)
	data_1996 = db.Column(db.Integer)
	data_1997 = db.Column(db.Integer)
	data_1998 = db.Column(db.Integer)
	data_1999 = db.Column(db.Integer)
	data_2000 = db.Column(db.Integer)
	data_2001 = db.Column(db.Integer)
	data_2002 = db.Column(db.Integer)
	data_2003 = db.Column(db.Integer)
	data_2004 = db.Column(db.Integer)
	data_2005 = db.Column(db.Integer)
	data_2006 = db.Column(db.Integer)
	data_2007 = db.Column(db.Integer)
	data_2008 = db.Column(db.Integer)
	data_2009 = db.Column(db.Integer)
	data_2010 = db.Column(db.Integer)
	data_2011 = db.Column(db.Integer)
	data_2012 = db.Column(db.Integer)
	data_2013 = db.Column(db.Integer)
	data_2014 = db.Column(db.Integer)
	data_2015 = db.Column(db.Integer)
	data_2016 = db.Column(db.Integer)
	data_2017 = db.Column(db.Integer)

class NuclearPower(db.Model):
	__tablename__ = 'NuclearPower'
	state_name = db.Column(db.Unicode, db.ForeignKey('State.name'), primary_key=True)
	state_rs = db.relationship(State, backref=db.backref('nuclearpower_data'))
	data_1993 = db.Column(db.Integer)
	data_1994 = db.Column(db.Integer)
	data_1995 = db.Column(db.Integer)
	data_1996 = db.Column(db.Integer)
	data_1997 = db.Column(db.Integer)
	data_1998 = db.Column(db.Integer)
	data_1999 = db.Column(db.Integer)
	data_2000 = db.Column(db.Integer)
	data_2001 = db.Column(db.Integer)
	data_2002 = db.Column(db.Integer)
	data_2003 = db.Column(db.Integer)
	data_2004 = db.Column(db.Integer)
	data_2005 = db.Column(db.Integer)
	data_2006 = db.Column(db.Integer)
	data_2007 = db.Column(db.Integer)
	data_2008 = db.Column(db.Integer)
	data_2009 = db.Column(db.Integer)
	data_2010 = db.Column(db.Integer)
	data_2011 = db.Column(db.Integer)
	data_2012 = db.Column(db.Integer)
	data_2013 = db.Column(db.Integer)
	data_2014 = db.Column(db.Integer)
	data_2015 = db.Column(db.Integer)
	data_2016 = db.Column(db.Integer)
	data_2017 = db.Column(db.Integer)

class SolarEnergy(db.Model):
	__tablename__ = 'SolarEnergy'
	state_name = db.Column(db.Unicode, db.ForeignKey('State.name'), primary_key=True)
	state_rs = db.relationship(State, backref=db.backref('solarenergy_data'))
	data_1993 = db.Column(db.Integer)
	data_1994 = db.Column(db.Integer)
	data_1995 = db.Column(db.Integer)
	data_1996 = db.Column(db.Integer)
	data_1997 = db.Column(db.Integer)
	data_1998 = db.Column(db.Integer)
	data_1999 = db.Column(db.Integer)
	data_2000 = db.Column(db.Integer)
	data_2001 = db.Column(db.Integer)
	data_2002 = db.Column(db.Integer)
	data_2003 = db.Column(db.Integer)
	data_2004 = db.Column(db.Integer)
	data_2005 = db.Column(db.Integer)
	data_2006 = db.Column(db.Integer)
	data_2007 = db.Column(db.Integer)
	data_2008 = db.Column(db.Integer)
	data_2009 = db.Column(db.Integer)
	data_2010 = db.Column(db.Integer)
	data_2011 = db.Column(db.Integer)
	data_2012 = db.Column(db.Integer)
	data_2013 = db.Column(db.Integer)
	data_2014 = db.Column(db.Integer)
	data_2015 = db.Column(db.Integer)
	data_2016 = db.Column(db.Integer)
	data_2017 = db.Column(db.Integer)

class WindEnergy(db.Model):
	__tablename__ = 'WindEnergy'
	state_name = db.Column(db.Unicode, db.ForeignKey('State.name'), primary_key=True)
	state_rs = db.relationship(State, backref=db.backref('windenergy_data'))
	data_1993 = db.Column(db.Integer)
	data_1994 = db.Column(db.Integer)
	data_1995 = db.Column(db.Integer)
	data_1996 = db.Column(db.Integer)
	data_1997 = db.Column(db.Integer)
	data_1998 = db.Column(db.Integer)
	data_1999 = db.Column(db.Integer)
	data_2000 = db.Column(db.Integer)
	data_2001 = db.Column(db.Integer)
	data_2002 = db.Column(db.Integer)
	data_2003 = db.Column(db.Integer)
	data_2004 = db.Column(db.Integer)
	data_2005 = db.Column(db.Integer)
	data_2006 = db.Column(db.Integer)
	data_2007 = db.Column(db.Integer)
	data_2008 = db.Column(db.Integer)
	data_2009 = db.Column(db.Integer)
	data_2010 = db.Column(db.Integer)
	data_2011 = db.Column(db.Integer)
	data_2012 = db.Column(db.Integer)
	data_2013 = db.Column(db.Integer)
	data_2014 = db.Column(db.Integer)
	data_2015 = db.Column(db.Integer)
	data_2016 = db.Column(db.Integer)
	data_2017 = db.Column(db.Integer)

class WoodAndWaste(db.Model):
	__tablename__ = 'WoodAndWaste'
	state_name = db.Column(db.Unicode, db.ForeignKey('State.name'), primary_key=True)
	state_rs = db.relationship(State, backref=db.backref('woodandwaste_data'))
	data_1993 = db.Column(db.Integer)
	data_1994 = db.Column(db.Integer)
	data_1995 = db.Column(db.Integer)
	data_1996 = db.Column(db.Integer)
	data_1997 = db.Column(db.Integer)
	data_1998 = db.Column(db.Integer)
	data_1999 = db.Column(db.Integer)
	data_2000 = db.Column(db.Integer)
	data_2001 = db.Column(db.Integer)
	data_2002 = db.Column(db.Integer)
	data_2003 = db.Column(db.Integer)
	data_2004 = db.Column(db.Integer)
	data_2005 = db.Column(db.Integer)
	data_2006 = db.Column(db.Integer)
	data_2007 = db.Column(db.Integer)
	data_2008 = db.Column(db.Integer)
	data_2009 = db.Column(db.Integer)
	data_2010 = db.Column(db.Integer)
	data_2011 = db.Column(db.Integer)
	data_2012 = db.Column(db.Integer)
	data_2013 = db.Column(db.Integer)
	data_2014 = db.Column(db.Integer)
	data_2015 = db.Column(db.Integer)
	data_2016 = db.Column(db.Integer)
	data_2017 = db.Column(db.Integer)

class Congresses(db.Model):
	__tablename__ = "Congresses"
	id = db.Column(db.Unicode, primary_key = True)
	member_id = db.Column(db.Integer, db.ForeignKey('CongressMember.member_id'))
	member_rs = db.relationship(CongressMember, backref=db.backref('congresses')) # adds 'congresses' list to CongressMember instances
	chamber = db.Column(db.Unicode)
	con_num = db.Column(db.Integer)

class Cosponsors(db.Model):
	__tablename__ = "Cosponsors"
	id = db.Column(db.Integer, primary_key=True)
	bill_id = db.Column(db.Unicode, db.ForeignKey('Bills.bill_id'))
	bill_rs = db.relationship(Bills, backref=db.backref('cosponsors'))
	cosponsor_id = db.Column(db.Unicode, db.ForeignKey('CongressMember.member_id'))
	cosponsor_rs = db.relationship(CongressMember, backref=db.backref('bills_cosponsored'))

# Create the Flask-Restless API manager and initialize it with our Flask app
manager = flask_restless.APIManager(app, flask_sqlalchemy_db=db)

# Generate APIs for the models
manager.create_api(CongressMember, methods=['GET'], max_results_per_page=9, collection_name='congressmembers')
manager.create_api(Bills, methods=['GET'], max_results_per_page=9, collection_name='bills')
manager.create_api(State, methods=['GET'], max_results_per_page=9, collection_name='states')
manager.create_api(Petroleum, methods=['GET'], max_results_per_page=9, collection_name='petroleum')
manager.create_api(Biomass, methods=['GET'], max_results_per_page=9, collection_name='biomass')
manager.create_api(Coal, methods=['GET'], max_results_per_page=9, collection_name='coal')
manager.create_api(Geothermal, methods=['GET'], max_results_per_page=9, collection_name='geothermal')
manager.create_api(Hydroelectricity, methods=['GET'], max_results_per_page=9, collection_name='hydroelectricity')
manager.create_api(NaturalGas, methods=['GET'], max_results_per_page=9, collection_name='naturalgas')
manager.create_api(NuclearPower, methods=['GET'], max_results_per_page=9, collection_name='nuclearpower')
manager.create_api(SolarEnergy, methods=['GET'], max_results_per_page=9, collection_name='solarenergy')
manager.create_api(WindEnergy, methods=['GET'], max_results_per_page=9, collection_name='windenergy')
manager.create_api(WoodAndWaste, methods=['GET'], max_results_per_page=9, collection_name='woodandwaste')
manager.create_api(Congresses, methods=['GET'], max_results_per_page=9, collection_name='congresses')
manager.create_api(Cosponsors, methods=['GET'], max_results_per_page=9, collection_name='cosponsors')


app.run(host="0.0.0.0")