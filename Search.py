from flask import Flask,render_template,url_for,request,redirect
from flask_sqlalchemy import SQLAlchemy
import flask_whooshalchemy as wa


#initiate the database
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///pin.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
app.config['WHOOSH_BASE']='whoosh'
db=SQLAlchemy(app)

class Todo(db.Model):
    __searchable__=['content']
    id=db.Column(db.Integer,primary_key=True)
    content=db.Column(db.String(200),nullable=False)

wa.whoosh_index(app,Todo)
@app.route('/')
def index():
    return render_template('search.html')

if __name__=="__main__":
    app.run(debug=True)
