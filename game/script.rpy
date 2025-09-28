define n = Character("Narrador")

transform floating_map:
    linear 3.0 yoffset 10
    linear 3.0 yoffset -10
    repeat

transform small_icon:
    zoom 0.15
    alpha 0.8

image bg_guerra = Movie(
    play="CampoBatalla.webm",
    loop=True,
    size=(config.screen_width, config.screen_height)
)

label start:

    play music "musica_batalla.ogg" fadein 2.0

    scene bg_guerra
    window show
    n "Estás en el campo de batalla, defendiendo de los ataques enemigos."
    n "Luchas junto a tus compañeros con armas viejas y poca munición."

    # Video 2
    show Movie("Disparo.webm") as v2 with fade
    n "Un estruendo corta el silencio. El disparo atraviesa tu carne, y todo se apaga."
    n "La oscuridad te envuelve… el dolor desaparece. No queda cuerpo, solo vacío."

    # Video 3
    show Movie("Masacre.webm") as v3 with fade
    n "Abres los ojos, pero ya no son ojos de carne. Tus manos tiemblan, translúcidas, fantasmales."
    n "Has dejado el cuerpo atrás, y sin embargo sigues aquí, en medio de la guerra."
    n "El suelo está sembrado de cuerpos sin vida, hermanos caídos..."
    n "El aire es denso, la bruma lo cubre todo… pero aún puedes sentir la esperanza que dejaron en su último aliento."

    # Video 4
    show Movie("SoldadoNota.webm") as v4 with fade
    n "Entre tantos cuerpos, uno atrae tu mirada. Su mano aferrada a un papel manchado de sangre resiste incluso a la muerte."

    # Video 5
    show Movie("TomandoNota.webm") as v5 with fade
    n "Extiendes tu mano espectral y tomas la nota."
    n "El papel se ilumina bajo tu tacto, como si reconociera tu espíritu."
    n "\"Los días cada vez son más duros, lucha tras lucha y muerte tras muerte...\""
    n "\"No sueño con otro día de vida… sueño con un futuro soberano.\""

    # Video 6
    show Movie("Levantar.webm") as v6 with fade
    n "Tus rodillas se clavan en la tierra. La rabia arde en tu pecho, más fuerte que el miedo."
    n "Comprendes que no has vuelto para descansar, sino para luchar desde la memoria."

    # Video 7
    show Movie("Tumbas.webm") as v7 with fade
    n "Cuando levantas la mirada, el campo se transforma."
    n "Un sendero de tumbas se abre frente a ti, cada una marcada por un marco vacío..."
    n "Flores frescas reposan sobre ellas, y en cada pétalo palpita la gratitud de un pueblo."
    n "No hay olvido en estas cruces mudas."
    n "Aquí viven los guerreros que dieron su vida por la libertad de Nicaragua..."
    n "Aunque sus cuerpos no fueran hallados, aunque sus nombres se perdieran en la bruma..."
    n "Siguen vivos en el corazón de su patria… como raíces, como orgullo eterno."

    # Video final
    show Movie("TumbaBanderas.webm") as v8 with fade
    n "QUIEN NO CONOCE SU HISTORIA ESTA CONDENADO A REPETIRLA..."

    call screen mapa_menu

label historia1:
    scene bg city with fade
    "Aquí empieza la primera historia..."
    return

label historia2:
    scene bg jungle with fade
    "Aquí empieza la segunda historia..."
    return

# Pantalla del mapa
screen mapa_menu():
    tag menu 

    add Movie(play="lago.webm", loop=True) xysize(1.0, 1.0) 

    add "menu.png" at floating_map xalign 0.5 yalign 0.5

    imagebutton:
        idle "icono1.png"
        xpos 800
        ypos 250
        at small_icon
        action Jump("historia1")

    imagebutton:
        idle "icono2.png"
        xpos 700
        ypos 500
        at small_icon
        action Jump("historia2")




