from flask import Flask, render_template, url_for, flash
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'e736f275f88a4e881c23a1e0508c64db'

posts = [
    {
        'author': 'Ronnie Young',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'December 01, 2019'
    },
    {
        'author': 'Ronnie Young',
        'title': 'Blog Post 2',
        'content': 'First post content',
        'date_posted': 'December 08, 2019'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title="About")

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
    return render_template('register.html', title='Login', form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Register', form=form)

if __name__ == '__main__':
    app.run(debug=True)
