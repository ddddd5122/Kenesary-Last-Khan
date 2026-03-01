## Настройки дисплея
define config.screen_width = 1920
define config.screen_height = 1080
define config.window_title = "Кенесары - Последний Хан"
define config.window_icon = "gui/window_icon.png"

init -1 python:
    config.default_music_volume = 0.08

    # Курсоры: обычный и при наведении на кликабельные элементы
    # Отключаем системный курсор, чтобы использовался config.mouse
    _preferences.system_cursor = False
    config.mouse = {
        "default": [("images/ui/cursor_1.png", 0, 0)],
        "button": [("images/ui/cursor_2.png", 0, 0)],
    }

    # Запуск в полноэкранном режиме
    if not persistent.fullscreen_set:
        _preferences.fullscreen = True
        persistent.fullscreen_set = True
    
    # После заставки показываем главное меню
    config.main_menu_music = "audio/music/main_menu.mp3"
    
    # Растягиваем изображения на весь экран
    config.adjust_view_size = None
    
    # КРИТИЧНО: Всегда показывать главное меню при запуске
    config.auto_load = None
    config.has_autosave = False
    config.has_quicksave = False
    
    # Отключаем автозапуск label start
    # Явно указываем, что хотим показать главное меню
    def force_main_menu():
        return False
    
    config.game_main_transition = None
    
# Трансформация для фоновых изображений
init python:
    # Автоматическое растягивание фонов
    config.default_transform = Transform(xysize=(config.screen_width, config.screen_height))
