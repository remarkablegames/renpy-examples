# https://makevisualnovels.itch.io/make-visual-novels-rspv1
label shader:

    scene bg lecturehall
    show sylvie blue surprised
    e "No shader"

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

    camera at CoolWarmLighting
    e "CoolWarmLighting"
    camera

    jump start
