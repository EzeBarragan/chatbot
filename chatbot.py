import streamlit as st

from datetime import date

from diccionario import tecnicaturas

from supabase import create_client, Client
url = "https://spdpjswckovboheiaxum.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InNwZHBqc3dja292Ym9oZWlheHVtIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzI1NTI3NTEsImV4cCI6MjA0ODEyODc1MX0.VvIeU5MEiEfhAx1Lpa1NdEAAWDSZJOLNqE4RW5hLuyg"

supabase: Client = create_client(url, key)

min_date = date(1970, 1, 1)
max_date = date(2024, 12, 31)
# URL del proyecto y clave API


def agregar_encuesta(nombre, apellido, nacimiento, dni, cuil, nacionalidad, trabaja, lugar_trabajo,
                     estado_civil, tiene_hijos, calle, numero, cp, provincia, localidad, correo,
                     salud, alergia, condiciones_salud, medicacion, medicacion_detalle, operacion,
                     operacion_motivo, obra_social, obra_social_detalle, afiliado,
                     secundario, instituto_secundario, estudios_superiores):
    data = {
        "nombre": nombre,
        "apellido": apellido,
        "fecha_nacimiento": nacimiento,
        "dni": dni,
        "cuil": cuil,
        "nacionalidad": nacionalidad,
        "trabaja": trabaja,
        "lugar_trabajo": lugar_trabajo,
        "estado_civil": estado_civil,
        "tiene_hijos": tiene_hijos,
        "calle": calle,
        "numero_casa": numero,
        "cp": cp,
        "provincia": provincia,
        "localidad": localidad,
        "correo": correo,
        "salud": salud,
        "alergia": alergia,
        "condiciones_salud": condiciones_salud,
        "medicacion": medicacion,
        "medicacion_detalle": medicacion_detalle,
        "operacion": operacion,
        "operacion_motivo": operacion_motivo,
        "obra_social": obra_social,
        "obra_social_detalle": obra_social_detalle,
        "numero_afiliado": afiliado,
        "secundario": secundario,
        "instituto_secundario": instituto_secundario,
        "estudios_superiores": estudios_superiores
    }
    
    try:
        response = supabase.table('encuesta_personal').insert(data).execute()
        
        if response.error:
            st.error(f"Error al agregar datos: {response.error.message}")
        else:
            st.success("Datos de la encuesta agregados correctamente.")
    except Exception as e:
        st.error(f"Se produjo un error al insertar los datos: {str(e)}")


def agregar_pregunta(carrera, pregunta):
    data = {
        "carrera": carrera,
        "pregunta": pregunta
    }
    
    try:
        response = supabase.table('preguntas_usuario').insert(data).execute()

        # Verificar si ocurrió un error
        if response.error:  # Acceso al atributo `error`
            st.error(f"Error al agregar pregunta: {response.error.message}")
        else:
            st.success("Pregunta agregada correctamente.")
    except Exception as e:
        st.error(f"Se produjo un error al insertar los datos: {str(e)}")


# Variables para almacenar puntuaciones
puntajes = {
    "Ciencia de Datos e IA": 0,
    "Internet de las Cosas y Sistemas Embebidos": 0,
    "Desarrollo de Software": 0,
    "Administración Contable": 0,
    "Administración Financiera": 0,
    "Higiene y Seguridad en el Trabajo": 0,
    "Ceremonial y Protocolo": 0,
}
# Función para buscar respuestas en el diccionario
def buscar_respuesta(tecnicatura, pregunta_usuario):
    if tecnicatura in tecnicaturas:
        preguntas_frecuentes = tecnicaturas[tecnicatura]
        for key in preguntas_frecuentes:
            if key in pregunta_usuario.lower():
                return preguntas_frecuentes[key]
    return None

def mostrar_preguntas_frecuentes(tecnicatura):
    st.subheader(f"Preguntas frecuentes sobre {tecnicatura}")

    # Muestra las preguntas y respuestas específicas para la tecnicatura seleccionada
    preguntas_frecuentes = tecnicaturas.get(tecnicatura, {})
    for pregunta, respuesta in preguntas_frecuentes.items():
        st.write(f"**Pregunta:** {pregunta}")
        st.write(f"**Respuesta:** {respuesta}")


# Menú en el sidebar
st.sidebar.title("Opciones")
menu = st.sidebar.radio("Elige una opción:", ["Tecnicaturas","Chatbot", "Test Vocacional", "Encuesta Personal"])

if menu == "Tecnicaturas":
    st.title("Tecnicaturas")

    # Mostramos imágenes como botones
    col1, col2 = st.columns(2)

    with col1:
        if st.button("Ciencia de Datos e IA"):
            st.write("1. ¿Qué es la ciencia de datos?")
            st.markdown("""
                La ciencia de datos es una disciplina que se dedica a analizar grandes cantidades de datos para descubrir patrones, tendencias y conocimientos útiles. Estos datos pueden venir de cualquier lugar: redes sociales, aplicaciones, sensores, o hasta registros de ventas de una tienda. La idea principal es transformar esos datos en información valiosa que pueda ayudar a tomar decisiones.

                Los expertos en ciencia de datos usan varias herramientas, como estadísticas, programación y algoritmos de aprendizaje automático (machine learning), para procesar, analizar y visualizar estos datos. Así, pueden convertir información cruda en ideas valiosas para las empresas, como entender mejor a los clientes, optimizar procesos o hasta predecir comportamientos futuros.

                Si te interesa entrar en este campo, saber programar en Python o R, entender algo de estadística y familiarizarte con bases de datos es un buen inicio. La ciencia de datos es muy demandada y abre muchas puertas, ya que prácticamente cualquier industria puede beneficiarse de una buena interpretación de sus datos.
            """)
            st.write("2. ¿Cuánto dura la tecnicatura?")
            st.write("La carrera dura 3 años")
            url = "http://www.i12.com.ar/i12/wp-content/uploads/2023/03/Anexo-I-Res-2730-22-Cs-deDatos-e-Inteligencia-Artificial.pdf"
            st.write("si quieres ver la resolucion completa aprieta este [link](%s)" % url)
        st.image("IA.jpg", use_column_width=True)

        if st.button("Análisis de Sistemas"):
             st.write("1. ¿Cuál es el campo laboral para Análisis de Sistemas?")
             st.write("""El Analista de Sistemas trabaja diseñando, implementando y mejorando sistemas informáticos para gestionar la información en una organización. Su campo laboral incluye empresas de tecnología, bancos, instituciones gubernamentales, o cualquier empresa que necesite optimizar sus sistemas informáticos y flujos de información. Se encarga de analizar las necesidades de los usuarios y asegurar que los sistemas funcionen de forma eficiente y segura.""")
             st.write("2. ¿Cómo se diferencia de Desarrollo de Software?")
             st.write("""Análisis de Sistemas se enfoca en entender y diseñar la estructura completa de un sistema informático para cumplir con los objetivos de una organización. Desarrollo de Software, en cambio, está más orientado a la creación de programas y aplicaciones. Mientras que el Analista de Sistemas se encarga de estudiar el sistema en general, el Desarrollador de Software se centra en escribir el código y crear aplicaciones que sean parte del sistema.""")
             st.write("3. ¿Cuánto dura la tecnicatura?")
             st.write("La carrera dura 3 años")
             url = "http://www.i12.com.ar/i12/wp-content/uploads/2019/12/sistemas679019.pdf"
             st.write("si quieres ver la resolucion completa aprieta este [link](%s)" % url)
        st.image("Sistemas.jpg", use_column_width=True)
        
        if st.button("Desarrollo de Sotware"):
             st.write("1. ¿Cuál es el campo laboral para Desarrollo de Software?")
             st.write("""El Desarrollador de Software puede trabajar en empresas de tecnología, consultorías, startups, y también en áreas específicas como el desarrollo de aplicaciones móviles, videojuegos o software para empresas. Su campo laboral es amplio, ya que cada vez más sectores requieren aplicaciones y soluciones tecnológicas personalizadas.""")
             st.write("2. ¿Cómo se diferencia de Analisis de Sistemas?")
             st.write("""Desarrollo de Software está orientado principalmente a la programación y creación de aplicaciones y programas específicos. Análisis de Sistemas, por su parte, se centra en diseñar la estructura general de un sistema de información para satisfacer las necesidades de una organización, lo que implica un enfoque más amplio en el diseño y la gestión del sistema en su totalidad.""")
             st.write("3. ¿Cuánto dura la tecnicatura?")
             st.write("La carrera dura 3 años")
             url = "http://www.i12.com.ar/i12/wp-content/uploads/2019/11/DesarrolloSoftware-5847-19.pdf"
             st.write("si quieres ver la resolucion completa aprieta este [link](%s)" % url)
        st.image("desarrollosoftware.jpg", use_column_width=True)

        if st.button("Administración Financiera"):
             st.write("1. ¿Qué es la administración financiera?")
             st.write("""La administración financiera es el área de una empresa encargada de gestionar sus recursos financieros para asegurar su estabilidad y crecimiento. Incluye funciones como la planificación financiera, el análisis de inversiones, la administración de presupuestos y la toma de decisiones sobre la mejor forma de obtener y usar los fondos. Es crucial en empresas de cualquier sector, ya que busca maximizar el valor de la organización.""")
             st.write("2. ¿Cuánto dura la tecnicatura?")
             st.write("La carrera dura 3 años")
             url = "http://www.i12.com.ar/i12/wp-content/uploads/2024/03/FINAN-IF-2023-48118919-GDEBA-DESFTDGCYE-Resol-456_23-TSAF.pdf"
             st.write("si quieres ver la resolucion completa aprieta este [link](%s)" % url)
        st.image("Financiera.jpg", use_column_width=True)

        if st.button("Administración Contable"):
             st.write("1. ¿Cuáles son las funciones principales de un administrador contable?")
             st.write("""Un administrador contable se encarga de gestionar y supervisar las finanzas de una organización. Sus funciones incluyen llevar la contabilidad, gestionar el flujo de caja, preparar informes financieros, controlar el presupuesto y asegurar que la empresa cumpla con las normativas fiscales. Su rol es fundamental para mantener la salud financiera de la empresa y para proporcionar información financiera confiable que ayude a la toma de decisiones.""")
             st.write("2. ¿Cuánto dura la tecnicatura?")
             st.write("La carrera dura 3 años")
             url = "http://www.i12.com.ar/i12/wp-content/uploads/2024/03/CONTABLE-IF-2023-48114561-GDEBA-DESFTDGCYE-Resol-455_23-TSAC.pdf"
             st.write("si quieres ver la resolucion completa aprieta este [link](%s)" % url)
        st.image("Contable.jpg", use_column_width=True)

    with col2:
        if st.button("Internet de las Cosas y Sistemas Embebidos"):
             st.write("1. ¿Qué es el Internet de las Cosas (IoT)?")
             st.write(""" El Internet de las Cosas (IoT) es una tecnología que permite conectar objetos físicos, como electrodomésticos, vehículos, sensores y otros dispositivos, a Internet. Esto permite que estos dispositivos recopilen y compartan datos, y puedan ser controlados de forma remota. El IoT se usa en diversas áreas, como domótica, salud, industria y ciudades inteligentes, ayudando a mejorar la eficiencia y ofrecer servicios innovadores.""")
             st.write("2. ¿Cuánto dura la tecnicatura?")
             st.write("La carrera dura 3 años")
             url = "http://www.i12.com.ar/i12/wp-content/uploads/2023/03/Anexo-I_Internet-de-las-cosas_IF-2022-42723468-GDEBA-SSEDGCYE-1.pdf"
             st.write("si quieres ver la resolucion completa aprieta este [link](%s)" % url)
        st.image("Iot.jpg", use_column_width=True)

        if st.button("Higiene y Seguridad en el Trabajo"):
             st.write("1. ¿De que se trata la Tecnicatura en Higiene y Seguridad en el Trabajo?")
             st.write("""Esta tecnicatura se enfoca en la prevención de accidentes laborales y en garantizar un ambiente de trabajo seguro para los empleados. Los profesionales en esta área aprenden a identificar riesgos en el lugar de trabajo, proponer medidas preventivas y supervisar el cumplimiento de normas de seguridad. Es una carrera clave en industrias como la construcción, la manufactura y cualquier entorno con riesgos ocupacionales.""")
             st.write("2. ¿Cuánto dura la tecnicatura?")
             st.write("La carrera dura 3 años")
             url = "http://www.i12.com.ar/i12/wp-content/uploads/2019/11/Hig-y-Seg-Tbjo_320-13.pdf"
             st.write("si quieres ver la resolucion completa aprieta este [link](%s)" % url)
        st.image("seguridad.jpg", use_column_width=True)

        if st.button("Ceremonial y Protocolo"):
             st.write("1. ¿Qué es Ceremonial y Procolo?")
             st.write("""Ceremonial y Protocolo se refiere al conjunto de normas y técnicas que organizan eventos oficiales, ceremonias y actividades de representación. Los profesionales en esta área aprenden a gestionar y planificar eventos respetando tradiciones y normas culturales o institucionales, y se desempeñan en organizaciones gubernamentales, empresas, y otras instituciones que requieren eventos formales.""")
             st.write("2. ¿Cuánto dura la tecnicatura?")
             st.write("La carrera dura 3 años")
             url = "http://www.i12.com.ar/i12/wp-content/uploads/2022/09/Resolucion-1623-04.pdf"
             st.write("si quieres ver la resolucion completa aprieta este [link](%s)" % url)
        st.image("ceremonial.jpg", use_column_width=True)

        if st.button("Certificación en Salud y Seguridad Ocupacional"):
             st.write("1. ¿De que se trata la Certificación en Salud y Seguridad Ocupacional?")
             st.write("""Esta certificación se enfoca en el estudio y la aplicación de prácticas que promuevan la seguridad y salud de los empleados en el ambiente laboral, específicamente en el sector de la salud. Los profesionales certificados están capacitados para identificar y minimizar riesgos laborales y asegurar el cumplimiento de normas de salud ocupacional en entornos de atención médica, como hospitales y clínicas.""")
             st.write("2. ¿Cuánto dura la tecnicatura?")
             st.write("La carrera dura 1 año")
             url = "http://www.i12.com.ar/i12/wp-content/uploads/2019/11/CertificacionensaludRes-302-10.pdf"
             st.write("si quieres ver la resolucion completa aprieta este [link](%s)" % url)
        st.image("salud.jpg", use_column_width=True)

# Chatbot
elif menu == "Chatbot":
   # Inicio del flujo conversacional
    st.write("👋 ¡Buenos días! ¿En qué puedo ayudarte hoy?")

    # Mostrar opciones de tecnicaturas
    tecnicaturas_list = list(tecnicaturas.keys())
    st.write("Estas son las tecnicaturas que ofrecemos:")
    for idx, tecnicatura in enumerate(tecnicaturas_list, start=1):
        st.write(f"{idx}. {tecnicatura}")

    # Preguntar si le interesa alguna tecnicatura
    selected_tecnicatura = st.selectbox("¿Te interesa alguna de estas tecnicaturas o tenes preguntas acerca del instituto?", ["Selecciona una opción"] + tecnicaturas_list)

    if selected_tecnicatura and selected_tecnicatura != "Selecciona una opción":
        mostrar_preguntas_frecuentes(selected_tecnicatura)
        
        # Preguntar si tiene otra consulta
        st.write("¿Tenés otra pregunta? Escribila abajo y la responderemos pronto.")
        pregunta_usuario = st.text_input("Escribe tu pregunta aquí:")

        if st.button("Enviar Pregunta"):
            agregar_pregunta(selected_tecnicatura, pregunta_usuario)
            st.success("Pregunta enviada exitosamente. ¡Gracias por tu consulta!")
    else:
        st.write("Si tenés dudas sobre la inscripción o cualquier otra consulta, escribinos abajo.")
        pregunta_usuario = st.text_input("Escribe tu pregunta aquí:")

        if st.button("Enviar Pregunta"):
            agregar_pregunta("General", pregunta_usuario)
            st.success("Pregunta enviada exitosamente. ¡Gracias por tu consulta!")
# Test Vocacional
elif menu == "Test Vocacional":
    st.title("Test Vocacional")
    
   # Pregunta 1
    st.subheader("1. ¿Qué tipo de actividades disfrutas más?")
    resp1 = st.radio("Selecciona una opción:", 
                ("Desarrollar o programar sistemas de software.",
                 "Gestionar datos y analizarlos para tomar decisiones.",
                 "Investigar e implementar tecnologías emergentes como el IoT.",
                 "Organizar eventos y planificar protocolos.",
                 "Trabajar con números, cuentas y finanzas."))

    if resp1 == "Desarrollar o programar sistemas de software.":
        puntajes["Desarrollo de Software"] += 1
    elif resp1 == "Gestionar datos y analizarlos para tomar decisiones.":
        puntajes["Ciencia de Datos e IA"] += 1
    elif resp1 == "Investigar e implementar tecnologías emergentes como el IoT.":
        puntajes["Internet de las Cosas y Sistemas Embebidos"] += 1
    elif resp1 == "Organizar eventos y planificar protocolos.":
        puntajes["Ceremonial y Protocolo"] += 1
    elif resp1 == "Trabajar con números, cuentas y finanzas.":
        puntajes["Administración Contable"] += 1
        puntajes["Administración Financiera"] += 1

# Pregunta 2
    st.subheader("2. ¿Cuál de las siguientes situaciones te resulta más interesante?")
    resp2 = st.radio("Selecciona una opción:", 
                ("Crear soluciones de software para resolver problemas complejos.",
                 "Descubrir patrones en grandes volúmenes de datos.",
                 "Diseñar dispositivos conectados para automatizar tareas.",
                 "Asegurarte de que los trabajadores operen en ambientes seguros.",
                 "Administrar los presupuestos y optimizar las finanzas de una empresa."))

    if resp2 == "Crear soluciones de software para resolver problemas complejos.":
        puntajes["Desarrollo de Software"] += 1
    elif resp2 == "Descubrir patrones en grandes volúmenes de datos.":
        puntajes["Ciencia de Datos e IA"] += 1
    elif resp2 == "Diseñar dispositivos conectados para automatizar tareas.":
        puntajes["Internet de las Cosas y Sistemas Embebidos"] += 1
    elif resp2 == "Asegurarte de que los trabajadores operen en ambientes seguros.":
        puntajes["Higiene y Seguridad en el Trabajo"] += 1
    elif resp2 == "Administrar los presupuestos y optimizar las finanzas de una empresa.":
        puntajes["Administración Financiera"] += 1

# Pregunta 3
    st.subheader("3. Si tuvieras que elegir una tarea para hacer todo el día, ¿cuál sería?")
    resp3 = st.radio("Selecciona una opción:", 
                ("Desarrollar aplicaciones o software.",
                 "Analizar bases de datos y crear modelos predictivos.",
                 "Diseñar dispositivos electrónicos o sistemas inteligentes.",
                 "Supervisar un evento social o diplomático importante.",
                 "Planificar y revisar las políticas de seguridad en el trabajo.",
                 "Revisar y preparar informes contables o financieros."))

    if resp3 == "Desarrollar aplicaciones o software.":
        puntajes["Desarrollo de Software"] += 1
    elif resp3 == "Analizar bases de datos y crear modelos predictivos.":
        puntajes["Ciencia de Datos e IA"] += 1
    elif resp3 == "Diseñar dispositivos electrónicos o sistemas inteligentes.":
        puntajes["Internet de las Cosas y Sistemas Embebidos"] += 1
    elif resp3 == "Supervisar un evento social o diplomático importante.":
        puntajes["Ceremonial y Protocolo"] += 1
    elif resp3 == "Planificar y revisar las políticas de seguridad en el trabajo.":
        puntajes["Higiene y Seguridad en el Trabajo"] += 1
    elif resp3 == "Revisar y preparar informes contables o financieros.":
        puntajes["Administración Contable"] += 1
        puntajes["Administración Financiera"] += 1

# Pregunta 4
    st.subheader("4. ¿Qué tipo de entorno laboral te imaginas en el futuro?")
    resp4 = st.radio("Selecciona una opción:", 
                ("En un equipo desarrollando nuevas aplicaciones.",
                 "En una oficina analizando datos y generando informes para la toma de decisiones.",
                 "En un laboratorio de electrónica o en campo, trabajando con dispositivos IoT.",
                 "Supervisando la seguridad en grandes proyectos industriales o de construcción.",
                 "En un entorno administrativo, gestionando cuentas y finanzas."))

    if resp4 == "En un equipo desarrollando nuevas aplicaciones.":
        puntajes["Desarrollo de Software"] += 1
    elif resp4 == "En una oficina analizando datos y generando informes para la toma de decisiones.":
        puntajes["Ciencia de Datos e IA"] += 1
    elif resp4 == "En un laboratorio de electrónica o en campo, trabajando con dispositivos IoT.":
        puntajes["Internet de las Cosas y Sistemas Embebidos"] += 1
    elif resp4 == "Supervisando la seguridad en grandes proyectos industriales o de construcción.":
        puntajes["Higiene y Seguridad en el Trabajo"] += 1
    elif resp4 == "En un entorno administrativo, gestionando cuentas y finanzas.":
        puntajes["Administración Contable"] += 1
        puntajes["Administración Financiera"] += 1

# Pregunta 5
    st.subheader("5. ¿Qué habilidad te gustaría mejorar o aprender más?")
    resp5 = st.radio("Selecciona una opción:", 
                ("Programación avanzada y desarrollo de software.",
                 "Aprender a extraer información útil de datos complejos.",
                 "Diseñar y programar dispositivos conectados y sensores.",
                 "Aprender sobre normas y reglas de seguridad para el trabajo.",
                 "Desarrollar habilidades para organizar grandes eventos.",
                 "Gestionar mejor los recursos financieros y contables de una empresa."))

    if resp5 == "Programación avanzada y desarrollo de software.":
        puntajes["Desarrollo de Software"] += 1
    elif resp5 == "Aprender a extraer información útil de datos complejos.":
        puntajes["Ciencia de Datos e IA"] += 1
    elif resp5 == "Diseñar y programar dispositivos conectados y sensores.":
        puntajes["Internet de las Cosas y Sistemas Embebidos"] += 1
    elif resp5 == "Aprender sobre normas y reglas de seguridad para el trabajo.":
        puntajes["Higiene y Seguridad en el Trabajo"] += 1
    elif resp5 == "Desarrollar habilidades para organizar grandes eventos.":
        puntajes["Ceremonial y Protocolo"] += 1
    elif resp5 == "Gestionar mejor los recursos financieros y contables de una empresa.":
        puntajes["Administración Contable"] += 1
        puntajes["Administración Financiera"] += 1

# Pregunta 6
    st.subheader("6. ¿Qué tecnología o área de conocimiento te interesa más?")
    resp6 = st.radio("Selecciona una opción:", 
                ("Inteligencia artificial y análisis de datos.",
                 "Dispositivos inteligentes y el Internet de las Cosas.",
                 "Programación y desarrollo de aplicaciones.",
                 "Finanzas y contabilidad.",
                 "Seguridad en el trabajo.",
                 "Protocolo y organización de eventos."))

    if resp6 == "Inteligencia artificial y análisis de datos.":
        puntajes["Ciencia de Datos e IA"] += 1
    elif resp6 == "Dispositivos inteligentes y el Internet de las Cosas.":
        puntajes["Internet de las Cosas y Sistemas Embebidos"] += 1
    elif resp6 == "Programación y desarrollo de aplicaciones.":
        puntajes["Desarrollo de Software"] += 1
    elif resp6 == "Finanzas y contabilidad.":
        puntajes["Administración Contable"] += 1
        puntajes["Administración Financiera"] += 1
    elif resp6 == "Seguridad en el trabajo.":
        puntajes["Higiene y Seguridad en el Trabajo"] += 1
    elif resp6 == "Protocolo y organización de eventos.":
        puntajes["Ceremonial y Protocolo"] += 1

# Evaluación final
    if st.button("Ver Resultado"):
        # Obtener la tecnicatura con mayor puntaje
        max_puntaje = max(puntajes.values())
        tecnicaturas_recomendadas = [tec for tec, puntaje in puntajes.items() if puntaje == max_puntaje]
    
        if len(tecnicaturas_recomendadas) == 1:
            st.write(f"Te recomendamos la {tecnicaturas_recomendadas[0]}")
        else:
            st.write("Te recomendamos considerar las siguientes opciones:")
            for tec in tecnicaturas_recomendadas:
                st.write(f"- {tec}")
# Encuesta Personal
elif menu == "Encuesta Personal":
    st.title("Encuesta Personal")
    
    # Preguntas de la encuesta
    st.subheader("Datos personales")
    nombre = st.text_input("Nombre")
    apellido = st.text_input("Apellido")
    nacimiento = st.date_input("Introduzca su fecha de nacimiento")
    dni = st.text_input("Coloque su Dni")
    cuil = st.text_input("Cuil")
    nacionalidad = st.text_input("Lugar de nacimiento")
    trabaja = st.selectbox("¿Actualmente trabajas?", ["Sí", "No"])
    lugar_trabajo = st.text_input("¿Dónde trabajas?") if trabaja == "Sí" else ""
    estado_civil = st.selectbox("Estado civil", ["Soltero/a", "Casado/a", "Divorciado/a", "Viudo/a"])
    tiene_hijos = st.selectbox("¿Tienes hijos?", ["Sí", "No"])
    
    st.subheader("Domicilio")
    calle = st.text_input("Calle")
    numero = st.text_input("Número de casa")
    cp = st.text_input("Código postal")
    provincia = st.text_input("Provincia")
    localidad = st.text_input("Localidad")
    correo = st.text_input("Su email")

    st.subheader("Información de Salud")
    salud = st.selectbox("¿Padece o ha padecido alguna condición de salud?", ["Sí", "No"])
    condiciones_salud = st.text_input("¿Cuáles?", key="input_cual") if salud == "Sí" else ""
    
    alergia = st.selectbox("¿Padece o ha padecido algún tipo de alergia grave?", ["Sí", "No"])
    condiciones_alergia = st.text_input("¿Cuáles?", key="input_condiciones_alergia") if alergia == "Sí" else ""
    
    medicacion = st.selectbox("¿Recibe de manera habitual algún tipo de medicación?", ["Sí", "No"])
    medicacion_detalle = st.text_input("¿Cuáles?", key="input_medi") if medicacion == "Sí" else ""
    
    operacion = st.selectbox("¿Tuvo alguna operación?", ["Sí", "No"])
    operacion_motivo = st.text_input("¿Por qué motivo?") if operacion == "Sí" else ""
    
    obra_social = st.selectbox("¿Posee obra social?", ["Sí", "No"])
    obra_social_detalle = st.text_input("¿Cuál es su obra social?") if obra_social == "Sí" else ""
    
    afiliado = st.text_input("Número de afiliado", key="input_numero") if obra_social == "Sí" else ""
    
    st.subheader("Estudios Cursados")
    secundario = st.selectbox("¿Tiene secundario completo?", ["Sí", "No"])
    instituto_secundario = st.text_input("Instituto de donde se recibió", key="input_instituto") if secundario == "Sí" else ""
    estudios_superiores = st.text_input("Otros estudios superiores realizados") 
    if st.button("Enviar Encuesta"):
        agregar_encuesta(nombre, apellido, nacimiento, dni, cuil, nacionalidad, trabaja, lugar_trabajo,
                     estado_civil, tiene_hijos, calle, numero, cp, provincia, localidad, correo,
                     salud, alergia, condiciones_salud, medicacion, medicacion_detalle, operacion,
                     operacion_motivo, obra_social, obra_social_detalle, afiliado,
                     secundario, instituto_secundario, estudios_superiores)
        st.success("Encuesta enviada exitosamente.")

elif menu == "Tecnicaturas":
    st.title("Tecnicaturas")

    # Mostramos imágenes como botones
    col1, col2 = st.columns(2)

    with col1:
        if st.button("Ciencia de Datos e IA"):
            st.write("1. ¿Qué es la ciencia de datos?")
            st.markdown("""
                La ciencia de datos es una disciplina que se dedica a analizar grandes cantidades de datos para descubrir patrones, tendencias y conocimientos útiles. Estos datos pueden venir de cualquier lugar: redes sociales, aplicaciones, sensores, o hasta registros de ventas de una tienda. La idea principal es transformar esos datos en información valiosa que pueda ayudar a tomar decisiones.

                Los expertos en ciencia de datos usan varias herramientas, como estadísticas, programación y algoritmos de aprendizaje automático (machine learning), para procesar, analizar y visualizar estos datos. Así, pueden convertir información cruda en ideas valiosas para las empresas, como entender mejor a los clientes, optimizar procesos o hasta predecir comportamientos futuros.

                Si te interesa entrar en este campo, saber programar en Python o R, entender algo de estadística y familiarizarte con bases de datos es un buen inicio. La ciencia de datos es muy demandada y abre muchas puertas, ya que prácticamente cualquier industria puede beneficiarse de una buena interpretación de sus datos.
            """)
            st.write("2. ¿Cuánto dura la tecnicatura?")
            st.write("La carrera dura 3 años")
            url = "http://www.i12.com.ar/i12/wp-content/uploads/2023/03/Anexo-I-Res-2730-22-Cs-deDatos-e-Inteligencia-Artificial.pdf"
            st.write("si quieres ver la resolucion completa aprieta este [link](%s)" % url)
        st.image("IA.jpg", use_column_width=True)

        if st.button("Análisis de Sistemas"):
             st.write("1. ¿Cuál es el campo laboral para Análisis de Sistemas?")
             st.write("""El Analista de Sistemas trabaja diseñando, implementando y mejorando sistemas informáticos para gestionar la información en una organización. Su campo laboral incluye empresas de tecnología, bancos, instituciones gubernamentales, o cualquier empresa que necesite optimizar sus sistemas informáticos y flujos de información. Se encarga de analizar las necesidades de los usuarios y asegurar que los sistemas funcionen de forma eficiente y segura.""")
             st.write("2. ¿Cómo se diferencia de Desarrollo de Software?")
             st.write("""Análisis de Sistemas se enfoca en entender y diseñar la estructura completa de un sistema informático para cumplir con los objetivos de una organización. Desarrollo de Software, en cambio, está más orientado a la creación de programas y aplicaciones. Mientras que el Analista de Sistemas se encarga de estudiar el sistema en general, el Desarrollador de Software se centra en escribir el código y crear aplicaciones que sean parte del sistema.""")
             st.write("3. ¿Cuánto dura la tecnicatura?")
             st.write("La carrera dura 3 años")
             url = "http://www.i12.com.ar/i12/wp-content/uploads/2019/12/sistemas679019.pdf"
             st.write("si quieres ver la resolucion completa aprieta este [link](%s)" % url)
        st.image("Sistemas.jpg", use_column_width=True)
        
        if st.button("Desarrollo de Sotware"):
             st.write("1. ¿Cuál es el campo laboral para Desarrollo de Software?")
             st.write("""El Desarrollador de Software puede trabajar en empresas de tecnología, consultorías, startups, y también en áreas específicas como el desarrollo de aplicaciones móviles, videojuegos o software para empresas. Su campo laboral es amplio, ya que cada vez más sectores requieren aplicaciones y soluciones tecnológicas personalizadas.""")
             st.write("2. ¿Cómo se diferencia de Analisis de Sistemas?")
             st.write("""Desarrollo de Software está orientado principalmente a la programación y creación de aplicaciones y programas específicos. Análisis de Sistemas, por su parte, se centra en diseñar la estructura general de un sistema de información para satisfacer las necesidades de una organización, lo que implica un enfoque más amplio en el diseño y la gestión del sistema en su totalidad.""")
             st.write("3. ¿Cuánto dura la tecnicatura?")
             st.write("La carrera dura 3 años")
             url = "http://www.i12.com.ar/i12/wp-content/uploads/2019/11/DesarrolloSoftware-5847-19.pdf"
             st.write("si quieres ver la resolucion completa aprieta este [link](%s)" % url)
        st.image("desarrollosoftware.jpg", use_column_width=True)

        if st.button("Administración Financiera"):
             st.write("1. ¿Qué es la administración financiera?")
             st.write("""La administración financiera es el área de una empresa encargada de gestionar sus recursos financieros para asegurar su estabilidad y crecimiento. Incluye funciones como la planificación financiera, el análisis de inversiones, la administración de presupuestos y la toma de decisiones sobre la mejor forma de obtener y usar los fondos. Es crucial en empresas de cualquier sector, ya que busca maximizar el valor de la organización.""")
             st.write("2. ¿Cuánto dura la tecnicatura?")
             st.write("La carrera dura 3 años")
             url = "http://www.i12.com.ar/i12/wp-content/uploads/2024/03/FINAN-IF-2023-48118919-GDEBA-DESFTDGCYE-Resol-456_23-TSAF.pdf"
             st.write("si quieres ver la resolucion completa aprieta este [link](%s)" % url)
        st.image("Financiera.jpg", use_column_width=True)

        if st.button("Administración Contable"):
             st.write("1. ¿Cuáles son las funciones principales de un administrador contable?")
             st.write("""Un administrador contable se encarga de gestionar y supervisar las finanzas de una organización. Sus funciones incluyen llevar la contabilidad, gestionar el flujo de caja, preparar informes financieros, controlar el presupuesto y asegurar que la empresa cumpla con las normativas fiscales. Su rol es fundamental para mantener la salud financiera de la empresa y para proporcionar información financiera confiable que ayude a la toma de decisiones.""")
             st.write("2. ¿Cuánto dura la tecnicatura?")
             st.write("La carrera dura 3 años")
             url = "http://www.i12.com.ar/i12/wp-content/uploads/2024/03/CONTABLE-IF-2023-48114561-GDEBA-DESFTDGCYE-Resol-455_23-TSAC.pdf"
             st.write("si quieres ver la resolucion completa aprieta este [link](%s)" % url)
        st.image("Contable.jpg", use_column_width=True)

    with col2:
        if st.button("Internet de las Cosas y Sistemas Embebidos"):
             st.write("1. ¿Qué es el Internet de las Cosas (IoT)?")
             st.write(""" El Internet de las Cosas (IoT) es una tecnología que permite conectar objetos físicos, como electrodomésticos, vehículos, sensores y otros dispositivos, a Internet. Esto permite que estos dispositivos recopilen y compartan datos, y puedan ser controlados de forma remota. El IoT se usa en diversas áreas, como domótica, salud, industria y ciudades inteligentes, ayudando a mejorar la eficiencia y ofrecer servicios innovadores.""")
             st.write("2. ¿Cuánto dura la tecnicatura?")
             st.write("La carrera dura 3 años")
             url = "http://www.i12.com.ar/i12/wp-content/uploads/2023/03/Anexo-I_Internet-de-las-cosas_IF-2022-42723468-GDEBA-SSEDGCYE-1.pdf"
             st.write("si quieres ver la resolucion completa aprieta este [link](%s)" % url)
        st.image("Iot.jpg", use_column_width=True)

        if st.button("Higiene y Seguridad en el Trabajo"):
             st.write("1. ¿De que se trata la Tecnicatura en Higiene y Seguridad en el Trabajo?")
             st.write("""Esta tecnicatura se enfoca en la prevención de accidentes laborales y en garantizar un ambiente de trabajo seguro para los empleados. Los profesionales en esta área aprenden a identificar riesgos en el lugar de trabajo, proponer medidas preventivas y supervisar el cumplimiento de normas de seguridad. Es una carrera clave en industrias como la construcción, la manufactura y cualquier entorno con riesgos ocupacionales.""")
             st.write("2. ¿Cuánto dura la tecnicatura?")
             st.write("La carrera dura 3 años")
             url = "http://www.i12.com.ar/i12/wp-content/uploads/2019/11/Hig-y-Seg-Tbjo_320-13.pdf"
             st.write("si quieres ver la resolucion completa aprieta este [link](%s)" % url)
        st.image("seguridad.jpg", use_column_width=True)

        if st.button("Ceremonial y Protocolo"):
             st.write("1. ¿Qué es Ceremonial y Procolo?")
             st.write("""Ceremonial y Protocolo se refiere al conjunto de normas y técnicas que organizan eventos oficiales, ceremonias y actividades de representación. Los profesionales en esta área aprenden a gestionar y planificar eventos respetando tradiciones y normas culturales o institucionales, y se desempeñan en organizaciones gubernamentales, empresas, y otras instituciones que requieren eventos formales.""")
             st.write("2. ¿Cuánto dura la tecnicatura?")
             st.write("La carrera dura 3 años")
             url = "http://www.i12.com.ar/i12/wp-content/uploads/2022/09/Resolucion-1623-04.pdf"
             st.write("si quieres ver la resolucion completa aprieta este [link](%s)" % url)
        st.image("ceremonial.jpg", use_column_width=True)

        if st.button("Certificación en Salud y Seguridad Ocupacional"):
             st.write("1. ¿De que se trata la Certificación en Salud y Seguridad Ocupacional?")
             st.write("""Esta certificación se enfoca en el estudio y la aplicación de prácticas que promuevan la seguridad y salud de los empleados en el ambiente laboral, específicamente en el sector de la salud. Los profesionales certificados están capacitados para identificar y minimizar riesgos laborales y asegurar el cumplimiento de normas de salud ocupacional en entornos de atención médica, como hospitales y clínicas.""")
             st.write("2. ¿Cuánto dura la tecnicatura?")
             st.write("La carrera dura 1 año")
             url = "http://www.i12.com.ar/i12/wp-content/uploads/2019/11/CertificacionensaludRes-302-10.pdf"
             st.write("si quieres ver la resolucion completa aprieta este [link](%s)" % url)
        st.image("salud.jpg", use_column_width=True)

