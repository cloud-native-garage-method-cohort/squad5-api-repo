from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import json
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI', default='mysql+pymysql://root:123456@localhost:3306/wordpress-mysql')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS', default=True)
db = SQLAlchemy(app, use_native_unicode='utf8')


class Member(db.Model):
    __tablename__ = 'squad5_members'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    role = db.Column(db.String(255))
    reserved = db.Column(db.String(255))


@app.route('/', methods=['GET'])
def index():
    return 'Squad 5 API'


@app.route('/search', methods=['POST'])
def search():
    data = json.loads(json.dumps(request.form, ensure_ascii=False))
    print(data)
    member = Member.query.filter(Member.name==data['name']).first()
    return jsonify({'name': member.name, 'role': member.role, 'reserved': member.reserved})


@app.route('/add', methods=['POST'])
def add():
    data = json.loads(json.dumps(request.form, ensure_ascii=False))
    member = Member(name=data['name'], role=data['role'], reserved=['reserved'])
    db.session.add(member)
    db.session.commit()
    return jsonify({'result': "OK"})


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
