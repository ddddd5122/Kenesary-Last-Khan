# Постоянно видимые характеристики (HUD)

screen stats_hud():
    zorder 100

    frame:
        xalign 0.02
        yalign 0.02
        padding (12, 10)
        background "#0008"

        has vbox
        spacing 2

        text _("Бірлік: [unity]") size 18
        text _("Әскер: [army]") size 18
        text _("Экономика: [economy]") size 18
        text _("Қысым: [external_pressure]") size 18


screen quick_menu():
    zorder 100

    default quick_menu_open = False

    hbox:
        xalign 0.5
        yalign 0.98
        spacing 12

        textbutton _( "Назад" ) action Rollback() style "quick_menu_button"
        textbutton _( "Пропустить" ) action Skip() style "quick_menu_button"

    # Кнопка "три полоски" справа сверху
    textbutton "≡" action ToggleScreenVariable("quick_menu_open") style "quick_menu_toggle":
        xalign 0.98
        yalign 0.02

    # Кнопка "Справочник" слева от "три полоски"
    textbutton "Справочник" action ShowMenu("help") style "quick_menu_top_button":
        xalign 0.88
        yalign 0.02

    if quick_menu_open:
        frame:
            xalign 0.98
            yalign 0.08
            xpadding 16
            ypadding 12
            background "#00000090"

            vbox:
                spacing 8
                textbutton "Главное меню" action MainMenu(confirm=True) style "quick_menu_dropdown_button"
                textbutton "Сохранить" action ShowMenu("save") style "quick_menu_dropdown_button"
                textbutton "Настройки" action ShowMenu("preferences") style "quick_menu_dropdown_button"

style quick_menu_toggle:
    size 36
    color "#ffffff"
    hover_color "#d4af37"
    background None
    hover_background None
    xsize 50
    ysize 50
    xalign 0.5
    yalign 0.5
    mouse "button"

style quick_menu_top_button:
    size 20
    color "#ffffff"
    hover_color "#d4af37"
    background "#00000040"
    hover_background "#d4af37c0"
    xsize 150
    ysize 42
    padding (10, 6)
    xalign 0.5
    yalign 0.5
    mouse "button"

style quick_menu_button:
    size 20
    color "#ffffff"
    hover_color "#d4af37"
    background None
    hover_background None
    padding (10, 6)
    mouse "button"

style quick_menu_top_button_text:
    color "#ffffff"
    hover_color "#000000"
    xalign 0.5
    text_align 0.5

style quick_menu_dropdown_button:
    size 22
    xsize 220
    ysize 40
    background "#00000040"
    hover_background "#d4af37c0"
    padding (10, 6)
    mouse "button"

style quick_menu_dropdown_button_text:
    color "#ffffff"
    hover_color "#000000"
    xalign 0.5
    text_align 0.5

## Окно диалога (say screen)
screen say(who, what):
    zorder 10

    window:
        id "window"
        background None
        xalign 0.5
        yalign 0.5
        xsize config.screen_width
        ysize config.screen_height

        fixed:
            xysize (config.screen_width, config.screen_height)

            add "images/ui/dialogue_win.png" xalign 0.5 yalign 1.0

            if who:
                text who id "who":
                    style "say_name"
                    xalign 0.5
                    yalign 1.0
                    yoffset -330

            text what id "what":
                style "say_dialogue"
                xpos 0.08
                ypos 0.76
                xsize 0.84
                ysize 0.18

style say_name:
    size 28
    bold True
    color "#ffffff"
    xalign 0.5
    text_align 0.5

style say_dialogue:
    size 34
    color "#e6e6e6"
    line_spacing 8
    xalign 0.0
    text_align 0.0

## Кнопки выборов (menu choices)
style choice_button is button
style choice_button:
    mouse "button"

style help_header:
    size 20
    bold True
    color "#d4af37"

style help_title:
    size 48
    italic True
    color "#d4af37"

style help_body:
    size 22
    color "#e6e6e6"
    line_spacing 6
    xmaximum 740
    xsize 740
    xfill False
    text_align 0.0
    layout "subtitle"

style help_item:
    size 22
    color "#cfcfcf"

style help_item_active:
    size 22
    color "#d4af37"
    bold True

style help_item_frame:
    background None
    xsize 200
    ysize 40
    padding (10, 8)

style help_item_frame_active:
    background "#2a2416"
    xsize 200
    ysize 40
    padding (10, 8)

style help_item_button:
    background None
    hover_background "#2a2416"
    xsize 200
    ysize 40
    padding (10, 8)
    mouse "button"

style help_item_button_selected:
    background "#2a2416"
    xsize 200
    ysize 40
    padding (10, 8)

style help_item_button_text:
    color "#cfcfcf"
    hover_color "#d4af37"
    size 22
    xalign 0.0
    text_align 0.0

style help_photo_frame:
    background "#111111"
    padding (14, 14)
    xsize 380
    ysize 540

style help_photo_label:
    size 14
    color "#d4af37"
    xalign 0.5
    text_align 0.5

style help_text_viewport:
    xsize 740
    ysize 520
    xfill True

style help_back_button:
    size 20
    color "#d4af37"
    background None
    hover_background None
    mouse "button"

style help_back_button_text:
    color "#d4af37"
    hover_color "#ffffff"


## Главное меню с фото фоном
screen main_menu():
    tag menu
    
    # Запуск музыки при инициализации экрана
    python:
        if not renpy.music.get_playing(channel='music'):
            renpy.music.play("audio/music/main_menu.mp3", channel='music', fadein=2.0)
    
    # Фото фон
    add "images/bg/head_menu.png" size (1920, 1080)
    
    # Меню кнопок справа
    vbox:
        xalign 0.7
        yalign 0.5
        spacing 16
        
        text "Кенесары Хан" style "main_menu_title"
        null height 10
        
        button:
            action [Stop("music", fadeout=1.0), Jump("start_game")]
            style "main_menu_button"
            at menu_button_zoom

            fixed:
                xsize 600
                ysize 92

                add Solid("#4c0d0d80") xysize (600, 92) at menu_button_bg
                add Solid("#d4af37") xsize 600 ysize 2 xpos 0 ypos 0 at menu_button_line
                add Solid("#d4af37") xsize 600 ysize 2 xpos 0 ypos 90 at menu_button_line

                add "images/ui/for_button.png" xysize (80, 80) xpos 12 yalign 0.5 at menu_button_ornament
                text "Новая игра" style "main_menu_button_text" at menu_button_text_anim xalign 0.5 yalign 0.5
                add "images/ui/for_button.png" xysize (80, 80) xzoom -1 xpos 508 yalign 0.5 at menu_button_ornament

        button:
            action ShowMenu("load")
            style "main_menu_button"
            at menu_button_zoom

            fixed:
                xsize 600
                ysize 92

                add Solid("#4c0d0d80") xysize (600, 92) at menu_button_bg
                add Solid("#d4af37") xsize 600 ysize 2 xpos 0 ypos 0 at menu_button_line
                add Solid("#d4af37") xsize 600 ysize 2 xpos 0 ypos 90 at menu_button_line

                add "images/ui/for_button.png" xysize (80, 80) xpos 12 yalign 0.5 at menu_button_ornament
                text "Продолжить" style "main_menu_button_text" at menu_button_text_anim xalign 0.5 yalign 0.5
                add "images/ui/for_button.png" xysize (80, 80) xzoom -1 xpos 508 yalign 0.5 at menu_button_ornament

        button:
            action ShowMenu("help")
            style "main_menu_button"
            at menu_button_zoom

            fixed:
                xsize 600
                ysize 92

                add Solid("#4c0d0d80") xysize (600, 92) at menu_button_bg
                add Solid("#d4af37") xsize 600 ysize 2 xpos 0 ypos 0 at menu_button_line
                add Solid("#d4af37") xsize 600 ysize 2 xpos 0 ypos 90 at menu_button_line

                add "images/ui/for_button.png" xysize (80, 80) xpos 12 yalign 0.5 at menu_button_ornament
                text "Справочник" style "main_menu_button_text" at menu_button_text_anim xalign 0.5 yalign 0.5
                add "images/ui/for_button.png" xysize (80, 80) xzoom -1 xpos 508 yalign 0.5 at menu_button_ornament

        button:
            action ShowMenu("preferences")
            style "main_menu_button"
            at menu_button_zoom

            fixed:
                xsize 600
                ysize 92

                add Solid("#4c0d0d80") xysize (600, 92) at menu_button_bg
                add Solid("#d4af37") xsize 600 ysize 2 xpos 0 ypos 0 at menu_button_line
                add Solid("#d4af37") xsize 600 ysize 2 xpos 0 ypos 90 at menu_button_line

                add "images/ui/for_button.png" xysize (80, 80) xpos 12 yalign 0.5 at menu_button_ornament
                text "Настройки" style "main_menu_button_text" at menu_button_text_anim xalign 0.5 yalign 0.5
                add "images/ui/for_button.png" xysize (80, 80) xzoom -1 xpos 508 yalign 0.5 at menu_button_ornament

        button:
            action ShowMenu("about")
            style "main_menu_button"
            at menu_button_zoom

            fixed:
                xsize 600
                ysize 92

                add Solid("#4c0d0d80") xysize (600, 92) at menu_button_bg
                add Solid("#d4af37") xsize 600 ysize 2 xpos 0 ypos 0 at menu_button_line
                add Solid("#d4af37") xsize 600 ysize 2 xpos 0 ypos 90 at menu_button_line

                add "images/ui/for_button.png" xysize (80, 80) xpos 12 yalign 0.5 at menu_button_ornament
                text "Об игре" style "main_menu_button_text" at menu_button_text_anim xalign 0.5 yalign 0.5
                add "images/ui/for_button.png" xysize (80, 80) xzoom -1 xpos 508 yalign 0.5 at menu_button_ornament

        button:
            action Quit(confirm=True)
            style "main_menu_button"
            at menu_button_zoom

            fixed:
                xsize 600
                ysize 92

                add Solid("#4c0d0d80") xysize (600, 92) at menu_button_bg
                add Solid("#d4af37") xsize 600 ysize 2 xpos 0 ypos 0 at menu_button_line
                add Solid("#d4af37") xsize 600 ysize 2 xpos 0 ypos 90 at menu_button_line

                add "images/ui/for_button.png" xysize (80, 80) xpos 12 yalign 0.5 at menu_button_ornament
                text "Выход" style "main_menu_button_text" at menu_button_text_anim xalign 0.5 yalign 0.5
                add "images/ui/for_button.png" xysize (80, 80) xzoom -1 xpos 508 yalign 0.5 at menu_button_ornament

transform menu_button_zoom:
    on idle:
        ease 0.18 zoom 1.0 alpha 1.0
    on hover:
        ease 0.18 zoom 1.02 alpha 1.0

transform menu_button_bg:
    on idle:
        ease 0.18 alpha 0.35
    on hover:
        ease 0.18 alpha 0.65

transform menu_button_line:
    on idle:
        ease 0.18 alpha 0.45
    on hover:
        ease 0.18 alpha 1.0

transform menu_button_ornament:
    on idle:
        ease 0.18 alpha 0.85
    on hover:
        ease 0.18 alpha 1.0

transform menu_button_text_anim:
    on idle:
        ease 0.18 zoom 1.0
    on hover:
        ease 0.18 zoom 1.06

## Стиль заголовка главного меню
style main_menu_title:
    size 36
    bold True
    color "#d4af37"
    xalign 0.5

## Стиль кнопок главного меню
style main_menu_button:
    xsize 600
    ysize 92
    xalign 0.5
    background None
    hover_background None
    padding (14, 10)
    mouse "button"

style main_menu_button_text:
    color "#ffffff"
    hover_color "#d4af37"
    size 30
    hover_bold True
    xalign 0.5
    text_align 0.5

## Стили для баров (ползунков)
style bar:
    ysize 30
    left_bar "#d4af37"
    right_bar "#404040"
    thumb "#ffffff"
    thumb_offset 0
    thumb_shadow None
    
style vbar:
    xsize 30
    top_bar "#d4af37"
    bottom_bar "#404040"
    thumb "#ffffff"
    thumb_offset 0
    thumb_shadow None

## Экран справочника
screen help():
    tag menu
    layer "screens"

    default selected_category = "Персонажи"
    default selected_character = "Кенесары"

    frame:
        xalign 0.5
        yalign 0.5
        xsize 1800
        ysize 900
        background "#171717"
        padding (0, 0)

        fixed:
            # Границы и разделители
            add Solid("#d4af37") xsize 1800 ysize 2 xpos 0 ypos 0
            add Solid("#d4af37") xsize 1800 ysize 2 xpos 0 ypos 898
            add Solid("#d4af37") xsize 2 ysize 900 xpos 0 ypos 0
            add Solid("#d4af37") xsize 2 ysize 900 xpos 1798 ypos 0
            add Solid("#d4af37") xsize 2 ysize 900 xpos 260 ypos 0
            add Solid("#d4af37") xsize 2 ysize 900 xpos 580 ypos 0
            add Solid("#d4af37") xsize 1800 ysize 2 xpos 0 ypos 90

            # Верхняя панель
            text "КАТЕГОРИИ" style "help_header" xpos 30 ypos 30
            text "ПЕРСОНАЖИ" style "help_header" xpos 300 ypos 30

            textbutton "← ВЕРНУТЬСЯ В МЕНЮ" action Return() style "help_back_button":
                xalign 1.0
                yalign 0.0
                xoffset -20
                yoffset 20

            # Левый список (категории)
            vbox:
                xpos 30
                ypos 130
                spacing 16

                textbutton "Персонажи" action SetScreenVariable("selected_category", "Персонажи") style ("help_item_button_selected" if selected_category == "Персонажи" else "help_item_button") text_style ("help_item_active" if selected_category == "Персонажи" else "help_item")
                textbutton "Термины" action SetScreenVariable("selected_category", "Термины") style ("help_item_button_selected" if selected_category == "Термины" else "help_item_button") text_style ("help_item_active" if selected_category == "Термины" else "help_item")
                textbutton "События" action SetScreenVariable("selected_category", "События") style ("help_item_button_selected" if selected_category == "События" else "help_item_button") text_style ("help_item_active" if selected_category == "События" else "help_item")

            # Средний список (персонажи)
            vbox:
                xpos 300
                ypos 130
                spacing 16

                if is_character_unlocked("Кенесары"):
                    textbutton "Кенесары" action SetScreenVariable("selected_character", "Кенесары") style ("help_item_button_selected" if selected_character == "Кенесары" else "help_item_button") text_style ("help_item_active" if selected_character == "Кенесары" else "help_item")
                else:
                    textbutton "???" style "help_item_button" text_style "help_item" sensitive False

                if is_character_unlocked("Жанқожа"):
                    textbutton "Жанқожа" action SetScreenVariable("selected_character", "Жанқожа") style ("help_item_button_selected" if selected_character == "Жанқожа" else "help_item_button") text_style ("help_item_active" if selected_character == "Жанқожа" else "help_item")
                else:
                    textbutton "???" style "help_item_button" text_style "help_item" sensitive False

                if is_character_unlocked("Ағыбай батыр"):
                    textbutton "Ағыбай батыр" action SetScreenVariable("selected_character", "Ағыбай батыр") style ("help_item_button_selected" if selected_character == "Ағыбай батыр" else "help_item_button") text_style ("help_item_active" if selected_character == "Ағыбай батыр" else "help_item")
                else:
                    textbutton "???" style "help_item_button" text_style "help_item" sensitive False

                if is_character_unlocked("Наурызбай"):
                    textbutton "Наурызбай" action SetScreenVariable("selected_character", "Наурызбай") style ("help_item_button_selected" if selected_character == "Наурызбай" else "help_item_button") text_style ("help_item_active" if selected_character == "Наурызбай" else "help_item")
                else:
                    textbutton "???" style "help_item_button" text_style "help_item" sensitive False

                if is_character_unlocked("Абылай-хан"):
                    textbutton "Абылай-хан" action SetScreenVariable("selected_character", "Абылай-хан") style ("help_item_button_selected" if selected_character == "Абылай-хан" else "help_item_button") text_style ("help_item_active" if selected_character == "Абылай-хан" else "help_item")
                else:
                    textbutton "???" style "help_item_button" text_style "help_item" sensitive False

                if is_character_unlocked("Бопай"):
                    textbutton "Бопай" action SetScreenVariable("selected_character", "Бопай") style ("help_item_button_selected" if selected_character == "Бопай" else "help_item_button") text_style ("help_item_active" if selected_character == "Бопай" else "help_item")
                else:
                    textbutton "???" style "help_item_button" text_style "help_item" sensitive False

            # Правая область: карточка персонажа
            if is_character_unlocked(selected_character):
                text "[selected_character]" style "help_title" xpos 620 ypos 130
            else:
                text "???" style "help_title" xpos 620 ypos 130

            frame:
                xpos 620
                ypos 210
                xsize 1180
                ysize 620
                background None

                hbox:
                    spacing 24

                    frame:
                        style "help_photo_frame"

                        fixed:
                            xysize (352, 512)
                            xalign 0.5
                            yalign 0.5
                            clipping True

                            if not is_character_unlocked(selected_character):
                                add Solid("#222222") xysize (352, 512) xalign 0.5 yalign 0.5
                                text "ПЕРСОНАЖ НЕ ОТКРЫТ" style "help_photo_label" xalign 0.5 yalign 0.85
                            elif selected_character == "Кенесары":
                                add "images/characters/kenesary_khan.png" fit "cover" xysize (352, 512) xalign 0.5 yalign 0.5
                            elif selected_character == "Жанқожа":
                                add "images/characters/zhankozha.png" fit "cover" xysize (352, 512) xalign 0.5 yalign 0.5
                            elif selected_character == "Ағыбай батыр":
                                add "images/characters/agybai.png" fit "cover" xysize (352, 512) xalign 0.5 yalign 0.5
                            elif selected_character == "Наурызбай":
                                add "images/characters/nauryzbai.png" fit "cover" xysize (352, 512) xalign 0.5 yalign 0.5
                            elif selected_character == "Бопай":
                                add "images/characters/bopai.png" fit "cover" xysize (352, 512) xalign 0.5 yalign 0.5
                            else:
                                add Solid("#222222") xysize (352, 512) xalign 0.5 yalign 0.5
                                text "ПОРТРЕТ ВЫДАЮЩЕГОСЯ БАТЫРА" style "help_photo_label" xalign 0.5 yalign 0.85

                    frame:
                        xsize 12
                        ysize 520
                        background None
                        add Solid("#d4af37") xsize 4 ysize 520 xpos 4 ypos 0

                    viewport:
                        style "help_text_viewport"
                        xysize (740, 520)
                        mousewheel True
                        scrollbars "vertical"
                        clipping True

                        vbox:
                            xsize 740
                            xmaximum 740
                            xfill True
                            spacing 18
                            if not is_character_unlocked(selected_character):
                                text "Персонаж будет открыт по мере прохождения истории." style "help_body"
                            elif selected_character == "Кенесары":
                                text "Кенесары Қасымұлы — жай ғана көтеріліс жетекшісі емес, ол барлық үш жүздің соңғы мойындалған ханы, аңызға айналған Абылай ханның немересі және Шыңғыс ханның тікелей ұрпағы. Замандастарының көбінен айырмашылығы, Кенесары жеке пайдасын немесе уақытша одақтарды көздеген жоқ; оның басты мақсаты — Қазақ хандығының тәуелсіздігін отарлау басталғанға дейінгі шекарада қалпына келтіру болды." style "help_body"
                                text "Оның бойында сирек кездесетін қасиеттер: дипломаттың көрегендігі мен әскери қолбасшының қатаң ерік-жігері ұштасқан. Кенесары Даладағы соғыс жүргізудің ескі әдістері империяның тұрақты әскеріне қарсы тұра алмайтынын түсінді. Сондықтан ол түбегейлі реформалар жүргізді: қатаң тәртіпке негізделген тұрақты армия құрды, оқ құю үшін көшпелі ұстаханалар ұйымдастырды, тіпті өз артиллериясын жасауға талпынды. Оны халық құрметтеді, сонымен бірге одан сескенді — Отанға опасыздық жасағаны немесе қашқындығы үшін ол тегіне қарамай өлім жазасына кесетін." style "help_body"
                                text "1841 жылы Көкшетау өңірінде оны ресми түрде хан сайлау рәсімі өтті. Ақ киізге көтеріп хан сайлау — Кенесарының халық алдындағы жалғыз заңды билеуші екенін, ал Омбы немесе Орынбор бұйрықтарының қазақтар үшін бұдан былай күші жоқтығын білдірді. Ол Ресей императоры Николай I-мен, Хиуа және Бұхар хандықтарымен күрделі дипломатиялық қарым-қатынас жүргізіп, тек бір ғана талап қойды: қазақ жерлерін жайына қалдыру және салынған бекіністерді жою." style "help_body"
                                text "Оның тағдыры Қазақстан тарихының ең айбынды әрі қасіретті беттерінің біріне айналды. Феодалдық топтардың бір бөлігінің сатқындығы мен екі оттың ортасында қалуы салдарынан ол 1847 жылы қаза тапты. Соңғы деміне дейін ол өз мұратына — Дала бостандығына адал болып қалды." style "help_body"
                            elif selected_character == "Жанқожа":
                                text "Жанқожа Нұрмұхамедұлы — аңызға айналған батыр, Шекті руының ақсақалы және Кіші жүздің ең беделді көшбасшыларының бірі. Халық жадында ол өмірін екі майдандағы толассыз арпалысқа арнаған «даланың соңғы серісі» ретінде қалды: ол солтүстіктен келген отаршылдық экспансияға да, оңтүстіктен қыспаққа алған Хиуа мен Қоқан хандықтарының озбырлығына да қарсы тұрды." style "help_body"
                                text "Көптеген сұлтандардан айырмашылығы, Жанқожа Шыңғыс хан ұрпағына (төреге) жатпаса да, оның қарапайым халық (шаруалар) арасындағы беделі кез келген ақсүйектен жоғары болды. Ол ерен күш иесі, алып тұлға ретінде сипатталады; тіпті еңкейген кәрілік шағында да өзінің әйгілі ақ боз атына мініп, сарбаздарын шабуылға бастап шығатын. Жанқожа қатал әділдіктің символы еді: ол қазақтарға ауыр салық салған Хиуа бекіністерін аяусыз талқандады және қазақ даласын әскери бекіністер тізбегіне айналдыру әрекеттеріне батыл қарсы шықты." style "help_body"
                                text "1840-жылдардың басында Жанқожа батырдың Кенесары көтерілісіне қосылуы ірі стратегиялық соққы болды. Бұл көтеріліс отының Сырдария жағалауынан Көкшетауға дейінгі ұлан-ғайыр аумақты шарпығанын білдірді. Жас айырмашылығы мен тегіне қарамастан, Жанқожа Кенесарыны ұлттың біртұтас көшбасшысы деп танып, оның бойынан қазақ жерлерін түпкілікті бөлшектенуден сақтап қалу мүмкіндігін көрді. Кенесары қаза тапқаннан кейін де Жанқожа күресін тоқтатпай, 1850-жылдары көтеріліс туын қайта көтерді. Ол қорлықпен бағынып күн кешкеннен гөрі, шайқас үстіндегі өлімді биік қойды." style "help_body"
                            elif selected_character == "Ағыбай батыр":
                                text "Ағыбай Қоңырбайұлы (1802–1885) — Кенесары хан бастаған ұлт-азаттық қозғалысының ең жақын үзеңгілестерінің бірі, даңқты қолбасшы және стратег. Шұбыртпалы руынан шыққан ол халық арасында «Ақжолтай батыр» деген құрметті есіммен танымал болды. Бұл лақап ат оның қатысқан әрбір шайқасы жеңіспен аяқталып, жолы болғыш, сәттілік әкелетін қолбасшы болғаны үшін берілген." style "help_body"
                                text "Ағыбай батыр Кенесары әскерінің негізгі соққы беруші күшін басқарды. Ол партизандық соғыс тактикасын жетік меңгерген шебер ретінде белгілі. Оның басшылығымен жүргізілген Ақмола бекінісін алу и Ресей империясының жазалаушы отрядтарына қарсы бағытталған көптеген операциялар қазақ әскери өнерінің тарихында ерекше орын алады. Кенесары хан оның стратегиялық ойлау қабілеті мен жеке батылдығын жоғары бағалап, ең жауапты бағыттарды сеніп тапсырған." style "help_body"
                                text "Кенесары хан қаза тапқаннан кейін де Ағыбай батыр болаттай берік рухын жоғалтқан жоқ. Ол Сырдария бойындағы Жанқожа батырмен тізе қосып, қоқандық басқыншыларға қарсы күресті жалғастырды. Өмірінің соңына дейін ел бірлігі мен жер тұтастығын қорғауды мұрат еткен батырдың тұлғасы ұрпаққа ерлік пен адалдықтың үлгісі болып қалды." style "help_body"
                            elif selected_character == "Наурызбай":
                                text "Наурызбай Қасымұлы — Кенесары ханның кенже інісі, аңызға айналған қолбасшы және көтерілістің басты соққы беруші күші. Халық жадында ол қазақ даласының қаймықпас ерлігі мен асқан әскери өнерінің символы — «алдаспан» болып қалды." style "help_body"
                                text "Егер Кенесары қозғалыстың ақылы мен саяси стратегі болса, Наурызбай оның жүрегі мен ең батыл жауынгері болды. Жастайынан ол ерен физикалық күшімен және қару-жарақты шебер меңгеруімен ерекшеленді. Шайқас кезінде ол әрқашан ең қауіпті шептерде, таңдаулы жасақтардың алдында жүретін. Қарсыластың ең мықты батырларымен жекпе-жекке шығып, үнемі жеңіске жететін." style "help_body"
                                text "Оның ағасына және тәуелсіздік идеясына деген адалдығы шексіз еді. Наурызбай бекіністерді қоршауға алу және шегіну кезіндегі қорғаныс ұрыстары сияқты ең күрделі әскери операцияларға жетекшілік етті. Оның есімі жауларына үрей ұялатып, көтерілісшілерге сенім сыйлады. Өткір ақылы мен қағылездігі оған ең тығырыққа тірелген сәттердің өзінде жол тауып шығуға мүмкіндік беретін." style "help_body"
                            elif selected_character == "Бопай":
                                text "Бопай ханым: Даланың қайсар ханшайымы" style "help_body"
                                text "Бопай Қасымқызы — Кенесары ханның қарындасы, қазақ тарихындағы бірегей тұлға, дипломат және қолбасшы. Ол Кенесары бастаған ұлт-азаттық қозғалысына белсене қатысып, ерлермен иық тіресе соғысқан нағыз жауынгер әйелдің символына айналды." style "help_body"
                                text "Бопай ханым тек ханның қарындасы ғана емес, оның ең сенімді кеңесшілерінің бірі болды. Ол 600-ден астам сарбаздан тұратын ерекше жасақты басқарды. Это жасақ негізінен барлау жұмыстарымен, қамтамасыз ету мәселелерімен және жазалаушы отрядтарға тұтқиылдан соққы берумен айналысты. Бопай ханымның стратегиялық ойлау қабілеті мен ұйымдастырушылық дарыны Кенесары әскерінің ішкі тәртібін нығайтуға үлкен септігін тигізді." style "help_body"
                                text "Оның тағдыры ерік-жігердің үлгісі іспеттес. Бопай өзінің жайлы өмірін, отбасылық тыныштығын Отан азаттығы жолындағы күреске айырбастады. Ол көтеріліс кезінде ел ішіндегі бірлікті сақтау үшін дипломатиялық келіссөздер жүргізіп, ру басыларын хан маңына топтастыруға күш салды. Оның есімінен жаулары сескенетін, ал халық оны ерлігі үшін ерекше қадірледі." style "help_body"
                                text "1847 жылы Кенесары хан мен Наурызбай батыр қаза тапқаннан кейін де, Бопай ханым күресті тоқтатқан жоқ. Ол қозғалыстың қалдықтарын біріктіруге тырысып, соңғы деміне дейін Қасым сұлтандарының асқақ рухын сақтап қалды." style "help_body"
                            else:
                                text "Бұл бөлім кейінірек толықтырылады." style "help_body"

screen character_unlock_notification():
    zorder 200
    modal False

    timer 3.0 action Hide("character_unlock_notification")

    frame:
        xalign 0.5
        yalign 0.1
        background "#000000c0"
        padding (20, 12)

        text "Новый персонаж открыт в справочнике" style "help_body" xalign 0.5

## Экран "Об игре"
screen about():
    tag menu
    layer "screens"
    
    frame:
        xalign 0.5
        yalign 0.5
        xsize 1000
        ysize 700
        background "#000000c0"
        padding (50, 40)
        
        vbox:
            xalign 0.5
            yalign 0.5
            spacing 30
            
            text "Кенесары - Последний Хан" size 42 bold True xalign 0.5 color "#d4af37"
            text "Версия 1.0.0" size 24 xalign 0.5
            
            null height 40
            
            text "Историческая визуальная новелла о жизни" size 22 xalign 0.5
            text "последнего казахского хана Кенесары Касымулы" size 22 xalign 0.5
            
            null height 50
            
            text "Разработано:" size 28 bold True xalign 0.5 color "#d4af37"
            text "Qazaq Games Studio" size 22 xalign 0.5
            
            null height 40
            
            text "© 2026 Все права защищены" size 18 xalign 0.5
            
        textbutton "Назад" action Return() xalign 0.5 ypos 630 style "main_menu_button"

## Экран подтверждения
screen confirm(message, yes_action, no_action):
    modal True
    zorder 200
    
    # Полупрозрачный черный фон вместо картинки
    add "#00000080"
    
    frame:
        xalign 0.5
        yalign 0.5
        xsize 800
        ysize 400
        background "#000000e0"
        padding (50, 40)
        
        vbox:
            xalign 0.5
            yalign 0.5
            spacing 40
            
            text message size 32 xalign 0.5 color "#ffffff"
            
            hbox:
                xalign 0.5
                spacing 50
                
                textbutton "Да" action yes_action style "main_menu_button"
                textbutton "Нет" action no_action style "main_menu_button"

## Экран настроек (базовый)
screen preferences():
    tag menu
    layer "screens"
    
    frame:
        xalign 0.5
        yalign 0.5
        xsize 1000
        ysize 600
        background "#000000c0"
        padding (50, 40)
        
        vbox:
            xalign 0.5
            spacing 30
            
            text "НАСТРОЙКИ" size 40 bold True xalign 0.5 color "#d4af37"
            
            null height 20
            
            # Громкость музыки
            vbox:
                xalign 0.5
                spacing 8
                
                text "Громкость музыки:" size 24 color "#ffffff" xalign 0.5
                bar:
                    value Preference("music volume")
                    xsize 600
                    xalign 0.5
                    ysize 30
                    left_bar "#d4af37"
                    right_bar "#404040"
                    thumb "#ffffff"
            
            # Громкость звука
            vbox:
                xalign 0.5
                spacing 8
                
                text "Громкость звука:" size 24 color "#ffffff" xalign 0.5
                bar:
                    value Preference("sound volume")
                    xsize 600
                    xalign 0.5
                    ysize 30
                    left_bar "#d4af37"
                    right_bar "#404040"
                    thumb "#ffffff"
            
            # Полный экран
            hbox:
                xalign 0.5
                spacing 20
                
                text "Полный экран:" size 24 color "#ffffff" yalign 0.5
                textbutton "Вкл/Выкл" action Preference("display", "toggle") yalign 0.5
            
            null height 20
            
            textbutton "Назад" action Return() xalign 0.5 style "main_menu_button"

## Экраны сохранения/загрузки
screen save():
    tag menu
    use file_slots("СОХРАНИТЬ ИГРУ", is_load=False)

screen load():
    tag menu
    use file_slots("ЗАГРУЗИТЬ ИГРУ", is_load=True)

screen file_slots(title, is_load=False):
    layer "screens"
    
    frame:
        xalign 0.5
        yalign 0.5
        xsize 1200
        ysize 780
        background "#000000c0"
        padding (50, 40)
        
        vbox:
            spacing 24
            
            text title size 40 bold True xalign 0.5 color "#d4af37"
            
            null height 10
            
            grid 3 2:
                spacing 20
                
                for i in range(1, 7):
                    button:
                        xsize 330
                        ysize 140
                        background "#00000060"
                        hover_background "#d4af3720"
                        action (FileLoad(i) if is_load else FileSave(i))
                        
                        vbox:
                            spacing 6
                            add FileScreenshot(i) xysize (330, 90)
                            text FileTime(i, format="%d.%m.%Y %H:%M", empty="Пусто") size 16 xalign 0.5
                            text FileSaveName(i) size 14 xalign 0.5
            
            hbox:
                xalign 0.5
                spacing 20
                textbutton "Пред." action FilePagePrevious() style "main_menu_button"
                textbutton "След." action FilePageNext() style "main_menu_button"
            
            textbutton "Назад" action Return() xalign 0.5 style "main_menu_button"

# HUD и быстрое меню показываются только во время игры, а не в главном меню
init python:
    # Не добавляем их в overlay_screens - они будут показываться только в игре
    pass
