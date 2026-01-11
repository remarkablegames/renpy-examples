# https://www.renpy.org/doc/html/transforms.html

transform fadein:
    alpha 0.0
    easein 1.0 alpha 1.0

transform flip:
    xzoom -1.0

transform unflip:
    xzoom 1.0

transform resize(x, y):
    size (x, y)

transform scale(ratio):
    zoom ratio

transform tint(color):
    matrixcolor TintMatrix(color)

transform ypos(position):
    ypos position

transform bounce:
    yalign 1.0
    linear 3.0 xalign 1.0
    linear 3.0 xalign 0.0
    repeat

transform headright:
    linear 3 xalign 1.0

label transform_example:

    show eileen happy at bounce

    pause

    show eileen happy at headright

    pause

    show eileen happy at left, flip, fadein

    e "I'm on the left."

    show eileen vhappy at right, unflip, scale(1.5) with ease

    e "I'm on the right."

    jump start
