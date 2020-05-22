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


screen imagemap_podushki_net():
    imagemap:
        idle "bg komnata7"
        hover "bg komnata7"

        hotspot(63, 294, 145, 40) action  Jump("televizor")
        hotspot(320, 560, 154, 46) action Jump("shoroh")
        hotspot(1076, 229, 178, 46) action Jump("veshalka")


screen okno1():
    imagemap:
        idle "bg komnata8"
        hover "bg komnata8"

        hotspot(63, 294, 145, 40) action  Jump("okno1")

screen okno2():
    imagemap:
        idle "bg komnata8"
        hover "bg komnata8"

        hotspot(63, 294, 145, 40) action  Jump("kot")
