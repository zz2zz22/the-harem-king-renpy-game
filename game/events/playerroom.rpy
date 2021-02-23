screen roommenu:
    imagemap:
        idle "home config"
        hover "home menu bed"

        hotspot (499, 468, 457, 167) action Jump("bed") alt "Bed"
label room_menu:

    call screen roommenu

label bed:
    show home config
    "Chức năng giường chưa được thiết kế."
    jump room_menu

label imagemap_done:

    p "Anyway..."
