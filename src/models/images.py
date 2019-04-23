from src import db


class Images(db.Model):

    __tablename__='images'
    
    id = db.Column(db.Integer, primary_key=True)
    event_id=db.Column(db.Integer, db.ForeignKey('event.id'),
        nullable=False)
    image_url=db.Column(db.String)
