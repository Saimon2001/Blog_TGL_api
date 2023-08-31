# Información relevante para trabajar

1. Crear un ambiente virtual con conda.
```bash
conda create -n TGL_fastAPI python=3.9
```
2. Activar el ambiente virtual creado previamente.
```bash
conda activate TGL_fastAPI
```

3. Exportar el ambiente creado a un archivo `yml`. Esto se realiza cada que se agregan dependencias al ambiente. 
 ```bash
conda env export > requirements.yml
```

4. Actualizar el ambiente a partir de las dependencias que se especifican en el archivo `requirements.yml`. Cada que se bajen cambios habrá que actualizar el ambiente para que las dependencias que sean requeridas puedan servir. 
 ```bash
conda env update -f requirements.yml
```

5. Si requiero bajar cambios que se encuentran en un repositorio remoto. Me ubico en la rama en la que quiero bajar los cambios y especifico la rama de la que quiero bajar los cambios; en este caso rama `main`. 
```bash
git pull origin  main
```
También puede hacerse directamente desde el `source control` de visual studio code, en el área de de `branches`. 

6. Para correr una app de fastapi usando una especie de demonio (en este caso, uvicorn), se debe correr lo siguiente:
```bash
uvicorn main:app --reload
```
main es el archivo principal `main.py` y `app` es la instancia de fastapi creada en `main.py`.

7. Los `main.py` en cada subcarpeta hacen más simple, clara y evitan la redundancia de lineas cuando se realiza la importación de modulos a otras partes del proyecto.

8. **FastAPI** realiza una documentación automática de tipo **swagger** que se puede acceder así
```
http://localhost:8000/docs
```

9. Los modelos (los que se encuentran en `models`) usan el ORM para crear el modelo de datos en la base de datos; mientras que los esquemas (o `schemas`) se modelan los datos que se envian las rutas. 

10. Para crear la conexion base de datos
- descargar extension de visual "SQLite Viewer"
- installar sqlalchemy

