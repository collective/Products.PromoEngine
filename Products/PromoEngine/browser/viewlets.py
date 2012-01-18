from zope.component import getMultiAdapter
from plone.app.layout.viewlets.common import ViewletBase
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

class AdBannerViewlet(ViewletBase):
    render = ViewPageTemplateFile('ad_banner.pt')

    def update(self):
        ad_fetcher = getMultiAdapter((self.context, self.request), name=u'ad_fetcher')
        self.ad_items = ad_fetcher.getAds(
                            ad_context=self.context,
                            slot='Banner',
                            ad_states=['published'],
                            object_ads=False,
                            randomize=True)
