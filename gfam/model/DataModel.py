from gfam import db


class GeneData(db.Model):
    __tablename__= 'gfam_id'
    id = db.Column(db.Integer, primary_key=True)
    gfam_id = db.Column(db.String(10))
    name = db.Column(db.String(45))

    def __repr__(self):
         return '<User: {}>'.format(self.gfam_id)
