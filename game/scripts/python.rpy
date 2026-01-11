# https://www.renpy.org/doc/html/python.html
label python_example:

    "You flipped a coin."
    $ coinflip = renpy.random.choice([True, False])
    if coinflip:
        "It landed heads."
    else:
        "It landed tails."

    "You rolled a die."
    $ dice_roll = renpy.random.randint(1, 6)
    "The number is [dice_roll]."

    jump start
