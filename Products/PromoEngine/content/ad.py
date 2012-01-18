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
from Products.CMFCore.utils import getToolByName
from Products.Archetypes.atapi import registerType
from Products.ATContentTypes.content.document import ATDocument, \
    ATDocumentSchema
from Products.PromoEngine.content.basead import BaseAd, BaseAdSchema
from Products.PromoEngine.config import PROJECTNAME

AdSchema = BaseAdSchema.copy() + ATDocumentSchema.copy()

class Ad(ATDocument, BaseAd):
    """Create an ad
    """
    schema = AdSchema
           
registerType(Ad, PROJECTNAME)
