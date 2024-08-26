# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg club

    menu:
        "Which example do you want to see?"

        "Text":
            jump text

        "End":
            jump end
