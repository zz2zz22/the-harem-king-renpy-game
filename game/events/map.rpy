screen mapmenu:
    imagemap:
        idle map_i
        hover map_h

        hotspot (1113, 606, 144, 86) action Jump("map_home") alt "Home"
screen the_img(img):
    add img
label map_menu:
    call screen mapmenu with dissolve
label map_home:
    jump room_menu
