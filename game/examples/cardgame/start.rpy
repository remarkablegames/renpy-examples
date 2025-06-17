# https://www.renpy.org/wiki/renpy/Cardgame

image dim = "#0008"

label cardgame:

    scene bg table

    python:
        k = Klondike(1)
        k.set_sensitive(False)
        k.show()

    show dim
    with dissolve

    "Welcome to the cardgame demo. Let's play some solitaire!"

    "I might show up from time to time to give you some advice, but it's up to you if you want to take it."

    "Good luck!"

    window hide

label continue:

    hide dim
    with dissolve

label quick_continue:

    $ hint_count = renpy.random.randint(10, 20)

    while True:

        python:

            ui.textbutton("Give Up", ui.jumps("giveup"), xalign=.02, yalign=.98)
            k.set_sensitive(True)
            event = k.interact()

            if event:
                renpy.checkpoint()

        if event == "win":
            jump win

        if event == "tableau_drag" or event == "stock_click":
            $ hint_count -= 1
            if hint_count <= 0:
                jump hint

label win:

    show dim
    with dissolve

    "Congratulations!"

    jump newgame

label giveup:

    $ k.set_sensitive(False)
    
    show dim
    with dissolve

    menu:
        "Are you sure you want to give up?"

        "Yes":

            "Oh well, better luck next time."

            jump newgame

        "No":

            jump continue

label newgame:

    menu:    
        "Would you like to try again?"

        "Yes":
            pass

        "No":
            "Well, I hope to see you again soon."
            return 

    "Okay, here we go!"

    scene bg table

    python:
        k = Klondike(1)
        k.sensitive = False
        k.show()

    jump continue


label hint:

    $ under, over = k.hint()

    $ print under, over

    if under is None:
        jump quick_continue
        
    $ under = k.card_name(under)
    $ over = k.card_name(over)

    $ k.set_sensitive(False)

    show dim
    with dissolve

    $ hint = renpy.random.randint(0, 2)

    if hint == 0:
        "Maybe put the %(over)s on top of the %(under)s."

    elif hint == 1:
        "You can try moving the %(over)s to the %(under)s."

    elif hint == 2:
        "I think something can go on the %(under)s."

    jump continue
