conexiones = [
    # Alonso Cano
    ("Alonso Cano", "Avenida de América", True, "Línea 7", 4),

    # Alonso Martínez
    ("Alonso Martínez", "Argüelles", True, "Línea 4", 5),
    ("Alonso Martínez", "Velázquez", True, "Línea 4", 2),
    ("Alonso Martínez", "Callao", True, "Línea 5", 4),
    ("Alonso Martínez", "Diego de León", True, "Línea 5", 8),
    ("Alonso Martínez", "Tribunal", True, "Línea 10", 1),
    ("Alonso Martínez", "Nuevos Ministerios", True, "Línea 10", 4),

    # Avenida de América
    ("Avenida de América", "Diego de León", True, "Línea 4", 2),
    ("Avenida de América", "Alonso Cano", True, "Línea 7", 4),
    ("Avenida de América", "Colombia", True, "Línea 9", 12),

    # Argüelles
    ("Argüelles", "Moncloa", True, "Línea 3", 1),
    ("Argüelles", "Plaza de España", True, "Línea 3", 8),
    ("Argüelles", "Alonso Martínez", True, "Línea 4", 4),
    ("Argüelles", "Príncipe Pío", True, "Línea 6", 3 ),
    ("Argüelles", "Moncloa", True, "Línea 6", 1),

    # Callao
    ("Callao", "Sol", True, "Línea 3", 1),
    ("Callao", "Plaza de España", True, "Línea 3", 4),
    ("Callao", "Ópera", True, "Línea 5", 1),
    ("Callao", "Alonso Martínez", True, "Línea 5", 4),

    # Chamartín
    ("Chamartín", "Plaza de Castilla", True, "Línea 10", 1),
    ("Chamartín", "Plaza de Castilla", True, "Línea 1", 1),

    # Colombia
    ("Colombia", "Nuevos Ministerios", True, "Línea 8", 8),
    ("Colombia", "Avenida de América", True, "Línea 9", 5),
    ("Colombia", "Plaza de Castilla", True, "Línea 9", 15),

    # Cuatro Caminos
    ("Cuatro Caminos", "Tribunal", True, "Línea 1", 5),
    ("Cuatro Caminos", "Plaza de Castilla", True, "Línea 1", 7),
    ("Cuatro Caminos", "Plaza de España", True, "Línea 2", 5),
    ("Cuatro Caminos", "Moncloa",  True, "Línea 6", 8),
    ("Cuatro Caminos", "Nuevos Ministerios", True, "Línea 6", 2),

    # Diego de León
    ("Diego de León", "Avenida de América", True, "Línea 4", 1),
    ("Diego de León", "Goya", True, "Línea 4", 3),
    ("Diego de León", "Alonso Martínez", True, "Línea 5", 7),
    ("Diego de León", "Avenida de América", True, "Línea 6", 1),
    ("Diego de León", "Manuel Becerra", True, "Línea 6", 1),

    # Goya
    ("Goya", "Manuel Becerra", True, "Línea 2", 1),
    ("Goya", "Sol", True, "Línea 2", 6),
    ("Goya", "Diego de León", True, "Línea 4", 3),
    ("Goya", "Velázquez", True, "Línea 4", 2),

    # Manuel Becerra
    ("Manuel Becerra", "Goya", True, "Línea 2", 1),
    ("Manuel Becerra", "Diego de León", True, "Línea 6", 1),

    # Moncloa
    ("Moncloa", "Argüelles", True, "Línea 3", 1),
    ("Moncloa", "Argüelles", True, "Línea 6", 1),
    ("Moncloa", "Cuatro Caminos", True, "Línea 6", 8),

    # Nuevos Ministerios
    ("Nuevos Ministerios", "Avenida de América", True, "Línea 6", 4),
    ("Nuevos Ministerios", "Cuatro Caminos", True, "Línea 6", 2),
    ("Nuevos Ministerios", "Colombia", True, "Línea 8", 8),
    ("Nuevos Ministerios", "Alonso Martínez", True, "Línea 10", 1),
    ("Nuevos Ministerios", "Santiago Bernabéu", True, "Línea 10", 1),

    # Ópera
    ("Ópera", "Sol", True, "Línea 2", 2),
    ("Ópera", "Plaza de España", True, "Línea 2", 2),
    ("Ópera", "Callao", True, "Línea 5", 1),
    ("Ópera", "Príncipe Pío", True, "Ramal", 3),

    # Plaza de Castilla
    ("Plaza de Castilla", "Cuatro Caminos", True, "Línea 1", 7),
    ("Plaza de Castilla", "Chamartín", True, "Línea 1", 1),
    ("Plaza de Castilla", "Colombia", True, "Línea 9", 15),
    ("Plaza de Castilla", "Chamartín", True, "Línea 10", 1),
    ("Plaza de Castilla", "Santiago Bernabéu", True, "Línea 10", 3),

    # Plaza de España
    ("Plaza de España", "Cuatro Caminos", True, "Línea 2", 5),
    ("Plaza de España", "Ópera", True, "Línea 2", 2),
    ("Plaza de España", "Callao", True, "Línea 3", 1),
    ("Plaza de España", "Argüelles", True, "Línea 3", 1),
    ("Plaza de España", "Príncipe Pío", True, "Línea 10", 1),
    ("Plaza de España", "Tribunal", True, "Línea 10", 1),

    # Príncipe Pío
    ("Príncipe Pío", "Ópera", True, "Ramal", 3),
    ("Príncipe Pío", "Argüelles", True, "Línea 6", 1),
    ("Príncipe Pío", "Plaza de España", True, "Línea 10", 1),

    # Santiago Bernabéu
    ("Santiago Bernabéu", "Plaza de Castilla", True, "Línea 10", 3),
    ("Santiago Bernabéu", "Nuevos Ministerios", True, "Línea 10", 6),

    # Sol
    ("Sol", "Tribunal", True, "Línea 1", 2),
    ("Sol", "Goya", True, "Línea 2", 6),
    ("Sol", "Ópera", True, "Línea 2", 2),
    ("Sol", "Callao", True, "Línea 3", 1),

    # Tribunal
    ("Tribunal", "Cuatro Caminos", True, "Línea 1", 5),
    ("Tribunal", "Sol", True, "Línea 1", 2),
    ("Tribunal", "Plaza de España", True, "Línea 10", 1),
    ("Tribunal", "Alonso Martínez", True, "Línea 10", 1),

    # Velázquez
    ("Velázquez", "Goya", True, "Línea 4", 2),
    ("Velázquez", "Alonso Martínez", True, "Línea 4", 2)
]
