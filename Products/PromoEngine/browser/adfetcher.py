from random import choice

from zope.interface import implements
from ZTUtils import LazyFilter

from Products.CMFCore.utils import getToolByName
from Products.Five import BrowserView
from Products.PromoEngine.browser.interfaces import IAdFetcher


class AdFetcher(BrowserView):
    implements(IAdFetcher)

    def getAds(self,
               ad_context=None,
               slot=None,
               ad_states=[],
               object_ads=True,
               randomize=False,
               ad_types=['Ad', 'FlashAd']):
        """Get the ads with the given options
        """
        catalog_tool = getToolByName(self.context, 'ad_catalog')
        #prop_tool = getToolByName(context, 'portal_properties')
        ads = []
        unique_objects = []
        unique_slots = []

        # XXX: There has to be a better way to do something like this.
        #      CMFUID or plone.related hopefully...
        # get the ads based on the object's references
        # try and except in case the object doesn't support references
        try:
            raw_object_ads = ad_context.getBRefs('AdLocation')
            allowed_object_ads = LazyFilter(raw_object_ads, skip='View')
            # ads of a given type
            filtered_ads = [
                obj for obj in allowed_object_ads
                if obj.portal_type in ad_types]
            wf_tool = getToolByName(self.context, 'portal_workflow')
            # get ads of workflow states defined in the properties
            published_object_ads = [
                obj for obj in filtered_ads
                if wf_tool.getInfoFor(obj, 'review_state', None) in ad_states]
            unique_objects = [item.UID() for item in published_object_ads]
        except AttributeError:
            # Object does not support refs
            unique_objects = []

        # get the ads based the slot wanted
        if slot != '':
            query = {'portal_type': ad_types,
                     'getAdSlot': slot,
                     'review_state': ad_states}
            slot_ads = catalog_tool.searchResults(query)
            unique_slots = [item.UID for item in slot_ads]

        # slot and object defined
        if object_ads and slot != '':
            ads = [item for item in unique_objects if item in unique_slots]
        # only a slot defined (exclude ads with object defined)
        elif slot != '':
            ads = [item for item in unique_slots if item not in unique_objects]
        # only ads assigned to the object, no slot defined
        elif object_ads:
            ads = [item for item in unique_objects if item not in unique_slots]

        ad_objs = []
        # if there are ads then choose one and then get the object
        if ads:
            uidtool = getToolByName(self.context, 'uid_catalog')
            # TODO: could optionaly use some 80/20 type functionality here
            if randomize:
                ad_uid = choice(ads)
            else:
                ad_uid = ads[0]
            ad_brains = uidtool({'UID': ad_uid})
            ad_objs.append(ad_brains[0].getObject())
        return ad_objs
