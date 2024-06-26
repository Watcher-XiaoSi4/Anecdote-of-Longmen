﻿# 游戏的脚本可置于此文件中。

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。

define l = Character("林",image = "lin")
define d = Character("蝶",image = "die")
define j = Character("缄默",image = "jian")
define x = Character("星熊",image = "xing")
define c = Character("陈",image = "chen")
define z = Character("钟",image = "zhong")
define w = Character("未堰",image = "wei")
define g = Character("谷涸",image = "gu")
define i = Character("景",image = "jing")
define s = Character("诗怀雅",image = "shi")
define ou = Character("人偶",image = "ou")
define u = Character("未知")
define a = Character("阿姨")

# define narrator = nvl_narrator

$_dissmiss_pause = False
default count_lin = 0
default count_die = 0
default count_lindie = 0
define Character_lin = False
define Character_gu = False

#声明角色图片

image lin = ConditionSwitch("Character_lin == False",im.FactorScale("images/new-human/character/林.png",0.75),"Character_lin == True",im.FactorScale("images/new-human/character/林残.png",0.75))
image die = im.FactorScale("images/new-human/character/蝶.png",0.75)
image zhong = im.FactorScale("images/new-human/character/钟.png",0.75)
image gu = ConditionSwitch("Character_gu == False",im.FactorScale("images/new-human/character/谷涸.png",0.75),"Character_gu == True",im.FactorScale("images/new-human/character/新谷.png",0.75))
image wei = im.FactorScale("images/new-human/character/未堰.png",0.75)
image jian = im.FactorScale("images/new-human/character/缄默.png",0.75)
image jing = im.FactorScale("images/new-human/character/景.png",0.75)
image chen = im.FactorScale("images/new-human/character/陈.png",0.75)
image xing = im.FactorScale("images/new-human/character/星熊.png",0.75)
image shi = im.FactorScale("images/new-human/character/诗怀雅.png",0.8)
image ou = im.FactorScale("images/new-human/character/人偶.png",0.75)

#特殊图片，有1为水平翻转

image lin1 = im.FactorScale("images/new-human/special-character/林1.png",0.75)
# image lincan = im.FactorScale("images/new-human/special-character/林残.png",0.75)
image linjian = im.FactorScale("images/new-human/special-character/林与缄默.png",0.75)
image diejian = im.FactorScale("images/new-human/special-character/蝶与缄默.png",0.75)
image diejian1 = im.FactorScale("images/new-human/special-character/蝶与缄默1.png",0.75)
image zhongdie = im.FactorScale("images/new-human/special-character/钟与蝶.png",0.75)
image lingu = im.FactorScale("images/new-human/special-character/林与谷涸.png",0.75)
image lincangu = im.FactorScale("images/new-human/special-character/林残谷.png",0.75)
image guigu = im.FactorScale("images/new-human/special-character/星熊与谷涸.png",0.75)
image weimao = im.FactorScale("images/new-human//special-character/未堰与猫.png",0.75)
image xing2 = im.FactorScale("images/new-human//special-character/星熊2.png",0.6)
# image xingu = im.FactorScale("images/new-human//special-character/新谷.png",0.6)
image guran1 = im.FactorScale("images/new-human//special-character/谷染1.png",0.75)
image guran2 = im.FactorScale("images/new-human//special-character/谷染2.png",0.75)

#说话侧边头像

image side lin = im.FactorScale("images/new-human/side-character/side_林.png",0.3)
image side die = im.FactorScale("images/new-human/side-character/side_蝶.png",0.3)
image side zhong = im.FactorScale("images/new-human/side-character/side_钟.png",0.3)
image side gu = im.FactorScale("images/new-human/side-character/side_谷涸.png",0.3)
image side jing = im.FactorScale("images/new-human/side-character/side_景.png",0.3)
image side wei = im.FactorScale("images/new-human/side-character/side_未堰.png",0.3)
image side jian = im.FactorScale("images/new-human/side-character/side_缄默.png",0.3)
image side chen = im.FactorScale("images/new-human/side-character/side_陈.png",0.3)
image side xing = im.FactorScale("images/new-human/side-character/side_星熊.png",0.3)
image side shi = im.FactorScale("images/new-human/side-character/side_诗怀雅.png",0.3)

#背景图

image game0 = "images/横置game0.png"
image hei ="images/横置game1.png"
image jiedao = im.FactorScale("images/screen/街道.png",1)
image jiedao6 = im.FactorScale("images/screen/街道6.png",1)
image jiedao7 = im.FactorScale("images/screen/街道7.png",1)
image jiedao8 = im.FactorScale("images/screen/白日的街道.png",1.38)
image xiaodao = im.FactorScale("images/screen/小道.png",1.38)
image jiujiedao = "images/screen/旧街道.png"
image hutong = im.FactorScale("images/screen/胡同.png",1.38)
image zhensuo = im.FactorScale("images/screen/诊所.png",1.38)
image zhensuoneibu = im.FactorScale("images/screen/诊所内部.png",1.38)
image dingceng = im.FactorScale("images/screen/顶层.png",1.38)
image jiewei = im.FactorScale("images/screen/结尾.png",1.38)
image feixuchen = im.FactorScale("images/screen/废墟晨.png",1.38)
image benzhi = im.FactorScale("images/screen/本质探寻.png",1.38)
image jiufangwu = "images/screen/旧房屋.png"
image pinmin = "images/screen/贫民区.png"
image pinminye = "images/screen/贫民区夜.png"
image jieti = "images/screen/无声阶梯.png"
image louti = "images/screen/楼梯.png"
image huanmeng = "images/screen/幻梦1.png"
image huanmeng1 = "images/screen/幻梦.png"
image duzi = "images/screen/独自一人的屋子.png"
image bengsui = "images/screen/镜中世界崩碎.png"
image jingjia = "images/screen/景家.png"
image jiance = "images/screen/向外看.png"
image zaigebi = im.FactorScale("images/screen/在隔壁.png",1.42)
image jingshu = im.FactorScale("images/screen/警署.png",1.1)
image pojiudalou = im.FactorScale("images/screen/破旧大楼.png",1.42)
image posui = im.FactorScale("images/screen/侵蚀破碎.png",1.42)
image weishengjian = im.FactorScale("images/screen/卫生间.png",1.38)
image shuangrenchuang = "images/screen/双人床.png"
image shuangrenchuangye = "images/screen/双人床1.png"
image shuangrenchuangchen = "images/screen/双人床2.png"
image jingjie = "images/screen/镜中世界密布.png"
image jingjiebengsui = "images/screen/镜中世界崩碎.png"
image jingjiebengsui1 = "images/screen/镜中世界崩碎1.png"
image jingjiebijin = "images/screen/镜中世界-景的逼近.png"
image weisuo = "images/screen/未堰的研究室.png"
image lingyitiaolu = "images/screen/另一条路.png"
image guizi = "images/screen/倒下的柜子.png"
image cuihua = "images/screen/脆化.png"
image canhai = "images/screen/残骸.png"
image weiwan = im.FactorScale("images/screen/未完成.png",1.38)
image jiyi = im.FactorScale("images/screen/如果有记忆.png",1.38)
image dianhua = im.FactorScale("images/screen/未知的电话.png",1.38)
image zhankai = im.FactorScale("images/screen/境界展开.png",1.38)

# 游戏在此开始。

label splashscreen:
    show game0 with fade
    with Pause(0.2)
    return

define config.fade_music = 0.5

label start:
    stop music

    # 显示一个背景。此处默认显示占位图，但您也可以在图片目录添加一个文件
    # （命名为 bg room.png 或 bg room.jpg）来显示。

    scene game0

    # 显示角色立绘。此处使用了占位图，但您也可以在图片目录添加命名为
    # eileen happy.png 的文件来将其替换掉。

    show lin at left
    with dissolve
    # 此处显示各行对话。

    "本作是个人向同人作品。"

    show die at right

    "内容不免OOC，还望谅解。"

    scene jiyi with fade

    play music dia_babel

    # nvl clear

    """

    “你叫什么名字？”

    “安特-博古。”

    “不！你叫做林。”

    “不要。”

    “嘶，嘶嘶嘶~”

    “你叫什么名字。”

    “安特……”

    “嘶，嘶嘶嘶~”

    “你叫什么名字？”
    
    “林。”

    """

    jump 镜中之人01

    return
