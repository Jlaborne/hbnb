from flask import Blueprint, request, jsonify
from model.city import City

cities_bp = Blueprint('cities_bp', __name__)

@cities_bp.route('/cities', methods=['POST'])
def create_city():
    data = request.json
    if 'name' not in data or 'country_code' not in data:
        return jsonify({"error": "Missing name or country_code"}), 400

    city = City(name=data['name'], country_code=data['country_code'])
    city.save()
    return jsonify({"id": city.id, "name": city.name, "country_code": city.country_code, "created_at": city.created_at, "updated_at": city.updated_at}), 201

@cities_bp.route('/cities', methods=['GET'])
def get_cities():
    cities = City.get_all()
    return jsonify([vars(city) for city in cities]), 200

@cities_bp.route('/cities/<string:city_id>', methods=['GET'])
def get_city(city_id):
    city = City.get(city_id)
    if city:
        return jsonify(vars(city)), 200
    else:
        return jsonify({"error": "City not found"}), 404

@cities_bp.route('/cities/<string:city_id>', methods=['PUT'])
def update_city(city_id):
    city = City.get(city_id)
    if not city:
        return jsonify({"error": "City not found"}), 404

    data = request.json
    city.update(**data)
    return jsonify(vars(city)), 200

@cities_bp.route('/cities/<string:city_id>', methods=['DELETE'])
def delete_city(city_id):
    city = City.get(city_id)
    if not city:
        return jsonify({"error": "City not found"}), 404

    city.delete()
    return '', 204
