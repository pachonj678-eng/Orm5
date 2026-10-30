from flask import Blueprint, jsonify
from flask_sqlalchemy import SQLAlchemy

# Configuración de la base de datos y Swagger
class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/db_products'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SWAGGER = {
        'title': 'API de Productos - SENA ADSO',
        'uiversion': 3
    }

# Instancia de SQLAlchemy
db = SQLAlchemy()

# Blueprint centralizado para manejo de errores
error_bp = Blueprint('error_bp', __name__)

@error_bp.app_errorhandler(404)
def not_found(error):
    return jsonify({"error": "Recurso no encontrado"}), 404

@error_bp.app_errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Error interno del servidor"}), 500