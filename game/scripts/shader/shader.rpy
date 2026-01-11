# https://makevisualnovels.itch.io/make-visual-novels-rspv1
label shader:

    scene bg lecturehall
    show sylvie blue surprised

    # Spotlight transform
    camera at Spotlight(0.5, 0.5)
    e "Spotlight transform. Shine a spotlight using:\n{b}camera at Spotlight(X,Y)"
    camera at reset

    # Flashlight mode transform
    camera at FlashLightMode
    e "Flashlight mode transform. It follows your mouse:\n{b}camera at FlashLightMode"
    camera

    jump start
