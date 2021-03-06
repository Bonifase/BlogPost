import secrets
import os
from PIL import Image
from flask import render_template, flash, redirect, url_for, request, abort
from flask_login import login_user, current_user, logout_user, login_required
from blogpost import app, db, bcrypt
from blogpost.forms.forms import RegistrationForm, LoginForm, UpdateAccountForm, PostForm  # noqa
from blogpost.models.models import User, Post


@app.route("/")
@app.route("/home")
def home():
    posts = Post.query.all()
    return render_template('home.html', posts=posts)


@app.route("/latest_posts", methods=['GET'])
def latest_posts():
    posts = Post.query.order_by(Post.date_posted.desc()).limit(3).all()
    if posts:
        return render_template('latest_posts.html', posts=posts)
    else:
        flash(f'No latest posts', 'info')
        return redirect(url_for('home'))


@app.route("/active_users", methods=['GET'])
def active_users():
    users = User.query.all()
    users = [user for user in users if len(user.posts) >= 2]
    if users:
        return render_template('active_users.html', users=users)
    else:
        flash(
            f'There are no active users',
            'info')
        return redirect(url_for('home'))


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(
            form.password.data).decode('utf')
        user = User(
            username=form.username.data, email=form.email.data,
            password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(
            f'{form.username.data} accout has been created! You can login',
            'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/user/<username>", methods=['GET'])
def user(username):
    user = User.query.filter_by(username=username).first()
    print("This is user", user.image_file)
    return render_template('user.html', user=user)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):  # noqa
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            flash(
                f'You logged in successfully for {user.username}!',
                'success')
            return redirect(next_page) if next_page else redirect(url_for('home'))  # noqa
        flash(
            f'Invalid login credentials',
            'danger')

    return render_template('login.html', title='Login', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)  # noqa
    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    return picture_fn


@app.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for(
        'static', filename='profile_pics/' + current_user.image_file)
    return render_template(
        'account.html', title='Account', image_file=image_file, form=form)


@app.route("/post/new", methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(
            title=form.title.data, content=form.content.data,
            author=current_user)
        db.session.add(post)
        db.session.commit()
        flash(
            f'Your post has been created!',
            'success')
        return redirect(url_for('home'))
    return render_template(
        'new_post.html', title='New Post', form=form, legend='New Post')


@app.route("/post/<int:post_id>", methods=['GET', 'POST'])
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post)


@app.route('/like/<int:post_id>/<action>')
@login_required
def like_action(post_id, action):
    post = Post.query.filter_by(id=post_id).first_or_404()
    print("this is very funny", current_user)
    if action == 'like':
        current_user.like_post(post)
        db.session.commit()
    if action == 'unlike':
        current_user.unlike_post(post)
        db.session.commit()
    return redirect(request.referrer)


@app.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash(
            f'Your post has been updated!',
            'success')
        return redirect(url_for('post', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    return render_template(
        'new_post.html', title='Update Post',
        form=form, legend='Update Post')


@app.route("/post/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash(
        f'Your post has been deleted!',
        'success')
    return redirect(url_for('home'))
