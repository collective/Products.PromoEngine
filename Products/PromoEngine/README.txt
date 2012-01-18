About

    PromoEngine is a product designed to give you the ability to create ads for
    your site.  There are two types of ads, kupu based and flash based.  The ads
    show up using the right and left column portlets or by calling the macros
    from a template (if you want banner ads you'll have to edit your 
    main_template and add the macros you want to use).
    
Installation

    This product is installed through GenericSetup.  Go into your plone site
    and go to the 'portal_setup' tool.  Click on the 'properties' tab and select
    the PromoEngine profile.  Then click on the 'import' tab and then click on
    'run all steps' at the bottom of the page.  Now all the PromoEngine tools
    and content types have been installed and are ready for use.

Usage
    
    If you want to use the Ad type with Kupu and add images or links, then you
    will have to turn on uid generation in the Kupu settings.  Otherwise your
    links will be relative and not show up correctly.
    
    Next you will need to add one of the portlets to your right or left slots
    definition (via the properties tab).  You can also call the macros via any
    template.  There are portlet files per 'ad type' the macros are as follows:
    
    portlet_ad_macros
      * content        'Ad' referenced to the object you are on
      * content_slot1  'Ad' referenced to the object and 'Slot 1' selected
      * content_slot2  'Ad' referenced to the object and 'Slot 2' selected
      * content_slot3  'Ad' referenced to the object and 'Slot 3' selected
      * slot1          'Slot 1' selected and no reference selected
      * slot2          'Slot 2' selected and no reference selected
      * slot3          'Slot 3' selected and no reference selected
      
    portlet_flash_ad_macros
      * content        'Flash Ad' referenced to the object you are on
      * content_slot1  'Flash Ad' referenced to the object and 'Slot 1' selected
      * content_slot2  'Flash Ad' referenced to the object and 'Slot 2' selected
      * content_slot3  'Flash Ad' referenced to the object and 'Slot 3' selected
      * slot1          'Slot 1' selected and no reference selected
      * slot2          'Slot 2' selected and no reference selected
      * slot3          'Slot 3' selected and no reference selected
      
    To call the macro or add it to the 'right_slots' or 'left_slots' you can use
    the following:
    
      context/portlet_ad_macros/macros/content
      
    If you need to define more ad slots you can add more macros.  Then add the
    slot names to the Ad Manager via it's edit screen.
    
    There is a promo_engine_properties in portal_properties that allows you to
    configure the Ad states that will show when you call getAd().  The default
    is set to just 'published'.  If you want Ads in the 'visible' state to show
    up you can add the state to the property ad_states.
    
    Now that you have set up your portlets you can start adding some ads. You
    can access the Ad Manger through the 'site setup'.  This will take you into
    the ad repository.

Dependencies
    
    Plone 2.5.3+

Bug reporting

    Please report any bugs you find and/or feature requests to
    clayton AT sixfeetup DOT com
    
Author

    Clayton Parker (clayton AT sixfeetup DOT com) for Six Feet Up, Inc.
    
    "http://www.sixfeetup.com":http://www.sixfeetup.com
    
    claytron on #plone IRC channel on Freenode (irc.freenode.net)
