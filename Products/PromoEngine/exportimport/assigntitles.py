"""Do some cleanup that GenericSetup can't do yet (as far as I know)"""

def assignTitles(context):
    """Assigning the titles to the tools"""
    if context.readDataFile('PromoEngine-default.txt') is None:
        return
    
    site = context.getSite()
    if site.ad_manager.Title() == '':
        site.ad_manager.setTitle('Ad Manager')
        # reindex the object so that it gets hidden
        site.ad_manager.processForm({})
        # hide the id from the nav
        banned_ids = list(site.portal_properties.navtree_properties.idsNotToList)
        if 'ad_manager' not in banned_ids:
            banned_ids.append('ad_manager')
            site.portal_properties.navtree_properties.manage_changeProperties({'idsNotToList': banned_ids})
    if site.ad_catalog.title == '':
        site.ad_catalog.title = 'Ad Catalog'
