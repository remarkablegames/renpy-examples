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
            (20, "back"),
            (-20, "front1"),
            (-20, "front2"),
            (-40, "front3"),
            (-60, "front4"),
            (-80, "front5"),
            (-100, "front6"),
            (-120, "front7"),
            (-140, "front8"),
        ])

    scene bg sky onlayer farback at Position(ypos = 1080)
    show 1 forest onlayer back at Position(ypos = 1200)
    show 2 forest onlayer front1 at Position(ypos = 1140)
    show 3 forest onlayer front2  at Position(ypos = 1120)
    show 4 forest onlayer front3 at Position(ypos = 1080)
    show 5 particles onlayer front4 at Position(ypos = 1200)
    show 6 forest onlayer front5 at Position(ypos = 1140)
    show 7 particles onlayer front6 at Position(ypos = 1120)
    show 8 bushes onlayer front7 at Position(ypos = 1080)
    show 9 mist onlayer front8 at Position(ypos = 1200)

    pause

    return
