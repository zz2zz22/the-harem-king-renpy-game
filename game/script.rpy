#Khởi tạo biến nhân vật
define y = Character("Yuko", color="ff3399")
define h = Character("Haruna", color="ff3399")
define a = Character("Aisha")
define p = Character("[player_name]", color="#00dd00")
define i = Character("Ires", color="ff3399")

#Khởi tạo hiệu ứng chuyển cảnh
define slow_dissolve = Dissolve(1.0)
define fast_dissolve = Dissolve(-1.0)
define circlewipe = ImageDissolve("imagedissolve circlewipe.png", 1.0, 8)
define circleirisout = ImageDissolve("imagedissolve circleiris.png", 1.0, 8)
define slow_circleirisout = ImageDissolve("imagedissolve circleiris.png", 2.0, 8)


# The game starts here.
label start:
    #Khởi tạo các biến
    $ player_name = ""
    $ p_money = 50000

    show black
    $ player_name = renpy.input("Nhập tên nhân vật muốn đặt: \n{size=-5}{i}Nếu bỏ trống thì sẽ dùng tên mặc định là \"Shirogane\".{/i}{/size}")
    if player_name == "":
        $ player_name = "Shirogane"
    pause 0.5
    jump intro
    return #này là return end ga
