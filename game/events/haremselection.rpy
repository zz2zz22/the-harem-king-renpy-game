screen haremmenu:
    imagemap:
        idle ("harem_i")
        hover ("harem_h")

        hotspot (0, 34, 174, 40) action Jump("h_return")
        hotspot (698, 130, 68, 66) clicked Jump("haruna") hovered ShowTransient("the_img",dissolve, img="preview haruna") unhovered Hide("the_img")
        hotspot (773, 128, 76, 67) clicked Jump("yuko") hovered ShowTransient("the_img",dissolve, img="preview yuko") unhovered Hide("the_img")
        hotspot (859, 129, 78, 69) clicked Jump("asahi") hovered ShowTransient("the_img",dissolve, img="preview asahi") unhovered Hide("the_img")
        hotspot (948, 130, 65, 66) clicked Jump("mahiru") hovered ShowTransient("the_img",dissolve, img="preview mahiru") unhovered Hide("the_img")
        hotspot (1017, 129, 72, 67) clicked Jump("seguchi") hovered ShowTransient("the_img",dissolve, img="preview saeguchi") unhovered Hide("the_img")
        hotspot (1100, 130, 66, 66) clicked Jump("saya") hovered ShowTransient("the_img",dissolve, img="preview saya") unhovered Hide("the_img")
        hotspot (1179, 129, 81, 71) clicked Jump("yayoi") hovered ShowTransient("the_img",dissolve, img="preview yayoi") unhovered Hide("the_img")
screen the_img(img):
    add img
label harem_menu:
    call screen haremmenu with dissolve
label h_return:
    jump room_menu
label haruna:
    jump room_menu
label yuko:
    jump room_menu
label asahi:
    jump room_menu
label mahiru:
    jump room_menu
label seguchi:
    jump room_menu
label saya:
    jump room_menu
label yayoi:
    jump room_menu
