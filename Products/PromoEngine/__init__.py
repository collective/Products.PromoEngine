#  Copyright (c) 2006 Six Feet Up, Inc.
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#

from Products.Archetypes.atapi import listTypes, process_types
from Products.Archetypes.public import registerClasses
from Products.CMFCore import utils as cmf_utils
from Products.PromoEngine.config import PROJECTNAME
from permissions import initialize as initialize_permissions

def initialize(context):
    # Importing the content types allows for their registration
    # with the Archetypes runtime
    import content
    import tools
    
    types = listTypes(PROJECTNAME)
    content_types, constructors, ftis = \
       process_types(types, PROJECTNAME)
    
    tools=[tools.admanager.AdManager, tools.adcatalog.AdCatalog]
    cmf_utils.ToolInit(PROJECTNAME+' Tools',
                tools = tools,
                icon='tool.gif'
                ).initialize(context)

    permissions = initialize_permissions()
    allTypes = zip(content_types, constructors)
    for atype, constructor in allTypes:
       kind = "%s: %s" % (PROJECTNAME, atype.archetype_name)
       cmf_utils.ContentInit(
           kind,
           content_types      = (atype,),
           permission         = permissions[atype.portal_type],
           extra_constructors = (constructor,),
           fti                = ftis,
           ).initialize(context)
    registerClasses(context, PROJECTNAME)
