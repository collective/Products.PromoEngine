from Products.Archetypes import public as atapi
from Products.CMFCore import permissions as cmfcore_permissions

import config
# Add a new member
ADD_PERMISSION = ADD_MEMBER_PERMISSION = cmfcore_permissions.AddPortalMember

# This file is used to set up permissions for your product.

ADD_PERMISSIONS = {}
def initialize():
    permissions = {}
    types = atapi.listTypes(config.PROJECTNAME)
    for atype in types:
        portal_type = atype['portal_type']
        permission = ADD_PERMISSIONS.get(portal_type, None)
        if permission is None:
            # construct a permission on the fly
            permission = "%s: Add %s" % (config.PROJECTNAME,
                                         portal_type)
            cmfcore_permissions.setDefaultRoles(permission, ('Manager',))
        permissions[portal_type] = permission
    return permissions
