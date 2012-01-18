from zope.app.schema.vocabulary import IVocabularyFactory
from zope.interface import implements
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary
from Products.CMFCore.utils import getToolByName

class AdSlotsVocabulary(object):
    """Vocabulary factory for workflow states.
    """
    implements(IVocabularyFactory)

    def __call__(self, context):
        context = getattr(context, 'context', context)
        ad_man = getToolByName(context, 'ad_manager')
        items = ad_man.getSlots()
        terms = [SimpleTerm(i, i) for i in items]
        return SimpleVocabulary(terms)

AdSlotsVocabularyFactory = AdSlotsVocabulary()
