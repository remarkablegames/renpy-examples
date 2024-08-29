# https://zeillearnings.itch.io/map-navigation
label map:

    call screen map

    pause

# https://www.renpy.org/doc/html/screens.html
screen map():
    add "map/bg map.jpg"

    # https://www.renpy.org/doc/html/screens.html#imagebutton
    imagebutton:
        xpos 618
        ypos 570
        idle "map/house1_idle.png"
        hover "map/house1_hover.png"
        # https://www.renpy.org/doc/html/screen_actions.html
        action Jump("start")

    imagebutton:
        xpos 596
        ypos 165
        auto "map/house2_%s.png"
        action Jump("start")
