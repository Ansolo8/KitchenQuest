from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pantry.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define a model for your ingredients
class Ingredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.String(100), nullable=False)
    expiration_date = db.Column(db.String(100), nullable=False)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dispensa')
def dispensa():
    ingredients = Ingredient.query.all()
    return render_template('dispensa.html', ingredients=ingredients)
# Route to add new ingredient
@app.route('/add', methods=['POST'])
def add_ingredient():
    name = request.form.get('name')
    quantity = request.form.get('quantity')
    expiration_date = request.form.get('expiration_date')

    # Create new Ingredient object
    ingredient = Ingredient(name=name, quantity=quantity, expiration_date=expiration_date)
    db.session.add(ingredient)
    db.session.commit()

    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables for our data models
    app.run(debug=True)
