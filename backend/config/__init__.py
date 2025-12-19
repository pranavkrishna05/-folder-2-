# __init__.py
import os

def configure_app(app, config_name):
    app.config.from_object(f'backend.config.settings.{config_name.capitalize()}Config')
