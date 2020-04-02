#import SQLAlchemy as SQLAlchemy


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, Text

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///pin.db'
db=SQLAlchemy(app)

class Pin(db.Model):
    id=Column(Integer,primary_key=True)
    title=Column(Text,unique=False)
    image=Column(Text,unique=False)

db.create_all()
@app.route('/')
def hello_world():
    return 'Hello world'
app.debug=True
if __name__=='__main__':
    app.run()