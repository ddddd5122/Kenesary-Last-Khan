## Дисплей баптаулары
define config.screen_width = 1920
define config.screen_height = 1080
define config.window_title = "Кенесары - Соңғы Хан"
define config.window_icon = "gui/window_icon.png"

## Тіл баптаулары
define config.language = "kazakh"

init -1 python:
    config.default_music_volume = 0.08
    
    # Стандартты хабарламаларды аудару
    config.quit_action = ui.callsinnewcontext("confirm", message="Шынымен шығуды қалайсыз ба?", yes=Quit(confirm=False), no=Return())

    # Курсорлар: қарапайым және басқару элементтеріне нұсқағанда
    # Жүйелік курсорды өшіреміз, config.mouse пайдалану үшін
    _preferences.system_cursor = False
    config.mouse = {
        "default": [("images/ui/cursor_1.png", 0, 0)],
        "button": [("images/ui/cursor_2.png", 0, 0)],
    }

    # Толық экран режимінде іске қосу
    if not persistent.fullscreen_set:
        _preferences.fullscreen = True
        persistent.fullscreen_set = True
    
    # Бастапқы экраннан кейін басты мәзірді көрсету
    config.main_menu_music = "audio/music/main_menu.mp3"
    
    # Суреттерді бүкіл экранға созу
    config.adjust_view_size = None
    
    # МАҢЫЗДЫ: Іске қосқанда әрқашан басты мәзірді көрсету
    config.auto_load = None
    config.has_autosave = False
    config.has_quicksave = False
    
    # label start автоматты іске қосуды өшіру
    # Басты мәзірді көрсеткіміз келетінін анық көрсету
    def force_main_menu():
        return False
    
    config.game_main_transition = None
    
# Фондық суреттерге арналған трансформация
init python:
    # Фондарды автоматты түрде созу
    config.default_transform = Transform(xysize=(config.screen_width, config.screen_height))
