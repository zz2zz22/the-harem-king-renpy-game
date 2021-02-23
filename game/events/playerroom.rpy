screen roommenu:
    imagemap:
        idle "home config"
        hover "home config hover"

        hotspot (499, 468, 457, 167) action Jump("bed") alt "Bed"
        hotspot (5, 303, 350, 235) action Jump("computer") alt "Computer"
        hotspot (1043, 124, 231, 109) action Jump("harem") alt "Harem"
        hotspot (1062, 29, 211, 92) action Jump("map") alt "Map"
        hotspot (1177, 621, 93, 92) action Jump("preferences") alt "Preferences"
label room_menu:
    call screen roommenu

label bed:
    show home config
    "Chức năng giường chưa được thiết kế."
    jump room_menu
label computer:
    show home config
    "Chức năng máy tính chưa được thiết kế."
label harem:
    pass
label map:
    pass

label imagemap_done:
    p "Anyway..."
