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
        text _("Қор: [treasury]") size 18
        text _("Дипломатия: [diplomacy]") size 18


screen quick_menu():
    zorder 100

    hbox:
        xalign 0.5
        yalign 0.98
        spacing 12

        textbutton _( "Назад" ) action Rollback()
        textbutton _( "Пропустить" ) action Skip()


## Главное меню с видео фоном
screen main_menu():
    tag menu
    
    # Запуск музыки при инициализации экрана
    python:
        if not renpy.music.get_playing(channel='music'):
            renpy.music.play("audio/music/main_menu.mp3", channel='music', fadein=2.0)
    
    # Видео фон (WebM формат)
    add Movie(play="images/bg/main_menu_bg.webm", loop=True) size (1920, 1080)
    
    # Меню кнопок
    vbox:
        xalign 0.5
        yalign 0.5
        spacing 25
        
        textbutton "Начать новую игру" action [Stop("music", fadeout=1.0), Jump("start_game")] style "main_menu_button"
        textbutton "Продолжить" action ShowMenu("load") style "main_menu_button"
        textbutton "Справочник" action ShowMenu("help") style "main_menu_button"
        textbutton "Настройки" action ShowMenu("preferences") style "main_menu_button"
        textbutton "Об игре" action ShowMenu("about") style "main_menu_button"
        textbutton "Выход" action Quit(confirm=True) style "main_menu_button"

## Стиль кнопок главного меню
style main_menu_button:
    size 32
    xsize 400
    ysize 60
    xalign 0.5
    background "#00000090"
    hover_background "#d4af37c0"
    padding (20, 10)

style main_menu_button_text:
    color "#ffffff"
    hover_color "#000000"
    size 28
    xalign 0.5

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
    
    frame:
        xalign 0.5
        yalign 0.5
        xsize 1400
        ysize 900
        background "#000000c0"
        padding (50, 40)
        
        viewport:
            scrollbars "vertical"
            mousewheel True
            
            vbox:
                spacing 40
                
                # Заголовок
                text "СПРАВОЧНИК" size 50 bold True xalign 0.5 color "#d4af37"
                
                null height 20
                
                text "Персонажи" size 40 bold True color "#d4af37"
                
                # Кенесары-хан
                hbox:
                    spacing 30
                    add "images/characters/kenesary_khan.png" xysize (200, 300)
                    vbox:
                        text "Кенесары Касымулы" size 32 bold True
                        null height 10
                        text "Последний казахский хан (1802-1847)" size 24
                        null height 15
                        text "Возглавил народное восстание против царской России\nи Кокандского ханства." size 20
                
                null height 30
                
                # Агыбай батыр
                hbox:
                    spacing 30
                    add "images/characters/agybai.png" xysize (200, 300)
                    vbox:
                        text "Агыбай батыр" size 32 bold True
                        null height 10
                        text "Верный соратник хана" size 24
                        null height 15
                        text "Храбрый воин и советник Кенесары." size 20
                
                null height 30
                
                # Наурызбай батыр
                hbox:
                    spacing 30
                    add "images/characters/nauryzbai.png" xysize (200, 300)
                    vbox:
                        text "Наурызбай батыр" size 32 bold True
                        null height 10
                        text "Отважный воин" size 24
                        null height 15
                        text "Один из ближайших соратников хана." size 20
        
        textbutton "Назад" action Return() xalign 0.5 ypos 850 style "main_menu_button"

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

## Экран загрузки/сохранения (базовый)
screen load():
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
            spacing 30
            
            text "ЗАГРУЗИТЬ ИГРУ" size 40 bold True xalign 0.5 color "#d4af37"
            
            null height 30
            
            text "Сохранений пока нет" size 24 xalign 0.5
            
            null height 30
            
            textbutton "Назад" action Return() xalign 0.5 style "main_menu_button"

# HUD и быстрое меню показываются только во время игры, а не в главном меню
init python:
    # Не добавляем их в overlay_screens - они будут показываться только в игре
    pass
