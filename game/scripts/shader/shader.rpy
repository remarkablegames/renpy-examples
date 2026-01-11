##
# https://makevisualnovels.itch.io/make-visual-novels-rspv1
##
label shader:

    scene bg lecturehall
    show sylvie blue surprised
    e "No shader"

    ##
    # MVNTemplates
    ##
    show sylvie blue surprised at AnimatedAberate
    e "AnimatedAberate"

    show sylvie blue surprised at StillAberate
    e "StillAberate"

    show sylvie blue surprised at IntenseAberate
    e "IntenseAberate"

    show sylvie blue surprised at bits16
    e "bits16"

    show sylvie blue surprised at bits8
    e "bits8"

    show sylvie blue surprised at VHS
    e "VHS"

    show sylvie blue surprised at WhiteNoise
    e "WhiteNoise"

    show sylvie blue surprised at Static
    e "Static"

    show sylvie blue surprised at TransRights
    e "TransRights"

    show sylvie blue surprised at TheFuzz
    e "TheFuzz"

    hide sylvie blue surprised

    show bg lecturehall at LightDemo
    e "LightDemo"
    show bg lecturehall at reset

    show bg lecturehall at DramaticRevealBG
    e "DramaticRevealBG"
    show bg lecturehall at reset

    show bg lecturehall at DramaticReveal
    e "DramaticReveal"
    show bg lecturehall at reset

    show bg lecturehall at DramaticLayerReveal
    e "DramaticLayerReveal"
    show bg lecturehall at reset

    show bg lecturehall at RaveLights
    e "RaveLights"
    show bg lecturehall at reset

    show sylvie blue surprised

    show sylvie blue surprised at Bisexuality
    e "Bisexuality"

    show sylvie blue surprised at SunsetLighting
    e "SunsetLighting"

    show sylvie blue surprised at SimulatedLighting
    e "SimulatedLighting"

    show sylvie blue surprised at Regicide
    e "Regicide"

    show sylvie blue surprised at VirtualBoy
    e "VirtualBoy"

    show sylvie blue surprised at Manga
    e "Manga"

    show sylvie blue surprised at OldManga
    e "OldManga"

    show sylvie blue surprised at TakeOnMe
    e "TakeOnMe"

    hide sylvie blue surprised

    menu:
        "Show Sylvie?"

        "Yes":
            show sylvie blue surprised

        "No":
            pass

    ##
    # SimulatedLightingExpansion
    ##
    show bg lecturehall at NewSimLight
    e "NewSimLight"
    show bg lecturehall at reset

    camera at MouseKeyLight
    e "MouseKeyLight"
    camera

    camera at MouseRimLight
    e "MouseRimLight"
    camera

    camera at Spotlight(0.5, 0.5)
    e "Spotlight"
    camera

    camera at FlashLightMode
    e "FlashLightMode"
    camera

    show bg lecturehall at CoolWarmLighting
    e "CoolWarmLighting"
    show bg lecturehall at reset

    jump start
