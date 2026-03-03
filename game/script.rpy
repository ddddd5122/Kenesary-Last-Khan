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
    def _get_persistent_encyclopedia():
        if (not hasattr(persistent, "encyclopedia_characters_unlocked")
                or persistent.encyclopedia_characters_unlocked is None):
            persistent.encyclopedia_characters_unlocked = {
                "Кенесары": False,
                "Жанқожа": False,
                "Ағыбай батыр": False,
                "Наурызбай": False,
                "Бопай": False,
                "Абылай-хан": False,
            }

        for _name in encyclopedia_characters_unlocked:
            if _name not in persistent.encyclopedia_characters_unlocked:
                persistent.encyclopedia_characters_unlocked[_name] = False

        for _name, _val in encyclopedia_characters_unlocked.items():
            if _val:
                persistent.encyclopedia_characters_unlocked[_name] = True

        return persistent.encyclopedia_characters_unlocked

    def is_character_unlocked(name):
        return _get_persistent_encyclopedia().get(name, False)

    def unlock_character(name):
        data = _get_persistent_encyclopedia()
        if name in data and not data[name]:
            data[name] = True
            if name in encyclopedia_characters_unlocked:
                encyclopedia_characters_unlocked[name] = True
            renpy.show_screen("character_unlock_notification")
        elif name in encyclopedia_characters_unlocked:
            encyclopedia_characters_unlocked[name] = True

# Кейіпкерлер суреттері
image kenesary_khan = "images/characters/kenesary_khan.png"
image agybai_batyr = "images/characters/agybai_batyr.png"
image nauryzbai_batyr = "images/characters/nauryzbai_batyr.png"
image nauryzbai = "images/characters/nauryzbai.png"
image bopai = "images/characters/bopai.png"
image zhankozha = "images/characters/zhankozha.png"
image bg_1 = "images/bg/bg-1.jpg"
image bg_1_2 = "images/bg/bg-1_2.jpg"
image bg_2 = "images/bg/bg-2.jpg"
image bg_2_2 = "images/bg/bg-2-2.png"
image bg_2_1 = "images/bg/bg-2-1.png"
image bg_2_1_2 = "images/bg/bg-2-1-2.png"
image bg_2_1_3 = "images/characters/bg-2-1-3.png"
image bg_2_1_4 = "images/bg/bg-2-1-4.jpeg"
image bg_2_1_5 = "images/bg/bg-2-1-5.jpeg"
image bg_3 = "images/bg/bg-3.png"
image bg_4 = "images/bg/bg-4.png"
image bg_2_2_1 = "images/bg/bg-2-2-1.png"
image agybai = "images/characters/agybai.png"
image kenesary_2 = "images/characters/kenesary-2.png"
image war_kazak_h = "images/bg/war_kazak_h.png"
image kh_kill = "images/characters/kh_kill.png"
image kh_with_sw = "images/ui/kh_with_sw.png"
image batyr_die1 = "images/bg/batyr_die1.png"
image batyr_die2 = "images/bg/batyr_die2.png"
image kenesary_cry = "images/bg/kenesary_cry.png"

# Фондық суреттер (толық экранға созылған)
transform fullscreen_bg:
    xysize (config.screen_width, config.screen_height)
    
image bg_1 = Transform("images/bg/bg-1.jpg", xysize=(config.screen_width, config.screen_height))
image bg_1_2 = Transform("images/bg/bg-1_2.jpg", xysize=(config.screen_width, config.screen_height))
image bg_2 = Transform("images/bg/bg-2.jpg", xysize=(config.screen_width, config.screen_height))
image bg_2_2 = Transform("images/bg/bg-2-2.png", xysize=(config.screen_width, config.screen_height))
image bg_2_1 = Transform("images/bg/bg-2-1.png", xysize=(config.screen_width, config.screen_height))
image bg_2_1_2 = Transform("images/bg/bg-2-1-2.png", xysize=(config.screen_width, config.screen_height))
image bg_2_1_3 = Transform("images/characters/bg-2-1-3.png", xysize=(config.screen_width, config.screen_height))
image bg_2_1_4 = Transform("images/bg/bg-2-1-4.jpeg", xysize=(config.screen_width, config.screen_height))
image bg_2_1_5 = Transform("images/bg/bg-2-1-5.jpeg", xysize=(config.screen_width, config.screen_height))
image bg_3 = Transform("images/bg/bg-3.png", xysize=(config.screen_width, config.screen_height))
image bg_2_2_1 = Transform("images/bg/bg-2-2-1.png", xysize=(config.screen_width, config.screen_height))
image war_kazak_h = Transform("images/bg/war_kazak_h.png", xysize=(config.screen_width, config.screen_height))
image kh_kill = Transform("images/characters/kh_kill.png", xysize=(config.screen_width, config.screen_height))
image kh_with_sw = Transform("images/ui/kh_with_sw.png", xysize=(config.screen_width, config.screen_height))
image batyr_die1 = Transform("images/bg/batyr_die1.png", xysize=(config.screen_width, config.screen_height))
image batyr_die2 = Transform("images/bg/batyr_die2.png", xysize=(config.screen_width, config.screen_height))
image kenesary_cry = Transform("images/bg/kenesary_cry.png", xysize=(config.screen_width, config.screen_height))

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
    k "{cps=25}Ал Ресей... Ресей шегінуді білмейді. Ол бір келсе, МӘҢГІЛІККЕ қалады.{/cps}"

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
    k "{cps=25}Биліктің менің өзімнен не сұрайтынына дайын болуым керек.{/cps}"

    show kenesary_khan at kenesary_center

    voice "voices/kh-4.mp3"
    k "{cps=25}Ал, ендеше... Ханын күткен елге барайық.{/cps}"

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
    k "{cps=25}Сосын келіп «Міне — шекара... Оның арғы жағы енді сендердікі емес», дейді.{/cps}"

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
    zb "{cps=25}Хан ием... Елің сені ақ киізге көтергеніне дән риза, бұл орын саған ата қаныңмен бұйырған.{/cps}"

    voice "<from 8.911 to 16.340>voices/zb-1.mp3"
    zb "{cps=25}Бірақ зекет... Зекет — ауыр сөз. Өткен қыстағы жұт халықтың малын қырды.{/cps}"

    voice "<from 16.340 to 21.767>voices/zb-1.mp3"
    zb "{cps=25}Оның алдындағы қуаңшылық тағы бар. Елдің тынысы әрең шығып тұр.{/cps}"

    voice "<from 21.767>voices/zb-1.mp3"
    zb "{cps=25}Бұл салық... онсыз да жүгі ауыр түйенің белін үзіп кететін соңғы шөмшек болып жүрмей ме?{/cps}"

    menu:
        "Әр тиын қаруға жұмсалады. Билер кеңесі алдында есеп беремін":
            voice "<from 0.0 to 6.942>voices/kh-9.mp3"
            k "{cps=25}Жанқожа бидікі жөн. Өткен қыс қатал болды, оны білемін. Сондықтан тік айтамын...{/cps}"

            voice "<from 6.942 to 13.562>voices/kh-9.mp3"
            k "{cps=25}Зекеттің әр тиыны қару мен оқ-дәріге жұмсалады. Басқа ештеңеге емес!{/cps}"

            voice "<from 13.562 to 17.079>voices/kh-9.mp3"
            k "{cps=25}Билер кеңесі әр шығынды көріп отырады.{/cps}"

            voice "<from 17.079>voices/kh-9.mp3"
            k "{cps=25}Егер осы сөзімнен тайсам, мені осы ақ киізден қайта түсіруге хақыларыңыз бар!{/cps}"

            voice "voices/zb-2.mp3"
            zb "{cps=25}Көрейік... хан ием... Көрейік.{/cps}"

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
    bp "{cps=25}Ол ашуланбайды, ол кек алмайды. Ол тек баса береді. Әдіспен, шыдаммен, сені таптап тастағанша тоқтамайды.{/cps}"

    voice "<from 0.0 to 5.437>voices/bp-3.mp3"
    bp "{cps=25}Бізге уақыт керек. Тағы бір ай. Сонда үш жүздің басы бірігеді.{/cps}"

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
    k "{cps=25}Бопайдыкі дұрыс...{/cps}"

    voice "<from 2.263 to 12.544>voices/kh-14.mp3"
    k "{cps=25}Уақыт — бәрінен де маңызды. Уақытсыз әскердің берекесі кетеді, әкемнің одағы сияқты шашылып қалады.{/cps}"

    voice "<from 12.544>voices/kh-14.mp3"
    k "{cps=25}Ақылды хан күте білуі керек.{/cps}"

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
    k "{cps=25}Казактармен қалай соғысуды білемін. Ал көлеңкемен... жоқ.{/cps}"

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
            jump attack_before_dawn
        "Далада ізімізді суытайық.":
            jump cool_down_trail
        "Тұзаққа түсіреміз.":
            jump trap_choice

label attack_before_dawn:
        scene black
        with fade

        scene bg_2_1
        with fade

        voice "voices/kh-21.mp3"
        k "{cps=25}Ағыбай... Найза бойы жақындағанша бірде-бір оқ атылмасын. Бізді көрмейінше, естімеуі тиіс{/cps}"

        voice "voices/ab-4.mp3"
        ab "{cps=25}Құп болады, хан ием.{/cps}"

        scene black
        with fade

        scene bg_2_1_2
        with fade

        voice "<from 0.0 to 2.321>voices/ab-5.mp3"
        ab "{cps=25}Хан ием, қараңыз...{/cps}"

        voice "<from 2.321 to 8.759>voices/ab-5.mp3"
        ab "{cps=25}Күзеттегілері ұйқылы-ояу. Аттары тұсаулы, оттары өшіп барады.{/cps}"

        voice "<from 8.759>voices/ab-5.mp3"
        ab "{cps=25}Дәл қазір соқсақ — естерін жинап үлгермейді.{/cps}"

        voice "voices/nb-2.mp3"
        nb "{cps=25}Неге тұрмыз?! Аруақ!!!{/cps}"

        scene black
        with fade

        scene bg_2_1_3
        with fade

        $ renpy.music.set_volume(0.30, delay=0.0, channel="music")
        play music "voices/music/Steppe_s_Last_Stand (1).mp3"

        window hide

        play sound "voices/sounds/napad_group_horse.mp3"
        pause
        stop sound fadeout 1.0

        scene black
        with fade

        scene war_kazak_h
        with fade

        play sound "voices/sounds/sword-fighting-of-a-small-crowd-people-screaming (1).mp3"
        pause
        stop sound fadeout 1.0

        scene kh_kill
        with fade

        play sound "voices/sounds/warfare_sword_swipe_slash_b.mp3"
        pause
        stop sound fadeout 1.0

        scene kh_with_sw
        with fade

        voice "voices/kh-24.mp3"
        pause

        scene batyr_die1
        with fade

        pause

        scene batyr_die2
        with fade

        pause

        scene kenesary_cry
        with fade

        play sound "voices/sounds/place_in_sheath_fast_002.mp3"
        pause
        stop sound fadeout 1.0

        scene bg_2_1_5
        with fade
    
        show kenesary_2 at kenesary_2_left_mirror_big
        show nauryzbai at nauryzbai_right_mirror
    
        $ renpy.music.set_volume(0.05, delay=1.0, channel="music")
    
        voice "<from 0.0 to 2.049>voices/nb-3.mp3"
        nb "{cps=25}Аға! Біз оларды талқандадық!{/cps}"

        voice "<from 2.049>voices/nb-3.mp3"
        nb "{cps=25}Шығын жоқ деуге де болады! Екі адам қаза тапты, жетеуі жаралы{/cps}"

        voice "voices/kg-22.mp3"
        k "{cps=25}Бұл — тек бір ғана жасақ. Ал Омбыда олардың мыңдағаны бар{/cps}"

        voice "<from 0.0 to 3.606>voices/kh-23.mp3"
        k "{cps=25}Жеңісті кейін тойлаймыз. Қазір — кетеміз.{/cps}"

        voice "<from 3.606>voices/kh-23.mp3"
        k "{cps=25}Және маған сатқынды тауып бер{/cps}"

        return

label trap_choice:
    scene black
    with fade

    scene bg_2_1_4
    with fade

    show kenesary_khan at kenesary_mirror_left
    show agybai at agybai_right

    voice "voices/kh-29.mp3"
    k "{cps=25}Жақсы. Оларды күтетін жер біздікі болады.{/cps}"

    voice "voices/ab-6.mp3"
    ab "{cps=25}Тұзақ дайын, хан ием. Із қалдырдық.{/cps}"

    voice "voices/kh-30.mp3"
    k "{cps=25}Онда олардың бәрі сол жерге келсін.{/cps}"

    return

label cool_down_trail:
    scene black
    with fade

    scene bg_2_2_1
    with fade

    show kenesary_khan at kenesary_mirror_left
    show nauryzbai at nauryzbai_right_mirror_close

    voice "<from 0.0 to 4.168>voices/nb-4.mp3"
    nb "{cps=25}Аға... Біз үш жүз казактан қашып барамыз ба?{/cps}"

    voice "<from 4.168>voices/nb-4.mp3"
    nb "{cps=25}Үш жүз! Ал біз... мыңдағанбыз! Неге?!{/cps}"

    voice "voices/kh-25.mp3"
    k "{cps=25}Білемін... Mәселе санда емес, Наурызбай. Мәселе — уақытта.{/cps}"

    voice "<from 0.0 to 2.570>voices/nb-5.mp3"
    nb "{cps=25}Халық мұны көріп тұр, аға.{/cps}"

    voice "<from 2.570>voices/nb-5.mp3"
    nb "{cps=25}Олар сенің артыңнан ерді... қашу үшін емес.{/cps}"

    voice "voices/kh-26.mp3"
    k "{cps=25}Білемін... Халық бәрін көреді. Бірақ, жеңіс пен ажалдың арасын тек Мен білемін.{/cps}"

    voice "<from 0.0 to 5.138>voices/nb-6.mp3"
    nb "{cps=25}Ендеше... не үшін? Бәрі не үшін, аға?{/cps}"

    voice "<from 0.0 to 3.203>voices/kh-27.mp3"
    k "{cps=25}Өйткені арамызда — сатқын бар{/cps}"

    voice "<from 3.203 to 10.343>voices/kh-27.mp3"
    k "{cps=25}Біз шегінгенде — ол өзін аман қалдым деп ойлайды. Қауіпсіздіктемін деп сенеді. Сене берсін.{/cps}"

    voice "<from 10.343>voices/kh-27.mp3"
    k "{cps=25}Мен оған Омбымен байланысуға тағы бір мүмкіндік беремін. Ол мұны істеген кезде — біз оның кім екенін білетін боламыз{/cps}"

    voice "voices/nb-7.mp3"
    nb "{cps=25}Сен... осыны бағанадан бері ойлап жүрдің бе, аға?{/cps}"

    voice "<from 0.0 to 5.733>voices/kh-28.mp3"
    k "{cps=25}Ағыбай маған «олар бізді күтіп отыр» деген сәттен бастап, осыны ойлап келемін.{/cps}"

    voice "<from 5.733>voices/kh-28.mp3"
    k "{cps=25}Сатқын қасымызда, Наурызбай. Ол біздің әр басқан қадамымызды Омбыға жеткізіп отыр{/cps}"

    return