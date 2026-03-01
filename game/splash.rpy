# Студия логотипімен бастапқы экран
label splashscreen:
    scene black
    with Pause(1)
    
    # Студия логотипін көрсетеміз
    show image "images/splash/studio_logo.jpg" at truecenter
    with dissolve
    pause 3.0
    
    scene black
    with dissolve
    
    # label start іске қосудың орнына басты мәзірге қайтамыз
    return
