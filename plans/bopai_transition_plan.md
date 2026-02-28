# План: уход Наурызбая вправо и выход Бопай слева

## Требования
- Наурызбай уходит вправо за 0.5с и становится прозрачным (alpha 0.0).
- Бопай плавно выходит слева до xalign 0.1, масштаб 0.7.

## Изменения в `game/transforms.rpy`
1. Добавить трансформ ухода Наурызбая (например `nauryzbai_exit_right`):
   - `zoom 0.7`, `alpha 1.0`, `xalign 0.5`, `yalign 1.0`
   - `ease 0.5 xalign 1.05 alpha 0.0`
2. Обновить трансформ Бопай:
   - заменить `bopai_center` на вход слева:
     - старт `xalign -0.05`, `alpha 0.0`, `zoom 0.7`
     - `ease 0.5 xalign 0.1 alpha 1.0`

## Изменения в `game/script.rpy`
- Вместо `hide nauryzbai_batyr` использовать:
  - `show nauryzbai_batyr at nauryzbai_exit_right`
- Заменить `show bopai at bopai_center` на `show bopai at bopai_left` (или обновленный `bopai_center`).

## Примечания
- Эти изменения повторяются в каждой ветке меню.
