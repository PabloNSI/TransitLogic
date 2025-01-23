t = 1  # Tiempo de viaje entre dos estaciones consecutivas
conexiones = [
        # Línea 1
    ("Pinar de Chamartín", "Bambú", True, "Línea 1", t),
    ("Bambú", "Chamartín", True, "Línea 1", t),
    ("Chamartín", "Plaza de Castilla", True, "Línea 1", t),
    ("Plaza de Castilla", "Valdeacederas", True, "Línea 1", t),
    ("Valdeacederas", "Tetuán", True, "Línea 1", t),
    ("Tetuán", "Estrecho", True, "Línea 1", t),
    ("Estrecho", "Alvarado", True, "Línea 1", t),
    ("Alvarado", "Cuatro Caminos", True, "Línea 1", t),
    ("Cuatro Caminos", "Ríos Rosas", True, "Línea 1", t),
    ("Ríos Rosas", "Iglesia", True, "Línea 1", t),
    ("Iglesia", "Bilbao", True, "Línea 1", t),
    ("Bilbao", "Tribunal", True, "Línea 1", t),
    ("Tribunal", "Gran Vía", True, "Línea 1", t),
    ("Gran Vía", "Sol", True, "Línea 1", t),
    ("Sol", "Tirso de Molina", True, "Línea 1", t),
    ("Tirso de Molina", "Antón Martín", True, "Línea 1", t),
    ("Antón Martín", "Estación del Arte", True, "Línea 1", t),
    ("Estación del Arte", "Atocha", True, "Línea 1", t),
    ("Atocha", "Menéndez Pelayo", True, "Línea 1", t),
    ("Menéndez Pelayo", "Pacífico", True, "Línea 1", t),
    ("Pacífico", "Puente de Vallecas", True, "Línea 1", t),
    ("Puente de Vallecas", "Nueva Numancia", True, "Línea 1", t),
    ("Nueva Numancia", "Portazgo", True, "Línea 1", t),
    ("Portazgo", "Buenos Aires", True, "Línea 1", t),
    ("Buenos Aires", "Alto del Arenal", True, "Línea 1", t),
    ("Alto del Arenal", "Miguel Hernández", True, "Línea 1", t),
    ("Miguel Hernández", "Sierra de Guadalupe", True, "Línea 1", t),
    ("Sierra de Guadalupe", "Villa de Vallecas", True, "Línea 1", t),
    ("Villa de Vallecas", "Congosto", True, "Línea 1", t),
    ("Congosto", "La Gavia", True, "Línea 1", t),
    ("La Gavia", "Las Suertes", True, "Línea 1", t),
    ("Las Suertes", "Valdecarros", True, "Línea 1", t),

    # Línea 2
    ("Cuatro Caminos", "Canal", True, "Línea 2", t),
    ("Canal", "Quevedo", True, "Línea 2", t),
    ("Quevedo", "San Bernardo", True, "Línea 2", t),
    ("San Bernardo", "Noviciado", True, "Línea 2", t),
    ("Noviciado", "Santo Domingo", True, "Línea 2", t),
    ("Santo Domingo", "Ópera", True, "Línea 2", t),
    ("Ópera", "Sol", True, "Línea 2", t),
    ("Sol", "Sevilla", True, "Línea 2", t),
    ("Sevilla", "Banco de España", True, "Línea 2", t),
    ("Banco de España", "Retiro", True, "Línea 2", t),
    ("Retiro", "Príncipe de Vergara", True, "Línea 2", t),
    ("Príncipe de Vergara", "Goya", True, "Línea 2", t),
    ("Goya", "Manuel Becerra", True, "Línea 2", t),
    ("Manuel Becerra", "Ventas", True, "Línea 2", t),
    ("Ventas", "La Elipa", True, "Línea 2", t),
    ("La Elipa", "La Almudena", True, "Línea 2", t),
    ("La Almudena", "Alsacia", True, "Línea 2", t),
    ("Alsacia", "Avenida de Guadalajara", True, "Línea 2", t),
    ("Avenida de Guadalajara", "Las Rosas", True, "Línea 2", t),

    # Línea 3
    ("Moncloa", "Argüelles", True, "Línea 3", t),
    ("Argüelles", "Ventura Rodríguez", True, "Línea 3", t),
    ("Ventura Rodríguez", "Plaza de España", True, "Línea 3", t),
    ("Plaza de España", "Callao", True, "Línea 3", t),
    ("Callao", "Sol", True, "Línea 3", t),
    ("Sol", "Lavapiés", True, "Línea 3", t),
    ("Lavapiés", "Embajadores", True, "Línea 3", t),
    ("Embajadores", "Delicias", True, "Línea 3", t),
    ("Delicias", "Legazpi", True, "Línea 3", t),
    ("Legazpi", "Almendrales", True, "Línea 3", t),
    ("Almendrales", "Hospital 12 de Octubre", True, "Línea 3", t),
    ("Hospital 12 de Octubre", "San Fermín-Orcasur", True, "Línea 3", t),
    ("San Fermín-Orcasur", "Ciudad de los Ángeles", True, "Línea 3", t),
    ("Ciudad de los Ángeles", "Villaverde Bajo-Cruce", True, "Línea 3", t),
    ("Villaverde Bajo-Cruce", "San Cristóbal", True, "Línea 3", t),
    ("San Cristóbal", "Villaverde Alto", True, "Línea 3", t),

    # Línea 4
    ("Argüelles", "San Bernardo", True, "Línea 4", t),
    ("San Bernardo", "Bilbao", True, "Línea 4", t),
    ("Bilbao", "Alonso Martínez", True, "Línea 4", t),
    ("Alonso Martínez", "Colón", True, "Línea 4", t),
    ("Colón", "Serrano", True, "Línea 4", t),
    ("Serrano", "Velázquez", True, "Línea 4", t),
    ("Velázquez", "Goya", True, "Línea 4", t),
    ("Goya", "Lista", True, "Línea 4", t),
    ("Lista", "Diego de León", True, "Línea 4", t),
    ("Diego de León", "Avenida de América", True, "Línea 4", t),
    ("Avenida de América", "Prosperidad", True, "Línea 4", t),
    ("Prosperidad", "Alfonso XIII", True, "Línea 4", t),
    ("Alfonso XIII", "Avenida de la Paz", True, "Línea 4", t),
    ("Avenida de la Paz", "Arturo Soria", True, "Línea 4", t),
    ("Arturo Soria", "Esperanza", True, "Línea 4", t),
    ("Esperanza", "Canillas", True, "Línea 4", t),
    ("Canillas", "Mar de Cristal", True, "Línea 4", t),
    ("Mar de Cristal", "San Lorenzo", True, "Línea 4", t),
    ("San Lorenzo", "Parque de Santa María", True, "Línea 4", t),
    ("Parque de Santa María", "Hortaleza", True, "Línea 4", t),
    ("Hortaleza", "Manoteras", True, "Línea 4", t),
    ("Manoteras", "Pinar de Chamartín", True, "Línea 4", t),

    # Línea 5
    ("Alameda de Osuna", "El Capricho", True, "Línea 5", t),
    ("El Capricho", "Canillejas", True, "Línea 5", t),
    ("Canillejas", "Torre Arias", True, "Línea 5", t),
    ("Torre Arias", "Suanzes", True, "Línea 5", t),
    ("Suanzes", "Ciudad Lineal", True, "Línea 5", t),
    ("Ciudad Lineal", "Pueblo Nuevo", True, "Línea 5", t),
    ("Pueblo Nuevo", "Quintana", True, "Línea 5", t),
    ("Quintana", "El Carmen", True, "Línea 5", t),
    ("El Carmen", "Ventas", True, "Línea 5", t),
    ("Ventas", "Diego de León", True, "Línea 5", t),
    ("Diego de León", "Núñez de Balboa", True, "Línea 5", t),
    ("Núñez de Balboa", "Rubén Darío", True, "Línea 5", t),
    ("Rubén Darío", "Alonso Martínez", True, "Línea 5", t),
    ("Alonso Martínez", "Chueca", True, "Línea 5", t),
    ("Chueca", "Gran Vía", True, "Línea 5", t),
    ("Gran Vía", "Callao", True, "Línea 5", t),
    ("Callao", "Ópera", True, "Línea 5", t),
    ("Ópera", "La Latina", True, "Línea 5", t),
    ("La Latina", "Puerta de Toledo", True, "Línea 5", t),
    ("Puerta de Toledo", "Acacias", True, "Línea 5", t),
    ("Acacias", "Pirámides", True, "Línea 5", t),
    ("Pirámides", "Marqués de Vadillo", True, "Línea 5", t),
    ("Marqués de Vadillo", "Urgel", True, "Línea 5", t),
    ("Urgel", "Oporto", True, "Línea 5", t),
    ("Oporto", "Vista Alegre", True, "Línea 5", t),
    ("Vista Alegre", "Carabanchel", True, "Línea 5", t),
    ("Carabanchel", "Eugenia de Montijo", True, "Línea 5", t),
    ("Eugenia de Montijo", "Aluche", True, "Línea 5", t),
    ("Aluche", "Empalme", True, "Línea 5", t),
    ("Empalme", "Campamento", True, "Línea 5", t),
    ("Campamento", "Casa de Campo", True, "Línea 5", t),

    # # Línea 6
    # ("Cuatro Caminos", "Guzmán el Bueno", True, "Línea 6", t),
    # ("Guzmán el Bueno", "Vicente Aleixandre", True, "Línea 6", t),
    # ("Vicente Aleixandre", "Ciudad Universitaria", True, "Línea 6", t),
    # ("Ciudad Universitaria", "Moncloa", True, "Línea 6", t),
    # ("Moncloa", "Argüelles", True, "Línea 6", t),
    # ("Argüelles", "Príncipe Pío", True, "Línea 6", t),
    # ("Príncipe Pío", "Puerta del Ángel", True, "Línea 6", t),
    # ("Puerta del Ángel", "Alto de Extremadura", True, "Línea 6", t),
    # ("Alto de Extremadura", "Lucero", True, "Línea 6", t),
    # ("Lucero", "Laguna", True, "Línea 6", t),
    # ("Laguna", "Carpetana", True, "Línea 6", t),
    # ("Carpetana", "Oporto", True, "Línea 6", t),
    # ("Oporto", "Opañel", True, "Línea 6", t),
    # ("Opañel", "Plaza Elíptica", True, "Línea 6", t),
    # ("Plaza Elíptica", "Usera", True, "Línea 6", t),
    # ("Usera", "Legazpi", True, "Línea 6", t),
    # ("Legazpi", "Arganzuela-Planetario", True, "Línea 6", t),
    # ("Arganzuela-Planetario", "Méndez Álvaro", True, "Línea 6", t),
    # ("Méndez Álvaro", "Pacífico", True, "Línea 6", t),
    # ("Pacífico", "Conde de Casal", True, "Línea 6", t),
    # ("Conde de Casal", "Sainz de Baranda", True, "Línea 6", t),
    # ("Sainz de Baranda", "O'Donnell", True, "Línea 6", t),
    # ("O'Donnell", "Manuel Becerra", True, "Línea 6", t),
    # ("Manuel Becerra", "Diego de León", True, "Línea 6", t),
    # ("Diego de León", "Avenida de América", True, "Línea 6", t),
    # ("Avenida de América", "República Argentina", True, "Línea 6", t),
    # ("República Argentina", "Nuevos Ministerios", True, "Línea 6", t),
    # ("Nuevos Ministerios", "Cuatro Caminos", True, "Línea 6", t),

    # # Línea 7
    # ("Pitis", "Arroyofresno", True, "Línea 7", t),
    # ("Arroyofresno", "Lacoma", True, "Línea 7", t),
    # ("Lacoma", "Avenida de la Ilustración", True, "Línea 7", t),
    # ("Avenida de la Ilustración", "Peñagrande", True, "Línea 7", t),
    # ("Peñagrande", "Antonio Machado", True, "Línea 7", t),
    # ("Antonio Machado", "Valdezarza", True, "Línea 7", t),
    # ("Valdezarza", "Francos Rodríguez", True, "Línea 7", t),
    # ("Francos Rodríguez", "Guzmán el Bueno", True, "Línea 7", t),
    # ("Guzmán el Bueno", "Islas Filipinas", True, "Línea 7", t),
    # ("Islas Filipinas", "Canal", True, "Línea 7", t),
    # ("Canal", "Alonso Cano", True, "Línea 7", t),
    # ("Alonso Cano", "Gregorio Marañón", True, "Línea 7", t),
    # ("Gregorio Marañón", "Avenida de América", True, "Línea 7", t),
    # ("Avenida de América", "Cartagena", True, "Línea 7", t),
    # ("Cartagena", "Parque de las Avenidas", True, "Línea 7", t),
    # ("Parque de las Avenidas", "Barrio de la Concepción", True, "Línea 7", t),
    # ("Barrio de la Concepción", "Pueblo Nuevo", True, "Línea 7", t),
    # ("Pueblo Nuevo", "Ascao", True, "Línea 7", t),
    # ("Ascao", "García Noblejas", True, "Línea 7", t),
    # ("García Noblejas", "Simancas", True, "Línea 7", t),
    # ("Simancas", "San Blas", True, "Línea 7", t),
    # ("San Blas", "Las Musas", True, "Línea 7", t),
    # ("Las Musas", "Estadio Metropolitano", True, "Línea 7", t),
    # ("Estadio Metropolitano", "Barrio del Puerto", True, "Línea 7", t),
    # ("Barrio del Puerto", "Coslada Central", True, "Línea 7", t),
    # ("Coslada Central", "La Rambla", True, "Línea 7", t),
    # ("La Rambla", "San Fernando", True, "Línea 7", t),
    # ("San Fernando", "Jarama", True, "Línea 7", t),
    # ("Jarama", "Henares", True, "Línea 7", t),
    # ("Henares", "Hospital del Henares", True, "Línea 7", t),
    
    # # Línea 9
    # ("Paco de Lucía", "Mirasierra", True, "Línea 9", t),
    # ("Mirasierra", "Herrera Oria", True, "Línea 9", t),
    # ("Herrera Oria", "Barrio del Pilar", True, "Línea 9", t),
    # ("Barrio del Pilar", "Ventilla", True, "Línea 9", t),
    # ("Ventilla", "Plaza Castilla", True, "Línea 9", t),
    # ("Plaza Castilla", "Duque de Pastrana", True, "Línea 9", t),
    # ("Duque de Pastrana", "Pio XII", True, "Línea 9", t),
    # ("Pio XII", "Colombia", True, "Línea 9", t),
    # ("Colombia", "Concha Espina", True, "Línea 9", t),
    # ("Concha Espina", "Cruz del Rayo", True, "Línea 9", t),
    # ("Cruz del Rayo", "Avenida de América", True, "Línea 9", t),
    # ("Avenida de América", "Núñez de Balboa", True, "Línea 9", t),
    # ("Núñez de Balboa", "Príncipe de Vergara", True, "Línea 9", t),
    # ("Príncipe de Vergara", "Ibiza", True, "Línea 9", t),
    # ("Ibiza", "Sainz de Baranda", True, "Línea 9", t),
    # ("Sainz de Baranda", "Estrella", True, "Línea 9", t),
    # ("Estrella", "Vinateros", True, "Línea 9", t),
    # ("Vinateros", "Artilleros", True, "Línea 9", t),
    # ("Artilleros", "Pavones", True, "Línea 9", t),
    # ("Pavones", "Valdebernardo", True, "Línea 9", t),
    # ("Valdebernardo", "Vicálvaro", True, "Línea 9", t),
    # ("Vicálvaro", "San Cipriano", True, "Línea 9", t),
    # ("San Cipriano", "Puerta de Arganda", True, "Línea 9", t),
    # ("Puerta de Arganda", "Rivas Urbanizaciones", True, "Línea 9", t),
    # ("Rivas Urbanizaciones", "Rivas Futura", True, "Línea 9", t),
    # ("Rivas Futura", "Rivas Vaciamadrid", True, "Línea 9", t),
    # ("Rivas Vaciamadrid", "La Poveda", True, "Línea 9", t),
    # ("La Poveda", "Arganda del Rey", True, "Línea 9", t),

    # # Línea 10
    # ("Hospital Infanta Sofía", "Reyes Católicos", True, "Línea 10", t),
    # ("Reyes Católicos", "Baunatal", True, "Línea 10", t),
    # ("Baunatal", "Manuel de Falla", True, "Línea 10", t),
    # ("Manuel de Falla", "Marqués de la Valdavia", True, "Línea 10", t),
    # ("Marqués de la Valdavia", "La Moraleja", True, "Línea 10", t),
    # ("La Moraleja", "La Granja", True, "Línea 10", t),
    # ("La Granja", "Ronda de la Comunicación", True, "Línea 10", t),
    # ("Ronda de la Comunicación", "Las Tablas", True, "Línea 10", t),
    # ("Las Tablas", "Montecarmelo", True, "Línea 10", t),
    # ("Montecarmelo", "Tres Olivos", True, "Línea 10", t),
    # ("Tres Olivos", "Fuencarral", True, "Línea 10", t),
    # ("Fuencarral", "Begoña", True, "Línea 10", t),
    # ("Begoña", "Chamartín", True, "Línea 10", t),
    # ("Chamartín", "Plaza de Castilla", True, "Línea 10", t),
    # ("Plaza de Castilla", "Cuzco", True, "Línea 10", t),
    # ("Cuzco", "Santiago Bernabéu", True, "Línea 10", t),
    # ("Santiago Bernabéu", "Nuevos Ministerios", True, "Línea 10", t),
    # ("Nuevos Ministerios", "Gregorio Marañón", True, "Línea 10", t),
    # ("Gregorio Marañón", "Alonso Martínez", True, "Línea 10", t),
    # ("Alonso Martínez", "Tribunal", True, "Línea 10", t),
    # ("Tribunal", "Plaza de España", True, "Línea 10", t),
    # ("Plaza de España", "Príncipe Pío", True, "Línea 10", t),
    # ("Príncipe Pío", "Lago", True, "Línea 10", t),
    # ("Lago", "Batán", True, "Línea 10", t),
    # ("Batán", "Casa de Campo", True, "Línea 10", t),
    # ("Casa de Campo", "Colonia Jardín", True, "Línea 10", t),
    # ("Colonia Jardín", "Aviación Española", True, "Línea 10", t),
    # ("Aviación Española", "Cuatro Vientos", True, "Línea 10", t),
    # ("Cuatro Vientos", "Joaquín Vilumbrales", True, "Línea 10", t),
    # ("Joaquín Vilumbrales", "Puerta del Sur", True, "Línea 10", t),

    # # Ramal
    # ("Ópera", "Príncipe Pío", True, "Ramal", t),

]