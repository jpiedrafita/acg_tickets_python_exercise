from flask_sqlalchemy import SQLAlchemy

#Creates a database
db = SQLAlchemy()

#Class for ticket model
class Ticket(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), nullable=False)
  status = db.Column(db.Integer, nullable=False)
  url = db.Column(db.String(100), nullable=True)

  statuses_dic = {
    0: 'Reported',
    1: 'In Progress',
    2: 'In Review',
    3: 'Resolved'
  }

  def status_string(self):
    return self.statuses_dic[self.status]
    
  def to_json(self):
    """
    Return the JSON serializable fromat
    """
    return {
      'id': self.id,
      'name': self.name,
      'status': self.status_string(),
      'url': self.url
    }