# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define y = Character("Yuko", color="ff3399")
define a = Character("Aisha")
define p = Character("[player_name]", color="#00dd00")

# transitions
define circlewipe = ImageDissolve("imagedissolve circlewipe.png", 1.0, 8)
define circleirisout = ImageDissolve("imagedissolve circleiris.png", 1.0, 8)


# The game starts here.

label start:
    $ player_name = ""

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    $ player_name = renpy.input("Nhập tên vào đi ku !\n{size=-5}{i}Nếu bỏ trống thì sẽ dùng tên mặc định là \"Shirogane\".{i}{/size}")
    if player_name == "":
        $ player_name = "Shirogane"
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.
    show bg school hall
    with fade
    "{i}Tôi, [p] là một học sinh trung học bình thường không có gì nổi bật, từ ngoại hình cho đến đầu óc đều gói gọn trong chữ {b}BÌNH THƯỜNG{b}{i}."
    "{i}Là một người ý thức được bản thân mình ra sao tôi đã chuẩn bị sẵn sàng từ rất lâu cho một cuộc sống trung học buồn tẻ cô đơn. \n {size=-5}\*Chuyện đời thằng dev (Q w Q)\*{/size}{i}"

    show bg street shopping
    with circlewipe
    "{i}Như mọi ngày, sau khi trải qua những tiết học vô vị, tôi men theo cung đường quen thuộc để đến Trần Duy Hưng ngắm những \"tâm hồn\" mơn mởn.{i}"
    p "Hôm nay sao không thấy \"em\" nào vậy ta ?"
    "{i}Sau một hồi dò xét thì tôi đã phát hiện một cặp bưởi 5 roi to facking wow shiet, tôi lấy điện thoại ra để chuẩn bị lưu giữ tài liệu \"học tập\"{i}"
    "{i}Khi đang mải mê ngắm nhìn và tìm góc đẻ chụp ảnh cặp bưởi ấy, tôi đã vô tình va trúng thứ gì đó.{i}"


    "???" "Au..au..đau..quá"
    show aisha uniform akward
    with dissolve
    "{i}Trước mắt tôi là một cô bé tiểu học, cô bé thở gấp mồ hôi nhễ nhại như thể vừa chịc...à không như đang chạy trốn vậy.{i}"
    show aisha uniform rush
    "???" "Ahh! Em xin lỗi nhưng em đang bị đuổi theo, giúp em với!"
    "{i}Tôi nhìn về sau cô bé thì thấy 3 anh Minh Béo đang chạy hết tốc lực về phía tôi và cô bé...{i}"
    menu:
        "Ok con dê (Chăn rau thôi chứ gì nữa)":
            hide aisha uniform rush
            jump choice_begin
        "Không":
            jump choice_end

    label choice_end:
        "{b}Vãi cả cuz cắt cu đi bro :<{b}  \n Lời khuyên của dev : Hãy nghe con trym, đừng nghe lý trí"
        p "Hả hả gì ?"
        "{i}Vì tôi đã do dự nên em ấy đã bị mang đi bởi đám người lạ."
        return
        # This ends the game.
    label choice_begin:
        "{i}Tôi nắm lấy tay cô bé và bắt đầu chạy thật nhanh đến khu phố mua sắm gần đó và lẫn vào dòng người tấp nập dần tiến vào một con hẻm vắng.{i}"
        show aisha uniform akward
        with dissolve
        p "Hộc..Hộc...Anh nghĩ mình cắt đuôi được chúng rồi đấy!"
        p "Mà sao chúng lại đuổi theo em thế ?"
        "???" "Chúng đuổi theo em là vì thứ này.."
        "{i}Cô bé lấy một vật gì đó màu đen ở trong túi ra, đó là một chiếc điện thoại cũ hết sức bình thường.{i}"
        p "Đinh Công Mạnh..3 thằng Minh Béo không đuổi em vì màng trinh mà vì cái điện thoại cũ xì này à ??"
        show aisha uniform rush
        "???" "Không phải như anh nghĩ đâu, chiếc điện thoại này rất đặc biệt."
        p "Nhìn thế quái nào nó cũng như một chiếc điện thoại bình thường mà?"
        p "Thôi bỏ đi. Làm anh mày không thể lưu được tài liệu \"học tập\" quý giá..."
        hide aisha uniform rush
        "{i}Đột nhiên cảm giác nhẹ tênh hai bên túi quần làm tôi xám cả mặt mà hét lớn.{i}"
        p "ĐẠ MẤU!! RỚT CMN ĐIỆN THOẠI RỒIIII ! TÀI LIỆU \"HOX CMN TẬP\" CỦA BỐ !!!!"
        p "Tất cả là tại em đó biết cái điện thoại đó quan trọng với anh như thế nào kg hả ?"
        show aisha uniform rush
        "???" "Em xin lỗi! Em xin lỗi! Em xin lỗi! Em xin lỗi! ..."
        "{i}Cô bé bắt đầu bối rối và liên tục xin lỗi, thấy vậy tôi cũng không muốn quát thêm rồi cho con bé khóc lớn, như vậy chỉ khiến tôi rơi vào tình huống khó xử hơn.{i}"
        p "Haizzzz.. Thiệt hết cách, coi như anh mày xui vậy."
        p "Đã không được ngắm gái còn bị rượt cho chạy rớt hai hòn dái, xong còn mất \"kho báu\" bao nhiêu năm thu thập."
        "{i}Tôi xoay người định bước đi thì..{i}"
        show aisha uniform akward
        "???" "Anh ơi khoan đã!"
        p "Gì nữa đây ?"
        "???" "Anh hãy giữ nó dùng đi, xem như em đền lại cho anh."
        "{i}Cô bé dúi cái điện thoại của cô bé vào tay tôi.{i}"
        p "Iphone S đổi điện thoại cũ. Wow trao đổi hong có miếng lời nào luôn á."
        show aisha uniform normal
        "???" "Anh yên tâm! Chiếc điện thoại này rất đặc biệt nó sẽ mang lại nhiều bất ngờ cho anh."
        p "Ừa rồi giữ cho 3 thằng Minh Béo nó kiếm anh mày lấy trinh đít ha."
        "???" "Anh đừng lo, chúng vẫn nghĩ em là người giữ nó, giao cho anh vẫn anh toàn hơn. Dù gì anh cũng giống người tốt."
        "???" "À quên em tên là Aisha, rất vui được gặp anh."
        p "Ừ anh thì không vui khi gặp mày. Anh tên là [p]."
        a "Thôi em phải đi đây, về cách dùng nó thì anh sẽ tự khám phá ra ngay thôi. Tạm biệt"
        a "Hẹn gặp lại anh [p]."
        p "Thôi thôi con xin. Đi luôn dùm con một cái."
        hide aisha uniform normal
        with moveoutright
        "{i}[a] sau khi nói xong thì chạy đi thật nhanh vào dòng người tấp nập ngoài phố.{i}"
        "{i}Tôi đứng nhìn chiếc điện thoại cũ trong tay thở dài, tôi vừa kiểm tra chiếc điện thoại vừa xoay người đi ra khỏi con hẻm.{i}"
        p "Haizz...Nay ra đường không coi ngày cái là gặp chuyện gì đâu không thôi."
        p "\*Cái điện thoại nát này thì có gì ghê gớm trời?"


        play sound 'audio/punch.opus'
        show truck hit:
            xalign 0.5
            yalign 0.5
        with hpunch
        "{i}Khi đang mải mê xem xét chiếc điện thoại, tôi đã bị truck-kun hun một phát nhẹ nhàng và bất tỉnh ngay sau đó.{i}"


    return
