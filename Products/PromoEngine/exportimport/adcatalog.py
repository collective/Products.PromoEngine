from Products.CMFCore.utils import getToolByName
from Products.GenericSetup.ZCatalog.exportimport import ZCatalogXMLAdapter
from Products.GenericSetup.utils import exportObjects
from Products.GenericSetup.utils import importObjects

from Products.PromoEngine.interfaces import IAdCatalog

class AdCatalogXMLAdapter(ZCatalogXMLAdapter):
    """
    Mode im- and exporter for AdCatalog.
    """
    __used_for__ = IAdCatalog

    name = 'ad_catalog'

    def _exportNode(self):
        """
        Export the settings as a DOM node.
        """
        node = ZCatalogXMLAdapter._exportNode(self)

        self._logger.info('ad catalog settings exported.')
        return node

    def _importNode(self, node):
        """
        Import the settings from the DOM node.
        """
        ZCatalogXMLAdapter._importNode(self, node)

        self._logger.info('ad catalog settings imported.')

def importAdCatalog(context):
    """
    Import membrane_tool configuration.
    """
    site = context.getSite()
    tool = getToolByName(site, 'ad_catalog')

    importObjects(tool, '', context)

def exportAdCatalog(context):
    """
    Export membrane_tool configuration.
    """
    site = context.getSite()
    tool = getToolByName(site, 'ad_catalog', None)
    if tool is None:
        logger = context.getLogger("adcatalog")
        logger.info("Nothing to export.")
        return

    exportObjects(tool, '', context)
