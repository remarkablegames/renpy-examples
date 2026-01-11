# https://www.renpy.org/doc/html/dialogue.html
label dialogue:

    # The say statement is used for dialogue and narration.
    "This is narration."

    "Eileen" "This is dialogue, with an explicit character name."

    e "This is dialogue, using a character object instead."

    "Bam!!" with vpunch

    # Certain characters have special meaning to Ren'Py, and so can't be used in dialogue strings. The { character begins a text tag, and the [ character begins a substitution. To use them in dialogue, double them. It may also be necessary to precede a quote with a backslash to prevent it from closing the string.
    "I walked past a sign saying, \"Let's give it 100%%!\""

    # When a character is defined with an associated image tag, say statement involving that character may have image attributes placed between the character name and the second string.
    show eileen
    e concerned "I'm a little upset at you."

    # When an @ is included in the list of attributes, any element placed after it has an only temporary effect, and is reverted at the end of the line of dialogue.
    e @ happy "That's funny."

    e -happy "I'm not sure what to think now."

    # A single line can combine permanent changes coming before the @, and temporary ones coming after.
    e happy @ vhappy "Really! That changes everything."

    # The minus sign can also be used after the @ sign
    e @ happy -concerned "My anger is temporarily suspended..."
    e "HOWEVER !"

    # Automatically changes the expression when the first line is finished showing. This only makes sense when the user doesn't have text speed set all the way up.
    show eileen concerned
    e "Sometimes, I feel sad.{nw}"
    show eileen happy
    extend " But I usually quickly get over it!"

    window show # shows the window with the default transition, if any.
    pause       # the window is shown during this pause.
    window hide # hides the window.
    pause       # the window is hidden during this pause.

    # Ren'Py supports monologue mode. When dialogue is inside triple-quoted strings, Ren'Py will break the dialogue up into blocks at blank lines. Each block is then used to create its own say statement.
    """
    This is the first line of narration. It's longer than the other two
    lines, so it has to wrap.

    This is the second line of narration.

    This is the third line of narration.
    """

    e """
    This is the first line of dialogue. It's longer than the other two
    lines, so it has to wrap.

    This is the second line of dialogue.

    This is the third line of dialogue.
    """

    jump start
