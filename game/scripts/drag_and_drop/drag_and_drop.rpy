# https://github.com/VimislikArt/dragdropcode/blob/main/dragdrop.rpy
init python:
    def drag_placed(drags, drop) -> bool:
        if not drop:
            return False

        store.draggable = drags[0].drag_name
        store.droppable = drop.drag_name

        return True

# https://www.renpy.org/doc/html/drag_drop.html
label drag_and_drop:

    show screen drag_example1
    call screen drag_example2
    show screen drag_example3

    if droppable == "The Left Circle":
        $ xpos_var = 150
    elif droppable == "The Right Circle":
        $ xpos_var = 790
    else:
        $ xpos_var = 640

    if draggable == "circle":
        show circle:
            xpos xpos_var ypos 460
    elif draggable == "triangle":
        show triangle:
            xpos xpos_var ypos 460
    elif draggable == "square":
        show square:
            xpos xpos_var ypos 460

    "The [draggable] was put in [droppable]"

    hide screen drag_example1
    hide screen drag_example2
    hide screen drag_example3

    jump drag_and_drop_inventory

screen drag_example1():
    draggroup:
        drag:
            xpos 0.25
            ypos 0.25
            draggable True
            drag_raise True
            frame:
                xpadding 20
                ypadding 20
                text "Draggable"

        drag:
            xpos 0.5
            ypos 0.25
            draggable True
            drag_raise True
            frame:
                xpadding 20
                ypadding 20
                text "Draggable"

        drag:
            xpos 0.75
            ypos 0.25
            draggable True
            drag_raise True
            frame:
                xpadding 20
                ypadding 20
                text "Draggable"

screen drag_example2():
    draggroup:
        drag:
            drag_name "circle"
            child "drag_and_drop/circle.png"
            xpos 100
            ypos 100
            draggable True
            droppable False
            dragged drag_placed
            drag_raise True

        drag:
            drag_name "triangle"
            child "drag_and_drop/triangle.png"
            xpos 400
            ypos 100
            draggable True
            droppable False
            dragged drag_placed
            drag_raise True

        drag:
            drag_name "square"
            child "drag_and_drop/square.png"
            xpos 700
            ypos 100
            draggable True
            droppable True
            dragged drag_placed
            drag_raise True

        drag:
            drag_name "The Left Circle"
            xpos 0.1
            ypos 0.6
            child "drag_and_drop/spot.png"
            draggable False
            droppable True

        drag:
            drag_name "The Right Circle"
            xpos 0.6
            ypos 0.6
            child "drag_and_drop/spot.png"
            draggable False
            droppable True

screen drag_example3():
    draggroup:
        drag:
            drag_name "The Left Circle"
            xpos 0.1
            ypos 0.6
            child "drag_and_drop/spot.png"
            draggable False
            droppable False

        drag:
            drag_name "The Right Circle"
            xpos 0.6
            ypos 0.6
            child "drag_and_drop/spot.png"
            draggable False
            droppable False
