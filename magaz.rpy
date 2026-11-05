init python:

    def narr(event, **kwargs):
        if event == "show":
            renpy.music.play("audio/magaz/narr.wav", channel="sounds_m", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sounds_m", fadeout=0.3)

    def eii(event, **kwargs):
        if event == "show":
            renpy.music.play("audio/magaz/eii.wav", channel="sounds_m", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sounds_m", fadeout=0.3)

    def treska(event, **kwargs):
        if event == "show":
            renpy.music.play("audio/magaz/treska.ogg", channel="sounds_m", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sounds_m", fadeout=0.3)
    

init:

    $ ddpm = ImageDissolve(im.Tile("str/magaz/transmask.png"), 0.5, 0.5)
    
    image nm = "str/magaz/nm.png"
    
    image 1 = "str/magaz/1.png"
    image 2 = "str/magaz/2.png"
    image 3 = "str/magaz/3.png"
    image 4 = "str/magaz/4.png"
    image 5 = "str/magaz/5.png"
    image 6 = "str/magaz/6.png"
    image 7 = "str/magaz/7.png"
    image 8 = "str/magaz/8.png"
    image 9 = "str/magaz/9.png"
    image 10 = "str/magaz/10.png"
    image 11 = "str/magaz/11.png"
    image 12 = "str/magaz/12.png"
    image 13 = "str/magaz/13.png"
    image 14 = "str/magaz/14.png"
    image 15 = "str/magaz/15.png"
    
    define nm = Character(None, window_background=None, what_xpos=400, what_ypos=80, what_color='#7d128d')
    define mm = Character(None, window_background=None, what_xpos=400, what_ypos=80, what_color='#7d128d', callback=eii)
    define ggm = Character(None, window_background=None, what_xpos=400, what_ypos=80, what_color='#7d128d', callback=narr)
    define trm = Character(None, window_background=None, what_xpos=400, what_ypos=80, what_color='#7d128d', callback=treska)
    
label magaz:
    
    $ achievement.grant("Achievement01_magaz1")
    init:
        $ achievement.register("Achievement01_magaz1")
        $ achievement.sync()

    $ achievement.sync()
    
    $ change_cursor("no")
    
    show nm
    
    $ renpy.pause(3, hard=True)
    
    play music "audio/magaz/magaz1.mp3"
    
    show 1 with ddpm
    
    $ renpy.pause(3, hard=True)
    
    nm"Я просыпаюсь на деревянной лавке; перед глазами - узкая и слабо освещенная аллея. До боли знакомая дорога... где же я могла ее видеть?"
    trm"- Ну наконец-то..."
    
    hide 1 with ddpm
    $ renpy.pause(1, hard=True)
    show 2 with ddpm
    
    nm"Сбоку разносится голос. Я поворачиваюсь и вижу перед собой мальчика с крайне странным выражением лица."
    
    hide 2 with ddpm
    $ renpy.pause(1, hard=True)
    scene 3 with ddpm
    
    trm"- Ты опоздала!"
    scene 4
    ggm"- Эм-м-м... а ты кто?" 
    nm"Мальчик удивленно моргнул."
    scene 3
    trm"- Так мы с тобой далеко не уйдем. Попробуй заново."
    nm"Затем он набирает полную грудь воздуха."
    trm"- Ты! Опоздала!"
    scene 4
    nm"Я непонимающе смотрю на него. Он непонимающе смотрит на меня." 
    ggm"- И-извини?.."
    scene 3
    nm"Мальчик довольно кивнул."
    trm"- Вот, уже лучше."
    trm"- Имя-то у тебя есть? Меня вот Треской звать!"
    scene 4
    nm"Я оценивающе оглядываю наглеца. Совсем маленький, а уже лезет с такими вопросами!"
    ggm"- Не твое дело..."
    ggm"- И вообще!.. Мне кто-нибудь скажет, что я тут делаю?"
    scene 3
    trm"- Эй, это невежливо! Будто тут есть кто-то еще..."
    scene 4
    nm"..."
    scene 3
    trm"- Тебе совсем ничего не рассказали? Вот я все знаю, например!"
    scene 4
    ggm"- О чем?"
    scene 3
    trm"- Ты обязана проводить меня в магазин!"
    nm"После этих слов Треска встал в победную позу."
    scene 4
    ggm"- Еще чего..."
    scene 3
    trm"- Ты ведь понимаешь, что отказ не принимается?"
    scene 4
    ggm"- Многовато ты о себе возомнил."
    scene 3
    trm"- Я серьезно." 
    trm"- Это, как бы, не мне решать."
    trm"- Думаешь, я в восторге от такой компании?"
    scene 4
    nm"Какой-то он странный. То веселый, то грустный, то громкий, то тихий. Ненормальный какой-то. И имя дурацкое."
    scene 3
    trm"- Мы идем или как?"
    scene 4
    ggm"- Ты иди, а мне подумать надо."
    scene 3
    trm"- Я бы с радостью, да только дороги не знаю..."
    nm"Треска хитро улыбается. Я с досадой кусаю губы."
    scene 4
    ggm"- Буду с тобой честна - ты мне совсем не нравишься."
    nm"В ответ он лишь заливается смехом."
    show nm
    show 3
    
    trm"- Зато ты мне - очень!" 
    nm"После этого он с уверенностью хватает меня за руку - я и рта не успеваю открыть."
    trm"- Веди!"
    
    stop music fadeout 2
    
    show nm
    
    hide 3 with ddpm
    $ renpy.pause(1, hard=True)
    
    play music "audio/magaz/magaz4.mp3"
    
    show 5 with ddpm
    
    nm"Дорога до магазина прошла нормально, если не считать того, что Треска шел заметно быстрее." 
    nm"И наоборот - в какие-то моменты он резко останавливался и начинал идти назад, внимательно глядя себе под ноги." 
    nm"В итоге дорога заняла гораздо больше времени, чем могла бы."
    
    hide 5 with ddpm
    $ renpy.pause(1, hard=True)
    show 6 with ddpm
    
    nm"Оказавшись у дверей магазина, мы видим перед собой вывеску."
    nm"'Магазин закрывается через 20 минут!'"
    ggm"- И взбрело же кому-то в голову таким образом обозначить часы работы своего магазина..."
    trm"- Наверно, у них для этого специальный человек есть. Каждые пять минут бегает и меняет табличку. Удобно же!"
    ggm"- Шутишь, что ли?"
    trm"- Да!"
    ggm"- До чего же ты надоедливый..."
    trm"- Всяко лучше, чем быть занудой! Тебе, кстати, лет-то сколько?"
    ggm"- Не твое дело."
    trm"- А-а-а... а зовут как?"
    ggm"- Не твое дело!"
    nm"Я уже готова была дать мелкому поганцу подзатыльник, как вдруг за стеклом появляется жуткого вида человек. В руках он держит картонную табличку с надписью 'До закрытия магазина 15 минут!'"
    trm"- Пойдем, чего стоишь?"
    ggm"- А? Д-да..."
    
    stop music fadeout 2
    
    hide 6 with ddpm
    $ renpy.pause(1, hard=True)
    show 7 with ddpm
    
    play music "audio/magaz/magaz2.mp3"
    
    nm"В очередной раз проходя мимо длинного ряда с консервными банками, мы поняли, что заблудились."
    ggm"- Поверить не могу, что ты не знаешь, где продается молоко."
    trm"- Я... эм-м-м..."
    ggm"- Может, спросим кого-нибудь?"
    trm"- Давай!"
    ggm"- Эй, постой!.."
    nm"Треска отпустил мою руку и уверенно зашагал к одному из немногочисленных посетителей магазина. Тот стоял спиной к нам, что-то сосредоточенно рассматривая на прилавке."
    trm"- Здрасьте, а можно!.."
    nm"Последнюю часть вопроса я не расслышала - как и ответ на него. Но мой непутевый друг внезапно застыл как вкопанный, глядя прямо в глаза посетителя магазина. Я поспешила подойти к ним."
    
    hide 7 with ddpm
    $ renpy.pause(1, hard=True)
    show 8 with ddpm
    
    mm"- Это ваш?" 
    nm"Посетитель обратился ко мне. В его голосе явно слышалось отвращение, а на лице застыла презрительная гримаса."
    
    stop music fadeout 2
    
    hide 8 with ddpm
    $ renpy.pause(1, hard=True)
    
    play music "audio/magaz/magaz3.mp3"
    
    show 9 with ddpm
    
    ggm"- Я...  эм-м..."
    mm"- Если так, то будьте добры - уберите его подальше." 
    ggm"- Д-да, извините..."
    nm"Я хватаю Треску за руку и спешу увести в сторону - тот все глядит на посетителя, открыв рот и выпучив глаза. И дрожит." 
    
    stop music fadeout 2
    
    hide 9 with ddpm
    $ renpy.pause(1, hard=True)
    show 7 with ddpm
    
    play music "audio/magaz/magaz2.mp3"
    
    nm"Лишь когда мы свернули за угол, Треска успокоился." 
    ggm"- Ну и как это понимать?" 
    trm"- Я... я так перепугался!.. Он сказал..." 
    ggm"- Что?"
    trm"- НЕТ, ТОЛЬКО НЕ ОПЯТЬ!" 
    nm"Внезапно Треска завопил как сумасшедший. Я зажимаю ему рот ладонью; его лицо буквально горит, а сам он плачет." 
    ggm"- Ты можешь вести себя нормально?" 
    trm"- Т-ты не понимаешь..." 
    ggm"- Ну конечно, что я вообще могу понимать!" 
    ggm"- Вот только приставать к людям - это неправильно. Этого, видимо, не понимаешь ты." 
    trm"- Ты злая!.. Хнык.." 
    ggm"- Я?.."
    
    hide 7 with ddpm
    $ renpy.pause(1, hard=True)
    show 10 with ddpm
    
    nm"Оттолкнув меня, Треска убежал прочь."
    
    stop music fadeout 2
    
    hide 10 with ddpm
    $ renpy.pause(1, hard=True)
    show 7 with ddpm
    
    ggm"- Блин."
    nm"Краем глаза я замечаю, как работник магазина вешает на дверь новую табличку."
    
    hide 7 with ddpm
    $ renpy.pause(1, hard=True)
    
    play music "audio/magaz/magaz6.mp3"
    
    show 11 with ddpm
    
    ggm"- Вот ты где!" 
    nm"Я встречаю Треску у кассы. До этого я успела сбегать в молочный отдел, предварительно узнав, где он находится."
    mm"- Эй, шевелись!" 
    nm"Недовольный голос раздался с конца длинной очереди, что образовалась позади Трески. Я протискиваюсь к нему." 
    ggm"- Что случилось?" 
    nm"Мальчик не отвечает. Смотрит себе под ноги, едва слышно хныкая, а кассир коршуном нависает над ним. Между ними лежит пакет молока." 
    mm"- Это ваш?" 
    ggm"- Мой." 
    mm"- В следующий раз оставьте его дома." 
    nm"Люди в очереди согласно кивают." 
    mm"- Оплатите стоимость товара." 
    ggm"- Да, конечно..." 
    mm"- И издержку за ожидание!" 
    ggm"- Ч-что?" 
    mm"- Вы слышали." 
    ggm"- Я-то слышала, но это же неслыханно!"
    
    hide 11
    show 12
    
    nm"Вдруг Треска начинает хихикать." 
    mm"- И за то, что ваш сын придурок, тоже заплатите!" 
    ggm"- Н-но..."
    mm"- Вы слышали." 
    ggm"- Знаете, что?!.." 
    nm"В гневе я бросаю кассиру смятую купюру гораздо большего номинала, чем требовалось - даже с учетом всех идиотских надбавок - хватаю пакет молока и круто разворачиваюсь."
    ggm"- Мы уходим, Треска!"
    
    stop music fadeout 2
    
    hide 12 with ddpm
    $ renpy.pause(1, hard=True)
    
    play music "audio/magaz/magaz4.mp3"
    
    show 13 with ddpm
    
    nm"Всю дорогу из магазина мы шли молча. В какой-то момент мы незаметно для себя свернули вправо и оказались у автозаправки - тогда-то Треска и решил нарушить молчание."
    trm"- Любишь мороженое?"
    ggm"- Нет."
    trm"- Ладно..."
    nm"Я смотрю в поникшее лицо мальчика - на секунду в его глазах блеснул огонек и тут же погас."
    trm"- Знаешь..."
    nm"Он уверенно сворачивает с тропы прямо на автомобильную дорогу. Я провожаю его недоуменным взглядом."
    
    hide 13 with ddpm
    $ renpy.pause(1, hard=True)
    show 14 with ddpm
    $ renpy.pause(1, hard=True)
    hide 14 with ddpm
    $ renpy.pause(1, hard=True)
    show 15 with ddpm
    
    $ renpy.pause(2, hard=True)
    
    trm"- Похоже, ты мне совсем не помогаешь."
    nm"В глазах Трески вновь блестит озорной огонек..."
    
    hide 15
    
    stop music

    jump arxe

