from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo, Email, ValidationError
from application.models import User

class LoginForm(FlaskForm):
    username = StringField("用户名", validators=[DataRequired()])
    password = StringField("密码", validators=[DataRequired()])
    remember_me = BooleanField("记住我")
    submit = SubmitField("登陆")

    
class RegisterForm(FlaskForm):
    username = StringField("用户名", validators=[DataRequired()])
    password = PasswordField("密码", validators=[DataRequired(),Length(min=5,max=15,message="密码长度应介于5-15!")])
    confirm_password = PasswordField("确认密码", validators=[DataRequired(), Length(min=5,max=15,message="密码长度应介于5-15!"), EqualTo("password",message="两次输入密码不一致！")])
    email = StringField("邮箱", validators=[DataRequired(),Email()])
    real_name = StringField("真实姓名", validators=[DataRequired(), Length(max=30,message="密码长度不超过30位!")])
    department = StringField("部门", validators=[DataRequired(), Length(max=20,message="部门名称不超过20位!")])
    submit = SubmitField("注册")

    def validate_username(self, username):
        user = User.objects(username=self.username.data).first()
        if user:
            raise ValidationError("用户名已被使用，请重新输入!")
