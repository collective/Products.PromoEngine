from zope import schema
from zope.component import getMultiAdapter

from plone.app.portlets.portlets import base
from plone.memoize.instance import memoize
from plone.portlets.interfaces import IPortletDataProvider

from Acquisition import aq_inner
from Products.CMFPlone import PloneMessageFactory as _


class IAdPortlet(IPortletDataProvider):

    slot = schema.Choice(
        title=_(u"Ad Slot"),
        description=_(u"Select the slot name"),
        required=False,
        vocabulary="Products.PromoEngine.vocabularies.AdSlotsVocabulary"
        )
        
    object_ads = schema.Bool(
        title=_(u"Referenced Ads"),
        description=_(u"Set this to true if you want only the ads referenced "
                       "to the object you are on to show"),
        default=True,
        required=False)

    state = schema.Tuple(
        title=_(u"Workflow state"),
        description=_(u"Items in which workflow state to show."),
        default=('published', ),
        required=True,
        value_type=schema.Choice(
            vocabulary="plone.app.vocabularies.WorkflowStates")
        )
    
    randomize = schema.Bool(
        title=_(u"Randomize Ads"),
        description=_(u"Randomly pick an ad assigned to this portlet"),
        default=True,
        required=False)
        
class Renderer(base.Renderer):

    def __init__(self, *args):
        base.Renderer.__init__(self, *args)

        portal_state = getMultiAdapter((self.context, self.request), name=u'plone_portal_state')
        self.portal_url = portal_state.portal_url()
        self.portal = portal_state.portal()
        self.ad_fetcher = getMultiAdapter((self.context, self.request), name=u'ad_fetcher')

    @property
    def available(self):
        return len(self._data())
        
    def ad_items(self):
        return self._data()

    @memoize
    def _data(self):
        context = aq_inner(self.context)
        ad_objs = self.ad_fetcher.getAds(
                    ad_context=context,
                    slot=self.data.slot,
                    ad_states=self.data.state,
                    object_ads=self.data.object_ads,
                    randomize=self.data.randomize)
        return ad_objs
