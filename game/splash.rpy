# Заставка с логотипом студии
label splashscreen:
    scene black
    with Pause(1)
    
    # Показываем логотип студии
    show image "images/splash/studio_logo.jpg" at truecenter
    with dissolve
    pause 3.0
    
    scene black
    with dissolve
    
    # Возвращаемся в главное меню вместо запуска label start
    return
