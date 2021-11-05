label intro:
        scene black
        "{b}Đây chỉ là sản phẩm tưởng tượng hoàn toàn không liên quan đến bất kỳ cá nhân hay tổ chức nào. Hãy chắc chắn rằng bạn trên 18 tuổi khi chơi trò chơi này.{/b}"
        menu:
            "{b}Tôi đã đủ 18 tuổi{/b}":
                "{b}Game có chứa nhiều yếu tố khiêu dâm, bạo lực, ... bạn có chắc chắn ?{/b}"
                menu:
                    "{b}Có !{/b}":
                        "Đây hoàn toàn là lựa chọn của bạn chúng tôi sẽ không chịu bất cứ trách nhiệm nào về việc này !!"
                        pause 0.5
                        jump agecheckpass
                    "{b}Không !{/b}":
                        return
            "{b}Chưa đủ 18{/b}":
                return

label agecheckpass:
        "Lời văn mình không được tốt và đây là project làm cá nhân nên nếu có cơ hội sẽ trau chuốt lãi sau!!"
        pause 0.5
        show bg pandemic with slow_dissolve
        "Vào năm 2020, một vụ nổ khu nghiên cứu vũ khí sinh học đã xảy ra và làm rò rỉ loại virus lạ làm cho con người mắc một dịch bệnh liên quan đến đường hô hấp."
        "Dịch bệnh này có tốc độ lan truyền cực nhanh, chỉ vỏn vẹn sau vài tuần nó đã quét sạch 98\% số đàn ông trên thế giới."
        "Những người đàn ông còn sống đã được quốc gia của họ cho ngủ đông để theo dõi và phân tích kháng thể trong cơ thể họ nếu có."
        "Nhưng dù cố gắng thử mọi cách nhưng họ vẫn không thể nào tạo ra được vaccine để chống lại virus dù đã có kháng thể."
        "Cuối cùng các quốc gia đều đưa đến quyết định cuối cùng của riêng mình để có thể khắc phục tình trạng hiện tại."
        "Tôi là [player_name] một học sinh cấp 3 bình thường cho đến khi dịch bệnh quái ác này ập đến và lấy đi sinh mạng của bố tôi."
        "Để lại tôi cùng mẹ kế và đứa em gái không cùng huyết thống, khi đó tôi và họ cũng nghĩ rằng đến một lúc nào đó sẽ đến lượt tôi."
        "Một ngày nọ lực lượng của chính phủ đã đến và mang tôi đi trước sự bàng hoàng của mẹ và em gái tôi."
        "Sau hàng loạt các quy trình kiểm tra, biết rằng tôi không bị lây nhiễm họ đã giải thích tình hình hiện tại và nhanh chóng đưa tôi tiến hành quá trình ngủ đông."

        ##Change scene 2
        hide bg pandemic with dissolve
        "{b}Năm 20XX,...{/b}"
        show bg hospital room with circleirisout
        "Tôi dần dần tỉnh lại sau khi hoàn tất quá trình ngủ đông ..." ##check lại story chỗ này
        anonymous "Anh ơiiiiii..."
        anonymous "...Anh [player_name]..."
        "Một cô gái đột nhiên lao đến và ôm chầm lấy tôi."
        anonymous "Cuối cùng anh cũng tỉnh lại rồi."
        p "Arghh... Cô..là ai ?"
        anonymous "Em là Yuko, em gái anh đây."
        show yuko uniform sad with dissolve
        y "Anh đã ngủ đông 6 năm rồi, khi họ thông báo hôm nay anh sẽ tỉnh lại em và mẹ đã lập tức đến đây."
        p "Anh không nhận ra được em luôn, dù gì cũng đã 6 năm rồi nhỉ."
        p "6 năm qua đã để em và mẹ phải chịu khổ nhiều rồi."
        show yuko uniform smile with dissolve
        y "Không đâu anh. Em và mẹ rất vui vì anh đã tỉnh lại."
        y "Để em ra gọi mẹ, mẹ đang nói chuyện với các bác sĩ phụ trách chăm sóc anh ở ngoài."
        p "{i}Vậy là mình đã ngủ đông được 6 năm rồi à. Có nghĩa là đã có cách giải quyết cái dịch bệnh kia rồi nhỉ.{/i}"
        p "{i}...Bố...Mặc dù họ không phải ruột thịt với con nhưng con hứa sẽ chăm sóc tốt cho em và mẹ.{/i}"
        p "{i}{b}Xoạch{/b}{/i}"
        anonymous "[player_name]... cuối cùng con cũng tỉnh lại rồi."
        "Cánh cửa phòng bệnh đột nhiên mở ra và một người phụ nữ trung niên lao đến ôm chầm lấy tôi."

        show haruna suit smile with dissolve
        p "Vâng, đã để mẹ lo lắng cho con nhiều rồi."
        h "Không sao cả, việc con vẫn ổn vẫn là trên hết."
        "Đây là mẹ kế của tôi - Haruna, mặc dù là một người phụ nữ đã kết hôn 2 lần nhưng bà vẫn giữ được nét quyến rũ mà cánh đàn ông khó có thể nào cưỡng lại được."
        "Đặc biệt là cái tâm hồn vãi cả chưởng đó, không trách vì sao bố lại bị bà ấy hớp hồn ngay từ lần đầu gặp mặt."
        "Yuko có vẻ thừa hưởng từ bà ấy nên con bé nhìn khá phát triển so với lứa tuổi của mình."

        ##Show nurse pics

        "{b}Hướng dẫn cụ thể thì chắc kg cần đâu nhỉ -> Kiếm tiền -> Phịch thủ. Xong rồi đó.{/b}"
        jump room_menu
        return
