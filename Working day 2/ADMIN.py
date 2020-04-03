from flask import Flask,render_template,url_for,request,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

#initiate the database
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///test.db'
db=SQLAlchemy(app)

#There will be id, content and datetime in the database table
class Todo(db.model):
    id=Column(Integer.primary_key=True)
    content=Column(String(200),nullable=False)
    date_created=Column(DateTime,default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>'% self.id
#add the books by admin
@app.route('/',methods=['POST','GET'])
def index():
    if request.method=='POST':
        task_content=request.form['content']
        new_task=Todo(content=task_content)
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return"There is a problem adding your book"
    else
        tasks=Todo.query.order_by(Todo.date_created).all()
        return render_template('index.html',tasks=tasks)
#delete the book
@app.route('/delete/<init:id>')
def delete(id):
    task_to_delete=Todo.query.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')

    except:
        return "There is a problem deleting this book"
#update the book's information
@app.route('/update/<init:id>',methods=['GET','POST'])
def update(id):
    task = Todo.query.get_or_404(id)
    if request.method=='POST':
        task.content=request.form['content']
        try:
            db.session.commit()
            return redirect('/')
        except:
            return "There is a problem updating the book"
    else:
        return render_template('update.html',task=task)
#run the app
if __name__=="__main__":
    app.run(debug=True)


