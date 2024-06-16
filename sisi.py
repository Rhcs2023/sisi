import streamlit as st

# Diccionario con palabras a traducir
diccionario = {
    'a': 'nuù ',
        'acarrear': 'jíkóñáá ',
        'adentro': 'inì ',
        'adonde': 'ndéchi ',
        'agarrar': 'kíhin(tiin)',
        'agradecido': 'kútahù',
        'al': 'ná ',
        'alcanzar': 'kanda ',
        'algo': 'joò ',
        'alli': 'uán ',
        'alto': 'súkú ', 
        'amargo': 'uhà ',
        'amarillo': 'kuáán ',
        'amontonarse': 'tihú',    
        'anda': 'jíka ',
        'aquel': 'uán ', 
        'aqui': 'yáha ',
        'asi': 'suán ', 
        'año': 'kuià ',
        'bien': 'kuééni ',
        'blanco': 'yáá ',
        'bonito': 'luu ',
        'borrego': 'rii ',
        'bravo': 'shraán ',
        'brotar': 'nana',
        'buenos': 'tanìn ',
        'buenas': 'tanì ', 
        'cabeza': 'shini ',
        'cantaro': 'kiyi',
        'cafe': 'yahá(color) ',
        'camino': 'ichi ',
        'canasta': 'jika ',
        'ceniza': 'yàà ',
        'cambiar': 'sama ',
        'cantidad': 'ñáá ',
        'chile': 'yaha ',
        'claro': 'kají ',
        'choches': 'kuaa ',
        'con': 'jiin',
        'comadre': 'kualiá ',
        'como': 'ndesa ',
        'compadre': 'mpáà ',
        'comprar': 'kuaan',
        'compro': 'kuáanná',
        'contiene': 'ñúhu ',
        'convertirse': 'nduu ',
        'cortarse': 'tehndè ',
        'costar': 'yaà ',
        'cuando': 'nuù ',
        'cueva': 'túnchi ',
        'cuesta': 'yaà ',
        'culebra': 'koó ', 
        'decir': 'kéi ',
        'deidad': 'ñuhú ',
        'despacio': 'kuéé ',
        'dia': 'dí ', 
        'dias': 'díí ',
        'dinero': 'shrúhún ',
        'egoista': 'jahà ',
        'en': 'nuù ', 
        'encontrarse': 'yóó ', 
        'encuentra': 'yóó ', 
        'enojarse': 'kiti-iní ',
        'entonceses': 'núsáá ',
        'es': 'kúu ', 
        'esa': 'uán ',
        'ese': 'uán ', 
        'esta': 'kúu ',
        'estan': 'kákuu ',
        'estar': 'yóó ',
        'este': 'yàhá ',
        'femenino':'síhí',
        'fiesta':'víko', 
        'filoso':'shraán ', 
        'finado':'shraán ', 
        'fuego': 'ñuhú ',
        'girar': 'jikó ',
        'grande': 'kánhu ', 
        'guajolote': 'kóhló ',
        'guajolotito': 'pípí ',
        'hacer': 'kisáhaní ',
        'hay': 'yóó ', 
        'hermano':'kuàha', 
        'hervir': 'hervir ',
        'hijo': 'séhe ',
        'humo': 'yahà(ollin) ',
        'ir': 'ki (futuro) ',
        'irse': 'kihín ',
        'jaguar': 'kuní ',
        'jarro': 'tindohò ',
        'jaguar': 'kuiní ',
        'la': 'ná ', 
        'lejos': 'jíká ',
        'lengua': 'yaa ',
        'leña': 'ndukú ',
        'llama': 'nání ',
        'llamarse': 'nání ',
        'llamas': 'náníró ',
        'llamo': 'nání ',
        'madera': 'yunu ',
        'madre': 'náà ',
        'maguey': 'yáú ',
        'mano': 'ndaha ', 
        'me': 'ná ',
        'mercado': 'yahu ',
        'mero': 'máá ', 
        'mi': 'ri',
        'mirar': 'koto ', 
        'mismo': 'máá ', 
        'monte': 'yuko ',
        'mucho': 'shraán ',
        'musica': 'yàà ',
        'muy': 'shraán ',
        'noche': 'kua ',
        'noches': 'kuaa ',
        'otro': 'inga ',
        'o': 'shí ',
        'odiar': 'koto-uhù ',
        'olla': 'kisi ',
        'padre': 'táà ',
        'para': 'ja kúu ',
        'parados': 'ká-íin',
        'pecho': 'jikà ',
        'petate': 'yuu ',
        'poseer': 'ñavàha ',
        'pesos': 'pesos', 
        'piedra': 'yuú',
        'plato': 'kohò',
        'pueblo': 'ñuù ',
        'que': 'já ',
        'quiere': 'kuní',
        'queda': 'ndòó',
        'quedarse': 'ndòó',
        'recoger': 'nastútú ',
        'recordar': 'náhá ',
        'regresar': 'yàà(kuánoho a casa) ',
        'relajado': 'kuééni ',
        'repartir': 'tehndè ',
        'romperse': 'tehndè ',
        'salir': 'nana ',
        'seco': 'íchí ',
        'se': 'kúu es ser pero  ',
        'señor':'ihá(divino)',
        'ser': 'kúu ',
        'si':'véè', 
        'solamente':'ni',
        'sólido': 'yúú ',
        'su': 'ní ',
        'tamal de helote': 'suu ',
        'tambien': 'suni ',
        'tarde': 'ñín ',
        'tardes': 'ñíni ', 
        'tierra': 'ñuhu ', 
        'tomar':'koro',
        'trabajo': 'tiun ',
        'tu': 'ró', 
        'un': 'in ',
        'una': 'in ',
        'uno': 'in ',
        'usted': 'ní ',
        'va': 'kihín ',
        'verdura': 'nduà (cruda) yuán (cocida) ',
        'vender':'shikó',
        'veinte':'okò',
        'virgen':'ihà(síhí)',
        'volver':'nduu',
        'volver': 'nduu ',
        'voy': 'kihín(ri)  ',
        'vueltas': 'jikó ',
        'y': 'te ',
        'yo': 'ri-ná(con respeto)',
}

def traducir_oracion(oracion):
    palabras = oracion.split()
    oracion_traducida = " ".join([diccionario.get(palabra.lower(), palabra) for palabra in palabras])
    return oracion_traducida

#import streamlit as st
# Load and display the image
#imagen = " https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.wolterskluwer.com%2Fen%2Fexpert-insights%2Fgenerative-ai-trends-to-watch&psig=AOvVaw3T1d3Uo45nWmKRh2QZSHfX&ust=1718343291412000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqGAoTCLjRz-nt14YDFQAAAAAdAAAAABDtAQ "
#st.image(imagen, caption='Es ', use_column_width=True )
import streamlit as st

# Título de la página
st.title("Reproductor de Video")

# Ruta del archivo de video
video_path = "https://www.youtube.com/watch?v=55dSm1Ikp_4"

# Mostrar el video en la página
video_file = open(video_path, 'rb')
video_bytes = video_file.read()
st.video(video_bytes)


st.title("Traductor de Español a Mixteco")

# Preguntar al usuario por una oración en español
oracion = st.text_input("Ingresa una oración en español, los pronombres posesivos van despues del sujeto, ejemplo: Padre mi va al centro").lower()

if st.button("Traducir"):
    oracion_traducida = traducir_oracion(oracion)
   
    color = "blue"
    st.write(f"Traducción: {oracion_traducida} ")





     
   
