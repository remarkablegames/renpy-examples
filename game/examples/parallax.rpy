# https://www.reddit.com/r/RenPy/comments/1br72fr/ingame_parallax_like_in_slay_the_princess/

init python:
    class MouseParallax(renpy.Displayable):
        def __init__(self, layer_info):
            super(renpy.Displayable, self).__init__()
            self.xoffset,self.yoffset = 0.0, 0.0
            self.sort_layer = sorted(layer_info, reverse=True)
            cflayer = []
            masteryet = False
            for m, n in self.sort_layer:
                if (not masteryet) and (m < 41):
                    cflayer.append("master")
                    masteryet = True
                cflayer.append(n)
            if not masteryet:
                cflayer.append("master")
            cflayer.extend(["transient", "screens", "overlay"])
            config.layers = cflayer
            config.overlay_functions.append(self.overlay)

        def render(self, width, height, st, at):
            return renpy.Render(width, height)

        def parallax(self, m):
            func = renpy.curry(trans)(disp=self, m=m)
            return Transform(function=func)

        def overlay(self):
            ui.add(self)
            for m, n in self.sort_layer:
                renpy.layer_at_list([self.parallax(m)], n)

        def event(self, ev, x, y, st):
            import pygame
            if persistent.parallax_on:
                if ev.type == pygame.MOUSEMOTION:
                    self.xoffset, self.yoffset = ((float)(x) / (config.screen_width)) - 0.5, ((float)(y) / (config.screen_height)) - 0.5

    def trans(d, st, at, disp=None, m=None):
        d.xoffset, d.yoffset = int(round(m * disp.xoffset)), int(round(m * disp.yoffset))
        return 0

label parallax:

    scene black

    init python:
        MouseParallax([
            (40, "farback"),
            (20, "01"),
            (0, "02"),
            (-20, "03"),
            (-40, "04"),
            (-60, "05"),
            (-80, "06"),
            (-100, "07"),
            (-120, "08"),
            (-140, "09"),
        ])

    scene bg sky onlayer farback at Position(ypos = 1080)
    show 01 forest onlayer 01 at Position(ypos = 1200)
    show 02 forest onlayer 02 at Position(ypos = 1140)
    show 03 forest onlayer 03 at Position(ypos = 1120)
    show 04 forest onlayer 04 at Position(ypos = 1080)
    show 05 particles onlayer 05 at Position(ypos = 1200)
    show 06 forest onlayer 06 at Position(ypos = 1140)
    show 07 particles onlayer 07 at Position(ypos = 1120)
    show 08 bushes onlayer 08 at Position(ypos = 1080)
    show 09 mist onlayer 09 at Position(ypos = 1200)

    pause

    return
