from flask import Flask,render_template,request,redirect,session,flash,url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import generate_password_hash , check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SECRET_KEY'] = "kulblog"

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    bio = db.Column(db.Text, nullable=True)
    url = db.Column(db.Text, nullable=True)
    git = db.Column(db.Text, nullable=True)

class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    createdat = db.Column(db.DateTime, default=datetime.utcnow)
    author = db.Column(db.String(100), nullable=False)

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    blogs = Blog.query.all()
    return render_template('index.html',blogs = blogs)


@app.route('/register', methods = ["GET","POST"])
def register():
    if request.method == "POST":
        name = request.form.get('name')
        username = request.form.get('username')
        password = request.form.get('password')
        bio = request.form.get('bio')
        url = request.form.get('url')
        git = request.form.get('git')
        new_password = generate_password_hash(password = password)
        user = User.query.filter_by(username = username).first()
        if not user:
            new_user = User(name = name ,username = username , password = new_password,bio = bio, url= url , git = git)
            db.session.add(new_user)
            db.session.commit()
            return redirect('/login')
    return render_template('register.html')

@app.route('/login', methods = ["GET","POST"])
def login():
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username = username).first()
        if user and check_password_hash(user.password , password) :
            session['user'] = username
            flash('Login Successful !' , 'success')
            return redirect('/')
        flash('Failed to login ! Try Again with your Credentials!' , 'danger')
    return render_template('/login.html')

@app.route('/logout')
def logout():
    session.pop('user')
    flash('Logged Out Successfully !' , 'info')
    return redirect('/')

@app.route('/create-blog',methods = ["GET","POST"])
def create_blog():
    if request.method == "POST":
        title = request.form.get('title')
        description = request.form.get('description')
        new_blog = Blog(title = title , description = description , author = session['user'])
        db.session.add(new_blog)
        db.session.commit()
        flash('Blog Created' , 'success')
    return render_template('create-blog.html')

@app.route('/blog-details/<int:blog_id>')
def blogdetails(blog_id):
    blog = Blog.query.get_or_404(blog_id)
    return render_template('details.html', blog=blog)

@app.route('/accounts')
def account():
    user = User.query.filter_by(username=session['user']).first_or_404()
    blogs = Blog.query.filter_by(author=user.username).all()
    return render_template(
        'account.html',
        user=user,
        blogs=blogs
    )



@app.route('/delete-blog/<int:blog_id>' , methods = ['POST','GET'])
def deleteblog(blog_id):
    blog = Blog.query.get_or_404(blog_id)
    db.session.delete(blog)
    db.session.commit()

    flash("Blog Deleted Successfully !" , "success")
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)