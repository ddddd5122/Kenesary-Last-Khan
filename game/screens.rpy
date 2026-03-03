# Үнемі көрінетін сипаттамалар (HUD)

default stats_visible = False
default menu_window_pause_text = False

screen stats_hud():
    zorder 100

    if stats_visible:
        fixed:
            xalign 0.02
            yalign 0.02
            xoffset 20
            yoffset 120
            xsize 360
            ysize 360

            add im.Scale("images/ui/for_info.png", 360, 360)

            vbox:
                xpos 78
                ypos 74
                xsize 222
                ysize 230
                spacing 6

                text _("Бірлік: [unity]") style "stats_info_text"
                text _("Әскер: [army]") style "stats_info_text"
                text _("Экономика: [economy]") style "stats_info_text"
                text _("Қысым: [external_pressure]") style "stats_info_text"


screen quick_menu():
    zorder 100

    if renpy.context()._menu:
        null
    else:
        key "game_menu" action ToggleScreen("menu_window")
        key "dismiss" action Return()
        key "K_SPACE" action Return()

    hbox:
        xalign 0.5
        yalign 0.98
        spacing 12

        textbutton _( "Артқа" ) action Rollback() style "quick_menu_button"
        textbutton _( "Өткізу" ) action Skip() style "quick_menu_button"

    # Сол жақ жоғарыдағы иконка (80x80, сол жақтан 20px)
    hbox:
        xalign 0.0
        yalign 0.0
        xoffset 20
        yoffset 20
        spacing 10

        imagebutton:
            idle im.Scale("images/ui/graphic_icon.png", 80, 80)
            hover im.Scale("images/ui/graphic_icon.png", 80, 80)
            action ToggleVariable("stats_visible")
            xsize 80
            ysize 80
            mouse "button"

    # Оң жақ жоғарыдағы иконкалар (80x80, оң жақтан 20px)
    hbox:
        xalign 1.0
        yalign 0.0
        xoffset -20
        yoffset 20
        spacing 10

        imagebutton:
            idle im.Scale("images/ui/book_icon.png", 80, 80)
            hover im.Scale("images/ui/book_icon.png", 80, 80)
            action [Play("sound", "voices/sounds/freesounds123-book-opening-345808.mp3"), ShowMenu("help")]
            xsize 80
            ysize 80
            mouse "button"

        imagebutton:
            idle im.Scale("images/ui/menu_icon.png", 80, 80)
            hover im.Scale("images/ui/menu_icon.png", 80, 80)
            action ToggleScreen("menu_window")
            xsize 80
            ysize 80
            mouse "button"

screen menu_window():
    tag menu
    zorder 120
    modal True

    key "game_menu" action Hide("menu_window")

    default menu_window_hover = None

    on "show" action [
        Function(renpy.music.set_pause, True, "voice"),
        Function(renpy.music.set_pause, True, "sound"),
        SetVariable("menu_window_pause_text", True)
    ]
    on "hide" action [
        Function(renpy.music.set_pause, False, "voice"),
        Function(renpy.music.set_pause, False, "sound"),
        SetVariable("menu_window_pause_text", False)
    ]

    add Solid("#00000080")

    fixed:
        xalign 0.5
        yalign 0.5
        xsize 900
        ysize 600

        add RoundRect("#d4af37") xysize (900, 600)
        add RoundRect("#5a1a1a") xysize (888, 588) xpos 6 ypos 6

        add im.Scale("images/ui/for_ui_win.png", 140, 140) xpos 0 ypos 0
        add im.Scale("images/ui/for_ui_win.png", 140, 140) xalign 1.0 yalign 0.0 xzoom -1
        add im.Scale("images/ui/for_ui_win.png", 140, 140) xalign 0.0 yalign 1.0 yzoom -1
        add im.Scale("images/ui/for_ui_win.png", 140, 140) xalign 1.0 yalign 1.0 xzoom -1 yzoom -1

        vbox:
            xalign 0.5
            yalign 0.5
            spacing 18

            text "МӘЗІР" style "menu_window_title"
            null height 6

            button:
                action Hide("menu_window")
                style "menu_window_button_base"
                hovered SetScreenVariable("menu_window_hover", "continue")
                unhovered SetScreenVariable("menu_window_hover", None)

                fixed:
                    xsize 520
                    ysize 64

                    add RoundRect("#d4af37", 10) xysize (520, 64)
                    if menu_window_hover == "continue":
                        add RoundRect("#ffffff1a", 10) xysize (520, 64)
                    text "Жалғастыру" style "menu_window_button_text_primary" xalign 0.5 yalign 0.5

            button:
                action [Hide("menu_window"), ShowMenu("pre_save_capture")]
                style "menu_window_button_base"
                hovered SetScreenVariable("menu_window_hover", "save")
                unhovered SetScreenVariable("menu_window_hover", None)

                fixed:
                    xsize 520
                    ysize 64

                    add RoundRect("#5a1a1a", 10) xysize (520, 64)
                    add RoundRect("#d4af37", 10) xysize (520, 64)
                    add RoundRect("#5a1a1a", 8) xysize (516, 60) xpos 2 ypos 2
                    if menu_window_hover == "save":
                        add RoundRect("#ffffff14", 10) xysize (520, 64)
                    text "Сақтау" style "menu_window_button_text_gold" xalign 0.5 yalign 0.5

            button:
                action ShowMenu("preferences")
                style "menu_window_button_base"
                hovered SetScreenVariable("menu_window_hover", "prefs")
                unhovered SetScreenVariable("menu_window_hover", None)

                fixed:
                    xsize 520
                    ysize 64

                    add RoundRect("#5a1a1a", 10) xysize (520, 64)
                    add RoundRect("#d4af37", 10) xysize (520, 64)
                    add RoundRect("#5a1a1a", 8) xysize (516, 60) xpos 2 ypos 2
                    if menu_window_hover == "prefs":
                        add RoundRect("#ffffff14", 10) xysize (520, 64)
                    text "Баптаулар" style "menu_window_button_text_gold" xalign 0.5 yalign 0.5

            button:
                action MainMenu(confirm=True)
                style "menu_window_button_base"
                hovered SetScreenVariable("menu_window_hover", "main_menu")
                unhovered SetScreenVariable("menu_window_hover", None)

                fixed:
                    xsize 520
                    ysize 64

                    add RoundRect("#5a1a1a", 10) xysize (520, 64)
                    add RoundRect("#ff2b2b", 10) xysize (520, 64)
                    add RoundRect("#5a1a1a", 8) xysize (516, 60) xpos 2 ypos 2
                    if menu_window_hover == "main_menu":
                        add RoundRect("#ffffff14", 10) xysize (520, 64)
                    text "Басты мәзір" style "menu_window_button_text_red" xalign 0.5 yalign 0.5

style menu_window_title:
    size 44
    color "#d4af37"
    bold True
    xalign 0.5
    text_align 0.5

style menu_window_button_base:
    background None
    hover_background None
    xsize 520
    ysize 64
    xalign 0.5
    mouse "button"

style menu_window_button_text_primary:
    size 32
    color "#5a1a1a"
    xalign 0.5
    text_align 0.5

style menu_window_button_text_gold:
    size 32
    color "#d4af37"
    xalign 0.5
    text_align 0.5

style menu_window_button_text_red:
    size 32
    color "#ff2b2b"
    xalign 0.5
    text_align 0.5

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

style stats_info_text:
    size 20
    color "#3b2a1c"
    bold True
    xalign 0.0
    text_align 0.0

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

## Диалог терезесі (say screen)
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

            add im.FactorScale("images/ui/dialogue_win.png", 0.8, 0.8) xalign 0.5 yalign 1.0

            if who:
                text who id "who":
                    style "say_name"
                    xalign 0.5
                    yalign 1.0
                    xoffset -2
                    yoffset -263

        text what id "what":
            style "say_dialogue"
            slow_cps_multiplier (0.0 if menu_window_pause_text else 1.0)
            xpos 0.13
            ypos 0.80
            xsize 0.74
            ysize 0.14

style say_name:
    size 24
    bold True
    color "#ffffff"
    xalign 0.5
    text_align 0.5

style say_dialogue:
    size 26
    color "#e6e6e6"
    line_spacing 8
    xalign 0.0
    text_align 0.0

## Таңдау түймелері (menu choices)
screen choice(items):
    zorder 11
    modal True
    key "dismiss" action NullAction()

    window:
        background None
        xalign 0.5
        yalign 0.5
        xsize config.screen_width
        ysize config.screen_height

        fixed:
            xysize (config.screen_width, config.screen_height)

            add im.FactorScale("images/ui/dialogue_win.png", 0.8, 0.8) xalign 0.5 yalign 1.0

            vbox:
                style_prefix "choice"
                xpos 0.13
                ypos 0.80
                xsize 0.74
                spacing 12

                for i in items:
                    textbutton i.caption action i.action

style choice_button is button
style choice_button:
    background None
    hover_background None
    xalign 0.0
    xsize 0.84
    mouse "button"

style choice_button_text:
    size 26
    color "#e6e6e6"
    hover_color "#d4af37"
    line_spacing 8
    xalign 0.0
    text_align 0.0

style help_header:
    size 20
    bold True
    color "#6a4a2f"

style help_title:
    size 48
    italic True
    color "#7a5531"

style help_body:
    size 22
    color "#5a3c24"
    line_spacing 6
    xmaximum 740
    xsize 740
    xfill False
    text_align 0.0
    layout "subtitle"

style help_item:
    size 22
    color "#5a3c24"

style help_item_active:
    size 22
    color "#f3dfb3"
    bold True

style help_item_frame:
    background None
    xsize 200
    ysize 40
    padding (10, 8)

style help_item_frame_active:
    background "#5a3c24"
    xsize 200
    ysize 40
    padding (10, 8)

style help_item_button:
    background "#dfcba6"
    hover_background "#cdb189"
    xsize 200
    ysize 40
    padding (10, 8)
    mouse "button"

style help_item_button_selected:
    background "#5a3c24"
    xsize 200
    ysize 40
    padding (10, 8)

style help_item_button_text:
    color "#5a3c24"
    hover_color "#7a5531"
    size 22
    xalign 0.0
    text_align 0.0

style help_photo_frame:
    background None
    padding (0, 0)
    xsize 380
    ysize 540

style help_photo_label:
    size 14
    color "#8a6a42"
    xalign 0.5
    text_align 0.5

style help_text_viewport:
    xsize 740
    ysize 520
    xfill True

style help_back_button:
    size 20
    color "#5a3c24"
    background None
    hover_background None
    mouse "button"

style help_back_button_text:
    color "#5a3c24"
    hover_color "#8a6a42"


## Фотосуретті фонды басты мәзір
screen main_menu():
    tag menu
    
    # Экранды бастапқы қалпына келтіргенде музыканы іске қосу
    python:
        if not renpy.music.get_playing(channel='music'):
            renpy.music.play("audio/music/main_menu.mp3", channel='music', fadein=2.0)
    
    # Фотосурет фоны
    add "images/bg/head_menu.png" size (1920, 1080)
    
    # Оң жақтағы түймелер мәзірі
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
                text "Жаңа ойын" style "main_menu_button_text" at menu_button_text_anim xalign 0.5 yalign 0.5
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
                text "Жалғастыру" style "main_menu_button_text" at menu_button_text_anim xalign 0.5 yalign 0.5
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
                text "Анықтама" style "main_menu_button_text" at menu_button_text_anim xalign 0.5 yalign 0.5
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
                text "Баптаулар" style "main_menu_button_text" at menu_button_text_anim xalign 0.5 yalign 0.5
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
                text "Ойын туралы" style "main_menu_button_text" at menu_button_text_anim xalign 0.5 yalign 0.5
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
                text "Шығу" style "main_menu_button_text" at menu_button_text_anim xalign 0.5 yalign 0.5
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

## Басты мәзір тақырыбының стилі
style main_menu_title:
    size 36
    bold True
    color "#d4af37"
    xalign 0.5

## Басты мәзір түймелерінің стилі
style main_menu_button:
    xsize 600
    ysize 92
    xalign 0.5
    background None
    hover_background None
    padding (14, 10)
    mouse "button"

style file_slot_delete_button:
    xsize 330
    ysize 36
    xalign 0.5
    background "#7a1b1b"
    hover_background "#b12b2b"
    padding (10, 6)
    mouse "button"

style file_slot_delete_button_text:
    color "#ffffff"
    hover_color "#ffffff"
    size 20
    bold True
    xalign 0.5
    text_align 0.5

style main_menu_button_text:
    color "#ffffff"
    hover_color "#d4af37"
    size 30
    hover_bold True
    xalign 0.5
    text_align 0.5

## Барлар үшін стильдер (жылжытқыштар)
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

## Анықтама экраны
screen help():
    tag menu
    layer "screens"

    default selected_category = "Кейіпкерлер"
    default selected_character = "Кенесары"

    add "images/bg/head_menu.png" size (1920, 1080)

    frame:
        xalign 0.5
        yalign 0.5
        xsize 1800
        ysize 900
        background None
        padding (0, 0)

        fixed:
            xysize (1800, 900)
            xalign 0.5
            yalign 0.5
            yoffset 0

            add Solid("#0000002a") xysize (1720, 860) xpos 40 ypos 56
            add Solid("#ffffff") xysize (1680, 820) xpos 60 ypos 40
            add Solid("#efe2c4") xysize (1648, 788) xpos 76 ypos 56

            # add "images/ui/scrip.png" xysize (140, 140) xpos 96 ypos 56 xoffset 824 yoffset -10

            fixed:
                xysize (1648, 788)
                xpos 76
                ypos 56
                xalign 0.0
                yalign 0.0

                add Solid("#c9b38b") xsize 2 ysize 788 xpos 260 ypos 0
                add Solid("#c9b38b") xsize 2 ysize 788 xpos 580 ypos 0
                add Solid("#c9b38b") xsize 1648 ysize 2 xpos 0 ypos 92

                text "САНАТТАР" style "help_header" xpos 32 ypos 28
                text "КЕЙІПКЕРЛЕР" style "help_header" xpos 300 ypos 28

                textbutton "← МӘЗІРГЕ ОРАЛУ" action Return() style "help_back_button":
                    xalign 1.0
                    yalign 0.0
                    xoffset -20
                    yoffset 20

                vbox:
                    xpos 32
                    ypos 130
                    spacing 16

                    textbutton "Кейіпкерлер" action SetScreenVariable("selected_category", "Кейіпкерлер") style ("help_item_button_selected" if selected_category == "Кейіпкерлер" else "help_item_button") text_style ("help_item_active" if selected_category == "Кейіпкерлер" else "help_item")
                    textbutton "Терминдер" action SetScreenVariable("selected_category", "Терминдер") style ("help_item_button_selected" if selected_category == "Терминдер" else "help_item_button") text_style ("help_item_active" if selected_category == "Терминдер" else "help_item")
                    textbutton "Оқиғалар" action SetScreenVariable("selected_category", "Оқиғалар") style ("help_item_button_selected" if selected_category == "Оқиғалар" else "help_item_button") text_style ("help_item_active" if selected_category == "Оқиғалар" else "help_item")

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

                add im.Scale("images/ui/bookmark.png", 110, 260) xpos 510 ypos 130 yoffset -178

                if is_character_unlocked(selected_character):
                    text "[selected_character]" style "help_title" xpos 620 ypos 128
                else:
                    text "???" style "help_title" xpos 620 ypos 128

                frame:
                    xpos 620
                    ypos 210
                    xsize 980
                    ysize 520
                    background None

                    hbox:
                        spacing 24

                        fixed:
                            xysize (360, 540)

                            add Solid("#00000014") xysize (332, 512) xpos 14 ypos 0
                            add Solid("#ffffff") xysize (332, 512) xpos 14 ypos 0
                            add Solid("#1b1b1b") xysize (300, 480) xpos 30 ypos 16


                            fixed:
                                xysize (300, 480)
                                xpos 30
                                ypos 16
                                clipping True

                                if not is_character_unlocked(selected_character):
                                    add Solid("#222222") xysize (300, 480)
                                    text "КЕЙІПКЕР АШЫЛМАҒАН" style "help_photo_label" xalign 0.5 yalign 0.85
                                elif selected_character == "Кенесары":
                                    add "images/characters/kenesary_khan.png" fit "cover" xysize (300, 480) xalign 0.5 yalign 0.5
                                elif selected_character == "Жанқожа":
                                    add "images/characters/zhankozha.png" fit "cover" xysize (300, 480) xalign 0.5 yalign 0.5
                                elif selected_character == "Ағыбай батыр":
                                    add "images/characters/agybai.png" fit "cover" xysize (300, 480) xalign 0.5 yalign 0.5
                                elif selected_character == "Наурызбай":
                                    add "images/characters/nauryzbai.png" fit "cover" xysize (300, 480) xalign 0.5 yalign 0.5
                                elif selected_character == "Бопай":
                                    add "images/characters/bopai.png" fit "cover" xysize (300, 480) xalign 0.5 yalign 0.5
                                else:
                                    add Solid("#222222") xysize (300, 480)
                                    text "БАТЫРДЫҢ ПОРТРЕТІ" style "help_photo_label" xalign 0.5 yalign 0.85

                            add "images/ui/vosk_marker.png" xysize (110, 110) xpos 290 ypos 440

                        frame:
                            xsize 12
                            ysize 520
                            background None
                            add Solid("#c9b38b") xsize 4 ysize 520 xpos 4 ypos 0

                        viewport:
                            style "help_text_viewport"
                            xysize (560, 520)
                            mousewheel True
                            scrollbars "vertical"
                            clipping True

                            vbox:
                                xsize 560
                                xmaximum 560
                                xfill True
                                spacing 18
                                if not is_character_unlocked(selected_character):
                                    text "Кейіпкер тарих өтуі барысында ашылады." style "help_body"
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
                                    text "Бопай ханым тек ханның қарындасы ғана емес, оның ең сенімді кеңесшілерінің бірі болды. Ол 600-ден астам сарбаздан тұратын ерекше жасақты басқарды. Бұл жасақ негізінен барлау жұмыстарымен, қамтамасыз ету мәселелерімен және жазалаушы отрядтарға тұтқиылдан соққы берумен айналысты. Бопай ханымның стратегиялық ойлау қабілеті мен ұйымдастырушылық дарыны Кенесары әскерінің ішкі тәртібін нығайтуға үлкен септігін тигізді." style "help_body"
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

        text "Анықтамада жаңа кейіпкер ашылды" style "help_body" xalign 0.5

## "Ойын туралы" экраны
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
            
            text "Кенесары - Соңғы Хан" size 42 bold True xalign 0.5 color "#d4af37"
            text "Нұсқа 1.0.0" size 24 xalign 0.5
            
            null height 40
            
            text "Соңғы қазақ ханы Кенесары Қасымұлының" size 22 xalign 0.5
            text "өміріне арналған тарихи визуалды роман" size 22 xalign 0.5
            
            null height 50
            
            text "Әзірлеген:" size 28 bold True xalign 0.5 color "#d4af37"
            text "Qazaq Games Studio" size 22 xalign 0.5
            
            null height 40
            
            text "© 2026 Барлық құқықтар қорғалған" size 18 xalign 0.5
            
        textbutton "Артқа" action Return() xalign 0.5 ypos 630 style "main_menu_button"

## Растау экраны
screen confirm(message, yes_action, no_action):
    modal True
    zorder 200
    
    # Жартылай мөлдір қара фон
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
                
                textbutton "Иә" action yes_action style "main_menu_button"
                textbutton "Жоқ" action no_action style "main_menu_button"

## Баптаулар экраны (негізгі)
screen preferences():
    tag menu
    layer "screens"
    
    add "images/bg/head_menu.png" size (1920, 1080)

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
            
            text "БАПТАУЛАР" size 40 bold True xalign 0.5 color "#d4af37"
            
            null height 20
            
            # Музыка дыбысы
            vbox:
                xalign 0.5
                spacing 8
                
                text "Музыка дыбысы:" size 24 color "#ffffff" xalign 0.5
                bar:
                    value Preference("music volume")
                    xsize 600
                    xalign 0.5
                    ysize 30
                    left_bar "#d4af37"
                    right_bar "#404040"
                    thumb "#ffffff"
            
            # Дыбыс эффектілері
            vbox:
                xalign 0.5
                spacing 8
                
                text "Дыбыс эффектілері:" size 24 color "#ffffff" xalign 0.5
                bar:
                    value Preference("sound volume")
                    xsize 600
                    xalign 0.5
                    ysize 30
                    left_bar "#d4af37"
                    right_bar "#404040"
                    thumb "#ffffff"
            
            # Толық экран
            hbox:
                xalign 0.5
                spacing 20
                
                text "Толық экран:" size 24 color "#ffffff" yalign 0.5
                textbutton "Қосу/Өшіру" action Preference("display", "toggle") yalign 0.5
            
            null height 20
            
            textbutton "Артқа" action Return() xalign 0.5 style "main_menu_button"

## Сақтау/жүктеу экрандары
screen save():
    tag menu
    use file_slots("ОЙЫНДЫ САҚТАУ", is_load=False)

screen load():
    tag menu
    use file_slots("ОЙЫНДЫ ЖҮКТЕУ", is_load=True)

# Сақтау ашылғанға дейін миниатюраны түсіру (менюсіз)
screen pre_save_capture():
    tag menu
    modal True

    on "show" action Hide("menu_window")

    # Бір кадрдан кейін экранды түсіреміз және сақтау экранын ашамыз
    timer 0.01 action [Function(renpy.take_screenshot), ShowMenu("save")]

screen file_slots(title, is_load=False):
    layer "screens"
    
    add "images/bg/head_menu.png" size (1920, 1080)
    
    frame:
        xalign 0.5
        yalign 0.5
        xsize 1200
        ysize 780
        background "#000000c0"
        padding (50, 40)
        
        vbox:
            xalign 0.5
            yalign 0.5
            spacing 24
            
            text title size 40 bold True xalign 0.5 color "#d4af37"
            
            null height 10
            
            grid 3 2:
                xalign 0.5
                yalign 0.5
                xsize 1042
                spacing 24
                xspacing 24
                yspacing 24
            
                for i in range(1, 7):
                    vbox:
                        xsize 330
                        xalign 0.5
                        spacing 8
                        
                        button:
                            xsize 330
                            ysize 150
                            background "#00000060"
                            hover_background "#d4af3720"
                            action (FileLoad(i) if is_load else FileSave(i))
                            
                            vbox:
                                spacing 6
                                add FileScreenshot(i) xysize (330, 90)
                                text FileTime(i, format="%d.%m.%Y %H:%M", empty="Бос") size 16 xalign 0.5
                                text FileSaveName(i) size 14 xalign 0.5
                        
                        textbutton "Өшіру" action Confirm("Сақтауды өшіргіңіз келе ме?", yes=FileDelete(i)) style "file_slot_delete_button"
            
            null height 6
            textbutton "Артқа" action Return() xalign 0.5 style "main_menu_button"

# HUD және жылдам мәзір тек ойын кезінде көрсетіледі, басты мәзірде емес
init python:
    # Оларды overlay_screens-ке қоспаймыз - олар тек ойында көрсетіледі
    pass
