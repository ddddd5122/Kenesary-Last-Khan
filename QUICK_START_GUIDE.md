# 🚀 Быстрый старт: Визуальная настройка игры "Кенесары"

## 📌 Краткое руководство

### Шаг 1: Подготовка графики

**Создайте папки и добавьте изображения:**

```bash
# В папке game/ создайте:
mkdir -p images/splash images/logo audio/music audio/sound
```

**Нужные файлы (минимум):**
1. `game/images/splash/studio_logo.png` — логотип студии (1920x1080)
2. `game/images/logo/game_title.png` — название игры
3. `game/images/bg/main_menu_bg.jpg` — фон главного меню (1920x1080)
4. `game/audio/music/main_menu.mp3` — музыка для меню

---

### Шаг 2: Создать файл заставки

**Создайте файл [`game/splash.rpy`](game/splash.rpy):**

```renpy
# Заставка с логотипом студии
label splashscreen:
    scene black
    with Pause(1)
    
    show image "images/splash/studio_logo.png" at truecenter
    with dissolve
    pause 3.0
    
    hide image "images/splash/studio_logo.png"
    with dissolve
    
    return
```

---

### Шаг 3: Настроить полный экран

**Откройте [`game/options.rpy`](game/options.rpy) и добавьте:**

```renpy
# В начало файла
define config.screen_width = 1920
define config.screen_height = 1080
define config.window_title = "Кенесары - Последний Хан"

# В конец файла
init python:
    if not persistent.fullscreen_set:
        _preferences.fullscreen = True
        persistent.fullscreen_set = True
```

---

### Шаг 4: Обновить главное меню

**Откройте [`game/screens.rpy`](game/screens.rpy)** и найдите `screen main_menu()`.

**Замените на:**

```renpy
screen main_menu():
    tag menu
    
    # Фон
    add "images/bg/main_menu_bg.jpg"
    
    # Логотип игры (если есть)
    add "images/logo/game_title.png" xalign 0.5 ypos 100
    
    # Музыка
    on "show" action Play("music", "audio/music/main_menu.mp3", fadein=2.0)
    
    # Меню
    vbox:
        xalign 0.5
        yalign 0.65
        spacing 25
        
        textbutton "Начать новую игру" action Start() style "main_menu_button"
        textbutton "Продолжить" action ShowMenu("load") style "main_menu_button"
        textbutton "Справочник" action ShowMenu("help") style "main_menu_button"
        textbutton "Настройки" action ShowMenu("preferences") style "main_menu_button"
        textbutton "Об игре" action ShowMenu("about") style "main_menu_button"
        textbutton "Выход" action Quit(confirm=True) style "main_menu_button"

# Стиль кнопок главного меню
style main_menu_button:
    size 32
    xsize 400
    ysize 60
    background "#00000080"
    hover_background "#d4af3780"
```

---

### Шаг 5: Добавить экран "Справочник"

**В [`game/screens.rpy`](game/screens.rpy) добавьте:**

```renpy
screen help():
    tag menu
    
    use game_menu("Справочник"):
        viewport:
            scrollbars "vertical"
            mousewheel True
            
            vbox:
                spacing 40
                
                # Заголовок
                text "Персонажи" size 40 bold True
                
                # Кенесары-хан
                hbox:
                    spacing 30
                    add "images/characters/kenesary_khan.png" xysize (250, 350)
                    vbox:
                        text "Кенесары Касымулы" size 32 bold True
                        text "Последний казахский хан (1802-1847)" size 24
                        null height 20
                        text "Возглавил народное восстание против царской России и Кокандского ханства." size 20
                
                null height 30
                
                # Агыбай батыр
                hbox:
                    spacing 30
                    add "images/characters/agybai.png" xysize (250, 350)
                    vbox:
                        text "Агыбай батыр" size 32 bold True
                        text "Верный соратник хана" size 24
                        null height 20
                        text "Храбрый воин и советник Кенесары." size 20
                
                null height 30
                
                # Наурызбай батыр
                hbox:
                    spacing 30
                    add "images/characters/nauryzbai.png" xysize (250, 350)
                    vbox:
                        text "Наурызбай батыр" size 32 bold True
                        text "Отважный воин" size 24
                        null height 20
                        text "Один из ближайших соратников хана." size 20
                
                textbutton "Назад" action Return() xalign 0.5
```

---

### Шаг 6: Добавить экран "Об игре"

**В [`game/screens.rpy`](game/screens.rpy) добавьте:**

```renpy
screen about():
    tag menu
    
    use game_menu("Об игре"):
        vbox:
            xalign 0.5
            yalign 0.5
            spacing 30
            
            text "Кенесары - Последний Хан" size 42 bold True xalign 0.5
            text "Версия 1.0.0" size 24 xalign 0.5
            
            null height 40
            
            text "Историческая визуальная новелла о жизни" size 22 xalign 0.5
            text "последнего казахского хана Кенесары Касымулы" size 22 xalign 0.5
            
            null height 50
            
            text "Разработано:" size 28 bold True xalign 0.5
            text "[Название вашей студии]" size 22 xalign 0.5
            
            null height 40
            
            text "© 2026 Все права защищены" size 18 xalign 0.5
            
            null height 30
            
            textbutton "Назад" action Return() xalign 0.5
```

---

### Шаг 7: Запуск и тестирование

1. **Запустите Ren'Py Launcher:**
   ```bash
   cd renpy-7.4.11-sdk
   ./renpy.sh   # или renpy.exe на Windows
   ```

2. **Выберите проект "game"**

3. **Нажмите "Launch Project"**

4. **Проверьте:**
   - ✅ Появляется заставка с логотипом
   - ✅ Игра запускается на полный экран
   - ✅ Главное меню отображается
   - ✅ Работает кнопка "Начать новую игру"
   - ✅ Открывается "Справочник"
   - ✅ Открывается "Об игре"

---

### Шаг 8: Сборка дистрибутива

1. **В Ren'Py Launcher выберите "Build Distributions"**

2. **Выберите платформы:**
   - ✅ PC: Windows and Linux
   - ✅ Mac
   - ✅ Android (если нужно)

3. **Нажмите "Build"**

4. **Готовые файлы будут в папке `game-dists/`**

---

## 🎨 Где взять графику?

### Временные решения для тестирования:

1. **Логотип студии:** Создайте в Canva / Figma или используйте текст
2. **Фон меню:** Используйте существующие фоны степи из [`game/images/bg/`](game/images/bg/)
3. **Логотип игры:** Красивый текст с названием игры

### Рекомендации:
- **Размер изображений:** 1920x1080 для фонов
- **Формат:** PNG для прозрачности, JPG для фонов
- **Стиль:** Казахская тематика, исторический стиль

---

## 🔧 Полезные настройки

### Шрифты с поддержкой кириллицы

**Добавьте в [`game/gui.rpy`](game/gui.rpy):**

```renpy
define gui.text_font = "DejaVuSans.ttf"
define gui.name_text_font = "DejaVuSans-Bold.ttf"
define gui.interface_text_font = "DejaVuSans.ttf"

define gui.text_size = 28
define gui.name_text_size = 36
```

### Казахская цветовая палитра

```renpy
define gui.accent_color = '#d4af37'      # Золотой
define gui.hover_color = '#00a9e0'       # Небесно-голубой
define gui.selected_color = '#d4af37'
define gui.text_color = '#ffffff'
```

---

## 📚 Дополнительная документация

- **Детальный план:** [`plans/game_visual_setup_plan.md`](plans/game_visual_setup_plan.md)
- **Структура проекта:** [`project_structure.md`](project_structure.md)
- **Документация Ren'Py:** [`renpy-7.4.11-sdk/doc/index.html`](renpy-7.4.11-sdk/doc/index.html)

---

## ❓ Частые вопросы

**Q: Игра не запускается на полный экран?**
A: Нажмите `Alt+Enter` или `F11` для переключения режима.

**Q: Кириллица отображается неправильно?**
A: Убедитесь, что используете шрифт с поддержкой кириллицы (DejaVu Sans, Noto Sans).

**Q: Как изменить язык интерфейса?**
A: В настройках игры есть опция выбора языка (если настроена локализация).

**Q: Где найти исходный код сценария?**
A: Основной сценарий в [`game/script.rpy`](game/script.rpy), дополнительные главы в [`game/scripts/`](game/scripts/).
