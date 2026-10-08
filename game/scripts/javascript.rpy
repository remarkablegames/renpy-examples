# https://www.renpy.org/doc/html/web.html#javascript
label javascript:

    "Ren'Py can run JavaScript, using the functions in the {a=https://www.renpy.org/doc/html/web.html#javascript}emscripten{/a} module."

    # When not running on the web platform, renpy.emscripten is False
    if renpy.emscripten:

        $ renpy.emscripten.run_script("document.getElementById('ContextContainer').style.display = 'none'")

        "The hamburger menu is hidden."

        $ renpy.emscripten.run_script("document.getElementById('ContextContainer').style.display = ''")

        "The hamburger menu is back."
