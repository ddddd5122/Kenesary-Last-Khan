# План исправления видео фона на главном меню

## Дата: 2026-02-28
## Статус: Анализ завершен

---

## Проблема

На главном меню вместо видео фона отображается черный экран. Видеофайл [`main_menu_bg.webm`](../game/images/bg/main_menu_bg.webm) должен проигрываться в качестве анимированного фона, но не отображается.

---

## Анализ текущей реализации

### Текущая конфигурация в [`screens.rpy`](../game/screens.rpy):

**Экран фона (строки 35-40):**
```renpy
screen menu_background():
    layer "master"
    zorder -100
    
    # Видео фон (WebM формат, замедленное в 2 раза, без звука)
    add Movie(play="images/bg/main_menu_bg.webm", loop=True, size=(config.screen_width, config.screen_height))
```

**Экран главного меню (строки 43-61):**
```renpy
screen main_menu():
    tag menu
    layer "screens"
    
    # Показываем фон и включаем музыку
    on "show" action [Show("menu_background", _layer="master"), Play("music", "audio/music/main_menu.mp3", fadein=2.0)]
    
    # Меню кнопок
    vbox:
        xalign 0.5
        yalign 0.5
        spacing 25
        
        textbutton "Начать новую игру" action [Stop("music", fadeout=1.0), Jump("game_start")] style "main_menu_button"
        # ... остальные кнопки
```

### Проблема в [`script.rpy`](../game/script.rpy:29-32):

```renpy
label start:
    # Переходим в главное меню
    call screen main_menu
    return
```

---

## Выявленные проблемы

### 1. **Конфликт с системой главного меню Ren'Py**
   - Label `start` вызывает `call screen main_menu` вместо автоматического перехода
   - Это нарушает стандартный механизм показа главного меню
   - Главное меню должно показываться автоматически, а label `start` - это точка входа в игру

### 2. **Проблема с двойным указанием layer**
   - В определении экрана: `layer "master"` (строка 36)
   - При вызове: `Show("menu_background", _layer="master")` (строка 48)
   - Это может вызывать конфликт

### 3. **Возможные проблемы с форматом видео**
   - WebM может не поддерживаться на всех платформах
   - Отсутствует fallback на другие форматы (есть также `.mp4` и `.gif`)

### 4. **Проблема с размером видео**
   - Использование `size=(config.screen_width, config.screen_height)` может не работать корректно
   - Лучше использовать параметр `xysize` для Transform

---

## Доступные видеофайлы

В проекте есть три версии фонового видео:
- `game/images/bg/main_menu_bg.webm` (3.97 MB)
- `game/images/bg/main_menu_bg.mp4` (1.83 MB)
- `game/images/bg/main_menu_bg.gif` (13.36 MB)

---

## Предложенные решения

### Вариант 1: Исправление структуры (Рекомендуется)

**Преимущества:**
- Следует стандартной архитектуре Ren'Py
- Надежная работа видео фона
- Поддержка fallback форматов

**Изменения:**

1. **В `script.rpy`** - убрать вызов главного меню из label start:
```renpy
label start:
    # Label start вызывается когда игрок нажимает "Начать новую игру"
    jump game_start
```

2. **В `screens.rpy`** - переделать экран главного меню:
```renpy
screen main_menu():
    tag menu
    
    # Видео фон с fallback
    add Movie(play="images/bg/main_menu_bg.webm", loop=True) size (1920, 1080)
    
    # Если WebM не поддерживается, используем MP4
    # add Movie(play="images/bg/main_menu_bg.mp4", loop=True) size (1920, 1080)
    
    # Запуск музыки
    on "show" action Play("music", "audio/music/main_menu.mp3", fadein=2.0)
    
    # Меню кнопок (остается без изменений)
    vbox:
        xalign 0.5
        yalign 0.5
        spacing 25
        
        textbutton "Начать новую игру" action [Stop("music", fadeout=1.0), Start()] style "main_menu_button"
        # ... остальные кнопки
```

3. **Удалить экран `menu_background`** - он больше не нужен

### Вариант 2: Простое исправление текущей структуры

**Преимущества:**
- Минимальные изменения
- Быстрое решение

**Изменения:**

1. **В `screens.rpy`** - исправить определение экрана фона:
```renpy
screen menu_background():
    zorder -100
    
    # Видео фон без указания layer в определении
    add Movie(play="images/bg/main_menu_bg.webm", loop=True) xysize (1920, 1080)
```

2. **В `script.rpy`** - оставить как есть, но добавить показ фона:
```renpy
label start:
    # Показываем фон явно
    show screen menu_background
    # Переходим в главное меню
    call screen main_menu
    return
```

### Вариант 3: Использование Movie с Transform

**Преимущества:**
- Более надежное масштабирование
- Поддержка различных разрешений экрана

**Изменения:**

В `screens.rpy`:
```renpy
screen main_menu():
    tag menu
    
    # Видео фон с Transform для правильного масштабирования
    add Transform(Movie(play="images/bg/main_menu_bg.webm", loop=True), xysize=(config.screen_width, config.screen_height))
    
    # Музыка
    on "show" action Play("music", "audio/music/main_menu.mp3", fadein=2.0)
    
    # Меню кнопок
    vbox:
        xalign 0.5
        yalign 0.5
        spacing 25
        
        textbutton "Начать новую игру" action [Stop("music", fadeout=1.0), Start()] style "main_menu_button"
        # ... остальные кнопки
```

---

## Рекомендации

### Основная рекомендация: **Вариант 1**

Это наиболее правильное решение с архитектурной точки зрения:

1. **Следует стандартам Ren'Py:**
   - Главное меню показывается автоматически
   - Label `start` используется для начала игры
   - Простая и понятная структура

2. **Надежность:**
   - Видео находится непосредственно в экране главного меню
   - Нет сложных взаимодействий между слоями
   - Легко добавить fallback на другие форматы

3. **Производительность:**
   - Меньше экранов = меньше overhead
   - Нет дублирования логики

### Дополнительные рекомендации:

1. **Проверить кодеки видео:**
   - WebM может не поддерживаться на старых системах
   - MP4 более универсален
   - Рекомендуется предусмотреть fallback

2. **Оптимизация размера:**
   - GIF файл слишком большой (13 MB)
   - WebM или MP4 предпочтительнее

3. **Тестирование:**
   - Проверить на разных разрешениях экрана
   - Убедиться, что видео проигрывается плавно
   - Проверить загрузку на слабых системах

---

## Следующие шаги

1. Выбрать один из вариантов решения
2. Внести изменения в соответствующие файлы
3. Протестировать работу главного меню
4. При необходимости добавить fallback на другие форматы видео

---

## Дополнительная информация

### Формат Movie в Ren'Py:

```renpy
Movie(play="путь/к/видео.webm", loop=True)
```

Параметры:
- `play` - путь к видеофайлу (относительно папки game/)
- `loop` - зацикливание видео
- `size` - размер (лучше использовать через Transform с xysize)

### Поддерживаемые форматы:
- **WebM** - хорошее сжатие, не все платформы
- **MP4** - универсальная поддержка
- **OGV** - альтернатива WebM

### Структура label в Ren'Py:
- `label start` - точка входа при нажатии "Начать игру"
- `label main_menu` - специальный label для возврата в меню
- `label splashscreen` - показывается перед главным меню
