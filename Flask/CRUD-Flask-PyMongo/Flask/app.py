from flask import Flask, redirect, url_for, render_template, request, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/CRUD"
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
mongo = PyMongo(app)
crud = mongo.db.crud

@app.route('/')
def index():
  return render_template('content/index.html')

@app.route('/create',methods=['POST','GET'])
def create():
  if request.method == 'POST':
    name = request.form['name']
    age = request.form['age']  
    user = {'name':name,'age':age}
    crud.insert_one(user)
    return redirect(url_for('index'))
  return render_template('content/create.html')

@app.route('/read')
def read():
  users = crud.find()
  return render_template('content/read.html',context=users)

@app.route('/update',methods=['POST','GET'])
def update():
  if request.method == 'POST':
    name = request.form['name']
    age = request.form['age']
    id = request.form['id']
    filter = {'_id':ObjectId(id)}
    update = {'$set':{'name':name,'age':age}}
    crud.update_one(filter,update)
    return redirect(url_for('update'))
  else:
    users = crud.find()
    return render_template('content/update.html',context=users)

@app.route('/update/<id>',methods=['POST','GET'])
def update_details(id):
  filter = {'_id':ObjectId(id)}
  user = crud.find_one(filter)
  return render_template('content/update_form.html',context=user)

@app.route('/delete')
def delete():
  users = crud.find()
  return render_template('content/delete.html',context=users)

@app.route('/delete/<id>',methods=['POST','GET'])
def delete_details(id):
  filter = {'_id':ObjectId(id)}
  crud.delete_one(filter)
  return redirect(url_for('index'))

if __name__ == '__main__':
  app.run(debug=True)