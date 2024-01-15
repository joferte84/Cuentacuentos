from flask import Flask, render_template, request
import openai
import random

app = Flask(__name__)

temas = {
    "historicos": [
        "En la corte de un reino antiguo, donde las conspiraciones se entrelazan con el destino.",
        "Durante el auge y caída de un imperio poderoso, donde los héroes y traidores son forjados.",
        "En las arenas de gladiadores romanos, un luchador busca la libertad.",
        "En el descubrimiento de nuevas tierras, donde exploradores y nativos se enfrentan.",
        "En la época de la Revolución Francesa, donde ideales y realidades chocan.",
        "Bajo el reinado de la Reina Victoria, en una era de cambio e innovación.",
        "En el corazón de la Guerra Civil Americana, donde la lealtad y la traición se mezclan.",
        "Durante la construcción de las grandes pirámides de Egipto, un misterio se desvela.",
        "En la época dorada de los samuráis en Japón, donde el honor lo es todo. ",
        "En las cruzadas medievales, donde caballeros y reyes buscan gloria. "
    ],
    "fantasia": [
        "En un reino encantado, donde la magia y los misterios abundan. ",
        "Bajo la sombra de un dragón milenario, una aldea busca un héroe. ",
        "En la cima de una torre encantada, un hechicero revela secretos antiguos.",
        "En un bosque embrujado, criaturas mágicas y humanos forjan un pacto.",
        "En un mundo donde los sueños y la realidad se entrelazan.",
        "En las ruinas de un castillo, un artefacto mágico espera ser descubierto.",
        "Bajo un cielo estrellado, un astrólogo descubre un destino profético.",
        "En un mercado mágico, un objeto misterioso cambia manos.",
        "En un reino dividido por clanes mágicos, una princesa busca la paz.",
        "En la noche de un eclipse, un ritual mágico tiene lugar."
    
    ],
    "elfos_y_enanos": [
        "En un antiguo bosque, elfos y enanos se unen contra un enemigo común.",
        "Bajo las montañas, una alianza frágil entre enanos y elfos se pone a prueba.",
        "En la forja de un reino enano, un elfo descubre un secreto ancestral.",
        "En un valle sagrado, elfos y enanos compiten en un torneo legendario.",
        "Una aldea enana está bajo asedio, y solo un grupo de elfos puede salvarla.",
        "Durante una tregua, un enano y un elfo descubren una conspiración.",
        "Una amistad inesperada surge en un viaje peligroso entre un elfo y un enano.",
        "En la búsqueda de un artefacto perdido, elfos y enanos enfrentan desafíos juntos.",
        "Un pacto antiguo entre las razas de elfos y enanos se ve amenazado.",
        "En la celebración de una alianza, un evento inesperado pone a prueba la confianza entre elfos y enanos."
        ],
    "estilo_star_wars": [
        "En una estación espacial remota, rebeldes planean su próximo movimiento.",
        "Un joven descubre su conexión con la Fuerza en un planeta olvidado.",
        "Una batalla épica entre cazas estelares sobre un planeta de hielo.",
        "Un maestro Jedi exiliado es llamado de nuevo a la acción.",
        "Un droide con información crucial se pierde en un vasto desierto.",
        "El enfrentamiento final entre el bien y el mal en la Estrella de la Muerte.",
        "Un piloto rebelde se infiltra en una base imperial.",
        "Un aprendiz Sith lucha con su lealtad al Lado Oscuro.",
        "Una princesa lidera la resistencia contra un imperio tiránico.",
        "En un bar de otra galaxia, se forman alianzas inesperadas."
        ],
    "el_señor_de_los_anillos": [
        "En las colinas verdes de la Comarca, un hobbit encuentra un anillo misterioso.",
        "Un consejo en Rivendel decide el destino de un poderoso anillo.",
        "En las Minas de Moria, un grupo de viajeros se enfrenta a sombras antiguas.",
        "Un reino humano en ruinas lucha por su supervivencia contra un ejército de orcos.",
        "El retorno de un rey marca el comienzo de una gran batalla por la Tierra Media.",
        "Un elfo y un enano forman una amistad inesperada en un viaje épico.",
        "Los Ents, antiguos guardianes del bosque, se alzan para proteger su tierra.",
        "Un mago enfrenta su caída y renacimiento en la lucha contra la oscuridad.",
        "En las llanuras de Rohan, un ejército se reúne para enfrentar una amenaza inminente.",
        "El viaje solitario de un hobbit hacia la Montaña del Destino para destruir el anillo."
    ],
    "novelas_cortas": [
        "Un encuentro fortuito en una cafetería cambia dos vidas para siempre.",
        "Una carta misteriosa lleva a un descubrimiento familiar inesperado.",
        "Una noche de invierno, un viejo recuerdo revive en la mente de un escritor.",
        "Dos amigos se reencuentran después de años y revelan secretos ocultos.",
        "Un sueño recurrente guía a una persona a una revelación sorprendente.",
        "Una pequeña tienda de antigüedades esconde un objeto con un pasado extraordinario.",
        "Un breve viaje en tren lleva a una aventura inesperada.",
        "Una decisión impulsiva conduce a una serie de eventos inolvidables.",
        "Un momento de claridad cambia la perspectiva de alguien sobre la vida.",
        "Una conversación en un parque revela una historia de amor perdida."
    ],
    "policiacas": [
        "Un detective novato recibe un caso que podría hacer o deshacer su carrera.",
        "Una serie de crímenes en una pequeña ciudad revela secretos oscuros.",
        "Una huella inusual es la clave para resolver un crimen misterioso.",
        "Un caso de desaparición lleva a un detective a un submundo criminal.",
        "Una evidencia falsificada pone en duda la integridad de una investigación.",
        "Un crimen aparentemente perfecto desafía a los mejores detectives.",
        "Una investigación sobre un robo lleva a una conspiración mucho mayor.",
        "Un asesinato en un hotel de lujo esconde más de lo que parece.",
        "Una pista olvidada reabre un caso de hace años.",
        "Una carrera contra el tiempo para detener a un asesino en serie antes de su próximo ataque."
    ],
        "aventuras_espaciales": [
        "En una nave perdida al borde de la galaxia, la tripulación descubre un secreto antiguo.",
        "Un explorador espacial aterriza en un planeta desconocido, lleno de misterios.",
        "Una carrera contra el tiempo para salvar una estación espacial de un desastre inminente.",
        "El primer contacto con una civilización alienígena no sale como se esperaba.",
        "Un piloto rebelde se embarca en una misión para desentrañar una conspiración galáctica.",
        "Una expedición a un asteroide revela más que solo minerales raros.",
        "El rescate de un astronauta perdido lleva a descubrimientos inesperados.",
        "Una guerra intergaláctica se desata, y un héroe improbable emerge.",
        "Una anomalía espacial lleva a un grupo de científicos a un viaje sin retorno.",
        "Un planeta artificial, una maravilla tecnológica, esconde un peligro desconocido."
    ],
    "distopia_futurista": [
        "En una ciudad controlada por una inteligencia artificial, un grupo de rebeldes planea una revolución.",
        "En un mundo donde los recuerdos pueden ser borrados, alguien lucha por conservar los suyos.",
        "La última colonia humana en la Tierra lucha por sobrevivir en un entorno hostil.",
        "Una sociedad dividida por el bio-aumento enfrenta un punto de quiebre.",
        "Un detective en una ciudad futurista investiga un crimen que desafía la realidad.",
        "En un futuro donde el agua es más valiosa que el oro, un héroe se alza.",
        "Un virus informático se convierte en una amenaza para la humanidad.",
        "La resistencia humana contra robots opresores toma un giro inesperado.",
        "Una ciudad utópica bajo una cúpula enfrenta su primera crisis.",
        "Una rebelión en un mundo donde las emociones han sido suprimidas."
    ],
    "misterio_sobrenatural": [
        "Una casa aparentemente normal esconde secretos sobrenaturales inquietantes.",
        "Una serie de eventos paranormales lleva a un grupo de amigos a investigar un antiguo misterio.",
        "Un investigador de lo paranormal se enfrenta a su caso más peligroso.",
        "En un pequeño pueblo, los habitantes empiezan a experimentar fenómenos inexplicables.",
        "Una médium recibe mensajes del más allá que conducen a una verdad oculta.",
        "La aparición de un fantasma en una escuela desata una serie de misterios.",
        "Un libro antiguo encontrado en un ático despierta fuerzas desconocidas.",
        "Un hotel abandonado resulta ser el centro de actividades paranormales.",
        "Un espejo antiguo muestra más que el reflejo de quien lo mira.",
        "Una serie de sueños premonitorios llevan a una revelación sorprendente."
    ],
    "viajes_en_el_tiempo": [
        "Un error en una máquina del tiempo envía a un científico a una era desconocida.",
        "En un futuro distópico, una persona encuentra la forma de regresar al pasado.",
        "Un viajero del tiempo intenta corregir un error que cambió el curso de la historia.",
        "Una pareja descubre un reloj que puede llevarlos a cualquier punto en el tiempo.",
        "Un grupo de amigos accidentalmente se transporta a momentos clave de la historia.",
        "Un historiador del futuro viaja al pasado para presenciar eventos históricos.",
        "Una agencia de viajes en el tiempo ofrece excursiones a épocas pasadas.",
        "Un experimento de viaje en el tiempo se convierte en una lucha por sobrevivir.",
        "En un mundo donde el tiempo fluye de manera diferente, un héroe emerge.",
        "Una guerra a través del tiempo amenaza con cambiar la historia para siempre."
    ],
    "utopia_idealista": [
        "En una sociedad perfecta, un ciudadano comienza a cuestionar la realidad a su alrededor.",
        "En un mundo sin enfermedades ni guerras, un científico descubre un oscuro secreto.",
        "Una utopía tecnológica enfrenta su primera gran crisis.",
        "Bajo una paz mundial aparente, se esconde una resistencia que busca la verdad.",
        "Un experimento social crea la comunidad perfecta, pero a un costo inesperado.",
        "Una ciudad del futuro, libre de crimen, enfrenta un dilema moral inesperado.",
        "En una sociedad donde todo es proporcionado, un grupo busca el significado de la libertad.",
        "La aparición de un visitante desconocido desafía las creencias de una sociedad utópica.",
        "En un mundo donde la felicidad está garantizada, un individuo siente algo falta.",
        "Una utopía ambiental perfecta comienza a mostrar fisuras en su fachada."
    ]
}

def elegir_prompt(tema, num_personajes):
    entradas = temas[tema]
    prompt_seleccionado = random.choice(entradas)
    prompt_modificado = f"{prompt_seleccionado} Esta historia debe incluir {num_personajes} personajes principales."
    return prompt_modificado

def generar_historia(prompt, max_length=1000):
    openai.api_key = 'tu_clave_api_aquí'
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=max_length,
            temperature=0.7,
            n=1,
            stop=None,
        )
        historia = response.choices[0].text.strip()
        return historia
    except Exception as e:
        return f"Ocurrió un error: {e}"
    
@app.route('/')

def index():
    return render_template('index.html')  

@app.route('/generate_story', methods=['POST'])
def generate_story():
    tema_seleccionado = request.form['tema']
    num_personajes_seleccionados = request.form['num_personajes']  # Obtiene el número de personajes del formulario
    prompt = elegir_prompt(tema_seleccionado, num_personajes_seleccionados)
    historia = generar_historia(prompt)
    return render_template('story.html', story=historia)


if __name__ == '__main__':
    app.run(debug=True)