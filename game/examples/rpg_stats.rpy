label rpg_stats:

    default attack = 0
    default defense = 0
    default magic = 0

    screen stat(name, amount):
        text "[name]: [amount]"
        bar value AnimatedValue(amount, 100) xalign 0.5 xsize 300

    screen stats():
        frame:
            xalign 0 ypos 0
            vbox:
                use stat("Attack", attack)
                null height 15
                use stat("Defense", defense)
                null height 15
                use stat("Magic", magic)

    show screen stats

    menu:
        "Which stat do you want to increase?"

        "Attack":
            $ attack += 1
            jump rpg_stats

        "Defense":
            $ defense += 1
            jump rpg_stats

        "Magic":
            $ magic += 1
            jump rpg_stats

        "End":
            hide screen stats
            jump start
