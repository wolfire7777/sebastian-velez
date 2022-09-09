basic.show_string("¡¡¡Hola Mundo!!!")

def on_forever():
    basic.show_string("Sebastian")
    basic.show_icon(IconNames.HEART)
    basic.pause(2000)
    basic.clear_screen()
basic.forever(on_forever)
