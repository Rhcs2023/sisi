import streamlit as st

# Diccionario con palabras a traducir
diccionario = {
                  'a': 'nuù ',
        'acarrear': 'jíkóñáá ',
        'adentro': 'inì ',
        'adonde': 'ndéchi ',
        'agarrar': 'kíhin(tiin)',
        'agradecido': 'kútahù',
        'ajo': 'aju ',
        'al': 'ná ',
        'alcanzar': 'kanda ',
        'alegria': 'aa ',
        'algo': 'joò ',
        'alli': 'uán ',
        'alto': 'súkú ', 
        'amargo': 'uhà ',
        'amarillo': 'akuaan ', 
        'amarillo': 'kuáán ',
        'amontonarse': 'tihú',    
        'ancho': 'ajite ',
        'anda': 'jíka ',
        'andar': 'jika ',
        'anochecer': 'akunee ', 
        'año': 'kuià ',
        'año': 'kuià ', 
        'aquel': 'uán ', 
        'aqui': 'yáha ',
        'asi': 'suán ', 
        'atras': 'xata ',
        'aunque': 'adua ', 
        'barriga': 'chìi ',
        'bien': 'kuééni ',
        'blanco': 'akuxi ', 
        'blanco': 'yáá ',
        'bonito': 'luu ',
        'borrego': 'rii ',
        'bravo': 'shraán ',
        'brotar': 'nana',
        'buenas': 'tanì ', 
        'buenos': 'tanìn ',
        'buen': 'tanì ',
        'cabe': 'aketa ', 
        'cabeza': 'shini ',
        'cafe': 'yahá(color) ',
        'cama': 'jito ',
        'cambiar': 'sama ',
        'camino': 'ichi ',
        'canasta': 'jika ',
        'cantaro': 'kiyi',
        'cantidad': 'ñáá ',
        'carcel': 'vehe kàa ',
        'ceniza': 'yàà ',
        'chile': 'yaha ',
        'choches': 'kuaa ',
        'ciénega': 'ndòhyo', 
        'ciertamente':'andaa' ' kuiti',
        'claro': 'kají ',
        'comadre': 'kualiá ',
        'como': 'ndesa ',
        'compadre': 'mpáà ',
        'comprar': 'kuaan',
        'compro': 'kuáanná',
        'con': 'jiin',
        'contiene': 'ñúhu ',
        'convertirse': 'nduu ',
        'cortarse': 'tehndè ',
        'costar': 'yaà ',
        'cuando': 'amavi ',
        'cuando': 'nuù ',
        'cuesta': 'yaà ',
        'cueva': 'túnchi ',
        'culebra': 'koó ', 
        'decir': 'kéi ',
        'deidad': 'ñuhú ',
        'desde': 'anda ' 'ó '' ansa ',
        'despacio': 'kuéé ',
        'dia': 'dí ', 
        'dias': 'díí ',
        'dibujar': 'anatava ',
        'dinero': 'shrúhún ',
        'disgusto': 'aa ',
        'donde': 'ami ',
        'echar': 'cháá',
        'egoista': 'jahà ',
        'elefante': 'anda ' ' yuku ',
        'ella': 'an ',
        'empezar': 'kejáhá ',
        'en': 'nuù ', 
        'encontrarse': 'yóó ', 
        'encuentra': 'yóó ', 
        'enloquecer': 'an ' 'sana ',
        'enojarse': 'kiti-iní ',
        'entero': 'níí', 
        'entonceses': 'núsáá ',
        'entrar': 'cháá chuko ',
        'es': 'kúu ', 
        'esa': 'uán ',
        'escribir': 'cháá ',
        'ese': 'uán ', 
        'espalda': 'xata ',
        'esta': 'kúu ',
        'estan': 'kákuu ',
        'estar': 'yóó ',
        'este': 'yàhá ',
        'facil': 'atuu ' 'yii ',
        'femenino':'síhí',
        'fiesta':'víko', 
        'filoso':'shraán ', 
        'finado':'shraán ', 
        'fuego': 'ñuhú ',
        'gatear': 'jikandee ',
        'girar': 'jikó ',
        'grande': 'kánhu ', 
        'guajolote': 'kóhló ',
        'guajolotito': 'pípí ',
        'hacer': 'kisáhaní ',
        'hasta': 'anda ',
        'hay': 'yóó ', 
        'hermano':'kuàha', 
        'hervir': 'hervir ',
        'hijo': 'séhe ',
        'humo': 'yahà  ',
        'incierto': 'adi nandaa ', 
        'incierto': 'andaa ',
        'inesperado': 'ama ', 
        'inocente': 'anajini ',
        'inutil': 'anandíii ',
        'ir': 'ki (futuro) ',
        'irse': 'kihín ',
        'jaguar': 'kuiní ',
        'jaguar': 'kuní ',
        'jarro': 'tindohò ',
        'la': 'ná ',
        'lago': 'ndòhyo', 
        'lejos': 'jíká ',
        'lengua': 'yaa ',
        'leña': 'ndukú ',
        'llama': 'nání ',
        'llamarse': 'nání ',
        'llamas': 'náníró ',
        'llamo': 'nání ',
        'llegar': 'chaá',
        'lumbre': 'ñuhù',
        'madera': 'yunu ',
        'madre': 'náà ',
        'maguey': 'yáú ',
        'mano': 'ndaha ',
        'mayor': 'yukuée ',
        'me': 'ná ',
        'mentira': 'adio ndije ', 
        'mercado': 'yahu ',
        'mero': 'máá ', 
        'mi': 'ri',
        'mirar': 'koto ', 
        'mismo': 'máá ', 
        'monte': 'yuko ',
        'mucho': 'anáan ',
        'mucho': 'shraán ',
        'mujer': 'adíi ',
        'musica': 'yàà ',
        'muy': 'shraán ',
        'nada': 'adana ',
        'nahual': 'akitsi ', 
        'no': 'a´an ', 
        'no': 'amiñi ',
        'noche': 'akuaa ', 
        'noche': 'kua ',
        'noches': 'kuaa ',
        'nunca': 'ama  ',
        'nunca': 'avasa ',
        'o': 'shí ',
        'odiar': 'koto-uhù ',
        'olla': 'kisi ',
        'otro': 'inga ',
        'padre': 'táà ',
        'para': 'ja kúu ',
        'parados': 'ká-íin',
        'pecho': 'jikà ',
        'pegar': 'kani ',
        'pena': 'aa ',
        'pesos': 'pesos', 
        'petate': 'yuu ',
        'piedra': 'yuú',
        'plato': 'kohò',
        'poner': 'cháá',
        'poseer': 'ñavàha ',
        'posible': 'akuvi ', 
        'probablemente': 'akiva ', 
        'pueblo': 'ñuù ',
        'qué': 'da ', 
        'que': 'já ',
        'queda': 'ndòó',
        'quedarse': 'ndòó',
        'quiere': 'kuní',
        'quizá': 'akiva ', 
        'recoger': 'nastútú ',
        'recordar': 'náhá ',
        'regresar': 'yàà(kuánoho a casa) ',
        'relajado': 'kuééni ',
        'repartir': 'tehndè ',
        'repente': 'ama ', 
        'rojo': 'akuáa ', 
        'romperse': 'tehndè ',
        'sabroso': 'adin ''ó ajin',
        'salado': 'ada ', 
        'salir': 'nana ',
        'se': 'kúu es ser pero  ',
        'seco': 'íchí ',
        'señor':'ihá(divino)',
        'ser': 'kúu ',
        'si':'véè', 
        'solamente':'ni',
        'sólido': 'yúú ',
        'sorpresa': 'aa ',
        'su': 'ní ',
        'tamal de helote': 'suu ',
        'tambien': 'suni ',
        'tarde': 'ñín ',
        'tarde': 'xañini ',
        'tardes': 'ñíni ', 
        'tierra': 'ñuhu ', 
        'tio': 'stoò ', 
        'todo': 'níí', 
        'tomar':'koro',
        'trabajo': 'tiun ',
        'trasero': 'shruù ',
        'tu': 'ró', 
        'un': 'in ',
        'una': 'in ',
        'uno': 'in ',
        'usted': 'ní ',
        'va': 'kihín ',
        'veinte':'okò',
        'vender':'shikó',
        'venir': 'cháá ',
        'verdaderamente': 'andaa ' ' kuiti',
        'verde': 'akuii ', 
        'verdura': 'nduà  ',
        'virgen':'ihà(síhí)',
        'volver': 'nduu ',
        'volver':'nduu',
        'voy': 'kihín  ',
        'vueltas': 'jikó ',
        'y': 'te ',
        'yo': 'ri ',
       'alla': 'andajan ',
       'alla': 'andajan ',
       'alma':'ani ',
       'anesteciar': 'asixixin ',
       'anotar':'anee ',
       'antiguo': 'ata ',
       'añejo': 'ava ',
       'bisabuelo': 'ata ''sánu ''siko ',
       'blancura': 'ayaa ' ' vìi ',
       'borrador': 'asndoo ',
       'caca': 'atyatya ',
       'calambre': 'atiyi ',
       'caro': 'ávi ',
       'cielo': 'andeve ',
       'consumir': 'ayaji ',
       'corazon':'anu ''anima ',
       'deidad':'ane ' 'ñúun',
       'dios':'ane ' 'ñúun',
       'él': 'da ',
       'entumir': 'asixixin ',
       'espiritu': 'ani ',
       'excremento': 'atyatya ',
       'frio': 'avijin ',
       'gente': 'ayavi ',
       'grande':'anduve ',
       'hoy': 'avine ',
       'ignora': 'atuu '  '  ini' ,
       'incierto': 'andije ',
       'insomnio': 'atuu '' ñidi',
       'juguete': 'asiki ',
       'lápiz': 'atee ',
       'mala': 'atuu '' ñúun iñi',
       'malo': 'aniváa ',
       'malo': 'atuu '' ñúun iñi',
       'mercado': 'ávi ',
       'nada': 'atuu ',
       'nadie': 'ayoo ',
       'negro': 'atuun ',
       'ninguno': 'ayoo ',
       'nunca': 'atnaa ',
       'panteon': 'andaya ',
       'permiso': 'ayáa ',
       'persona': 'ayivi ',
       'plaza': 'ávi ',
       'poderoso': 'atu ',
       'polvo': 'ayaka ',
       'quien':'andu',
       'rayo': 'atajia ',
       'registrar':'anee ',
       'salada': 'axe ',
       'simple': 'atuu   '' diko ',
       'terminado': 'ankuvi ',
       'tianguis': 'ávi ',
       'tibio': 'daa ',
       'vacio': 'atuu  ''jañúun ',
       'viejo': 'ata ',


}

def traducir_oracion(oracion):
    palabras = oracion.split()
    oracion_traducida = " ".join([diccionario.get(palabra.lower(), palabra) for palabra in palabras])
    return oracion_traducida

#import streamlit as st
# Load and display the image
#imagen = " https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.wolterskluwer.com%2Fen%2Fexpert-insights%2Fgenerative-ai-trends-to-watch&psig=AOvVaw3T1d3Uo45nWmKRh2QZSHfX&ust=1718343291412000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqGAoTCLjRz-nt14YDFQAAAAAdAAAAABDtAQ "
#st.image(imagen, caption='Es ', use_column_width=True )


st.title("Traductor de Español a Mixteco")

# Preguntar al usuario por una oración en español
oracion = st.text_input("Ingresa una oración en español, los pronombres posesivos van despues del sujeto, ejemplo: Padre mi va al centro").lower()

if st.button("Traducir"):
    oracion_traducida = traducir_oracion(oracion)
   
    
    st.write(f"Traducción: {oracion_traducida.capitalize()} ")





     
   
