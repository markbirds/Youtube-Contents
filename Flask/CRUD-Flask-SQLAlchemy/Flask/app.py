from flask import Flask, redirect, url_for, render_template, request, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'FALSE'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.name

@app.route('/')
def index():
  return render_template('content/index.html')

@app.route('/create',methods=['POST','GET'])
def create():
  if request.method == 'POST':
    name = request.form['name']
    age = request.form['age']  
    user = User(name=name,age=age)
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('index'))
  return render_template('content/create.html')

@app.route('/read')
def read():
  users = User.query.all()
  return render_template('content/read.html',context=users)

@app.route('/update',methods=['POST','GET'])
def update():
  if request.method == 'POST':
    name = request.form['name']
    age = request.form['age']
    id = request.form['id']
    user = User.query.filter_by(id=id).first()
    user.name = name
    user.age = age
    db.session.commit()
    return redirect(url_for('update'))
  else:
    users = User.query.all()
    return render_template('content/update.html',context=users)

@app.route('/update/<int:id>',methods=['POST','GET'])
def update_details(id):
  user = User.query.filter_by(id=id).first()
  return render_template('content/update_form.html',context=user)

@app.route('/delete')
def delete():
  users = User.query.all()
  return render_template('content/delete.html',context=users)

@app.route('/delete/<int:id>',methods=['POST','GET'])
def delete_details(id):
  user = User.query.filter_by(id=id).first()
  db.session.delete(user)
  db.session.commit()
  return redirect(url_for('index'))

if __name__ == '__main__':
  app.run(debug=True)