# https://www.fortunusgames.com/post/timed-choices-code
transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0

screen countdown:
    timer 0.01 repeat True action If(timer_time > 0, true=SetVariable('timer_time', timer_time - 0.01), false=[Hide('countdown'), Jump(timer_jump)]) 
        ### ^this code decreases variable time by 0.01 until time hits 0, at which point, the game jumps to label timer_jump (timer_jump is another variable that will be defined later)

    bar value timer_time range timer_range xalign 0.5 yalign 0.9 xmaximum 300 at alpha_dissolve 
        # ^This is the timer bar.

default timer_time = 0
default timer_range = 0
default timer_jump = 'start'

label timer:

    label menu1:

        $ timer_time = 3
        $ timer_range = 3
        $ timer_jump = 'menu1_slow'

        show screen countdown

        menu:
            "End timer":
                hide screen countdown
                jump start

    label menu1_slow:

        "Did you fall asleep, by any chance?"

        jump start
