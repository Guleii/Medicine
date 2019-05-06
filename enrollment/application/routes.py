from application import app, db
from flask import render_template, session, request, flash, redirect,url_for
from application.forms import LoginForm, RegisterForm
from application.models import User

# HOME页面
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', index=True)


# 登陆页面
@app.route('/login', methods=['GET','POST'])
def login():
    if session.get('username'):
        return redirect(url_for('index'))

    form = LoginForm()
    if form.validate_on_submit():
        username  =  form.username.data
        password  =  form.password.data

        user = User.objects(username=username).first()
        if user and user.get_password(password):
            flash(f"{user.real_name},登陆成功!", "success")
            session['user_id'] = user.user_id
            session['username'] = user.real_name
            session['department'] = user.department
            session['email'] = user.email
            session['real_name'] = user.real_name            
            session['is_login'] = True
            return redirect('/index')
        else:
            flash("用户名或密码输入错误!.", "danger")
    return render_template('login.html', title="登陆", form=form)


# 注销
@app.route('/logout')
def logout():
    session['user_id'] = False
    session.pop('username', None)
    session['is_login'] = False
    return redirect(url_for('index'))


# 注册
@app.route('/register', methods=['GET', 'POST'])
def register():
    if session.get('username'):
        return redirect(url_for('index'))

    form = RegisterForm(request.form)
    if form.validate_on_submit():      
        user_id = User.objects.count()
        user_id += 1

        username   = form.username.data
        password   = form.password.data
        email      = form.email.data
        real_name  = form.real_name.data
        department = form.department.data

        form.validate_username(form.username.data)
        user = User(user_id=user_id,username=username, password=password, email=email, real_name=real_name, department=department)
        user.set_password(form.password.data)
        user.save()
        flash(f"注册成功!", "success")
        session['is_regisered'] = True
        return redirect(url_for('login'))
        


    return render_template('register.html',  form=form, register=True, title="用户注册")


# 查询
@app.route('/search')
def search():
    # TODO
    return render_template('search.html', search=True)


# 个人信息
@app.route('/userinfo')
def userinfo():
    # User(user_id=1,username='admin',real_name='张三',department='研发中心',email="424307293@qq.com",password='123456').save()
    # User(user_id=2,username='test',real_name='李四',department='研发中心',email="2856594354@qq.com",password='123456').save()
    # users=User.objects.all()
    return render_template('userinfo.html', userinfo=True)
