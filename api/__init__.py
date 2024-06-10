from flask import Flask
from api.views.countries import countries_bp
from api.views.cities import cities_bp

app = Flask(__name__)

app.register_blueprint(countries_bp)
app.register_blueprint(cities_bp)

if __name__ == '__main__':
    app.run(debug=True)
