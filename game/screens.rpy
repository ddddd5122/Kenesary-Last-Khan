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


init python:
    if "stats_hud" not in config.overlay_screens:
        config.overlay_screens.append("stats_hud")
    if "quick_menu" not in config.overlay_screens:
        config.overlay_screens.append("quick_menu")
