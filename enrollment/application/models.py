from datetime import datetime
from application import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Document):
    user_id = db.IntField( unique=True )
    username = db.StringField( max_length=50 )
    real_name = db.StringField( max_length=50 )
    department = db.StringField( max_length=30 )
    email    = db.StringField( max_length=30 )
    password = db.StringField( max_length=500)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def get_password(self, password):
        return check_password_hash(self.password, password)    


class Drug(db.Document):
    drug_id = db.IntField( unique=True )
    drugname = db.StringField( max_length=50 )
    inventory = db.IntField( max_length=3 )
    formulation = db.StringField( max_length=50 )
    category  =  db.StringField( max_length=20 )
    peroid = db.IntField( max_length=2 )
    about  = db.StringField( max_length=500 )


# class User(UserMixin, db.Model):
#     __tablename__ = 'user'
#     u_id          =  db.Column(db.Integer, primary_key=True, autoincrement=True, index=True)  # "id"
#     username      =  db.Column(db.String(20), index=True)  # "用户名"
#     password      =  db.Column(db.String(128))  # "密码"
#     real_name     =  db.Column(db.String(30), index=True)  # 姓名
#     department    =  db.Column(db.String(20), index=True)  # "部门"
#     email         =  db.Column(db.String(128, index=True))
#     permission    =  db.Column(db.Boolean)
#     member_since  =  db.Column(db.DateTime, default=datetime.utcnow())

#     def set_password(self, password):
#         self.password = generate_password_hash(password)

#     def get_password(self, password):
#         return check_password_hash(self.password, password)


# class Drug(db.Model):
#     __tablename__ = 'drug'
#     d_id          =    db.Column(db.Integer, primary_key=True, autoincrement=True, index=True)  # "序列号"
#     d_name        =    db.Column(db.String(20), unique=True, index=True)  # "名称"
#     inventory     =    db.Column(db.Integer)  # "库存"
#     formulation   =    db.Column(db.String(20), index=True)  # "剂型"
#     # variety     =    db.Column(db.String(20)) # "品种"（暂时使用分类来代替）
#     period        =    db.Column(db.Integer, index=True)  # "有效期：/月"
#     about         =    db.Column(db.Text)  # "关于"
#     # categories  =    db.relationship('Category', backref='drug')  # "与【分类】建立双向关系"
#     category_id   =    db.Column(db.Integer, db.ForeignKey('category.c_id'))


# class Category(db.Model):
#     __tablename__ =  'category'
#     c_id          =  db.Column(db.Integer, primary_key=True, autoincrement=True)
#     c_name        =  db.Column(db.String(20), unique=True)