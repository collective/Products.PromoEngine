from zope import schema
from zope.formlib import form
from zope.interface import implements

from plone.app.portlets.portlets import base

from Products.CMFPlone import PloneMessageFactory as _
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from Products.PromoEngine.browser.portlets.common import IAdPortlet
from Products.PromoEngine.browser.portlets.common import Renderer as BaseRenderer

class IAdBlankPortlet(IAdPortlet):

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

class Assignment(base.Assignment):
    implements(IAdBlankPortlet)

    def __init__(self,
                 slot="",
                 object_ads=True,
                 state=('published', ),
                 randomize=True):
        self.slot = slot
        self.state = state
        self.object_ads = object_ads
        self.randomize = randomize

    @property
    def title(self):
        return _(u"Ad (No styles)")

class Renderer(BaseRenderer):
    render = ViewPageTemplateFile('ad_blank.pt')

class AddForm(base.AddForm):
    form_fields = form.Fields(IAdBlankPortlet)
    label = _(u"Add Ad Portlet")
    description = _(u"This portlet shows ads.")

    def create(self, data):
        return Assignment(slot=data.get('slot', ''),
                          state=data.get('state', ('published',)),
                          randomize=data.get('randomize', True),
                          object_ads=data.get('object_ads', True)
                          )

class EditForm(base.EditForm):
    form_fields = form.Fields(IAdBlankPortlet)
    label = _(u"Edit Ad Portlet")
    description = _(u"This portlet shows ads.")
