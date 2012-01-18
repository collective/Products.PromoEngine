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
A simple ad for use with the Ad Manager
"""
from AccessControl import ClassSecurityInfo
from Products.CMFCore.utils import getToolByName
try:
    from Products.CMFCore import CMFCorePermissions as permissions
except ImportError:
    from Products.CMFCore import permissions
from Products.CMFCore.utils import getToolByName

from Products.Archetypes.atapi import Schema, registerType
from Products.Archetypes.atapi import IntegerField, StringField
from Products.Archetypes.atapi import StringWidget, SelectionWidget, IntegerWidget
from Products.ATContentTypes.content.file import ATFile, ATFileSchema
from Products.PromoEngine.content.basead import BaseAd, BaseAdSchema
from Products.PromoEngine.config import PROJECTNAME, SCALE_LIST

from Products.PromoEngine.swfHeaderData import analyseContent

FlashAdSchema = BaseAdSchema.copy() + ATFileSchema.copy()

schema = FlashAdSchema + Schema((
    IntegerField(
        'scale',
         required = True,
         default = 100,
         validators = ('isInt'),
         vocabulary = SCALE_LIST,
         widget=SelectionWidget(
            label = 'Scale',
            description = 'Scale of the flash movie.',
        ),
    ),

    StringField(
        'bgcolor',
        required = True,
        default = '#FFFFFF',
        widget=StringWidget(
            label = 'Background Color',
            description = 'Enter the background color of the flash movie.',
        ),
    ),

    IntegerField(
        'width',
        validators = ('isInt'),
        widget=IntegerWidget(
            label ='Width',
            modes= ('view',),
            description = 'Width of flash movie.',
        ),
    ),
    
    IntegerField(
        'height',
        validators = ('isInt'),
        widget=IntegerWidget(
            label ='Height',
            modes= ('view',),
            description = 'Height of flash movie.',
        ),
    ),

    StringField(
        'flashversion',
        widget=StringWidget(
            modes= ('view',),
            label ='Flash Version',
        ),
    ),
))

class FlashAd(ATFile, BaseAd):
    """Create a flash based ad
    """
    schema = schema
    assocFileExt   = ('swf',)
    
    security = ClassSecurityInfo()

    security.declareProtected(permissions.ModifyPortalContent, 'setFile')
    def setFile(self, value, **kwargs):
        """Saves file and stores flash informations (size, flash version)"""
        ATFile.setFile(self, value, **kwargs)

        if value:
            value.seek(0) # rewind
            tags = analyseContent(value.read(1024))
            self.setWidth(tags['width'])
            self.setHeight(tags['height'])
            self.setFlashversion(tags['flashversion'])

    def getDisplayHeight(self):
        """Returns height in pixels for selected scale"""
        if self.height:
            return int(self.height * (self.getScale() / 100.0))
        else:
            return None
    
    def getDisplayWidth(self):
        """Returns width in pixels for selected scale"""
        if self.width:
            return int(self.width * (self.getScale() / 100.0))
        else:
            return None

    security.declarePublic('getIcon')
    def getIcon(self, relative_to_portal=0):
        """Returns icon for flash movies"""
        icon = self.content_icon

        if relative_to_portal:
            return icon
        else:
            utool = getToolByName( self, 'portal_url' )
            # Relative to REQUEST['BASEPATH1']
            res = utool(relative=1) + '/' + icon
            while res[:1] == '/':
                res = res[1:]
            return res
           
registerType(FlashAd, PROJECTNAME)
