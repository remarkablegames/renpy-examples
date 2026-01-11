# https://www.renpy.org/doc/html/screen_actions.html#tooltips
label tooltip:

    call screen tooltip1
    call screen tooltip2

    jump start

screen tooltip1():
    vbox:
        textbutton "{color=#fff}North":
            # action NullAction()
            action Return("n")
            tooltip "To meet a polar bear."

        textbutton "{color=#fff}South":
            action Return("s")
            tooltip "All the way to the tropics."

        textbutton "{color=#fff}East":
            action Return("e")
            tooltip "So we can embrace the dawn."

        textbutton "{color=#fff}West":
            action Return("w")
            tooltip "Where to go to see the best sunsets."

        $ tooltip = GetTooltip()

        if tooltip:
            text "[tooltip]"

screen tooltip2():
    frame:
        padding (20, 20)
        align (.5, .3)
        has vbox

        textbutton "North":
            action Return("n")
            tooltip "To meet a polar bear."

        textbutton "South":
            action Return("s")
            tooltip "All the way to the tropics."

        textbutton "East":
            action Return("e")
            tooltip "So we can embrace the dawn."

        textbutton "West":
            action Return("w")
            tooltip "Where to go to see the best sunsets."

    # This has to be the last thing shown in the screen.
    $ tooltip = GetTooltip()

    if tooltip:
        nearrect:
            focus "tooltip"
            prefer_top True

            frame:
                xalign 0.5
                text tooltip
