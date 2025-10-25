# https://www.renpy.org/doc/html/screens.html

label screens:

    show screen hello_world
    pause

    call screen dismiss_test

screen hello_world():
     tag example
     zorder 1
     modal False

     text "Hello, World." size 200

screen dismiss_test():

    dismiss action Return()

    frame:
        modal True

        align (.5, .3)
        padding (20, 20)

        has vbox

        text "This is a very important message.":
            xalign 0.5
            textalign 0.5

        # Dismiss can be confusing on its own, so we'll add a button as well.
        textbutton "Dismiss":
            xalign 0.5
            action Return()
