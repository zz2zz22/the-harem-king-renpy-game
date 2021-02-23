screen haremmenu:
    imagemap:
        idle "harem select idle"
        hover "harem select hover"

        hotspot (698, 130, 68, 66) clicked Jump("haruna") hovered ShowTransient("the_img", img="haruna suit smile.png") unhovered Hide("the_img")
        hotspot (773, 128, 76, 67) clicked Jump("yuko") hovered ShowTransient("the_img", img="yuko uniform smile.png") unhovered Hide("the_img")
        hotspot (859, 129, 78, 69) clicked Jump("asahi") hovered ShowTransient("the_img", img="asahi uniform shy.png") unhovered Hide("the_img")
        hotspot (948, 130, 65, 66) clicked Jump("mahiru") hovered ShowTransient("the_img", img="mahiru uniform normal") unhovered Hide("the_img")
        hotspot (1017, 129, 72, 67) clicked Jump("seguchi") hovered ShowTransient("the_img", img="seguchi pyjama normal.png") unhovered Hide("the_img")
        hotspot (1100, 130, 66, 66) clicked Jump("saya") hovered ShowTransient("the_img", img="saya uniform normal.png") unhovered Hide("the_img")
        hotspot (1179, 129, 81, 71) clicked Jump("yayoi") hovered ShowTransient("the_img", img="yayoi uniform smile.png") unhovered Hide("the_img")
screen the_img(img):
    add img at left
label harem_menu:
    call screen haremmenu with dissolve
label haruna:
    pass
    jump room_menu
label yuko:
    pass
    jump room_menu
label asahi:
    pass
    jump room_menu
label mahiru:
    pass
    jump room_menu
label seguchi:
    pass
    jump room_menu
label saya:
    pass
    jump room_menu
label yayoi:
    pass
    jump room_menu
