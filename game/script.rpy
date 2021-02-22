# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define y = Character("Yuko", color="ff3399")
define h = Character("Haruna", color="ff3399")
define a = Character("Aisha")
define p = Character("[player_name]", color="#00dd00")
define i = Character("Ires", color="ff3399")

# transitions
define slow_dissolve = Dissolve(2.0)
define circlewipe = ImageDissolve("imagedissolve circlewipe.png", 1.0, 8)
define circleirisout = ImageDissolve("imagedissolve circleiris.png", 1.0, 8)
define slow_circleirisout = ImageDissolve("imagedissolve circleiris.png", 2.0, 8)


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
    "{i}Sau một hồi dò xét thì tôi đã phát hiện một cặp bưởi năm roi chuẩn giống Vĩnh Long, tôi lấy điện thoại ra để chuẩn bị lưu giữ tài liệu \"học tập\"{i}"
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
        show bg backalley
        with dissolve
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
        "{i}Tôi đứng nhìn chiếc điện thoại cũ trong tay thở dài, vừa kiểm tra chiếc điện thoại tôi vừa xoay người đi ra khỏi con hẻm.{i}"
        p "Haizz...Nay ra đường không coi ngày cái là gặp chuyện gì đâu không thôi."
        p "{size=-3}\*Cái điện thoại nát này thì có gì ghê gớm trời ?{/size}"

        #play sound 'audio/punch.opus'
        show truck hit:
            xalign 0.5
            yalign 0.5
        with hpunch
        "{i}Khi đang mải mê xem xét chiếc điện thoại, tôi đã bị truck-kun hun một phát nhẹ nhàng và bất tỉnh ngay sau đó.{i}"
        hide truck hit
        show bg room with slow_dissolve

        "{b}4 ngày sau...{b}"

        show bg hospital room with slow_circleirisout
        "{i}Sau một thời gian, tôi dần lấy lại ý thức.{i}"
        show yuko uniform sad with dissolve
        "???" "Onii-chan! Anh tỉnh rồi!"
        "{i}Trước mắt tôi chính là Yuko-chan, cô em gái cùng cha khác mẹ của tôi.{i}"
        p "Urghh ... Yuko-chan ? Đây là đâu ..? Sao anh lại ở đây ?"
        y "Mồ .. anh đã bị một chiếc xe tải mất lái tông phải đấy, thật may là xe cứu thương đã đến kịp thời và đưa anh đến bệnh viện."
        y "Sau nhận được cuộc gọi từ phía bệnh viện em đã lập tức chạy đến đây ngay. Anh đã hôn mê 4 ngày rồi đấy."
        show yuko uniform sad yandere
        y "Nếu anh xảy ra chuyện gì có lẽ em đã  {size=-10}đi đồ sát cả gia đình thằng tài xế rồi tự sát rồi{/size}."
        p "Em nói gì cơ ? Anh còn khá chóng mặt nên không nghe rõ..."
        show yuko uniform smile
        y "Ah không có gì đâu. Anh nghỉ ngơi đi nhé, thật mừng vì anh đã tỉnh lại."
        y "Để em đi báo cho mẹ và bác sĩ, bà ấy đang nói chuyện với bác sĩ ở ngoài."
        hide yuko uniform smile with moveoutright
        #show hình điện thoại
        "{i}Sau khi Yuko đi tôi chợt để ý đến chiếc điện thoại để trên bàn gần đầu giường.{i}"
        p "{size=-3}\*Nhìn tới cái này là thấy ứa gan. Haizzz... Mặc dù là lolicon nhưng vái trời đừng gặp lại con bé đó.{/size}"
        p "{size=-3}\*Cái quần này thì có gì đặc biệt nhỉ, chắc khởi động còn không được.{/size}"
        "{i}Tôi thử khởi động chiếc máy, một âm thanh kì quái phát ra rồi chiếc điện thoại tắt ngúm.{i}"
        p "VÃIIIII CẢ LOZZZZZZ!!!!"
        p "Cái củ kec gì thế này ? Con mắm kia đừng để anh mày gặp lại mày..."
        "Xoạch ..."
        show haruna suit sad at left with moveinright
        show yuko uniform normal at right with moveinright
        "{i}Cánh cửa phòng mở tung ra, một người phụ nữ trung niên chạy vào ôm chầm lấy tôi.{i}"
        "???" "[p] con đã tỉnh lại rồi. Mẹ đã rất lo cho con đấy"
        "{i}Người phụ nữ này là mẹ kế của tôi - Haruna, bà ấy luôn xem tôi như con ruột của bà vậy. Sau khi bố mất vào hai năm trước, bà luôn phải quán xuyến toàn bộ công việc trong gia đình."
        h "Khi bác sĩ nói với mẹ con có thể sẽ không tỉnh lại nữa mẹ đã ngất đi đấy. Thật mừng vì con đã qua khỏi."
        p "Con xin lỗi đã làm mẹ lo lắng."
        show haruna suit normal at left
        h "Không sao đâu [p]-kun. Con tỉnh dậy là tốt rồi."
        p "Vân..."
        "{i}Đột nhiên trước mặt tôi xuất hiện một dòng chữ. {vspace=10}{space=40}{b}\"Bạn có muốn thôi miên mục tiêu trước mặt không ?\"{/b}{i}"
        p "{size=-3}\*Nà ní ... thôi miên ? ... really ?{/size}"
        p "{size=-3}\*Vãi cuz cái gì đây ?{/size}"
        show haruna suit consider at left
        h "[p] con sao thế ?"
        p "Ah không có gì đâu con chỉ hơi mệt thôi."
        show haruna suit normal at left
        h "Thế con nghỉ ngơi đi, mẹ chợt nhớ còn một số chuyện phải làm, Yuko cũng đã báo bác sĩ rồi họ sẽ đến kiểm tra sớm thôi."
        h "Yuko về thôi con, để anh hai nghỉ ngơi."
        show yuko uniform sad at right
        y "Hể con muốn ở với anh thêm một tí nữa được không mẹ ?"
        h "Thôi nào anh con chỉ mới tỉnh lại thôi trong người còn rất mệt."
        y "Vâng...con hiểu rồi."
        show yuko uniform smile at right
        y "Em về nha anh, mai em lại đến. Bye bye."
        show haruna suit smile at left
        h "Mẹ cũng về đây. Con nghỉ ngơi nhé."
        hide haruna suit smile with dissolve
        hide yuko uniform smile with dissolve

        #Bắt đầu scene 2
        "..."
        "???" "Em với mẹ chú ngon nhể ?"
        p "WTF thằng nào đấy ?"
        "???" "À quên mất chưa giới thiệu nhỉ ? {w}Bố là Ires, thần tình yêu."
        p "{size=-3}\*Quắc đờ hợi thằng điên nào đây ? Không lẽ xe tông não mình có vấn đề rồi."
        i "Điên điên con kec, nói ai điên đấy ?"
        p "Đù sao ông đọc được suy nghĩ của tui."
        i "Nãy giờ bố đang nói chuyện với mày qua suy nghĩ đó nói cách khác là bố đang trong đầu mày đó thằng não bò."
        p "Chết bà mình ảo cmn tưởng rồi !"
        i "Haizz .. bó tay.{w}Nói chung bố là thần tình yêu trú trong cái điện thoại mày đang cầm ấy."
        i "Khi mày bật nguồn thì bố cũng từ đó chui vô đầu mày. Hiểu chưa ?"
        p "À như ký sinh trùng á hả ?"
        i "Mã cha mày ký sinh trùng cái quần gì. Trắng ra từ bây giờ mày có thể sử dụng một phần năng lực của bố, nhớ cái bảng chữ nãy xuất hiện không ?"
        i "Đó là một phần năng lực của bố - Thôi miên chi thuật. Nó cho mày điểu khiển hành động hoặc thay đổi ký ức, suy nghĩ của một đối tượng mày đang nhìn vào."
        p "Ôi vãi cái năng lực buff cả tấn cheat này là thật à ?"
        i "Ừ từ lúc bố nhập vào mày thì mày đã có khế ước rồi nên cứ dùng thoải mái đi, thấy mày cũng tội nghiệp mặt vầy gái nào thèm ngó nên bố lập khế ước luôn, biết ơn đi."
        p "Mặt tui sao kệ cha tui."
        p "{size=-3}\*Có cái này thì đời mình nở hoa cmnr. Cảm ơn Aisha-chan, đổi được cái điện thoại này thì anh lời vc rồi.{/size}"
        p "Nếu cái này là thật thì đã tới lúc bố mày tỏa sáng rồi. Hehe boizzz."

    return #này là return end game
