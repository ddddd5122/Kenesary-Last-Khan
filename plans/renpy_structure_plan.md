# План: структура проекта Ren’Py 7.4.x (ПК)

## 1) Целевой контекст
- Платформы: ПК (Windows/macOS/Linux)
- Версия движка: Ren’Py 7.4.x для совместимости со старыми проектами

## 2) Рекомендуемая структура каталогов
```
project_root/
├─ game/
│  ├─ script.rpy
│  ├─ options.rpy
│  ├─ gui.rpy
│  ├─ screens.rpy
│  ├─ characters.rpy
│  ├─ variables.rpy
│  ├─ transforms.rpy
│  ├─ scripts/
│  │  ├─ prologue.rpy
│  │  ├─ chapter_01.rpy
│  │  └─ chapter_02.rpy
│  ├─ images/
│  │  ├─ bg/
│  │  ├─ cg/
│  │  └─ characters/
│  ├─ audio/
│  │  ├─ music/
│  │  ├─ sfx/
│  │  └─ voice/
│  ├─ gui/
│  └─ tl/
├─ launcher/
└─ renpy/
```

## 3) Ключевые файлы Ren’Py и назначение
- `game/script.rpy` — точка входа, `label start`, базовые `define`.
- `game/options.rpy` — настройки игры (название, версия, кодировка, окно).
- `game/gui.rpy` — стили и оформление GUI.
- `game/screens.rpy` — экраны интерфейса (меню, диалоги, настройки).
- `game/characters.rpy` — описания персонажей (`define e = Character(...)`).
- `game/variables.rpy` — глобальные переменные, флаги, состояния.
- `game/transforms.rpy` — трансформы и анимации.
- `game/scripts/*.rpy` — сюжетные главы/сцены.
- `game/images/` — фоны, персонажи, CG.
- `game/audio/` — музыка, SFX, озвучка.
- `game/gui/` — изображения интерфейса.
- `game/tl/` — локализации (если планируются).

## 4) Минимальные правила именования
- **Скрипты**: `snake_case` без пробелов, например `chapter_01.rpy`.
- **Лейблы**: `label chapter_01_intro`, `label prologue_end`.
- **Персонажи**: `define e = Character("Ева")`, идентификатор — короткий `snake_case`.
- **Фоны**: `bg_city_day`, `bg_room_night`.
- **Персонажи**: `ch_eva_happy`, `ch_eva_sad`.
- **CG**: `cg_reveal_01`, `cg_finale`.
- **Музыка**: `music_theme_main`, `music_tension_01`.
- **SFX**: `sfx_door_open`, `sfx_rain`.
- **Озвучка**: `voice_eva_0001`.

## 5) Итоговая сводка
Структура ориентирована на Ren’Py 7.4.x и ПК-таргет. Она разделяет логику (скрипты, переменные, трансформы), контент (изображения, аудио) и интерфейс (gui, screens), что упрощает масштабирование и поддержку проекта.
