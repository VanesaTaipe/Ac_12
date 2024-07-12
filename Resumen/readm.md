
1. Crear el Dockerfile:
   Crea un archivo llamado `Dockerfile` con el siguiente contenido:

   ```dockerfile
   FROM python:3.9-slim
   WORKDIR /app
   COPY requirements.txt requirements.txt
   COPY chunk_mp_mapreduce.py chunk_mp_mapreduce.py
   COPY main.py main.py
   RUN pip install --no-cache-dir -r requirements.txt
   EXPOSE 1936
   CMD ["python", "main.py"]
   ```

2. Crear el archivo requirements.txt:
   Crea un archivo llamado `requirements.txt` con el siguiente contenido:

   ```
   asyncio
   ```

3. Preparar los archivos de la aplicación:
   Asegúrate de que los archivos `chunk_mp_mapreduce.py` y `main.py` estén en el mismo directorio que el Dockerfile.

4. Construir la imagen Docker:
   Abre una terminal, navega hasta el directorio que contiene el Dockerfile y ejecuta el siguiente comando:

   ```
   docker build -t mapreduce_app .
   ```

   Este comando construirá la imagen Docker y la etiquetará como "mapreduce_app".

5. Verificar la imagen creada:
   Puedes verificar que la imagen se ha creado correctamente ejecutando:

   ```
   docker images
   ```

   Deberías ver "mapreduce_app" en la lista de imágenes.

6. Ejecutar un contenedor basado en la imagen:
   Para probar la imagen, puedes ejecutar un contenedor con el siguiente comando:

   ```
   docker run -p 1936:1936 mapreduce_app
   ```

   Esto iniciará un contenedor basado en la imagen "mapreduce_app" y mapeará el puerto 1936 del contenedor al puerto 1936 del host.
