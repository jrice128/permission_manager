from . import filters
from flask import Blueprint
from .settings import ROOT_ROLE, IGNORE_EMPTY, STORE_TYPE, USER_SCHEMA

class Flask_Perms(object):
    def __init__(self, app=None, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

        if app:
            self.init_app(app)

    def init_app(self, app):

        app.config.setdefault('STORE_TYPE', STORE_TYPE)

        app.config.setdefault('USER_MODEL_NAME', 'User')
        app.config.setdefault('ROLE_MODEL_NAME', 'Role')
        app.config.setdefault('PERMISSION_MODEL_NAME', 'Permission')

        app.config.setdefault('USER_TABLE_NAME', 'users')
        app.config.setdefault('ROLE_TABLE_NAME', 'roles')
        app.config.setdefault('PERMISSION_TABLE_NAME', 'permissions')

        app.config.setdefault('USER_PRIMARY_KEY', 'id')
        app.config.setdefault('ROLE_PRIMARY_KEY', 'id')
        app.config.setdefault('PERMISSION_PRIMARY_KEY', 'id')

        app.config.setdefault('USER_SCHEMA', USER_SCHEMA)
        app.config.setdefault('ROOT_ROLE', ROOT_ROLE)
        app.config.setdefault('IGNORE_EMPTY', IGNORE_EMPTY)



        app.add_template_filter(filters.perm_check)
        app.add_template_filter(filters.is_subset)
        blueprint = Blueprint('permission', __name__, template_folder='templates')
        app.register_blueprint(blueprint)






