# https://zeillearnings.itch.io/map-navigation
label map:

    call screen map

    pause

# https://www.renpy.org/doc/html/screens.html
screen map():
    add "map/bg map.jpg"

    # https://www.renpy.org/doc/html/screens.html#imagebutton
    imagebutton:
        xpos 618
        ypos 570
        idle "map/house1_idle.png"
        hover "map/house1_hover.png"
        action Jump("start")

        # Control Actions
        # ===============
        # Call - Calls a Label
        # Hide - Hides an Element
        # Jump - Jumps to a Label
        # Return - Returns a Value
        # Show - Shows an Element
        # Togglescreen - Shows/Hides a Screen
        # NullAction - Does Nothing
        #
        # Examples
        # --------
        # textbutton "button" action Call("start")
        #
        # Data Actions
        # ============
        # AddtoSet - Adds a variable to a set
        # RemovefromSet - Subtracts variable from a set
        # SetScreenVariable - Sets a Screen Variable
        # SetVariable - Sets a Variable
        #
        # Examples
        # --------
        # textbutton "Add 1" action SetVariable(num + 1)
        #
        # Audio Actions
        # =============
        # Play - Plays a Sound
        # Queue - Queues a Sound
        # SetMixer - Sets Sound Volume
        # Stop - Stops a Sound
        #
        # Examples
        # --------
        # textbutton "Play Next" action Play(music, "song.ogg")
        # textbutton "Volume 20%" action SetMixer(music, 0.2)
        #
        # Menu Actions
        # ============
        # Start - Starts Game
        # Quit - Quits the Game
        # ShowMenu - Shows a menu (can be user-defined)
        #
        # Examples
        # --------
        # textbutton "Start" action Start(label="start")
        # textbutton "Quit" action Quit(confirm="yes")
        # textbutton "Load" action ShowMenu("load")
        #
        # File Actions
        # ============
        # Quicksave - Quicksaves the Game
        #
        # Examples
        # --------
        # textbutton "Quicksave" action QuickSave(message="Quick save complete", newest=False)
        #
        # Other Actions
        # =============
        # Skip - Skips to the next Choice Menu
        #
        # Examples
        # --------
        # textbutton "Skip" action Skip(fast=False, confirm=False)
        #
        # https://www.renpy.org/doc/html/screen_actions.html

    imagebutton:
        xpos 596
        ypos 165
        # <image>_idle.png = idle image
        # <image>_hover.png = hover image
        # <image>_action.png = button when activated
        auto "map/house2_%s.png"
        action Jump("start")
