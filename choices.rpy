#приключения с подушкой

label osmotret:
    "Обычная такая подушка. Странные мысли спросонья в голову лезут."
    jump podushka
label pomyat:
    "Вылезшее из подушки перо укололо меня в палец."
    "Перо было необычное - красное и блестящее."
    "Я моргнул и оно исчезло. Палец болеть не перестал."
    jump podushka
label ponuhat:
    "Пахло пылью и сыростью."
    p "Еще скажи: пожевать."
    $ ponuhatb=True
    jump podushka
label shwyrnut:
    "Бубнеж голос продолжился, но я ничего толком не смог расслышать."
    "Разозлившись, я швырнул подушку в темноту."
    "Голоса обиженно примолкли."
    p"Да-а, что только спросонья не прислышится."
    $ shwyrnutb = True
    jump shwyrnut_done
label golosa1:
    "Ответом мне послужило надменное молчание."
    "...И через несколько секунд снова начался еле различимый бубнеж."
    jump imagemap_ex
label shwyrnut_done:
    $ podushkadone=True
    "Подушка исчезла."
    jump imagemap_pn_done
label imagemap_pn_done:
    call screen imagemap_podushki_net

#приключения с углами
label okryknut:
    "Шебуршание прекратилось."
    "...Но ненадолго."
    p"Никакого уважения."
    jump shoroh
label proverit:
    "Я встал с дивана и заглянул в неспокойный угол."
    p"Странно."
    "В углу не было ничего, кроме большой картины."
    p"Это что, половцы?"
    "..."
    p"Ладно, ловить тут больше нечего."
    jump shoroh

#приключения с вешалкой
#приключение с ухой
label tolstoy:
    "Откуда-то из недр подсознания всплыло: 'И подавались ему обычные в трактирах блюда...'"
    "''Кислые щи, мозги с горошком, огурец соленый...'"
    "Я сглотнул."
    p "Может, почитать?"
    jump tolstoy1
label dikkens:
    "В комнате резко запахло омарами. Интересно, почему я в жизни никогда их не пробовал?"
    p "Или, скажем, устриц."
    p "У Диккенса все едят устриц."
    "Я сглотнул."
    p "Может, почитать?"
    jump dikkens1
label tolstoy1:
    "Это было 'Хмурое утро' Алексея Толстого."
    p "Что ж, теперь точно усну."
    "Я открыл наугад."
    python:
        tolstoy=[]
        f = open(renpy.loader.transfn("resources/tolstoy.txt"),"r")
        for line in f:
            tolstoy.append(line)
        f.close()
    call screen buttons3
    "Мда-а."
    jump nakormily

label dikkens1:
    p "Чарльз Диккенс: Избранные письма."
    p"Если и там о еде, то я не выдержу."
    "Я открыл наугад."
    python:
        dikkens=[]
        f = open(renpy.loader.transfn("resources/dikkens.txt"),"r")
        for line in f:
            dikkens.append(line)
        f.close()
    call screen buttons4
    "Мда-а."
    jump nakormily
