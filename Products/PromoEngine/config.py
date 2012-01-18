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
from Products.Archetypes.atapi import DisplayList

PROJECTNAME = "PromoEngine"
SKINS_DIR = 'skins'

GLOBALS = globals()

SCALE_LIST = DisplayList((
    ('200', '200%'),
    ('150', '150%'),
    ('100', '100%'),
    ('75', '75%'),
    ('50', '50%'),
    ('25', '25%'),
 ))

AD_CATALOG = 'ad_catalog'

STYLESHEETS = [{'id' : 'promoEngine.css'},]
