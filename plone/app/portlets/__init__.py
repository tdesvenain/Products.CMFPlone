
def initialize(context):
    """Register a GenericSetup profile when loaded as a Zope 2 product.
    """

    from Products.CMFPlone.interfaces import IPloneSiteRoot
    from Products.GenericSetup import profile_registry

    profile_registry.registerProfile('default',
                                     'plone.app.portlets',
                                     'Portlets and UI for Plone',
                                     'profiles/default',
                                     'plone.app.portlets',
                                     GenericSetup.EXTENSION,
                                     for_=IPloneSiteRoot)
