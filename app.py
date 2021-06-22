from operator import pos
from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import time

app=Flask(__name__)
# configure database with my app
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///Posts.db'
db=SQLAlchemy(app)
# database model
class BlogPosts(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(100),nullable=False)
    author=db.Column(db.String(20),nullable=False,default='N/A')
    content=db.Column(db.Text,nullable=False)
    day=time.strftime('%d')
    month=time.strftime('%B')
    year=time.strftime('%Y')
    date_posted=db.Column(db.DateTime,nullable=False,default=datetime.utcnow)

    def __repr__(self):
        return f'Blog Post {self.id}'
# posts route
# posts data

all_posts=[
    {
        'title':'Post1',
        'content':'This the content1 accessing from main page of flask',
        'author':'ENG-CJ'
    },
    {
        'title':'Post2',
        'content':'this is the content2  flask web framwork'
    },
    {
        'title':'Post3',
        'content':'this is the content2  flask web framwork'
    }
]

@app.route('/posts',methods=['GET','POST'])
def posts():
    # requests
    if request.method=='POST':
        post_title=request.form['title']
        post_content=request.form['content']
        post_author=request.form['author']
        new_post=BlogPosts(title=post_title,content=post_content,author=post_author)
        db.session.add(new_post)
        db.session.commit()
        return redirect('/posts')
        
    else:
        all_posts=BlogPosts.query.order_by(BlogPosts.date_posted).all()
        return render_template('posts.html',posts=all_posts)


# dlete page
@app.route('/posts/PC/ENGCJ/All_Posts/delete/<int:id>')
def delete(id):
    post=BlogPosts.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    return redirect('/posts')


# edit page
@app.route('/posts/PC/ENGCJ/All_Posts/edit/<int:id>',methods=['GET','POST'])
def edit(id):
    post=BlogPosts.query.get_or_404(id)
    if request.method=='POST':
        post.title=request.form['title']
        post.author=request.form['author']
        post.content=request.form['content']
        db.session.commit()
        return redirect('/posts')
    else:
        return render_template('/edit.html',post=post)
# new post page
@app.route('/posts/new',methods=['GET','POST'])
def new_post():
    if request.method=='POST':
        post.title=request.form['title']
        post.author=request.form['author']
        post.content=request.form['content']
        new_post=BlogPosts(title=post_title,content=post_content,author=post_author)
        db.session.add(new_post)
        db.session.commit()
        return redirect('/posts')
    else:
        return render_template('new_post.html')
 

# home page route
@app.route('/')
def home_page():
    return render_template('index.html')


if __name__=='__main__':
    app.run(debug=True)