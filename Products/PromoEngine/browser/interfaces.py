from zope.interface import Interface

class IAdFetcher(Interface):
    """Ad fetcher interface
    """
    
    def getAds():
        """Get the available ads
        """
