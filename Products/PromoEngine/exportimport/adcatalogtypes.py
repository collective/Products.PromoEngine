import logging 
logger = logging.getLogger('adcatalogtypes.py')
from Products.CMFCore.utils import getToolByName
from Products.Archetypes.public import listTypes
from Products.PromoEngine.config import PROJECTNAME, AD_CATALOG

def setupAdCatalogTypes(context):
    """Set up the types with the ad catalog
    """
    if context.readDataFile('PromoEngine-default.txt') is None:
        return
    
    site = context.getSite()
    
    attool = getToolByName(site, 'archetype_tool')
    typeslist = listTypes(PROJECTNAME)
    for portal_type in [ti['portal_type'] for ti in typeslist]:
        catalogs = [x.getId() for x in attool.getCatalogsByType(portal_type)]
        if AD_CATALOG not in catalogs:
            catalogs.append(AD_CATALOG)
            attool.setCatalogsByType(portal_type, catalogs)
