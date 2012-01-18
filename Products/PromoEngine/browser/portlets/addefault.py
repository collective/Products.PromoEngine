from zope import schema
from zope.formlib import form
from zope.interface import implements

from plone.app.portlets.portlets import base

from Products.CMFPlone import PloneMessageFactory as _
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from Products.PromoEngine.browser.portlets.common import IAdPortlet
from Products.PromoEngine.browser.portlets.common import Renderer as BaseRenderer

class IAdDefaultPortlet(IAdPortlet):

    header_title = schema.TextLine(
        title=_(u"Portlet Title"),
        description=_(u"Enter the title that will appear in the header of the portlet"),
        required=False,
        )

class Assignment(base.Assignment):
    implements(IAdDefaultPortlet)

    def __init__(self,
                 header_title="",
                 slot="",
                 object_ads=True,
                 state=('published', ),
                 randomize=True):
        self.header_title = header_title
        self.slot = slot
        self.state = state
        self.object_ads = object_ads
        self.randomize = randomize
    
    @property
    def title(self):
        return _(u"Ad portlet (default styles)")

class Renderer(BaseRenderer):
    render = ViewPageTemplateFile('ad_default.pt')

class AddForm(base.AddForm):
    form_fields = form.Fields(IAdDefaultPortlet)
    label = _(u"Add Ad Portlet")
    description = _(u"This portlet shows ads.")

    def create(self, data):
        return Assignment(header_title=data.get('header_title', ''),
                          slot=data.get('slot', ''),
                          state=data.get('state', ('published',)),
                          randomize=data.get('randomize', True),
                          object_ads=data.get('object_ads', True)
                          )

class EditForm(base.EditForm):
    form_fields = form.Fields(IAdDefaultPortlet)
    label = _(u"Edit Ad Portlet")
    description = _(u"This portlet shows an ad in a default plone portlet.")
