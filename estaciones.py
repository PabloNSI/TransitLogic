# Lista de estaciones
estaciones = [
    # Linea 1
    "Pinar de Chamartín", "Bambú", "Chamartín", "Plaza de Castilla", "Valdeacederas", "Tetuán",
    "Estrecho", "Alvarado", "Cuatro Caminos", "Ríos Rosas", "Iglesia", "Bilbao", "Tribunal", "Gran Vía", "Sol",
    "Tirso de Molina", "Antón Martín", "Estación del Arte", "Atocha", "Menéndez Pelayo", "Pacífico",
    "Puente de Vallecas", "Nueva Numancia", "Portazgo", "Buenos Aires", "Alto del Arenal", "Miguel Hernández",
    "Sierra de Guadalupe", "Villa de Vallecas", "Congosto", "La Gavia", "Las Suertes", "Valdecarros",
    # Linea 2
    "Las Rosas", "Avenida de Guadalajara", "Alsacia", "La Almudena", "La Elipa", "Ventas","Goya",
    "Manuel Becerra", "Príncipe de Vergara", "Retiro", "Banco de España", "Sevilla", "Sol",
    "Ópera", "Santo Domingo", "Noviciado", "San Bernardo", "Quevedo", "Canal", "Cuatro Caminos",
    # Linea 3
    "Villaverde Alto", "San Cristóbal", "Villaverde Bajo-Cruce", "Ciudad de los Ángeles", 
    "San Fermín-Orcasur", "Hospital 12 de Octubre", "Almendrales", "Legazpi", "Delicias", 
    "Palos de la Frontera", "Embajadores", "Lavapiés", "Callao", "Plaza de España", 
    "Ventura Rodríguez", "Argüelles", "Moncloa","Sol","Acacias",
    # Linea 4
    "Pinar de Chamartín",  "Bilbao","Argüelles",
    "San Bernardo", "Alonso Martínez", "Colón", "Serrano", "Velázquez","Gran Vía",
    "Goya", "Diego de León", "Avenida de América", "Prosperidad", "Alfonso XIII",
    "Avenida de la Paz", "Arturo Soria", "Esperanza", "Canillas", "Mar de Cristal", "San Lorenzo",
    "Parque de Santa María", "Hortaleza", "Manoteras",
    # Linea 5
    "Alameda de Osuna", "El Capricho", "Canillejas", "Torre Arias", "Suanzes", "Ciudad Lineal",
    "Pueblo Nuevo", "Quintana", "El Carmen", "Ventas", "Núñez de Balboa",
    "Rubén Darío",  "Chueca", "La Latina", "Ópera",  "Alonso Martínez",
    "Puerta de Toledo", "Acacias", "Pirámides", "Marqués de Vadillo", "Urgel", "Oporto", 
    "Vista Alegre", "Carabanchel", "Eugenia de Montijo", "Aluche", "Empalme", "Campamento", 
    "Casa de Campo","Embajadores","Diego de León","Callao",
    # # Linea 6
    # "Laguna", "Carpetana", "Oporto", "Opañel", "Plaza Elíptica", "Usera","Moncloa"
    # "Arganzuela-Planetario", "Méndez Álvaro", "Pacifico", "Conde de Casal", "Sainz de Baranda",
    # "O'Donnell", "República Argentina","Pacífico","Legazpi","Argüelles",
    # "Nuevos Ministerios", "Cuatro Caminos", "Guzmán el Bueno", "Vicente Aleixandre", 
    # "Ciudad Universitaria", "Príncipe Pío", "Puerta del Ángel","Avenida de América",
    # "Alto de Extremadura", "Lucero","Manuel Becerra","Diego de León",
    # # Linea 7
    # "Pitis", "Arroyofresno", "Lacoma", "Avenida de la Ilustración", "Peñagrande", 
    # "Antonio Machado", "Valdezarza", "Francos Rodríguez", "Guzmán el Bueno", "Islas Filipinas", 
    # "Alonso Cano", "Gregorio Marañón", "Cartagena", 
    # "Parque de las Avenidas", "Barrio de la Concepción", "Pueblo Nuevo", "Ascao",
    # "García Noblejas", "Simancas", "San Blas", "Las Musas", "Estadio Metropolitano", 
    # "Barrio del Puerto", "Coslada Central", "La Rambla", "San Fernando", "Jarama", 
    # "Henares", "Hospital del Henares","Canal","Avenida de América",
    # # Linea 9
    # "Plaza de Castilla",
    # "Paco de Lucía", "Mirasierra", "Herrera Oria", "Barrio del Pilar", "Ventilla", 
    # "Plaza Castilla", "Duque de Pastrana", "Pio XII", "Colombia", "Concha Espina",
    # "Cruz del Rayo", "Núñez de Balboa", "Príncipe de Vergara","Avenida de América",
    # "Ibiza", "Sainz de Baranda", "Estrella", "Vinateros", "Artilleros", "Pavones", 
    # "Valdebernardo", "Vicálvaro", "San Cipriano", "Puerta de Arganda", "Rivas Urbanizaciones",
    # "Rivas Futura", "Rivas Vaciamadrid", "La Poveda", "Arganda del Rey",
    # # Linea 10
    # "Hospital Infanta Sofía", "Reyes Católicos", "Baunatal", "Manuel de Falla", 
    # "Marqués de la Valdavia", "La Moraleja", "La Granja", "Ronda de la Comunicación", 
    # "Las Tablas", "Montecarmelo", "Tres Olivos", "Fuencarral", "Begoña", "Chamartín", 
    # "Plaza de Castilla", "Cuzco", "Santiago Bernabéu", "Nuevos Ministerios", "Gregorio Marañón",
    # "Príncipe Pío", "Lago", "Batán","Tribunal",
    # "Casa de Campo", "Colonia Jardín", "Aviación Española", "Cuatro Vientos",
    # "Joaquín Vilumbrales", "Puerta del Sur", "Alonso Martínez", 

]

pos = {
    # Línea 1
    "Pinar de Chamartín": (4370,5780), "Bambú": (4000,5650), "Chamartín": (3560,5650), 
    "Plaza de Castilla": (3500,5460), "Valdeacederas": (3210,5420), "Tetuán": (3100,5320),
    "Estrecho": (3070,5190), "Alvarado": (3070,5060), "Cuatro Caminos": (3070,4770), 
    "Ríos Rosas": (3260, 4570), "Iglesia": (3300,4310), "Bilbao": (3300,4130), "Tribunal": (3300,3830), 
    "Gran Vía": (3300,3540), "Sol": (3300,3300), "Tirso de Molina": (3480,3180), "Antón Martín": (3590,3070), 
    "Estación del Arte": (3700,2970), "Atocha": (3800,2860), "Menéndez Pelayo": (3950,2710), 
    "Pacífico": (4120,2540), "Puente de Vallecas": (4250,2410), "Nueva Numancia": (4330,2340), 
    "Portazgo": (4400,2270), "Buenos Aires": (4420,2180), "Alto del Arenal": (4420,2070), 
    "Miguel Hernández": (4420,1970), "Sierra de Guadalupe": (4420,1870), "Villa de Vallecas": (4420,1700), 
    "Congosto": (4420,1570), "La Gavia": (4470,1450), "Las Suertes": (4550,1370), "Valdecarros": (4630,1280),

    # Línea 2
    "Las Rosas": (5730, 3540), "Avenida de Guadalajara": (5520,3540), "Alsacia": (5300,3540), 
    "La Almudena": (5090,3720), "La Elipa": (4920,3910), "Ventas": (4630,4170), "Manuel Becerra": (4450,4000), 
    "Goya": (4270,3830), "Príncipe de Vergara": (4070,3630), "Retiro": (4000, 3530), "Banco de España": (3860,3410), 
    "Sevilla": (3620,3300),"Sol": (3300,3300), "Ópera": (3070,3300), "Santo Domingo": (3070,3530), "Noviciado": (3070,3750),
    "San Bernardo": (3070,4130), "Quevedo": (3070,4280), "Canal": (3070,4390),"Cuatro Caminos": (3070,4770),

    # Línea 3
    "Villaverde Alto": (3130,1180), "San Cristóbal": (3220,1260), "Villaverde Bajo-Cruce": (3270,1330), 
    "Ciudad de los Ángeles": (3270,1480), "San Fermín-Orcasur": (3270,1610), "Hospital 12 de Octubre": (3270,1630), 
    "Almendrales": (3270,1860), "Legazpi": (3520,2140), "Delicias": (3520,2460), "Palos de la Frontera": (3520,2630),
    "Embajadores": (3350,2880), "Lavapiés": (3350,3030), "Callao": (3200,3430), "Sol": (3300,3300),"Acacias": (3260,2880),
    "Plaza de España": (2840,3790), "Ventura Rodríguez": (2690,3940), "Argüelles": (2470,4130), "Moncloa": (2370,4240),

    # Línea 4
    "Argüelles": (2470,4130), "Alonso Martínez": (3560,3840), "Colón": (3780,3840), "Serrano": (3900,3840), "Velázquez": (4110,3840),
    "Lista": (4270,3990), "Diego de León": (4270,4230), "Avenida de América": (4090,4390), "Prosperidad": (4260,4540),"Pinar de Chamartín": (4370,5780),
    "Alfonso XIII": (4390,4670), "Avenida de la Paz": (4540,4820), "Arturo Soria": (4680,4970), "Esperanza": (4820,5100),
    "Canillas": (4880,5230), "Mar de Cristal": (4880,5370), "San Lorenzo": (4880,5540), "Parque de Santa María": (4860,5650), 
    "Hortaleza": (4760,5740), "Manoteras": (4700,5770),"Goya": (4270,3830), "San Bernardo": (3070,4130),"Bilbao": (3300,4130), 

    # Línea 5
    "Alameda de Osuna": (5850,4870), "El Capricho": (5750,4760), "Canillejas": (5630,4650), "Torre Arias": (5500,4530),
    "Suanzes": (5390,4410), "Ciudad Lineal": (5270,4290), "Pueblo Nuevo": (5150,4170), "Quintana": (4970,4170), "Diego de León": (4270,4230),
    "El Carmen": (4820,4170), "Ventas": (4630,4170),  "Núñez de Balboa": (3930,4170), "Gran Vía": (3300,3540), "Embajadores": (3350,2880),
    "Rubén Darío": (3760,4000), "Chueca": (3430,3470), "La Latina": (3060,3180), "Puerta de Toledo": (3100,3080), "Ópera": (3070,3300),
    "Acacias": (3260,2880), "Pirámides": (3160,2760), "Marqués de Vadillo": (2970,2580), "Urgel": (2840,2460), "Alonso Martínez": (3560,3840), 
    "Oporto": (2710,2320), "Vista Alegre": (2610,2210), "Carabanchel": (2430,2160), "Eugenia de Montijo": (2300,2210), 
    "Aluche": (2200,2340), "Empalme": (2200,2480), "Campamento": (2200,2620), "Casa de Campo": (2200,3130), "Callao": (3200,3430),

    # # Línea 6
    # "Laguna": (1000, 400), "Carpetana": (1010, 410), "Oporto": (2710,2320), "Opañel": (530, 810), 
    # "Plaza Elíptica": (520, 820), "Usera": (510, 830), "Arganzuela-Planetario": (1035, 560), "Argüelles": (2470,4130),
    # "Méndez Álvaro": (1030, 550), "Pacifico": (780, 800), "Conde de Casal": (1025, 540), "Sainz de Baranda": (1020, 530),
    # "O'Donnell": (1015, 520),"Manuel Becerra": (4450,4000), "Legazpi": (3520,2140),
    # "República Argentina": (820, 470), "Nuevos Ministerios": (735, 460), "Avenida de América": (4090,4390),
    # "Guzmán el Bueno": (630, 405), "Vicente Aleixandre": (620, 395), "Ciudad Universitaria": (610, 380),
    # "Príncipe Pío": (572, 632), "Puerta del Ángel": (584, 623),"Diego de León": (4270,4230),
    # "Alto de Extremadura": (600, 610), "Lucero": (610, 600), "Moncloa": (2370,4240),

    # # Línea 7
    # "Pitis": (1050, 170), "Arroyofresno": (1040, 180), "Lacoma": (1030, 190), "Avenida de la Ilustración": (1020, 200),
    # "Peñagrande": (1010, 210), "Antonio Machado": (1000, 220), "Valdezarza": (990, 230), "Francos Rodríguez": (980, 240),
    # "Guzmán el Bueno": (970, 250), "Islas Filipinas": (960, 260), "Alonso Cano": (940, 280),
    # "Gregorio Marañón": (930, 290), "Cartagena": (910, 310), "Parque de las Avenidas": (900, 320),
    # "Barrio de la Concepción": (890, 330), "Pueblo Nuevo": (5150,4170), "Ascao": (870, 350), "García Noblejas": (860, 360),
    # "Simancas": (850, 370), "San Blas": (840, 380), "Las Musas": (830, 390), "Estadio Metropolitano": (820, 400),
    # "Barrio del Puerto": (810, 410), "Coslada Central": (800, 420), "La Rambla": (790, 430), "San Fernando": (780, 440),
    # "Jarama": (770, 450), "Henares": (760, 460), "Hospital del Henares": (750, 470), "Avenida de América": (4090,4390),

    # # Línea 9
    # "Paco de Lucía": (1050, 500), "Mirasierra": (1040, 510), "Herrera Oria": (1030, 520),
    # "Barrio del Pilar": (1020, 530), "Ventilla": (1010, 540), "Plaza Castilla": (980, 550),
    # "Duque de Pastrana": (960, 560), "Pio XII": (940, 570), "Colombia": (920, 580),
    # "Concha Espina": (900, 590), "Cruz del Rayo": (880, 600),
    # "Núñez de Balboa": (3930,4170), "Ibiza": (800, 640),"Príncipe de Vergara": (4070,3630),
    # "Sainz de Baranda": (780, 650), "Estrella": (760, 660), "Vinateros": (740, 670),
    # "Artilleros": (720, 680), "Pavones": (700, 690), "Valdebernardo": (680, 700),
    # "Vicálvaro": (660, 710), "San Cipriano": (640, 720), "Puerta de Arganda": (620, 730),
    # "Rivas Urbanizaciones": (600, 740), "Rivas Futura": (580, 750), "Rivas Vaciamadrid": (560, 760),
    # "La Poveda": (540, 770), "Arganda del Rey": (520, 780),
    
    # # Línea 10
    # "Hospital Infanta Sofía": (466, 11), "Reyes Católicos": (460, 850), "Baunatal": (470, 860),
    # "Manuel de Falla": (480, 870), "Marqués de la Valdavia": (490, 880), "La Moraleja": (500, 890),
    # "La Granja": (510, 900), "Ronda de la Comunicación": (520, 910), "Las Tablas": (530, 920),
    # "Montecarmelo": (540, 930), "Tres Olivos": (550, 940), "Fuencarral": (560, 950),
    # "Begoña": (570, 960),"Alonso Martínez": (3560,3840), 
    # "Cuzco": (600, 990), "Santiago Bernabéu": (610, 1000), "Nuevos Ministerios": (620, 1010),
    # "Gregorio Marañón": (630, 1020),
    # "Príncipe Pío": (670, 1060), "Lago": (680, 1070),
    # "Batán": (690, 1080), "Casa de Campo": (2200,3130),  "Colonia Jardín": (710, 1100),
    # "Aviación Española": (720, 1110), "Cuatro Vientos": (730, 1120),
    # "Joaquín Vilumbrales": (740, 1130), "Puerta del Sur": (750, 1140),"Plaza de España": (2840,3790),
    
}
