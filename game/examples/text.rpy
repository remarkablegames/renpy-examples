label text:

    # Additional arguments can be passed to the say statement by including them in parenthesis after the say statement.
    e "Hello, world." (what_color="#8c8")

    # Ren'Py supports interpolating data into the text string before it is displayed.
    default playername = "Guy"
    "Welcome to the Nekomimi Institute, [playername]!"

    # It can also interpolate any valid Python expression.
    $ names = ["John", "Mary"]
    "My first name is [names[0]]."

    # It's possible to apply formatting when displaying numbers.
    $ points = 42
    $ max_points = 100
    "I like you [100.0 * points / max_points:.2] percent!"

    # Text tags are suitable for styling a portion of text block.
    "Plain {b}Bold {i}Bold-Italic{/i} Bold{/b} Plain"

    # Ren'Py will close all tags that are open at the end of the text block.
    "{size=+20}This is big!"

    # The anchor tag creates a hyperlink between itself and its closing tag.
    "Why don't you visit {a=https://renpy.org}Ren'Py's home page{/a}?"
    "Or {a=jump:more_text}here for more info{/a}."

    jump start

label more_text:

    # The alpha text tag renders the text between itself and its closing tag in the specified opacity. The opacity should be a value between 0.0 and 1.0, corresponding to fully invisible and fully opaque, respectively. If the value is prefixed by + or -, the opacity will be changed by that amount instead of completely replaced. If the value is prefixed by *, the opacity will be multiplied by that amount.
    "{alpha=0.1}This text is barely readable!{/alpha}"
    "{alpha=-0.1}This text is 10 percent more transparent than the default.{/alpha}"
    "{alpha=*0.5}This text is half as opaque as the default.{/alpha}"

    # The color text tag renders the text between itself and its closing tag in the specified color. The color should be in #rgb, #rgba, #rrggbb, or #rrggbbaa format.
    "{color=#f00}Red{/color}, {color=#00ff00}Green{/color}, {color=#0000ffff}Blue{/color}"

    # The characters per second tag sets the speed of text display, for text between the tag and its closing tag. If the argument begins with an asterisk, it's taken as a multiplier to the current text speed. Otherwise, the argument gives the speed to show the text at, in characters per second.
    "{cps=20}Fixed Speed{/cps} {cps=*2}Double Speed{/cps}"

    # The strikethrough tag draws a line through text between itself and its closing tag.
    "It's good {s}to see you{/s}."

    # The space tag is a self-closing tag that inserts horizontal space into a line of text.
    "Before the space.{space=30}After the space."

    # The underline tag underlines the text between itself and its closing tag.
    "It's good to {u}see{/u} you."

    # The vspace tag is a self-closing tag that inserts vertical space between lines of text.
    "Line 1{vspace=30}Line 2"

    # The wait tag is a self-closing tag that waits for the user to click to continue.
    "Line 1{w} Line 1{w=1.0} Line 1"

    # The paragraph pause tag is a self-closing tag that terminates the current paragraph, and waits for the user to click to continue.
    "Line 1{p}Line 2{p=1.0}Line 3"

    # The no-wait tag is a self-closing tag that causes the current line of dialogue to automatically dismiss itself once the end of line has been displayed.
    "Looks like they're{nw}"

    # If the fast tag is displayed in a line of text, then all text before it is displayed instantly, even in slow text mode.
    "Looks like they're{fast} playing with their trebuchet again."

    # Text can also be used as a displayable, which allows you to apply transforms to text, displaying it as if it was an image and moving it around the screen.
    show text "{size=50}{color=#f00}Hello, World" at truecenter
    with dissolve
    pause 5
    hide text
    with dissolve

    # You can use ParameterizedText directly to define similar images with different style properties.
    image top_text = ParameterizedText(xalign=0.5, yalign=0.0)
    show top_text "{size=50}{color=#f00}This text is shown at the center-top of the screen"
    pause 5

    jump start
