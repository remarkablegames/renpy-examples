﻿# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg club

    menu:
        "Which example do you want to see?"

        "Creator-Defined Statements (CDS)":
            jump creator_defined_statements

        "Dialogue":
            jump dialogue

        "Drag and Drop":
            jump drag_and_drop

        "Image":
            jump image_example

        "Map":
            jump map

        "Python":
            jump python

        "RPG Stats":
            jump rpg_stats

        "Text":
            jump text

        "Tooltip":
            jump tooltip

        "End":
            jump end
