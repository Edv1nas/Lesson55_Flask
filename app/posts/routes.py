from flask import render_template,  request, url_for, redirect
from app.posts import bp
from app.extensions import db
from app.models.post import Post
from app.posts.form import PostForm
# pylint: disable=all


# @bp.route('/')
# def index():
#     posts = Post.query.all()
#     return render_template('posts/index.html', posts=posts)


@bp.route('/categories/')
def categories():
    return render_template('posts/categories.html')


@bp.route('/', methods=('GET', 'POST'))
def index():
    forma = PostForm()
    posts = Post.query.all()
    if request.method == 'POST' and forma.validate_on_submit() is True:
        new_post = Post(
            title="Post #" + forma.title.data,
            content="Content #" + forma.content.data,
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('posts.index'))

    return render_template('posts/index.html', posts=posts, form=forma)
