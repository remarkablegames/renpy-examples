# https://discover-with-mia.itch.io/master-inventory-management-in-renpy-complete-tutorial
default inventory_icon = [
    "images/inventory/1.png",
    "images/inventory/2.png",
    "images/inventory/3.png",
    "images/inventory/4.png",
    "images/inventory/5.png",
    "images/inventory/6.png",
]

default item_name = {
    "images/inventory/1.png": "Item A",
    "images/inventory/2.png": "Item B",
    "images/inventory/3.png": "Item C",
    "images/inventory/4.png": "Item D",
    "images/inventory/5.png": "Item E",
    "images/inventory/6.png": "Item F",
}

default description = {
    "images/inventory/1.png": "Item A description",
    "images/inventory/2.png": "Item B description",
    "images/inventory/3.png": "Item C description",
    "images/inventory/4.png": "Item D description",
    "images/inventory/5.png": "Item E description",
    "images/inventory/6.png": "Item F description",
}

default name_item = ""
default story_name_item = ""
default show_description = ""
default show_item = ""
default open_inventory = False

default choices = [
    "images/inventory/1.png",
    "images/inventory/2.png",
    "images/inventory/3.png",
    "images/inventory/4.png",
    "images/inventory/5.png",
    "images/inventory/6.png",
]

default using_item = {
    "images/inventory/1.png": True,
    "images/inventory/2.png": True,
    "images/inventory/3.png": True,
    "images/inventory/4.png": True,
    "images/inventory/5.png": True,
    "images/inventory/6.png": True,
}

screen inventory_button():
    hbox:
        xalign 1.0
        yalign 0.0

        textbutton "Show Inventory":
            yalign 0.5
            action [Show("inventory_screen"), Hide("inventory_button")]

        imagebutton:
            idle "images/inventory/backpack.png"
            hover "images/inventory/backpack.png"
            action [Show("inventory_screen"), Hide("inventory_button")]

screen inventory_screen():
    modal True

    grid 3 2:
        xalign 0.5
        yalign 0.2

        for item in inventory_icon:
            if item in choices:
                frame:
                    imagebutton:
                        idle item
                        action [
                            SetVariable("name_item", (item_name.get(item))),
                            SetVariable("show_description", (description.get(item))),
                            SetVariable("show_item", item),
                            ToggleVariable("open_inventory", True)
                        ]
            elif item in inventory_icon:
                frame:
                    background Solid("#000")
                    xsize 136
                    ysize 136

    if open_inventory:
        frame:
            xfill True
            xalign 0.5
            yalign 1.0

            vbox:
                for item in inventory_icon:
                    if item in choices and item in show_item:
                        text name_item
                        image item
                        text show_description

                        frame:
                            xalign 1.0
                            yalign 1.0

                            if using_item[item]:
                                textbutton "Use":
                                    action [
                                        RemoveFromSet(choices, item),
                                        Notify(item_name[item])
                                    ]
                            else:
                                textbutton "Use":
                                    action Notify(item_name[item] + " can't be used now...")

    textbutton "Close Inventory":
        xalign 1.0
        yalign 0.0
        action [
            Hide("inventory_screen"),
            Show("inventory_button"),
            ToggleVariable("open_inventory", False),
        ]

label inventory:

    show screen inventory_button

    pause
