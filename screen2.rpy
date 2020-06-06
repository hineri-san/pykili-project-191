screen textstyle():
    frame:
        textbutton "Danger":
            text_color "#c04040"


style example_button is default:
    idle_background Frame('paper.png')
    hover_background Frame('paper.png')
    xalign 0.5 ypos 0.5
    xsize 150 ysize 50
style example_button_text:
    xalign 0.5
    color "404040"
    hover_color "4040c0"
style example_text:
    color "404040"
style padded_button is example_button:
    background 'paper.png'
    xpadding 40
    ypadding 20
style margin_button is padded_button:
    ymargin 20
screen buttons1():
    style_prefix "example"
    frame:
        xalign 0.5 ypos 250
        background Frame('paper1.png')
        xsize 300 ysize 300
        vbox:
            spacing 10
            text('"НККРЯ"'):
                xpos 100 ypos 100
            textbutton('Ясно'):
                xpos 150 ypos 175
                action Return(True)
screen mirror():
    style_prefix "example"
    frame:
        xalign 0.3 yalign 0.3
        background Frame('paper.png')
        xsize 200 ysize 50
        vbox:
            text("Зеркало"):
                xpos 0.5 ypos 0.3
screen buttons2():
    style_prefix "example"
    frame:
        xalign 0.5 yalign 0.25
        background Frame('paper1.png')
        xsize 900 ysize 400
        vbox:
            spacing 10
            text('Поздравляем! Нам не удалось вас слить. \nЧасть объектов в комнате кликабельна - жмите на кнопки \nи решайте, устроится ли честный программист на работу.'):
                size 20
                xpos 130 ypos 150
            textbutton('Ясно'):
                xpos 450 ypos 195
                action Return(True)

screen imagemap_ex():
    imagemap:
        idle "bg komnata7"
        hover "bg komnata7"

        hotspot(63, 294, 145, 40) action  Jump("televizor")
        hotspot(320, 560, 154, 46) action Jump("shoroh")
        hotspot(633, 451, 154, 43) action Jump("podushka")
        hotspot(1076, 229, 178, 46) action Jump("veshalka")
        hotspot(978, 637, 172, 52) action Jump("polovitsy")


screen imagemap_podushki_net():
    imagemap:
        idle "bg komnata7"
        hover "bg komnata7"

        hotspot(63, 294, 145, 40) action  Jump("televizor")
        hotspot(320, 560, 154, 46) action Jump("shoroh")
        hotspot(1076, 229, 178, 46) action Jump("veshalka")
        hotspot(978, 637, 172, 52) action Jump("polovitsy")

screen okno1():
    imagemap:
        idle "okno3"
        hover "okno3"

        hotspot(446, 260, 142, 49) action  Jump("okno1")

screen okno2():
    imagemap:
        idle "okno3"
        hover "okno3"

        hotspot(446, 260, 142, 49) action  Jump("kot")



screen buttons3():
    style_prefix "example"
    frame:
        xalign 0.5 yalign 0.25
        background Frame('paper1.png')
        xsize 900 ysize 400
        vbox:
            spacing 10
            text(tolstoy):
                size 20
                xpos 130 ypos 150
            textbutton('Ясно'):
                xpos 450 ypos 195
                action Return(True)

screen buttons4():
    style_prefix "example"
    frame:
        xalign 0.5 yalign 0.25
        background Frame('paper1.png')
        xsize 1000 ysize 500
        vbox:
            spacing 10
            text(dikkens):
                size 15
                xpos 130 ypos 125
            textbutton('Ясно'):
                xpos 500 ypos 195
                action Return(True)
screen imagemap_karta:
    imagemap:
        idle "bg karta"
        hover "bg karta"

        hotspot(126, 278, 279, 367) action Jump("zerkalo")
        hotspot(634, 38, 348, 224) action Jump("tv")
        hotspot(734, 377, 443, 290) action Jump("kniga")

screen nkkra():
    style_prefix "example"
    frame:
        xalign 0.5 yalign 0.25
        background Frame('paper1.png')
        xsize 1500 ysize 1000
        vbox:
            spacing 10
            text(nkkra):
                size 15
                xpos 100 ypos 125
            textbutton('Ясно'):
                xpos 500 ypos 195
                action Return(True)

screen viewport_test:
    side "c b r":
        area (89, 54, 1102, 619)
        viewport id "vp":
            draggable True
            frame:
                xalign 0.3 yalign 0.25
                background('#F7E989')
                xysize(1500, 1000)
                vbox:
                    spacing 10
                    text(nkkra):
                        color '4E380F'
                        size 20
                        xpos 70 ypos 105
                    textbutton('Ясно'):

                        xpos 500 ypos 195
                        action Return(True)
        bar value XScrollValue("vp")
        vbar value YScrollValue("vp")
screen the_end:
    style_prefix "example"
    frame:
        xalign 0.5 yalign 0.25
        background Frame('paper1.png')
        xsize 900 ysize 400
        vbox:
            spacing 10
            text('Наша команда разработчиков поздравляет Вас с прохождением игры! Вот бы все программисты так находили работу, не правда ли?\Надеемся, что вам понравилось!'):
                size 10
                xpos 130 ypos 150
            textbutton('Ясно'):
                xpos 450 ypos 195
                action Return(True)
