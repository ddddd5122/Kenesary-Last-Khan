# Кейіпкерлерді анықтау
define a = Character("Асанали")
define k = Character("Кенесары")
define zb = Character("Жанқожа")
define nb = Character("Наурызбай")
define ab = Character("Ағыбай батыр")
define bp = Character("Бопай")

default unity = 50
default economy = 45
default army = 60
default treasury = 30
default external_pressure = 70

default encyclopedia_characters_unlocked = {
    "Кенесары": False,
    "Жанқожа": False,
    "Ағыбай батыр": False,
    "Наурызбай": False,
    "Бопай": False,
    "Абылай-хан": False,
}

init python:
    def is_character_unlocked(name):
        return encyclopedia_characters_unlocked.get(name, False)

    def unlock_character(name):
        if name in encyclopedia_characters_unlocked and not encyclopedia_characters_unlocked[name]:
            encyclopedia_characters_unlocked[name] = True
            renpy.show_screen("character_unlock_notification")

# Кейіпкерлер суреттері
image kenesary_khan = "images/characters/kenesary_khan.png"
image agybai_batyr = "images/characters/agybai_batyr.png"
image nauryzbai_batyr = "images/characters/nauryzbai_batyr.png"
image bopai = "images/characters/bopai.png"
image zhankozha = "images/characters/zhankozha.png"
image bg_1 = "images/bg/bg-1.jpg"
image bg_1_2 = "images/bg/bg-1_2.jpg"
image bg_2 = "images/bg/bg-2.jpg"
image bg_2_2 = "images/bg/bg-2-2.png"
image bg_3 = "images/bg/bg-3.png"
image bg_4 = "images/bg/bg-4.png"
image agybai = "images/characters/agybai.png"

# Фондық суреттер (толық экранға созылған)
transform fullscreen_bg:
    xysize (config.screen_width, config.screen_height)
    
image bg_1 = Transform("images/bg/bg-1.jpg", xysize=(config.screen_width, config.screen_height))
image bg_1_2 = Transform("images/bg/bg-1_2.jpg", xysize=(config.screen_width, config.screen_height))
image bg_2 = Transform("images/bg/bg-2.jpg", xysize=(config.screen_width, config.screen_height))
image bg_2_2 = Transform("images/bg/bg-2-2.png", xysize=(config.screen_width, config.screen_height))
image bg_3 = Transform("images/bg/bg-3.png", xysize=(config.screen_width, config.screen_height))

# Ойынның басталуы - басты мәзірді көрсету үшін қайта анықталған
# Ren'Py-де label start автоматты түрде шақырылуы мүмкін, сондықтан оны мәзірге бағыттаймыз
label start:
    # Басты мәзірді көрсетеміз
    call screen main_menu
    return

# Ойынның шынайы басталуы - "Жаңа ойын" түймесімен шақырылады
label start_game:
        
    # HUD және жылдам мәзірді тек ойын кезінде көрсетеміз
    $ renpy.show_screen("stats_hud")
    $ renpy.show_screen("quick_menu")
    
    scene black
    with fade

    $ renpy.music.set_volume(0.08, delay=0.0, channel="music")
    play music "voices/music/Steppe_Serenity.mp3"
    play sound "voices/sounds/Звук ветра в природе пустыня степь.mp3" loop

    window show

    "..."

    stop sound fadeout 1.0

    scene bg_1_2
    with fade

    $ unlock_character("Кенесары")

    voice "<from 0.0 to 3.192>voices/kh-1-2.mp3"
    k "{cps=25}Абылай атамыз да дәл осылай тұрған еді.{/cps}"

    voice "<from 3.192 to 6.885>voices/kh-1-2.mp3"
    k "{cps=25}Осы далаға қарап, осы жұлдыздарға көз тіккен.{/cps}"

    voice "<from 6.885 to 12.493>voices/kh-1-2.mp3"
    k "{cps=25}Бірақ оның заманы басқа еді... ол кезде жеңіске сенуге болатын.{/cps}"

    voice "<from 12.493 to 21.277>voices/kh-1-2.mp3"
    k "{cps=25}Жоңғар... ол соғыста талқандап, бейбітшілікке көндіріп, таудың арғы жағына қуып тастайтын жау.{/cps}"

    voice "<from 21.277>voices/kh-1-2.mp3"
    k "{cps=25}Ал Ресей... Ресей шегінуді білмейд. Ол бір келсе, МӘҢГІЛІККЕ қалады.{/cps}"

    "{cps=25}...{/cps}"

    voice "<from 0.0 to 6.536>voices/kh-2-2.mp3"
    k "{cps=25}Әкем келісімге келмек болды. Жылдар бойы оның қалай жасығанын, өз көзіммен көрдім.{/cps}"

    voice "<from 6.536 to 10.919>voices/kh-2-2.mp3"
    k "{cps=25}Қадам сайын жол беріп, ақыры одан тек есімі ғана қалды.{/cps}"

    voice "<from 10.919 to 15.409>voices/kh-2-2.mp3"
    k "{cps=25}МЕН ӨЗІМЕ СЕРТ БЕРДІМ. Менің тағдырым бұлай болмайды.{/cps}"

    voice "<from 15.409>voices/kh-2-2.mp3"
    k "{cps=25}Не бұл дала біздікі болады, не мен бұл дүниеде болмаймын...{/cps}"

    voice "<from 0.0 to 2.235>voices/kh-3.mp3"
    k "{cps=25}Бүгін олар ханды таңдайды.{/cps}"

    voice "<from 2.235 to 6.024>voices/kh-3.mp3"
    k "{cps=25}Мені таңдайды... Мен дайын болуым керек.{/cps}"

    voice "<from 6.024 to 10.056>voices/kh-3.mp3"
    k "{cps=25}Билікке емес, биліктен кейін келетін сынаққа.{/cps}"

    voice "<from 10.056>voices/kh-3.mp3"
    k "{cps=25}Биліктің менің өзімнен не сұрайтынына дайын болуым керек{/cps}"

    show kenesary_khan at kenesary_center

    voice "voices/kh-4.mp3"
    k "{cps=25}Ал, ендеше... Ханын күткен елге барайық{/cps}"

    stop music fadeout 2.0
    scene black
    with fade
    stop music

    window hide

    play sound "<from 0.0 to 2.259>voices/d-1.mp3"

    show text "1841 ЖЫЛЫ" at truecenter
    pause
    if renpy.is_skipping():
        stop sound

    play sound "<from 2.259 to 4.041>voices/d-1.mp3"

    show text "ҚЫРКҮЙЕК" at truecenter
    pause
    if renpy.is_skipping():
        stop sound

    play sound "<from 4.041 to 5.630>voices/d-1.mp3"

    show text "КӨКШЕТАУ ДАЛАСЫ" at truecenter
    pause
    if renpy.is_skipping():
        stop sound

    play sound "<from 5.630>voices/d-1.mp3"

    show text "ҮШ ЖҮЗДІҢ ҚҰРЫЛТАЙЫ" at truecenter
    pause
    if renpy.is_skipping():
        stop sound

    hide text

    stop sound fadeout 1.0

    window auto

    scene bg_2_2
    with fade

    "{cps=25}...{/cps}"

    show kenesary_khan at kenesary_center

    voice "<from 0.0 to 4.087>voices/kh-5.mp3"
    k "{cps=25}Сендер мені ақ киізге көтеріп, хан сайладыңдар.{/cps}"

    voice "<from 4.087 to 9.774>voices/kh-5.mp3"
    k "{cps=25}Демек... бұдан былай мен сендердің әрқайсысың үшін жауаптымын.{/cps}"

    voice "<from 9.774 to 14.033>voices/kh-5.mp3"
    k "{cps=25}Ал сендер — менің алдымда жауаптысыңдар.{/cps}"

    voice "<from 14.033>voices/kh-5.mp3"
    k "{cps=25}Бұл той емес... БҰЛ — СЕРТ!{/cps}"

    play sound "voices/sounds/Хлопки в ладоши небольшой группы человек.mp3"
    "{cps=25}...{/cps}"

    stop sound fadeout 1.0

    voice "<from 0.0 to 9.893>voices/kh-6.mp3"
    k "{cps=25}Ресей жаңа бекіністер салып жатыр... Ақтау, Ақмола приказы, Ұлытау. Әр бекініс — бізге құрылған жаңа ҚАҚПАН.{/cps}"

    voice "<from 9.893 to 16.106>voices/kh-6.mp3"
    k "{cps=25}Олар бізбен қылышпен емес... қағазбен, шекарамен, салықпен соғысуда.{/cps}"

    voice "<from 16.106 to 22.272>voices/kh-6.mp3"
    k "{cps=25}Біз жайылым үшін таласып жүргенде, олар картаға жаңа сызықтар сызып жатыр.{/cps}"

    voice "<from 22.272>voices/kh-6.mp3"
    k "{cps=25}Сосын келіп «Міне — шекара... Оның арғы жағы енді сендердікі емес», дейді{/cps}"

    voice "<from 0.0 to 5.361>voices/kh-7.mp3"
    k "{cps=25}Әскерді асырау керек. Мылтық сатып алу керек. Барлаушыларды ұстау керек...{/cps}"

    voice "<from 5.361 to 11.272>voices/kh-7.mp3"
    k "{cps=25}Мен ЗЕКЕТ туралы айтып тұрмын... әр рудан алынатын әскери салық.{/cps}"

    voice "<from 11.272>voices/kh-7.mp3"
    k "{cps=25}Бұл сөздің қазір ешкімге ұнамайтынын білемін...{/cps}"

    play sound "voices/sounds/zvuk-tolpy-ljudej.mp3"
    "{cps=25}...{/cps}"
    stop sound fadeout 1.0

    voice "voices/kh-8.mp3"
    k "{cps=25}Айтыңыздар... не қалайсыздар?... Мен тыңдап тұрмын.{/cps}"

    show kenesary_khan at kenesary_mirror_left
    show zhankozha at zhankozha_right

    $ unlock_character("Жанқожа")

    "{cps=25}...{/cps}"

    voice "<from 0.0 to 8.911>voices/zb-1.mp3"
    zb "{cps=25}Хан ием... Елың сены ақ киызге көтергеныне дән риза, бұл орын саған ата қаныңмен бұйырған.{/cps}"

    voice "<from 8.911 to 16.340>voices/zb-1.mp3"
    zb "{cps=25}Бырақ зекет... Зекет — ауыр сөз. Өткен қыстағы жұт халықтың малын қырды.{/cps}"

    voice "<from 16.340 to 21.767>voices/zb-1.mp3"
    zb "{cps=25}Оның алдындағы қуаңшылық тағы бар. Елдың тынысы әрең шығып тұр.{/cps}"

    voice "<from 21.767>voices/zb-1.mp3"
    zb "{cps=25}Бұл салық... онсыз да жүгы ауыр түйеның белын үзып кететын соңғы шөмшек болып жүрмей ме?{/cps}"

    menu:
        "Әр тиын қаруға жұмсалады. Билер кеңесі алдында есеп беремін":
            voice "<from 0.0 to 6.942>voices/kh-9.mp3"
            k "{cps=25}Жанқожа бидыкы жөн. Өткен қыс қатал болды, оны былемын. Сондықтан тыке айтамын...{/cps}"

            voice "<from 6.942 to 13.562>voices/kh-9.mp3"
            k "{cps=25}Зекеттың әр тиыны қару мен оқ-дәрыге жұмсалады. Басқа ештеңеге емес!{/cps}"

            voice "<from 13.562 to 17.079>voices/kh-9.mp3"
            k "{cps=25}Билер кеңесы әр шығынды көрып отырады.{/cps}"

            voice "<from 17.079>voices/kh-9.mp3"
            k "{cps=25}Егер осы сөзымнен тайсам, мені осы ақ киызден қайта түсыруге хақыларыңыз бар!{/cps}"

            voice "voices/zb-2.mp3"
            zb "{cps=25}Көрейык... хан ием... Көрейык.{/cps}"

        "Зекет төлемеген — Ресей жағында. Үшінші жол жоқ!":
            voice "<from 0.0 to 9.513>voices/kh-10.mp3"
            k "{cps=25}Жанқожа би. Мен сені естіп тұрмын. Сен түйе мен соңғы шөмшек туралы айттың. Ал мен саған басқа түйе туралы айтайын...{/cps}"

            voice "<from 9.513 to 24.364>voices/kh-10.mp3"
            k "{cps=25}Ресей сенің жайылымыңнан екі күндік жерге бекініс салып жатыр. Бес жылдан соң сенің немерелерің зекетті маған емес... жұт пен қуаңшылықты білмейтін орыс шенеунігіне төлейтін болады.{/cps}"

            voice "<from 24.364>voices/kh-10.mp3"
            k "{cps=25}Зекет — бұл шөмшек қана. Ал оның орнына келетін дүние — тас.{/cps}"

            "{cps=25}...{/cps}"

        "Бұл салық емес — қан қарызы. Әр бай он атты сарбаз шығарсын!":
            voice "<from 0.0 to 6.577>voices/kh-11.mp3"
            k "{cps=25}Жақсы. Мен сені естідім, Жанқожа би. Онда бұл — салық емес. Бұл — борыш.{/cps}"

            voice "<from 6.577 to 18.953>voices/kh-11.mp3"
            k "{cps=25}Бізді асырап отырған ұлы дала алдындағы әр рудың борышы. Он еркегі бар әр бай — он атты сарбаз шығарсын. Атымен, қаруымен, бір айлық азығымен.{/cps}"

            voice "<from 18.953>voices/kh-11.mp3"
            k "{cps=25}Ешқандай ақша, ешқандай есеп-қисапсыз. Түсінікті әрі әділ.{/cps}"

            play sound "voices/sounds/zvuk-tolpy-ljudej.mp3"
            "{cps=25}*топтағы қуаныш*{/cps}"
            stop sound fadeout 1.0

    scene black
    with fade

    scene bg_3
    with fade

    show kenesary_khan at kenesary_edge_left

    "{cps=25}...{/cps}"

    play sound "voices/sounds/topot_horse.mp3" loop
    "{cps=25}*аттың тұяғы*{/cps}"
    stop sound

    play sound "voices/sounds/zvuk_hodb1.mp3" loop
    "{cps=25}*жүріс дыбысы*{/cps}"
    stop sound

    show agybai at agybai_right

    $ unlock_character("Ағыбай батыр")

    voice "<from 0.0 to 3.12>voices/ab-1-2.mp3"
    ab "{cps=25}Хан ием! Орыс жасағы келе жатыр.{/cps}"

    voice "<from 3.12 to 8.248>voices/ab-1-2.mp3"
    ab "{cps=25}Ақмола бекінісінен шыққан үш жүз атты әскер... екі зеңбірегі бар.{/cps}"

    voice "<from 8.248>voices/ab-1-2.mp3"
    ab "{cps=25}Таң ата осында болады.{/cps}"

    voice "voices/kh-12.mp3"
    k "{cps=25}Олар Құрылтай туралы білген бе?{/cps}"

    voice "voices/ab-2.mp3"
    ab "{cps=25}Солай, хан ием.{/cps}"

    voice "voices/kh-13.mp3"
    k "{cps=25}Демек... арамызда... хабар жеткізген сатқын бар.{/cps}"

    show nauryzbai at nauryzbai_center

    $ unlock_character("Наурызбай")

    voice "<from 0.0 to 6.965>voices/nb-1-2.mp3"
    nb "{cps=25}Ендеше... соғысты кеше бастау керек еді! Олар жолда келе жатқанда... таң атпай соққы береміз!{/cps}"

    voice "<from 6.965 to 10.722>voices/nb-1-2.mp3"
    nb "{cps=25}Қостарын тігіп... зеңбіректерін оқтауға мұрша бермейміз!{/cps}"

    voice "<from 10.722>voices/nb-1-2.mp3"
    nb "{cps=25}Түн қараңғысында...{/cps}"

    show nauryzbai at nauryzbai_shift_right_132
    show bopai at bopai_center

    $ unlock_character("Бопай")

    voice "voices/bp-1.mp3"
    bp "{cps=25}Ал содан кейін... не болмақ, Наурызбай?{/cps}"

    voice "<from 0.0 to 12.649>voices/bp-2.mp3"
    bp "{cps=25}Жүз сарбазын қырсақ... мыңын жібереді. Мыңын қырсақ... он мыңын аттандырады. Омбы... бізден бұрын шаршамайды.{/cps}"

    voice "<from 12.649 to 17.647>voices/bp-2.mp3"
    bp "{cps=25}Бұл жоңғардың шапқыншылығы емес, бұл — мемлекеттік машина.{/cps}"

    voice "<from 17.647>voices/bp-2.mp3"
    bp "{cps=25}Ол ашуланбайды, ол кек алмайды. Ол тек баса береді. Әдіспен, шыдаммен, сені таптап тастағанша тоқтамайды{/cps}"

    voice "<from 0.0 to 5.437>voices/bp-3.mp3"
    bp "{cps=25}Бізге уақыт керек. Тағы бір ай. Cонда үш жүздің басы бірігеді.{/cps}"

    voice "<from 5.437>voices/bp-3.mp3"
    bp "{cps=25}Сонда ғана шайқас туралы айтуға болады. Қазір емес.{/cps}"

    voice "voices/ab-3.mp3"
    ab "{cps=25}Шегінген батырды, халық ұмытпайды!{/cps}"

    scene black
    with fade

    scene bg_4
    with fade

    "{cps=25}...{/cps}"

    voice "<from 0.0 to 2.263>voices/kh-14.mp3"
    k "{cps=25}Бопайдікі дұрыс...{/cps}"

    voice "<from 2.263 to 12.544>voices/kh-14.mp3"
    k "{cps=25}Уақыт — бәрінен де маңызды. Уақытсыз әскердің берекесі кетеді, әкемнің одағы сияқты шашылып қалады.{/cps}"

    voice "<from 12.544>voices/kh-14.mp3"
    k "{cps=25}Ақылды хан күте білуі керек{/cps}"

    voice "<from 0.0 to 2.563>voices/kh-15.mp3"
    k "{cps=25}Наурызбай да... дұрыс айтады.{/cps}"

    voice "<from 2.563 to 6.616>voices/kh-15.mp3"
    k "{cps=25}Халық ақылдыны емес, батырды күтеді.{/cps}"

    voice "<from 6.616>voices/kh-15.mp3"
    k "{cps=25}Егер бүгін шегінсем, ертең билердің жартысы күмәндана бастайды... «Бұл сонда... кім болғаны? Оны ақ киізге бекер көтердік пе?»{/cps}"

    voice "<from 0.0 to 6.400>voices/kh-16.mp3"
    k "{cps=25}Мәселе де осында... Екеуінікі де дұрыс.{/cps}"

    voice "<from 6.400 to 12.302>voices/kh-16.mp3"
    k "{cps=25}Ал екі шындықтың арасында таңдау жасау, жақсы мен жаманды таңдау емес.{/cps}"

    voice "<from 12.302>voices/kh-16.mp3"
    k "{cps=25}Бұл — өзіңнің қай бөлігіңді құрбан ететініңді таңдау.{/cps}"

    "{cps=25}...{/cps}"

    voice "<from 0.0 to 4.500>voices/kh-18.mp3"
    k "{cps=25}Тағы бір мәселе — сатқын.{/cps}"

    voice "<from 4.500 to 10.837>voices/kh-18.mp3"
    k "{cps=25}Арамызда Омбының көзі мен құлағы жүр. Бұл казактардан да қауіпті.{/cps}"

    voice "<from 10.837>voices/kh-18.mp3"
    k "{cps=25}Казактармен қалай соғысуды білемін. Ал көлеңкемен... жоқ{/cps}"

    voice "<from 0.0 to 4.200>voices/kh-19.mp3"
    k "{cps=25}Солай болсын... Хан — дұрыс жауапты білетін адам емес.{/cps}"

    voice "<from 4.200>voices/kh-19.mp3"
    k "{cps=25}Хан — дұрыс жауап болмаған кезде, шешім қабылдай алатын адам.{/cps}"

    voice "<from 0.0 to 4.795>voices/kh-20.mp3"
    k "{cps=25}Сонда... не істеуім керек? Қай жолды таңдаймын?{/cps}"

    voice "<from 4.795>voices/kh-20.mp3"
    k "{cps=25}Екі оттың ортасында... қайсысын өшіремін?{/cps}"

    menu:
        "Таң атпай соққы береміз!":
            pass
        "Далада ізімізді суытайық.":
            pass
        "Тұзаққа түсіреміз.":
            pass
