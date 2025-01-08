# Plataforma de Reseñas de Películas

## Descripción General

Esta aplicación permite a los usuarios agregar películas y comentarios sobre ellas. Es un lugar para revisar películas y ver qué es popular. Los usuarios pueden agregar nuevas películas, comentar sobre películas existentes y editar sus perfiles. La página de inicio incluye una función de búsqueda para encontrar películas que ya se han agregado.

## Funcionalidades

- **Agregar Películas**: Los usuarios pueden agregar nuevas películas a la plataforma.
- **Agregar Comentarios**: Los usuarios pueden comentar sobre las películas.
- **Editar Perfil**: Los usuarios pueden actualizar la información de su perfil.
- **Buscar Películas**: Los usuarios pueden buscar películas por título.

## Instalación

1. **Clonar el repositorio**:
   ```bash
   git clone https://github.com/tuusuario/moviereviewplatform.git
   cd moviereviewplatform
   ```

2. **Crear un entorno virtual**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
   ```

3. **Instalar dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Aplicar migraciones**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Crear un superusuario**:
   ```bash
   python manage.py createsuperuser
   ```

6. **Ejecutar el servidor de desarrollo**:
   ```bash
   python manage.py runserver
   ```

## Uso

### Página de Inicio

- **Menú**: El menú superior proporciona enlaces para agregar una película, agregar un comentario y editar el perfil del usuario.
- **Buscar**: Usa la barra de búsqueda para encontrar películas por título.

### Agregar una Película

1. Navega a la página "Agregar Película" desde el menú superior.
2. Completa los detalles de la película (título, género, director, fecha de estreno).
3. Haz clic en "Enviar" para agregar la película.

### Agregar un Comentario

1. Navega a la película sobre la que deseas comentar.
2. Haz clic en "Agregar Comentario".
3. Completa el contenido del comentario y la calificación.
4. Haz clic en "Enviar" para agregar el comentario.

### Editar Perfil

1. Navega a la página "Editar Perfil" desde el menú superior.
2. Actualiza tu biografía y avatar.
3. Haz clic en "Guardar" para actualizar tu perfil.

### Buscar una Película

1. Usa la barra de búsqueda en la página de inicio.
2. Ingresa el título de la película que estás buscando.
3. Haz clic en "Buscar" para encontrar la película.

## Pruebas

Para probar las funcionalidades, sigue estos pasos:

1. **Agregar una Película**:
   - Ve a la página "Agregar Película" y agrega una nueva película.
   - Verifica que la película aparezca en la lista de películas.

2. **Agregar un Comentario**:
   - Ve a la página de detalles de una película y agrega un comentario.
   - Verifica que el comentario aparezca bajo la película.

3. **Editar Perfil**:
   - Ve a la página "Editar Perfil" y actualiza tu perfil.
   - Verifica que los cambios se reflejen en tu perfil.

4. **Buscar una Película**:
   - Usa la barra de búsqueda para encontrar una película por título.
   - Verifica que los resultados de la búsqueda muestren la película correcta.

## Contribuciones

Si deseas contribuir a este proyecto, por favor haz un fork del repositorio y envía un pull request.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT.