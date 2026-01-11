#####
## This is the expansion for the Simulated Lighting shader.  The SimulatedLighting shader has been 
## re-written mainly because the back light functionality has been goofy.
## NEW FEATURES:
## 1) The MouseLight function, which makes lights follow your mouse when used in transforms.
## 2) The Spotlight transform.  You can use this to drop a spotlight on a given X/Y.
##    Example: camera at Spotlight(0.5,0.5) will put a spotlight effect in the center of your scene.
## 3) The Flashlight mode transform.  Assign to your camera and you can use it to let your players
## explore your scenes with a flashlight.  Great for more interactive segments and image maps!
##
## USING MOUSELIGHT:
## STEP 1.Make a new transform from the SimulatedLighting templates.  You can use one of the ones here or 
## in the MVNTemplates.RPY file. If the template includes the position of the light you want to place, eg ## the key light or the rim light, delete that line.
## STEP 2. Add 'function MouseLight'.  This will make the center of the key light and/or rim light follow 
## your mouse.
## STEP 3. Add this transform to a character, background, or layer the usual ways.
## STEP 4. Go to the scene you placed the transform and press Alt+M to open a mouse position tracker. 
## STEP 5. Move your mouse around to position the light. Once you've placed the light somewhere you like
## take note of the X and Y values there.
## STEP 6. Write the values into your transform and remove function MouseLight 
## e.g: u_key_light_position (X,Y) and/or e.g u_rim_light_position (X,Y)
## 
## p.s. Make Visual Novels - Stella
#####

init python:
     config.underlay.append(renpy.Keymap(mousemonitor = Show("display_coordinates")))
     config.keymap["mousemonitor"] = ['alt_K_m']

init -999 python:
    MVNMouseX = 0.0
    MVNMouseY = 0.0
    MVNRPYMouseX = None
    MVNRPYMouseY = None

    def MouseLight(trans, st, at):
        location = getMousePos()
        trans.u_rim_light_position = (location[0],location[1])
        trans.u_key_light_position = (location[0],location[1])

    def getMousePos():
        size = renpy.get_physical_size()
        location = (getMouseX()/size[0],getMouseY()/size[1])
        return location

    def MonitorMouse():
        global MVNMouseX, MVNMouseY, MVNRPYMouseX, MVNRPYMouseY
        step = 0.001
        location = getMousePos()
        MVNMouseX = round(location[0] / step) * step
        MVNMouseY = round(location[1] / step) * step
        MVNRPYMouseX, MVNRPYMouseY = renpy.get_mouse_pos()

    def getMouseY():
        import pygame;
        x, y= pygame.mouse.get_pos()
        return (y)

    def getMouseX():
        import pygame;
        x, y= pygame.mouse.get_pos()
        return (x)

screen display_coordinates():
    frame:
        xalign 0.0
        yalign 0.0
        padding (10, 10)
        has vbox:
            text "Mouse X,Y"
            text "X: [MVNMouseX]" 
            text "Y: [MVNMouseY]"
            text "Pixel X: [MVNRPYMouseX]"
            text "Pixel Y: [MVNRPYMouseY]"
            timer 0.1 action Function(MonitorMouse) repeat True

transform NewSimLight:
    mesh True
    shader "MakeVisualNovels.SimulatedLighting"
    u_fill_light_color (1.0,1.0,0.6)
    u_key_light_color (1.0,0.7,0.5)
    u_fill_light_direction (-1.0, 0.0)
    u_key_light_position (0.5,0.2)
    u_fill_light_intensity (-0.5)
    u_key_light_intensity (0.5)
    u_key_light_radius (0.5)
    u_rim_light_position (0.5, 0.2)
    u_rim_light_radius (0.5)
    u_rim_light_intensity (1.0)
    u_rim_light_color (1.0,0.8,0.0)
    pause 0
    repeat

# This lets you place a key light while keeping the rim light still.
transform MouseKeyLight:
    mesh True
    shader "MakeVisualNovels.SimulatedLighting"
    function MouseLight
    u_fill_light_color (1.0,1.0,0.6)
    u_fill_light_direction (-1.0, 0.0)
    u_fill_light_intensity (-0.5)
    u_key_light_color (1.0,0.7,0.5)
    u_key_light_intensity (0.5)
    u_key_light_radius (0.5)
    u_rim_light_radius (0.0)
    u_rim_light_intensity (0.0)
    u_rim_light_color (0.0,0.0,0.0)
    pause 0
    repeat

# This lets you place a rim light while keeping the key light still.
transform MouseRimLight:
    mesh True
    function MouseLight
    shader "MakeVisualNovels.SimulatedLighting"
    u_fill_light_color (1.0,1.0,1.0)
    u_key_light_color (1.0,1.0,0.8)
    u_fill_light_direction (0.0, 0.0)
    u_key_light_position (0.5,0.2)
    u_fill_light_intensity (-0.5)
    u_key_light_intensity (0.6)
    u_key_light_radius (0.7)
    u_rim_light_radius (1.0)
    u_rim_light_intensity (0.9)
    u_rim_light_color (1.0,1.0,1.0)
    pause 0
    repeat

transform Spotlight(keyX,keyY):
    mesh True
    shader "MakeVisualNovels.SimulatedLighting"
    u_fill_light_color (1.0,1.0,0.6)
    u_key_light_color (1.0,0.7,0.5)
    u_fill_light_direction (-1.0, 0.0)
    u_key_light_position (keyX,keyY)
    u_fill_light_intensity (-0.8)
    u_key_light_intensity (1.05)
    u_key_light_radius (0.3)
    u_rim_light_position (0.5, 0.2)
    u_rim_light_radius (0.0)
    u_rim_light_intensity (0.0)
    u_rim_light_color (0.0,0.0,0.0)
    pause 0
    repeat

transform FlashLightMode:
    mesh True
    shader "MakeVisualNovels.SimulatedLighting"
    function MouseLight
    u_fill_light_color (1.0,1.0,0.6)
    u_key_light_color (1.0,0.8,0.6)
    u_fill_light_direction (-1.0, 0.0)
    u_fill_light_intensity (-1.0)
    u_key_light_intensity (1.2)
    u_key_light_radius (0.3)
    u_rim_light_position (0.0, 0.0)
    u_rim_light_radius (0.0)
    u_rim_light_intensity (0.0)
    u_rim_light_color (0.0,0.0,0.0)
    pause 0
    repeat

# This is an example of how to use the MouseLight function.  Customize the lights to your liking, then use MouseLight to find the idea positioning for your lighting effect.  This specifically places the key light.
transform CoolWarmLighting:
    mesh True
    shader "MakeVisualNovels.SimulatedLighting"
    function MouseLight
    u_fill_light_direction (1.0,1.0)
    u_rim_light_intensity (0.5)
    u_rim_light_radius(0.3)
    u_rim_light_position (0.5,0.2)
    u_rim_light_color (1.0,0.6,0.0)
    u_key_light_color (1.0, 0.6, 0.6)    
    u_fill_light_color (1.0, 1.0, 0.6) 
    u_key_light_radius (0.3)   
    u_key_light_intensity (0.8)            
    u_fill_light_intensity (-0.5)  
    pause 0
    repeat
