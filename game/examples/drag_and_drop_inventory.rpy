# https://discover-with-mia.itch.io/renpy-tutorial-drag-and-drop-inventory
init python:

    # update the expression of a given character based on preference for a particular item.
    def character_expression(character, item) -> None:
        global characters
        if item == characters[character]["preferences"]:
            characters[character]["expression"] = "happy"
        else:
            characters[character]["expression"] = "normal"

    # check if there are items in the inventory currently available for use.
    def items_are_available() -> bool:
        return any(item["available"] for item in inventory.values())

    # select the first available item from the inventory as a default choice.
    def select_default_item() -> tuple[any, any]:
        for item_id, item_info in inventory.items():
            if item_info["available"]:
                return item_id, item_info
        return None, None

    # handle the drag and drop interaction. Update global state when an item is dropped onto a character.
    def character_dragged(drags, drop) -> bool:
        global currentCharacter, lastGivenItem

        if not drop:
            return False

        item = drags[0].drag_name
        character = drop.drag_name

        if character in characters and item in inventory and inventory[item]["available"]:
            lastGivenItem = item

            character_expression(character, item)

            inventory[item]["available"] = False
            return True

        return False

default inventory = {
    "gem": {
        "name": "Gem",
        "image": "inventory/2.png",
        "description": "A gem that Sylvie will love!",
        "available": True,
        "xpos": 0.1,
        "ypos": 0.8,
    },
    "book": {
        "name": "Book",
        "image": "inventory/5.png",
        "description": "A book that Eileen will appreciate!",
        "available": True,
        "xpos": 0.1,
        "ypos": 0.8,
    },
}

default characters = {
    "Sylvie": {
        "normal": "sylvie/sylvie blue normal.png",
        "happy": "sylvie/sylvie blue smile.png",
        "preferences": "gem",
        "expression": "normal",
    },
    "Eileen": {
        "normal": "eileen/eileen happy.png",
        "happy": "eileen/eileen vhappy.png",
        "preferences": "book",
        "expression": "normal",
    },
}

default currentCharacter = "Sylvie"
default lastGivenItem = None

default selected_info = ""
default selected_item = ""

# screen for the main character interaction, displaying available items
screen interact_with_characters():
    zorder 1

    if not items_are_available():
        vbox:
            label "{color=#fff}No items to give at the moment."
            textbutton "Return":
                action Return()

    else:
        frame:
            xalign 0.0
            yalign 0.0
            xsize 400
            ysize 600

            vpgrid:
                cols 2
                spacing 10
                draggable False
                mousewheel True

                scrollbars "vertical"
                xalign 0.5

                vbox:
                    for item_id, item_info in inventory.items():
                        if item_info["available"]:
                            textbutton f"{item_info['name']} - {item_info['description']}" action [SetVariable('selected_item', item_id), SetVariable('selected_info', item_info)]
                        else:
                            text "??? - ???"

        if selected_item:
            draggroup:
                drag:
                    drag_name selected_item
                    droppable False
                    dragged character_dragged
                    xalign 0.1
                    yalign 0.8
                    image selected_info["image"]

                drag:
                    drag_name currentCharacter
                    draggable False
                    xalign 0.5
                    yalign 1.0
                    image characters[currentCharacter][characters[currentCharacter]["expression"]]

label drag_and_drop_inventory:

    $ selected_item, selected_info = select_default_item()
    $ item_given = False

    call screen interact_with_characters

    if lastGivenItem:
        $ character_expression(currentCharacter, lastGivenItem)
        $ expression = characters[currentCharacter]["expression"]

        $ character_image = characters[currentCharacter][expression]

        if expression == "happy":
            show expression character_image at center
            "[currentCharacter] is happy with her favorite gift."
        else:
            show expression character_image at center
            "[currentCharacter]: 'Thank you, but this isn't what I prefer.'"

        $ item_given = True

    jump suite_story

label suite_story:

    while items_are_available():
        jump drag_and_drop_inventory

    hide expression character_image

    "Congratulations, you gave all the items!"

    jump start
