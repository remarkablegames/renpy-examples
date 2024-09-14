# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg club

    menu:
        "Creator-Defined Statements (CDS)":
            jump creator_defined_statements

        "Dialogue":
            jump dialogue

        "Drag and Drop":
            jump drag_and_drop

        "Glitch":
            jump glitch_example

        "Image":
            jump image_example

        "Inventory":
            jump inventory

        "Kinetic Text":
            jump kinetic_text

        "Map":
            jump map

        "Parallax":
            jump parallax

        "Python":
            jump python_example

        "RPG Stats":
            jump rpg_stats

        "Text":
            jump text

        "Timer":
            jump timer

        "Tooltip":
            jump tooltip

        "Transform":
            jump transform_example

        "Voice":
            jump voice

        "End":
            jump end
