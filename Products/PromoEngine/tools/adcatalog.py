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
This is a Catalog to store all the ads so that they don't show up in
a search

TODO: there must be a better way to do this
"""
from Globals import InitializeClass
from zope.interface import implements

from Products.CMFPlone.CatalogTool import CatalogTool
from Products.PromoEngine.interfaces import IAdCatalog

class AdCatalog(CatalogTool):
    id = 'ad_catalog'
    portal_type = meta_type = 'Ad Catalog'
    
    implements(IAdCatalog)
    
    __implements__ = (CatalogTool.__implements__,)

InitializeClass(AdCatalog)