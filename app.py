from flask import Flask, render_template
from auth.routes import auth_blueprint


app = Flask(__name__)
app.config['SECRET_KEY'] = 'MY_SECRET_KEY'

# Register Blueprints
app.register_blueprint(auth_blueprint, url_prefix='/auth')

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Privacy route
@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

if __name__ == '__main__':
    app.run(debug=True)