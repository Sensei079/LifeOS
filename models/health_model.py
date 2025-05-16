from models import db


class HealthLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    metric = db.Column(db.String(120), nullable=False)
    value = db.Column(db.String(50), nullable=False)
    date = db.Column(db.String(50))

    def to_dict(self):
        return {
            "id": self.id,
            "metric": self.metric,
            "value": self.value,
            "date": self.date
        }
