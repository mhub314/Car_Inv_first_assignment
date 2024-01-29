from flask import Blueprint, render_template

site = Blueprint('site', __name__, template_folder='site_templates')

@site.route('/')
def home():
    return render_template('index.html')

@site.route('/profile')
def profile():
    return render_template('profile.html')

@site.route('/new_used_inventory')
def new_used_inventory():
    return render_template('new_used_inventory.html')

@site.route('/about_us')
def about_us():
    return render_template('about_us.html')