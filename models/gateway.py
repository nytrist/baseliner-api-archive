from db import db

class GatewayModel(db.Model):
	__tablename__ = 'gateways'

	id = db.Column(db.Integer, primary_key=True)
	gw_id = db.Column(db.String(20))
	gw_site = db.Column(db.String(20))
	gw_addr = db.Column(db.Integer)
	gw_locate = db.Column(db.String(20))
	gw_url = db.Column(db.String(20))
	gw_dir = db.Column(db.String(20))
	gw_port = db.Column(db.Integer)

	stations = db.relationship('StationModel', lazy='dynamic')

	def __init__(self, gw_id, gw_site, gw_addr, gw_locate, gw_url, gw_dir, gw_port):
		self.gw_id = gw_id
		self.gw_site = gw_site
		self.gw_addr = gw_addr
		self.gw_locate = gw_locate
		self.gw_url = gw_url
		self.gw_dir = gw_dir
		self.gw_port = gw_port

	def json(self):
		return{'gw_id': self.gw_id, 'gw_site': self.gw_site, 'gw_addr': self.gw_addr, 'gw_locate': self.gw_locate, 'gw_url': self.gw_url, 'gw_dir': self.gw_dir, 'gw_port': self.gw_port,'stations': [station.json() for station in self.stations.all()]} #may need to remove .all() if too slow

#search by gateway ID
	@classmethod
	def find_by_id(cls, gw_id):
		return cls.query.filter_by(gw_id=gw_id).first()

#insert new gateway, update existing gateway
	def save_to_db(self):
		db.session.add(self)
		db.session.commit()

#delete gateway
	def delete_from_db(self):
		db.session.delete(self)
		db.session.commit()
