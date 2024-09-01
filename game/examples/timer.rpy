# https://www.fortunusgames.com/post/timed-choices-code
default timer_time = 0
default timer_range = 0

screen countdown(timer_jump):
    timer 0.01:
        repeat True
        action If(
            timer_time > 0,
            true = SetVariable('timer_time', timer_time - 0.01),
            false=[
                Hide('countdown'),
                Jump(timer_jump),
            ]
        ) 

    bar value AnimatedValue(timer_time, timer_range):
        xalign 0.5
        yalign 0.9
        xmaximum 300

label timer:

    $ timer_time = 3
    $ timer_range = 3

    show screen countdown("timer_too_slow")

    menu:
        "End timer":
            hide screen countdown
            jump start

label timer_too_slow:

    "Did you fall asleep, by any chance?"

    jump start
