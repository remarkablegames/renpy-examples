# https://www.renpy.org/doc/html/transforms.html#animation-statement

image eileen happy moving:
    animation
    "eileen happy"
    xalign 1.0
    linear 5.0 xalign -1.0
    repeat

image eileen vhappy moving:
    animation
    "eileen vhappy"
    xalign 0.0
    linear 5.0 xalign 1.0
    repeat

label animation:
    show eileen happy moving
    pause

    show eileen vhappy moving
    pause

    jump start
