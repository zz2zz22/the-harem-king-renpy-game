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
                        jump agecheck
                    "{b}Không !{/b}":
                        return
            "{b}Chưa đủ 18{/b}":
                return

label agecheck:
        show bg pandemic with dissolve
        "Vào năm 2020, một vụ nổ khu nghiên cứu vũ khí sinh học đã xảy ra và làm rò rỉ loại virus lạ làm cho con người mắc một dịch bệnh liên quan đến đường hô hấp."
        "Dịch bệnh này có tốc độ lan truyền cực nhanh, chỉ vỏn vẹn sau vài tuần nó đã quét sạch 98\% số đàn ông trên thế giới."
        "Những người đàn ông còn sống đã được quốc gia của họ cho ngủ đông để theo dõi và phân tích kháng thể trong cơ thể họ nếu có."
        "Nhưng dù cố gắng thử mọi cách nhưng họ vẫn không thể nào tạo ra được vaccine để chống lại virus dù đã có kháng thể."
        "Cuối cùng các quốc gia đều đưa đến quyết định cuối cùng của riêng mình để có thể khắc phục tình trạng hiện tại."
        "Quốc gia của tôi đã quyết định đưa những người đàn ông còn lại vào buồng ngủ đông cho đến khi có thể phát triển một loại vaccine có thể khống chế được dịch bệnh này."
        "Tôi là [player_name] một học sinh cấp 3 bình thường cho đến khi dịch bệnh quái ác này ập đến và lấy đi sinh mạng của bố tôi."
        "Để lại tôi cùng mẹ và em gái, khi đó tôi và họ cũng nghĩ rằng đến một lúc nào đó sẽ đến lượt tôi."
        "Nhưng lực lượng của chính phủ đã đến và mang tôi đi sau khi kiểm tra rẳng tôi không bị lây nhiễm họ đã giải thích tình hình hiện tại và đưa tôi vào buồng ngủ đông."

        ##Change scene 2
        hide bg pandemic with dissolve
        "Năm 20XX,..."
        show bg hospital room with dissolve
        "Tôi dần dần tỉnh lại sau khi hoàn tất quá trình ngủ đông ..."

        ##Show nurse pics

        "{b}Hướng dẫn cụ thể thì chắc kg cần đâu nhỉ -> Kiếm tiền -> Phịch thủ. Xong rồi đó."
        jump room_menu
        return
