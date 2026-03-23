#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ********** IMPORTACIÓN DE LIBRERÍAS Y DATOS ************#

import nltk

# Nos aseguramos de que los recursos necesarios de NLTK están disponibles.
for resource in ["punkt", "punkt_tab"]:
    try:
        nltk.data.find(f"tokenizers/{resource}")
    except LookupError:
        nltk.download(resource)

from nltk.tokenize import word_tokenize

# Lectura del fichero de texto
with open('./texto.txt', encoding='utf-8') as f:
    words = word_tokenize(f.read().lower())

# Mostramos las palabras del texto más frequentes
fd = nltk.FreqDist(words)
fdf= fd.most_common(30)

print ('Palabras del texto ordenadas por frecuencia')
t=''
for w in fdf:
    t+='('+w[0]+','+str(w[1])+') '
print (t)


# ********** DICCIONARIO ************#

# Creamos un diccionario diccionario={} con las palabras que el algoritmo buscará literalmente, 
# con sus correspondientes categorias

# Se han incluído aquí todas las partículas que no tienen flexión (preposiciones, conjunciones, abreviaturas, 
# algunos adverbios), así como algunos nombres y verbos irregulares que aparecían en el texto de entramiento
# Para los grupos cerrados o semicerrados de partículas (preposiciones, conjunciones, adverbios), se ha consultado
# el Manual de la Nueva Gramática de la Lengua Española (RAE 2010)  y se han incorporado todas las más usuales.

diccionario ={}

diccionario['computadora']='NCFS'
diccionario['es']='VMIP3S'
diccionario['que']='PRON'
diccionario['y']='CONJ'
diccionario['para']='PREP'
diccionario['en']='PREP'
diccionario['a']='PREP'
diccionario['de']='PREP'
diccionario['salida']='NCFS'
diccionario['.']='PUNT'
diccionario['o']='CONJ'
diccionario['sistema']='NCMS'
diccionario['por']='PREP'
diccionario[',']='PUNT'
diccionario['como']='CONJ'
diccionario['autómata']='NCMS'
diccionario['más']='ADV'
diccionario['material']='NCMS'
diccionario['sobre']='PREP'
diccionario['permite']='VMIP3S'
diccionario[';']='PUNT'
diccionario['partes']='NCFP'
diccionario[':']='PUNT'
diccionario['computadoras']='NCFP'
diccionario['dispositivo']='NCMS'
diccionario['etc.']='ABRV'
diccionario['al']='PREP+ART'
diccionario['gestión']='NCFS'
diccionario['bases']='NCFP'
diccionario['informática']='NCFS'
diccionario['cables']='NCMP'
diccionario['e']='CONJ'
diccionario['conoce']='VMIP3S'
diccionario['comprende']='VMIP3S'
diccionario['son']='VMIP3P'
diccionario['entre']='PREP'
diccionario['hace']='VMIP3S'
diccionario['(']='PUNT'
diccionario['u']='CONJ'
diccionario[')']='PUNT'
diccionario['envía']='VMIP3S'
diccionario['ejecuta']='VMIP3S'
diccionario['cpu']='NCFS'
diccionario['dispositivos']='NCMP'
diccionario['interpreta']='VMIP3S'
diccionario['programa']='NCMS'
diccionario['mediante']='PREP'
diccionario['del']='PREP+ART'
diccionario['han']='VAIP3P'
diccionario['estado']='VAP0MS'
diccionario['desde']='PREP'
diccionario['ha']='VAIP3S'
diccionario['primeros']='NUM'
diccionario['pero']='CONJ'
diccionario['sigue']='VMIP3S'
diccionario['misma']='ADJ'
diccionario['bajo']='PREP'
diccionario['controla']='VMIP3S'
diccionario['está']='VAIP3S'
diccionario['con']='PREP'
diccionario['directa']='ADJ'
diccionario['escritas']='VMP0FP'
diccionario['fuente']='NCFS'
diccionario['le']='PRON'
diccionario['líneas']='NCFP'
diccionario['dicho']='VMP0MS'
diccionario[' ']='PUNT'
diccionario['   ']='PUNT'
diccionario['-']='PUNT'
diccionario['!']='PUNT'
diccionario['¡']='PUNT'
diccionario['¿']='PUNT'
diccionario['...']='PUNT'
diccionario['"']='PUNT'
diccionario['abajo']='ADV'
diccionario['acaso']='ADV'
diccionario['adelante']='ADV'
diccionario['adentro']='ADV'
diccionario['afuera']='ADV'
diccionario['ahí']='ADV'
diccionario['ahora']='ADV'
diccionario['algo']='PRON'
diccionario['alguien']='PRON'
diccionario['allá']='ADV'
diccionario['allí']='ADV'
diccionario['ante']='PREP'
diccionario['antes']='ADV'
diccionario['aquí']='ADV'
diccionario['arriba']='ADV'
diccionario['así']='ADV'
diccionario['atrás']='ADV'
diccionario['aunque']='CONJ'
diccionario['bastantes']='DET'
diccionario['bien']='ADV'
diccionario['cabe']='VMIPES'
diccionario['cada']='DET'
diccionario['cerca']='ADV'
diccionario['cómo']='PRON'
diccionario['conque']='CONJ'
diccionario['contra']='PREP'
diccionario['cuando']='CONJ'
diccionario['cuánta']='PRON'
diccionario['cuanto']='PRON'
diccionario['debajo']='ADV'
diccionario['delante']='ADV'
diccionario['demás']='PRON'
diccionario['demasiado']='ADV'
diccionario['dentro']='ADV'
diccionario['después']='ADV'
diccionario['detrás']='ADV'
diccionario['donde']='PRON'
diccionario['durante']='PREP'
diccionario['él']='PRON'
diccionario['encima']='ADV'
diccionario['enseguida']='ADV'
diccionario['entonces']='ADV'
diccionario['fuera']='ADV'
diccionario['hacia']='PREP'
diccionario['hasta']='PREP'
diccionario['hoy']='ADV'
diccionario['incluso']='ADV'
diccionario['lejos']='ADV'
diccionario['mal']='ADV'
diccionario['mañana']='ADV'
diccionario['mas']='CONJ'
diccionario['mí']='PRON'
diccionario['mucho']='ADV'
diccionario['nada']='PRON'
diccionario['nadie']='PRON'
diccionario['ni']='CONJ'
diccionario['no']='ADV'
diccionario['nunca']='ADV'
diccionario['poco']='ADV'
diccionario['porque']='CONJ'
diccionario['pronto']='ADV'
diccionario['qué']='PRON'
diccionario['quien']='PRON'
diccionario['quienes']='PRON'
diccionario['quizá']='ADV'
diccionario['salvo']='PREP'
diccionario['según']='PREP'
diccionario['si']='CONJ'
diccionario['sí']='ADV'
diccionario['siempre']='ADV'
diccionario['sin']='PREP'
diccionario['sino']='CONJ'
diccionario['también']='ADV'
diccionario['tan']='ADV'
diccionario['tanto']='ADV'
diccionario['temprano']='ADV'
diccionario['tras']='PREP'
diccionario['tú']='PRON'
diccionario['uno']='PRON'
diccionario['versus']='PREP'
diccionario['yo']='PRON'
diccionario['menos']='ADV'
diccionario['eso']='PRON'

diccionario['entrada/salida']='NCFP' # Aunque no sea exactamente asi, preferimos que el sistema lo etiquete así.

#SINGULARES Y PLURALES de palabras que aparecen en el texto de entrenamiento
diccionario['salidas']='NCFP'
diccionario['sistemas']='NCMP'
diccionario['autómatas']='NCMP'
diccionario['materiales']='NCMP'
diccionario['base']='NCCS'
diccionario['dato']='NCMS'
diccionario['parte']='NCFS'
diccionario['fuentes']='NCFP'
diccionario['cable']='NCMS'
diccionario['interpretan']='VMIP3P'
diccionario['programas']='NCMP'
diccionario['dispositivos']='NCMP' #para excluirlo de la regla ADJ -ivo(s)
diccionario['estados']='NCMP'

#FIN DICCIONARIO#


# ************ EXPRESIONES REGULARES ************#

# Creamos una lista p=[] con las expresiones regulares que el algoritmo aplicará a las palabras del texto, 
# en orden de prioridad de ejecución, de más específicas a más genéricas.

p=[

#PALABRAS COMPLETAS flexionadas# (se consideran únicamente las que aparecen en el texto de entrenamiento)
################################
#Se presentan ordenadas por categorías (al ser reglas específicas para palabras completas, el orden no es importante, 
# mientras estén antes que las reglas más genéricas)

#Determinantes (artículos)
(r'\b(el|l[ao]s?)?$','ART'),  #el

#Determinantes (otros)
#demostrativos
(r'\best?[eao]?s?$','DET'),  #este, ese
(r'\baquel(l[ao]s?)?$','DET'),  #aquella, aquellas, aquellos (aceptará aquela,etc.)

#indefinidos
(r'\bun[a]?(os|s)?$','DET'),  #un
(r'\balg[uú]n[a]?(os|s)?$','DET'),  #algún (aceptará "algun")
(r'\bning[uú]n[a]?(os|s)?$','DET'),  #ningún (aceptará "ningun")
(r'\btod[oa]s?$','DET'),  #todo
(r'\botr[oa]s?$','DET'),  #otro
(r'\bmuch[oa]s?$','DET'),  #mucho (Ídem)
(r'\bpoc[oa]s?$','DET'),  #poco (Ídem)
(r'\btant[oa]s?$','DET'),  #tanto (Ídem)
(r'\bvari[oa]s$','DET'),  #varias, varios (Nótese que esta forma no tiene singular) 
(r'\bamb[oa]s$','DET'),  #ambos
(r'\bbastantes?$','DET'),  #bastante
(r'\bciert[oa]s?$','DET'),  #cierto
(r'\bcual(es)?quiera?$','DET'),  #cualquier
(r'\bdemasiad[oa]s?$','DET'),  #demasiado (la forma masculina presente coincide en forma con el adverbio "demasiado", de categoría prioritaria (se incluye en el diccionario)
(r'\bescas[oa]s?$','DET'),  #escaso
(r'\bsendo[oa]s?$','DET'),  #
(r'\btal(es)?$','DET'),  #

#posesivos
(r'\bmis?$','DET'),  #mi mis
(r'\b[ts]us?$','DET'),  #su sus tus sus
(r'\b[nv]uestr[oa]s?$','DET'),  #nuestro vuestro

#Numerales
(r'\b[0-9]+\.?$','NUM'),  #números del cero al 99999... (en cifras) Se incluye la posibilidad que, trás la cifra, haya un número.
(r'\b(((diez)|((on|do|tre|cator|quin|)ce)|((dieci)(séis|siete|ocho|nueve)))|(((veint[ei])|((trein|cuaren|cincuen|sesen|seten|ochen|noven)ta(\sy\s)?)))?([uú]n[oa]?|d[oó]s|tr[eé]s|cuatro|cinco|s[eé]is|siete|ocho|nueve)?)$','NUM'),  #cardinales del uno al noventa y nueve (en texto). Para el "uno" se acepta también la versión apocopada "un". Las versiones ortográficamente incorrectas veintiúno y veintiúna también se aceptan. La palabra "uno" se ha incluído en el diccionario como pronombre.
(r'\b((primer|tercer)|(primer|segund|tercer|cuart|quint|sext|sépt|octav|noven|décim|undécim|duodécim)[oa]s?)$','NUM'),  #Ordinales del primero al duodécimo. Para el singular masculino de "primero" y "tercero", se añaden las formas apocopadas "primer" y "tercer".

#Pronombres
#personales
(r'\bell[ao]s?$','PRON'),  #personales ella  ellos ellas
(r'\b[nv](osotr)[oa]s$','PRON'),  #personales nosotros/as vosotros/as 
(r'\busted(es)?$','PRON'),  #personales usted, ustedes
(r'\b[mtls]es?$','PRON'),  #personales átonos (clíticos) me te le se (aceptará "ses")
(r'\b[nv]?os$','PRON'),  #personales átonos (clíticos) nos os

#demostrativos
(r'\best?[eao]?s?$','PRON'),  #este,ese,... Como también son determinantes y estos tienen prioridad (se han incluído antes), esta regla no será tenida en cuenta.
(r'\baquell[ao]s?$','PRON'),  #aquella, aquellas Ídem.

#relativos
(r'\bcual(es)?$','PRON'),  #cual cuales
(r'\bcuy[oa]s?$','PRON'),  #cuyo cuyas ...

#r'\balgun[oa]s?$','PRON'),  #alguno (detrás de los determinantes indefinidos, para dar prioridad a estos)

(r'\b$','PRON'),   #plantilla para nuevas regex

#Abreviaturas
(r'\betc.?$','ABRV'),  #incluímos el punto opcional, por si algún analizador lo incluye (Freeling lo hace).
(r'\b$','ABRV'),  #plantilla para nuevas regex

#adjetivos terminados en sufijos característicos
#terminación .*[oa]s?
(r'\b.*(a|i)d[oa]s?$','ADJ'),  # -ado / -ido (integrado, interrelacionadas). En algunos casos, el participio correspondiente se ha incluído en el diccionario, de modo que sea elegido de forma prioritaria. El criterio se ha basado en la probabilidad de aparicíón de la palabra según Freeling, con algunas excepciones, en que nos hemos basado en el texto de entrenamiento.
(r'\b.*ic[oa]s?$','ADJ'),  #-ico (informático, electróni""co, eléctrico, electromecánicos, periféricos)
(r'\b.*iv[oa]s?$','ADJ'),  #-ivo (operativo)
#(r'\b.*ífic[oa]s?$','ADJ'),  #-ífico (específicas)
(r'\b.*XX[oa]s?$','ADJ'),  #-

#terminación .*(es)?
(r'\b.*al(es)?$','ADJ'),  #-al (digital, central, personal)
(r'\b.*XX(es)?$','ADJ'),  #-

#terminación .*s?
(r'\b.*antes?$','ADJ'),   #-ante (importante)
(r'\b.*ables?$','ADJ'),   #-able (interpretable, microprogramable, ejecutable)
(r'\b.*ibles?$','ADJ'),   #-ible (tangibles, intangible, posible, legible)
#(r'\b.*XXs?$','ADJ'),   #-XX

#otros adjetivos (se consideran únicamente los que aparecen en el texto de entrenamiento)
#flexión .*[oa]s?
(r'\bpequeñ[oa]s?$','ADJ'),
(r'\bextern[oa]s?$','ADJ'),
(r'\búltim[oa]s?$','ADJ'),
(r'\bnecesari[oa]s?$','ADJ'),
(r'\bmism[oa]s?$','ADJ'),
(r'\bhuman[oa]s?$','ADJ'),
(r'\bescas[oa]s?$','ADJ'),
(r'\bsol[oa]s?$','ADJ'),
(r'\bXXX[oa]s?$','ADJ'),  #plantilla para nuevas regex

#flexión .*(es)?
(r'\bútil(es)?$','ADJ'),  
(r'\bXXX(es)?$','ADJ'),  #plantilla para nuevas regex

#flexión .*s?
(r'\bconvenientes?$','ADJ'),
(r'\bimportantes?$','ADJ'),
(r'\bhuman[oa]s?$','ADJ'),
(r'\bXXXs?$','ADJ'),  #plantilla para nuevas regex

#Nombres
(r'\bware$','NCMS'),  #angicismos -ware (software,...)
(r'\bwares$','NCMP'),  

#Excepciones a reglas que se incluirán más abajo
(r'\b.*imagen$','NCMS'),  # imagen, contraimagen


#TERMINACIONES que se presentan con cierta regularidad#
#######################################################
#Se presentan ordenadas por prioridad de ejecución, de más específicas a más genéricas. Si tienen la misma prioridad, es decir, no se sustituyen entre ellas, se agrupan por categorías.

#adverbios
(r'.*mente$','ADV'),  #-mente

#verbos
#formas impersonales
(r'\b.*(a|e|i)r$','VMN'),  # infinitivos (almacenar, procesar)
(r'\b.*(a|ie)ndo$','VMG'),  # gerundios (haciendo) EXCEPCIONES: cuando,bando,blando,comando,doctorando,mando...)

#formas impersonales con pronombres enclíticos
(r'\b.*(a|e|i)r(([mts]e)|(l[aeo]s?)|(n?os))$','VMN+PRON'),  #infinitivos + pronombres #me, te, se, le, les, la, las, lo, los, nos, os
(r'\b.*(a|ie)ndo(([mts]e)|(l[aeo]s?)|(n?os))$','VMG+PRON'),  #gerundios #me, te, se, le, les, la, las, lo, los, nos, os
(r'\b.*(a|ie)ndo(([mts]e)|(l[aeo]s?)|(n?os))$','VMG+PRON'),  #gerundios #me, te, se, le, les, la, las, lo, los, nos, os

#Verbo Principal Indicativo Presente Tercera Singular
(r'\b.*ee$','VMIP3S'),  # -ee (lee)
(r'\b.*iza$','VMIP3S'),  # -iza (realiza)(hay muchos más verbos acabados en -izar que nombres acabados en -iza)
(r'\b.*ye$','VMIP3S'),  # -ye (incluye)
(r'\b.*iere$','VMIP3S'),  # -iere (requiere)
(r'\b.*iene$','VMIP3S'),  # -iene (única EXCEPCIÓN: higiene)
(r'\b.*ede$','VMIP3S'),  # -ede (única EXCEPCIÓN importante: sede)
(r'\b.*ebe$','VMIP3S'),  # -ebe (únicas EXCEPCIÓN plebe, percebe)
(r'\b.*ece$','VMIP3S'),  # -ece (únicas EXCEPCIÓN trece, contemplada más arriba)
(r'\b$','VMIP3S'),   #plantilla para nuevas regex

#Verbo Principal Indicativo Presente Tercera Plural
(r'\b.*[ae]n$','VMIP3P'),  # -an, -en (envían, fabrican, componen) (EXCEPCIONES IMPORTANTES: imagen, plan)
#(r'\b.*izan$','VMIP3P'),  # -izan (hay muchos más verbos acabados en -izar que nombres acabados en -iza
#(r'\b.*ten$','VMIP3P'),  # -ten (hay muchos más verbos acabados en -izar que nombres acabados en -iza
(r'\b$','VMIP3P'),   #plantilla para nuevas regex

#Nombres femeninos que no acaban en -a
(r'\b.*[cs]ión$','NCFS'),  #-ión (información, dimensión)
(r'\b.*[cs]iones$','NCFP'),  #-ciones -siones
(r'\b.*idad$','NCFS'),  #-idad (unidad)
(r'\b.*idades?$','NCFP'),  #-idades 
(r'\b.*[cr]ie$','NCFS'),  #-cie -rie superfície
(r'\b.*[cr]ies?$','NCFP'),  #-cies -ries

#REGLAS FINALES#
#######################################################
#Las palabras que no sigan las reglas anteriores y no estén en diccionario, se clasificarán como nombres, según las reglas finales.
(r'.*as$','NCFP'),
(r'.*s$','NCMP'),

#femenino singular
(r'.*a$','NCFS'),

#masculino singular
(r'.*$','NCMS'),

    ]

# FIN EXPRESIONES REGULARES #

#******** ETIQUETADO DE LAS PALABRAS DEL TEXTO ************# 

# Etiquetamos el texto importado "words" aplicando las reglas incluídas en la lista de regex "p" 
# y las categorías indicadas en "diccionario". 

rt=nltk.RegexpTagger(p)
taggedText=rt.tag(words)
for item in taggedText:
    if item[0] in diccionario:
        print (item[0],' ',diccionario[item[0]])
    else:
        print (item[0]+' '+item[1])
