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
Base ad to create Ad types with
"""
from Globals import InitializeClass
from Products.CMFCore.utils import getToolByName
from Products.Archetypes.atapi import DisplayList
from Products.Archetypes.atapi import BaseSchema, Schema, BaseContent
from Products.Archetypes.atapi import ReferenceField, StringField
from Products.Archetypes.atapi import StringWidget, SelectionWidget
from Products.ATReferenceBrowserWidget.ATReferenceBrowserWidget \
    import ReferenceBrowserWidget
from Products.PromoEngine.config import PROJECTNAME

BaseAdSchema = BaseSchema.copy() + Schema((
    ReferenceField(
        'adLocation',
        multiValued = True,
        relationship = 'AdLocation',
        widget = ReferenceBrowserWidget(
            label = 'Ad Location Step 1',
            description = """Select where the ad should show up""",
            startup_directory = '/',
        ),
    ),
    StringField(
        'adSlot',
        vocabulary = '_slotVocab',
        index = 'ad_catalog/FieldIndex',
        widget = SelectionWidget(
            label = 'Ad Location Step 2',
            description = """Select an optional slot to use""",
            format = 'select',
            ),
    ),
))

class BaseAd(BaseContent):
    """Base ad class to create different types of ads
    """
    schema = BaseAdSchema
        
    def _slotVocab(self):
        ad_tool = getToolByName(self, 'ad_manager')
        raw_ad_slots = ad_tool.getSlots()
        ad_slots = [(slot, slot) for slot in raw_ad_slots]
        return DisplayList(ad_slots)

InitializeClass(BaseAd)
