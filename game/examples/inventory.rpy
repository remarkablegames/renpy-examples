# https://discover-with-mia.itch.io/master-inventory-management-in-renpy-complete-tutorial
default items = [
    {
        "id": "1",
        "name": "Item A",
        "description": "Item A description",
        "image": "inventory/1.png",
        "unlocked": True,
        "used": False,
    },
    {
        "id": "2",
        "name": "Item B",
        "description": "Item B description",
        "image": "inventory/2.png",
        "unlocked": True,
        "used": False,
    },
    {
        "id": "3",
        "name": "Item C",
        "description": "Item C description",
        "image": "inventory/3.png",
        "unlocked": True,
        "used": False,
    },
    {
        "id": "4",
        "name": "Item D",
        "description": "Item D description",
        "image": "inventory/4.png",
        "unlocked": True,
        "used": False,
    },
    {
        "id": "5",
        "name": "Item E",
        "description": "Item E description",
        "image": "inventory/5.png",
        "unlocked": True,
        "used": False,
    },
    {
        "id": "6",
        "name": "Item F",
        "description": "Item F description",
        "image": "inventory/6.png",
        "unlocked": True,
        "used": False,
    },
]

default show_item = ""
default open_inventory = False

screen inventory_button():
    hbox:
        xalign 1.0
        yalign 0.0

        textbutton "Show Inventory":
            yalign 0.5
            action [Show("inventory_screen"), Hide("inventory_button")]

        imagebutton:
            idle "inventory/backpack.png"
            hover "inventory/backpack.png"
            action [Show("inventory_screen"), Hide("inventory_button")]

screen inventory_screen():
    modal True

    grid 3 2:
        xalign 0.5
        yalign 0.2

        for item in items:
            if item["unlocked"] and not item["used"]:
                frame:
                    imagebutton:
                        idle item["image"]
                        action [
                            SetVariable("show_item", item["id"]),
                            ToggleVariable("open_inventory", True)
                        ]
            else:
                frame:
                    background Solid("#000")
                    xsize 140
                    ysize 140

    if open_inventory:
        frame:
            xfill True
            xalign 0.5
            yalign 1.0

            vbox:
                for item in items:
                    if item["id"] == show_item:
                        text item["name"]
                        image item["image"]
                        text item["description"]

                        frame:
                            xalign 1.0
                            yalign 1.0

                            if item["used"]:
                                textbutton "Use":
                                    action Notify(item["name"] + " can't be used")

                            else:
                                textbutton "Use":
                                    action [
                                        ToggleDict(item, "used", True),
                                        Notify(item["name"])
                                    ]

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
