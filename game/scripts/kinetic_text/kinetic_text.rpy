label kinetic_text:

    e "Here's a {glitch=1.1}{color=#0f0}{b}Glitch{/b}{/color} Tag{/glitch}"

    # I know these first couple are a bit of an eye sore but wanted to show here how to apply styles to the effects.
    # And how previous styling won't be applied through them...
    e "Here is some {sc}{i}{font=FOT-PopJoyStd-B.otf}{b}scared{/b} sha{/font}key{/i}{/sc} text"
    e "Here is some {rotat}spinning rotation{/rotat} text"
    e "{fi=0-0.5}Here is some fade in text{/fi}"
    e "Here is some more selective {fi=13-1.5-20}fade in{/fi} text"
    e "Here is some {move}{b}moveable sliding{/b}{/move} text. Move your mouse near it to see!!"

    e "{bt=2}There still seems to be some bugs. Like if I just keep typing this, this text will continue off the screen and you won't be able to read it.{/bt}"
    e "{bt=2}But if we insert a paragraph tag into our line, we'll be able to tell \nthe text displayable to make a new paragraph to avoid the issue! \nHuzzah!!{/bt}"

    e "And I feel something bad is about to {chaos}happen...{/chaos}"
    e "{chaos}Helllllp Mmeeeee!!!{/chaos}"

    # This is mostly to demonstrate that the tags can stack. However this does cause lag the more you apply
    # If you wish to apply this many, I advise you make a single Class that does all the effects itself or...
    e "{bt}{sc}{rotat}{chaos}Oh god NOooooo{/chaos}{/rotat}{/sc}{/bt}"

    # You could do this. Have them nest directly without as many render callbacks through Text displayables
    e "{omega=BT=5@SC=10@FI=20-0.5@ROT=400@CH}Oh god NOooooo{/omega}"
    e "{bt=20}{fi=20-1.5}Must{/fi} {rotat}gain{/rotat} {sc=10}control!!! For [playername]!!!{/sc}{/bt}"

    # They can be applied to menu options as well
    menu:
        "{bt}Breath{/bt}":
            e "{bt=3}*breathe*...{/bt}"
        "{chaos}Panic More{/chaos}":
            e "{sc=10}That probably won't help.{/sc}"
            e "{sc=3}I'ma just {/sc}{sc=1}calm down{/sc} now..."

    jump start
