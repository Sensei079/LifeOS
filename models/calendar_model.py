from models import db


class CalendarEvent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(50), nullable=False)
    time = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(300))

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "date": self.date,
            "time": self.time,
            "description": self.description
        }
