import streamlit as st

st.title("CocinaFacil - Tu Asistente de Cocina Personalizado")

# Mensaje de Bienvenida y Saludo Personalizado
st.write("Bienvenido a CocinaFacil. Por favor, introduce tu nombre para comenzar:")
nombre = st.text_input("Nombre")

if nombre:
    st.write(f"¡Hola {nombre}! Soy ChefAI, tu asistente de cocina personal. ¿Estás listo para explorar nuevas recetas deliciosas?")

    # Opciones para el Usuario
    st.write("Por favor, responde las siguientes preguntas para recibir recomendaciones de recetas personalizadas:")

    plato = st.radio("¿Qué tipo de plato prefieres para tu comida principal?", ('Plato de carne', 'Plato vegetariano', 'Plato de pescado'))

    tiempo = st.radio("¿Cuánto tiempo tienes para cocinar?", ('Menos de 30 minutos', 'Entre 30 y 60 minutos', 'Más de 60 minutos'))

    cocina = st.radio("¿Qué tipo de cocina te gustaría explorar hoy?", ('Cocina mexicana', 'Cocina italiana', 'Cocina asiática'))

    # Recetas Seleccionadas según las Respuestas del Usuario
    st.subheader("Recetas Seleccionadas según tus Preferencias:")

    if plato == 'Plato de carne':
        if tiempo == 'Menos de 30 minutos':
            if cocina == 'Cocina mexicana':
                st.subheader("Receta de Tacos de Pollo Mexicano:")
                st.write("Descripción: Deliciosos tacos de pollo con un toque mexicano.")
                st.write("Ingredientes: Pollo desmenuzado, tortillas de maíz, cebolla, tomate, aguacate, cilantro, limón, salsa de tomate, especias mexicanas.")
                st.write("Instrucciones: Saltear el pollo con las especias, calentar las tortillas, y servir con los ingredientes frescos y salsa.")
            elif cocina == 'Cocina italiana':
                st.subheader("Receta de Espaguetis a la Boloñesa:")
                st.write("Descripción: Clásicos espaguetis con una deliciosa salsa de carne italiana.")
                st.write("Ingredientes: Espaguetis, carne molida, cebolla, ajo, zanahoria, salsa de tomate, vino tinto, aceite de oliva, especias italianas.")
                st.write("Instrucciones: Cocinar la carne con las verduras, agregar la salsa de tomate y el vino, cocinar a fuego lento, y servir sobre los espaguetis.")
            else: # Cocina asiática
                st.subheader("Receta de Pollo Teriyaki:")
                st.write("Descripción: Pollo marinado y glaseado con una deliciosa salsa teriyaki.")
                st.write("Ingredientes: Pechugas de pollo, salsa teriyaki, aceite de sésamo, jengibre, ajo, cebolla verde, arroz blanco.")
                st.write("Instrucciones: Marinar el pollo, dorarlo en la sartén con la salsa, y servir con arroz cocido.")

        elif tiempo == 'Entre 30 y 60 minutos':
            if cocina == 'Cocina mexicana':
                st.subheader("Receta de Enchiladas de Carne:")
                st.write("Descripción: Enchiladas rellenas de carne de res sazonada y cubiertas con salsa de enchilada.")
                st.write("Ingredientes: Carne de res molida, tortillas de maíz, salsa de enchilada, queso, cebolla, crema agria, cilantro.")
                st.write("Instrucciones: Cocinar la carne con especias, rellenar las tortillas, cubrir con salsa y queso, hornear y servir con acompañamientos.")
            elif cocina == 'Cocina italiana':
                st.subheader("Receta de Lasaña de Carne:")
                st.write("Descripción: Capas de pasta, carne y salsa de tomate, horneadas con queso derretido.")
                st.write("Ingredientes: Pasta para lasaña, carne molida, salsa de tomate, queso ricotta, mozzarella, parmesano, especias italianas.")
                st.write("Instrucciones: Cocinar la carne con la salsa, armar las capas con pasta y queso, hornear y servir caliente.")
            else: # Cocina asiática
                st.subheader("Receta de Stir Fry de Ternera y Verduras:")
                st.write("Descripción: Ternera salteada con una variedad de verduras frescas y salsa de soja.")
                st.write("Ingredientes: Ternera en tiras, verduras mixtas (pimientos, cebolla, brócoli), salsa de soja, jengibre, ajo, aceite de sésamo.")
                st.write("Instrucciones: Saltear la ternera y las verduras con la salsa de soja y las especias, servir caliente.")

        else: # Más de 60 minutos
            if cocina == 'Cocina mexicana':
                st.subheader("Receta de Barbacoa de Res:")
                st.write("Descripción: Carne de res cocida a fuego lento con una mezcla de especias y jugos.")
                st.write("Ingredientes: Carne de res (como la falda), mezcla de especias para barbacoa, cebolla, ajo, jugo de naranja, hojas de aguacate.")
                st.write("Instrucciones: Cocinar la carne con las especias y jugos a fuego lento durante varias horas, servir con cebolla y cilantro.")

            elif cocina == 'Cocina italiana':
                st.subheader("Receta de Risotto de Champiñones:")
                st.write("Descripción: Arroz cremoso cocido lentamente con champiñones y caldo de pollo.")
                st.write("Ingredientes: Arroz arborio, champiñones, caldo de pollo, cebolla, vino blanco, mantequilla, queso parmesano.")
                st.write("Instrucciones: Saltear la cebolla y los champiñones, agregar el arroz y el vino, cocinar lentamente agregando caldo, servir con queso rallado.")

            else: # Cocina asiática
                st.subheader("Receta de Curry de Pollo y Verduras:")
                st.write("Descripción: Pollo y verduras cocidos en una salsa de curry aromática.")
                st.write("Ingredientes: Pechugas de pollo, verduras mixtas (pimientos, cebolla, zanahoria, brócoli), leche de coco, salsa de curry, jengibre, ajo.")
                st.write("Instrucciones: Saltear el pollo y las verduras, agregar la leche de coco y la salsa de curry, cocinar a fuego lento, servir con arroz.")

    elif plato == 'Plato vegetariano':
        # Lógica para recetas vegetarianas
        pass

    else: # Plato de pescado
        # Lógica para recetas de pescado
        pass



