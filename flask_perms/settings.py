defaultPermissions = {'view_missing_permissions':
                          'Allows user to view what permissions they are missing when denied access.',

                      'view_permission_errors':
                          'Grants user notifications when permission handling errors occur.'
                      }

ROOT_ROLE = 'Head Admin'
IGNORE_EMPTY = False

# PERMISSION_FILE

# ROLE_FILE
STORE_TYPE = 'DB'

USE_DB = True

USER_MODEL_NAME = 'User'
ROLE_MODEL_NAME = 'Role'
PERMISSION_MODEL_NAME = 'Permission'

USER_PRIMARY_KEY = 'id'
ROLE_PRIMARY_KEY = 'id'
PERMISSION_PRIMARY_KEY = 'id'

ROLE_LINK_NAME = 'role_links'
USER_ROLE_LINK_NAME = 'user_role_links'
USER_PERMISSION_LINK_NAME = 'user_permission_links'
ROLE_PERMISSION_LINK_NAME = 'role_permission_links'

USE_SCHEMAS = False

USER_SCHEMA = ""