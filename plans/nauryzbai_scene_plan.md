# План: дистанция между персонажами, новый фон и Наурызбай

## Требования
- Kenesary xalign 0.1, Agybai xalign 0.9.
- Agybai масштаб 0.72 (20% больше относительно 0.6).
- Плавное появление/сдвиг 0.5с.
- После реплик Агыбая: затемнение экрана, смена фона на `images/bg/bg-2.jpg` и появление Наурызбая в центре (scale 0.7) с плавной появой.

## Изменения в `game/transforms.rpy`
1. Обновить/заменить трансформы:
   - `kenesary_dim_left` → xalign 0.1, alpha 0.7, zoom 0.6, ease 0.5.
   - `agybai_right` → xalign 0.9, zoom 0.72, alpha 1.0, ease 0.5 (старт xalign 1.05).
2. Добавить трансформ для Наурызбая:
   - `nauryzbai_center` → zoom 0.7, alpha 0.0 → ease 0.5 alpha 1.0, xalign 0.5, yalign 1.0.

## Изменения в `game/script.rpy`
1. Добавить фон:
   - `image bg_2 = "images/bg/bg-2.jpg"`
2. Добавить образ:
   - `image nauryzbai_batyr = "images/characters/nauryzbai_batyr.png"`
3. После трёх реплик Агыбая (в каждой ветке меню):
   - `scene black` с `with fade` (или `with dissolve`)
   - `scene bg_2` + `with fade`
   - `show nauryzbai_batyr at nauryzbai_center`
4. Озвучка Наурызбая:
   - `voice "<from 0.0 to 6.910>voices/nb_1.mp3"`
     «Аға! Казактардың барлаушылары бір күндік жерде жүр. Жігіттердің қаны қайнап, ұрысқа асығуда.»
   - `voice "<from 6.910>voices/nb_1.mp3"`
     «Әміріңді бер, хан ие — түнделетіп барып, бәрін жайратып салайық!»

## Примечания
- Переходы можно подстроить после визуальной проверки.
- Если нужно, можно скрыть предыдущих персонажей перед `scene black`.
