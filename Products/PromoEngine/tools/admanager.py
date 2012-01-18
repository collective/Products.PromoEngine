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
"""
The Ad Manager that takes care of showing and storing ads
"""
from Products.CMFCore.utils import UniqueObject
from Products.Archetypes.atapi import Schema, registerType
from Products.Archetypes.atapi import LinesField, LinesWidget
from Products.ATContentTypes.content.folder import ATFolder
from Products.ATContentTypes.content.folder import ATFolderSchema

from Products.PromoEngine.config import PROJECTNAME

ATFolderSchemaCopy = ATFolderSchema.copy()
ATFolderSchemaCopy['id'].widget.visible = {'view' : 'hidden', 'edit' : 'hidden'}

AdManagerSchema = ATFolderSchemaCopy + Schema((
    LinesField(
        'slots',
        default=['Select a slot',
                 'Slot 1',
                 'Slot 2',
                 'Slot 3',
                 'Banner',
                 ],
        widget=LinesWidget(
            label='Slots for ads',
            description="""Set up the list of slots for the ads.  If you add
                slots then you will need to add a new portlet and modify the
                slot call.""",
            ),
    ),
))

class AdManager(ATFolder, UniqueObject):
    """Used to manage ads
    """
    schema = AdManagerSchema
    archetype_name = portal_type = meta_type = 'Ad Manager'
    
    def __init__(self, *args, **kwargs):
        ATFolder.__init__(self, 'ad_manager')
        
    # tool should not appear in portal_catalog (borrowed from AGX output)
    def at_post_edit_script(self):
        self.unindexObject()

registerType(AdManager, PROJECTNAME)
