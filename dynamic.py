from flask import  Flask,redirect,url_for,render_template_string


x = Flask(__name__)

@x.route('/')
def index():
    return "Index Page"

@x.route('/user/<user_name>')
def profile(user_name):
    return f"My name is {user_name}"

@x.route('/post/<int:post_id>')
def show_post(post_id):
    return f"My post_id is {post_id}"

@x.route('/admin')
def admin():
    return "Admin page"

@x.route('/redirect_to_admin')
def redirect_to_admin():
    return redirect(url_for('admin'))

@x.route('/links')
def links():
    home_url = url_for('index')
    profile_url = url_for('profile', user_name='JohnDoe')
    post_url = url_for('show_post', post_id=42)
    admin_url = url_for('admin')

    return render_template_string('''
    <ul>
        <li><a href="{{ home_url }}">Home</a></li>
        <li><a href="{{ profile_url }}">John Doe's Profile</a></li>
        <li><a href="{{ post_url }}">Post 42</a></li>
        <li><a href="{{ admin_url }}">Admin</a></li>
    </ul>
    ''', home_url=home_url, profile_url=profile_url, post_url=post_url, admin_url=admin_url)