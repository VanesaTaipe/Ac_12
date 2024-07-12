Respuestas al examen Parcial C8286
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Parte 1
~~~~~~~

1.1 Para responder a esta pregunta, debemos ejecutar la simulación con
las siguientes configuraciones:

-  Un solo trabajo (llamado ‘a’) con un tiempo de ejecución de 30 y un
   tamaño de conjunto de trabajo de 200.
-  Una CPU.
-  Activar la bandera -c para ver la respuesta final.
-  Activar la bandera -t para ver un rastro del trabajo paso a paso y
   cómo se programa.
-  El comando para ejecutar esta simulación sería:

.. code:: ipython3

    ./multi.py -n 1 -L a:30:200 -c -t

Antes de ejecutar el comando, podemos analizar y predecir cuánto tiempo
tomará completar el trabajo basándonos en la información proporcionada y
las configuraciones de la simulación:

-  Tiempo de ejecución del trabajo: 30 unidades de tiempo.
-  Tamaño del conjunto de trabajo: 200.
-  Número de CPUs: 1.
-  Tamaño de la caché: 100 (por defecto).
-  Tiempo de calentamiento de la caché: 10 (por defecto).
-  Velocidad de ejecución en caché caliente: 2.
-  Velocidad de ejecución en caché fría: 1.

Calentamiento de la caché:

-  El tamaño del conjunto de trabajo es 200, que es mayor que el tamaño
   de la caché (100).
-  Por lo tanto, el trabajo ‘a’ no cabe completamente en la caché.
-  Esto significa que el trabajo comenzará en caché fría.

Ejecución del trabajo:

-  Al comenzar en caché fría, la velocidad de ejecución será 1.
-  El trabajo requiere un tiempo de ejecución de 30 unidades de tiempo.
-  Durante cada unidad de tiempo, el trabajo se ejecutará a la velocidad
   de 1 unidad de tiempo.

Dado que la velocidad de ejecución en caché fría es 1 y el tiempo de
ejecución del trabajo es 30, el tiempo total de finalización será 30
unidades de tiempo, ya que no se alcanza el tiempo necesario para
calentar la caché completamente.

Para confirmar esta predicción, ejecutemos el comando y observemos la
salida:

Resultados esperados

1. Rastro del trabajo paso a paso:

-  La bandera -t mostrará cómo el trabajo ‘a’ es programado en la única
   CPU.
-  Veremos que el trabajo se ejecuta continuamente en la CPU hasta que
   se complete su tiempo de ejecución de 30 unidades de tiempo.

2. Respuesta final:

-  La bandera -c mostrará el tiempo total de finalización del trabajo,
   que esperamos que sea 30 unidades de tiempo.

.. code:: ipython3

    ARG seed 0
    ARG job_num 3
    ARG max_run 100
    ARG max_wset 200
    ARG job_list a:30:200
    ARG affinity 
    ARG per_cpu_queues False
    ARG num_cpus 1
    ARG quantum 10
    ARG peek_interval 30
    ARG warmup_time 10
    ARG cache_size 100
    ARG random_order False
    ARG trace True
    ARG trace_time False
    ARG trace_cache False
    ARG trace_sched False
    ARG compute True
    
    Nombre del trabajo:a tiempo_de_ejecución:30 tamaño_del_conjunto_de_trabajo:200
    
    Planificador cola central: ['a']
    
       0   a      
       1   a      
       2   a      
       3   a      
       4   a      
       5   a      
       6   a      
       7   a      
       8   a      
       9   a      
    ----------
      10   a      
      11   a      
      12   a      
      13   a      
      14   a      
      15   a      
      16   a      
      17   a      
      18   a      
      19   a      
    ----------
      20   a      
      21   a      
      22   a      
      23   a      
      24   a      
      25   a      
      26   a      
      27   a      
      28   a      
      29   a      
    
    Tiempo de finalización 30
    
    Estadísticas por CPU
      CPU 0  utilización 100.00 [ caliente 0.00 ]


La primera simulación ejecutará el trabajo ‘a’ con un tiempo de
ejecución de 30 y un tamaño de conjunto de trabajo de 200 en una sola
CPU. Dado que el trabajo no cabe completamente en la caché y la
velocidad de ejecución en caché fría es 1, tomará 30 unidades de tiempo
completarse. Este análisis será confirmado al ejecutar el comando con
las banderas -c y -t.

1.2 Para responder a esta pregunta, necesitamos entender cómo el tamaño
de la caché afecta la ejecución del trabajo y cómo los parámetros de
calentamiento y la tasa de ejecución influyen en el rendimiento.

Configuración del experimento

-  Trabajo ‘a’ con tiempo de ejecución de 30 y tamaño de conjunto de
   trabajo de 200.
-  Una CPU.
-  Tamaño de la caché: 300 (suficiente para contener el conjunto de
   trabajo de 200).
-  Tiempo de calentamiento de la caché: 10 (por defecto).
-  Tasa de ejecución en caché caliente: 2.
-  Tasa de ejecución en caché fría: 1.

El comando para ejecutar esta simulación será:

.. code:: ipython3

    ./multi.py -n 1 -L a:30:200 -M 300 -c

Dado que el tamaño de la caché es 300, que es mayor que el tamaño del
conjunto de trabajo de 200, el conjunto de trabajo completo cabrá en la
caché. Esto significa que después del tiempo de calentamiento, el
trabajo se ejecutará a la tasa de ejecución en caché caliente.

Calentamiento de la caché:

-  El tiempo de calentamiento de la caché es 10 unidades de tiempo.
-  Durante este tiempo, el trabajo se ejecutará a la tasa de ejecución
   en caché fría (1).

Ejecución en caché caliente:

-  Después de 10 unidades de tiempo, la caché estará caliente.
-  La tasa de ejecución en caché caliente es 2.
-  El tiempo restante para completar el trabajo será 30 - 10 = 20
   unidades de tiempo.
-  Con una tasa de ejecución de 2, el tiempo necesario para completar
   los 20 unidades de trabajo restantes será 20 / 2 = 10 unidades de
   tiempo.

Tiempo total de ejecución:

-  Tiempo de calentamiento de la caché: 10 unidades de tiempo.
-  Tiempo de ejecución en caché caliente: 10 unidades de tiempo.
-  Tiempo total de ejecución predicho: 10 + 10 = 20 unidades de tiempo.

Ejecutemos el comando para verificar nuestra predicción:

.. code:: ipython3

    ./multi.py -n 1 -L a:30:200 -M 300 -c
    
    ARG seed 0
    ARG job_num 3
    ARG max_run 100
    ARG max_wset 200
    ARG job_list a:30:200
    ARG affinity 
    ARG per_cpu_queues False
    ARG num_cpus 1
    ARG quantum 10
    ARG peek_interval 30
    ARG warmup_time 10
    ARG cache_size 300
    ARG random_order False
    ARG trace False
    ARG trace_time False
    ARG trace_cache False
    ARG trace_sched False
    ARG compute True
    
    Nombre del trabajo:a tiempo_de_ejecución:30 tamaño_del_conjunto_de_trabajo:200
    
    Planificador cola central: ['a']
    
    
    Tiempo de finalización 20
    
    Estadísticas por CPU
      CPU 0  utilización 100.00 [ caliente 50.00 ]


Respuesta final:

-  La bandera -c mostrará el tiempo total de finalización del trabajo.
-  Esperamos ver un tiempo total de finalización de 20 unidades de
   tiempo.

Al ejecutar el comando, la salida debe confirmar que el tiempo total de
ejecución del trabajo ‘a’ es 20 unidades de tiempo, una vez que el
conjunto de trabajo cabe en la caché y se aprovecha la tasa de ejecución
en caché caliente.

Al aumentar el tamaño de la caché a 300, el conjunto de trabajo del
trabajo ‘a’ cabe completamente en la caché. Después de un tiempo de
calentamiento de 10 unidades de tiempo, el trabajo se ejecutará a una
tasa de 2 unidades de tiempo por unidad de tiempo, completándose en 20
unidades de tiempo en total. Esta predicción se puede confirmar
ejecutando el comando con la bandera de solución activada.

1.3 Para ejecutar la simulación con el rastreo de tiempo restante
habilitado, usaremos la bandera -T. Esto nos permitirá ver no solo qué
trabajo se está programando en cada CPU en cada paso de tiempo, sino
también el tiempo de ejecución que le queda a ese trabajo después de
cada tick.

.. code:: ipython3

    ./multi.py -n 1 -L a:30:200 -M 300 -c -T

.. code:: ipython3

    ./multi.py -n 1 -L a:30:200 -M 300 -c -T
    ARG seed 0
    ARG job_num 3
    ARG max_run 100
    ARG max_wset 200
    ARG job_list a:30:200
    ARG affinity 
    ARG per_cpu_queues False
    ARG num_cpus 1
    ARG quantum 10
    ARG peek_interval 30
    ARG warmup_time 10
    ARG cache_size 300
    ARG random_order False
    ARG trace False
    ARG trace_time True
    ARG trace_cache False
    ARG trace_sched False
    ARG compute True
    
    Nombre del trabajo:a tiempo_de_ejecución:30 tamaño_del_conjunto_de_trabajo:200
    
    Planificador cola central: ['a']
    
       0   a [ 29]      
       1   a [ 28]      
       2   a [ 27]      
       3   a [ 26]      
       4   a [ 25]      
       5   a [ 24]      
       6   a [ 23]      
       7   a [ 22]      
       8   a [ 21]      
       9   a [ 20]      
    ----------------
      10   a [ 18]      
      11   a [ 16]      
      12   a [ 14]      
      13   a [ 12]      
      14   a [ 10]      
      15   a [  8]      
      16   a [  6]      
      17   a [  4]      
      18   a [  2]      
      19   a [  0]      
    
    Tiempo de finalización 20
    
    Estadísticas por CPU
      CPU 0  utilización 100.00 [ caliente 50.00 ]


La salida confirma que el trabajo ‘a’ se completó en 20 unidades de
tiempo, lo que es coherente con nuestra predicción cuando el conjunto de
trabajo cabe en la caché.

Ahora vamos a agregar más rastreo para mostrar el estado de cada caché
de CPU para cada trabajo, utilizando la bandera -C. También analizaremos
qué sucede cuando cambiamos el parámetro de tiempo de calentamiento (-w)
a valores menores o mayores que el predeterminado.

.. code:: ipython3

    ./multi.py -n 1 -L a:30:200 -M 300 -c -T -C

La ejecución confirma los detalles de cómo la caché se calienta y cómo
se refleja en el tiempo de ejecución del trabajo. Aquí tienes un
análisis detallado de la salida y lo que significa:

Rastreo de caché y tiempo restante Durante los primeros 9 ticks:

-  La caché está fría para el trabajo ‘a’, indicada por espacios en
   blanco.
-  El tiempo restante del trabajo ‘a’ disminuye en 1 por cada tick, ya
   que se está ejecutando en caché fría.

A partir del tick 10:

-  La caché se calienta para el trabajo ‘a’, indicada por ‘w’.
-  El tiempo restante del trabajo ‘a’ disminuye en 2 por cada tick, ya
   que se está ejecutando en caché caliente.

Tiempo de finalización y estadísticas

-  Tiempo de finalización: 20 unidades de tiempo.
-  Utilización de la CPU: 100%.
-  Calor en la CPU: 50%.

Estos resultados confirman que, después de 10 unidades de tiempo (el
tiempo de calentamiento predeterminado), la caché se calienta y la tasa
de ejecución se incrementa, reduciendo el tiempo de ejecución restante
más rápidamente.

Ajuste del tiempo de calentamiento (-w)

Ahora ajustemos el parámetro de tiempo de calentamiento (-w) a valores
menores y mayores que el predeterminado para observar cómo cambia el
comportamiento.

Tiempo de calentamiento menor (-w 5)

.. code:: ipython3

    ./multi.py -n 1 -L a:30:200 -M 300 -c -T -C -w 5

Predicción:

-  La caché se calentará después de 5 unidades de tiempo.
-  El trabajo ‘a’ se ejecutará en caché caliente después de 5 unidades
   de tiempo.

Tiempo de calentamiento mayor (-w 15)

Ejecuta el siguiente comando:

.. code:: ipython3

    ./multi.py -n 1 -L a:30:200 -M 300 -c -T -C -w 15

Predicción:

-  La caché se calentará después de 15 unidades de tiempo.
-  El trabajo ‘a’ se ejecutará en caché caliente después de 15 unidades
   de tiempo.

El comportamiento del calentamiento de la caché y su impacto en el
tiempo de ejecución del trabajo se observa claramente al ajustar el
tiempo de calentamiento (-w).

Tiempo de calentamiento predeterminado (-w 10):

-  La caché se calienta después de 10 unidades de tiempo.
-  El trabajo ‘a’ se completa en 20 unidades de tiempo.

Tiempo de calentamiento menor (-w 5):

-  La caché se calienta más rápidamente.
-  El trabajo ‘a’ se ejecuta a una tasa más rápida más pronto,
   potencialmente reduciendo el tiempo total de ejecución.

Tiempo de calentamiento mayor (-w 15):

-  La caché se calienta más lentamente.
-  El trabajo ‘a’ tarda más en beneficiarse de la tasa de ejecución más
   rápida, lo que puede aumentar el tiempo total de ejecución.

Ajustar el tiempo de calentamiento de la caché es una herramienta útil
para optimizar el rendimiento de los sistemas paralelos y distribuidos,
dependiendo de las características específicas de la carga de trabajo y
los recursos disponibles.

1.4 Para agregar más rastreo y mostrar el estado de cada caché de CPU
para cada trabajo, utilizamos la bandera -C como hicimos en el ítem
anterior. Esto nos permitirá ver si la caché está fría (espacio en
blanco) o caliente (w) para cada trabajo. Además, analizaremos cómo
cambia el comportamiento cuando ajustamos el parámetro de tiempo de
calentamiento (-w).

.. code:: ipython3

    ./multi.py -n 1 -L a:30:200 -M 300 -c -T -C 

Compara la planificación centralizada y distribuida en términos de
rendimiento y utilización de la CPU. Modifica el código para permitir la
simulación con una cola centralizada y colas distribuidas.

Posible soluciones:

.. code:: ipython3

    # Simulación con cola centralizada
    centralized_scheduler = Scheduler(
        job_list='', affinity='', per_cpu_queues=False, peek_interval=30,
        job_num=10, max_run=100, max_wset=200,
        num_cpus=4, time_slice=10, random_order=False,
        cache_size=100, cache_rate_cold=1, cache_rate_warm=2,
        cache_warmup_time=10, solve=True,
        trace=False, trace_time_left=False, trace_cache=False,
        trace_sched=False
    )
    centralized_scheduler.run()


.. code:: ipython3

    # Simulación con colas distribuidas
    distributed_scheduler = Scheduler(
        job_list='', affinity='', per_cpu_queues=True, peek_interval=30,
        job_num=10, max_run=100, max_wset=200,
        num_cpus=4, time_slice=10, random_order=False,
        cache_size=100, cache_rate_cold=1, cache_rate_warm=2,
        cache_warmup_time=10, solve=True,
        trace=False, trace_time_left=False, trace_cache=False,
        trace_sched=False
    )
    distributed_scheduler.run()


Después de ejecutar las simulaciones, reportaremos el tiempo total de
ejecución y la utilización de la CPU para cada enfoque.

.. code:: ipython3

    # Configuración de la simulación centralizada
    centralized_scheduler = Scheduler(
        job_list='', affinity='', per_cpu_queues=False, peek_interval=30,
        job_num=10, max_run=100, max_wset=200,
        num_cpus=4, time_slice=10, random_order=False,
        cache_size=100, cache_rate_cold=1, cache_rate_warm=2,
        cache_warmup_time=10, solve=True,
        trace=False, trace_time_left=True, trace_cache=False,
        trace_sched=True
    )
    centralized_scheduler.run()
    
    print("\n--- Simulación Centralizada ---")
    print(f"Tiempo de finalización: {centralized_scheduler.system_time}")
    for cpu in range(centralized_scheduler.num_cpus):
        print(f"CPU {cpu} utilización: {100.0 * float(centralized_scheduler.stats_ran[cpu]) / float(centralized_scheduler.system_time):.2f}%")
    
    # Configuración de la simulación distribuida
    distributed_scheduler = Scheduler(
        job_list='', affinity='', per_cpu_queues=True, peek_interval=30,
        job_num=10, max_run=100, max_wset=200,
        num_cpus=4, time_slice=10, random_order=False,
        cache_size=100, cache_rate_cold=1, cache_rate_warm=2,
        cache_warmup_time=10, solve=True,
        trace=False, trace_time_left=True, trace_cache=False,
        trace_sched=True
    )
    distributed_scheduler.run()
    
    print("\n--- Simulación Distribuida ---")
    print(f"Tiempo de finalización: {distributed_scheduler.system_time}")
    for cpu in range(distributed_scheduler.num_cpus):
        print(f"CPU {cpu} utilización: {100.0 * float(distributed_scheduler.stats_ran[cpu]) / float(distributed_scheduler.system_time):.2f}%")


Recuerda: la planificación distribuida generalmente ofrece un mejor
rendimiento y utilización de la CPU en sistemas con múltiples CPUs y
trabajos concurrentes, ya que distribuye la carga de trabajo de manera
más equilibrada. Sin embargo, es más compleja de implementar y gestionar
en comparación con la planificación centralizada. Elegir entre estos
enfoques depende de las características específicas del sistema y de las
necesidades de rendimiento.

Parte 2
~~~~~~~

2.1 Añadir manejo de errores Para manejar errores de manera efectiva,
vamos a envolver las secciones críticas del código en bloques try-except
y asegurarnos de capturar y manejar cualquier excepción que pueda
ocurrir.

El módulo logging de Python nos permite registrar mensajes en diferentes
niveles (info, warning, error, etc.). Configuraremos el logger para que
registre los eventos importantes y errores.

.. code:: ipython3

    import asyncio
    import marshal
    import multiprocessing as mp
    import pickle
    import logging
    from queue import Empty, Queue
    import threading
    import types
    import chunk_mp_mapreduce as mr
    
    # Configurar logging
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    logger = logging.getLogger(__name__)
    
    work_queue = Queue()
    results_queue = Queue()
    results = {}
    
    async def submit_job(job_id, reader, writer):
        try:
            writer.write(job_id.to_bytes(4, 'little'))
            await writer.drain()
            code_size = int.from_bytes(await reader.read(4), 'little')
            my_code = marshal.loads(await reader.read(code_size))
            data_size = int.from_bytes(await reader.read(4), 'little')
            data = pickle.loads(await reader.read(data_size))
            work_queue.put_nowait((job_id, my_code, data))
            logger.info(f"Job {job_id} submitted successfully.")
        except Exception as e:
            logger.error(f"Error submitting job {job_id}: {e}")
            writer.write(b'\x00\x00\x00\x00')  # Indicar error al cliente
            await writer.drain()
    
    def get_results_queue():
        while results_queue.qsize() > 0:
            try:
                job_id, data = results_queue.get_nowait()
                results[job_id] = data
            except Empty:
                return
    
    async def get_results(reader, writer):
        try:
            get_results_queue()
            job_id = int.from_bytes(await reader.read(4), 'little')
            data = pickle.dumps(None)
            if job_id in results:
                data = pickle.dumps(results[job_id])
                del results[job_id]
            writer.write(len(data).to_bytes(4, 'little'))
            writer.write(data)
            await writer.drain()
            logger.info(f"Results for job {job_id} retrieved successfully.")
        except Exception as e:
            logger.error(f"Error retrieving results: {e}")
            writer.write(b'\x00\x00\x00\x00')  # Indicar error al cliente
            await writer.drain()
    
    async def accept_requests(reader, writer, job_id=[0]):
        try:
            op = await reader.read(1)
            if op[0] == 0:
                await submit_job(job_id[0], reader, writer)
                job_id[0] += 1
            elif op[0] == 1:
                await get_results(reader, writer)
        except Exception as e:
            logger.error(f"Error accepting request: {e}")
    
    def worker():
        pool = mp.Pool()
        while True:
            try:
                job_id, code, data = work_queue.get()  # blocking
                func = types.FunctionType(code, globals(), 'mapper_and_reducer')
                mapper, reducer = func()
                counts = mr.map_reduce(pool, data, mapper, reducer, 100, mr.reporter)
                results_queue.put((job_id, counts))
                logger.info(f"Trabajo {job_id} procesado exitosamente .")
            except Exception as e:
                logger.error(f"Error en el procesamiento de trabajo del worker {job_id}: {e}")
        pool.close()
        pool.join()
    
    async def main():
        try:
            server = await asyncio.start_server(accept_requests, '127.0.0.1', 1936)
            worker_thread = threading.Thread(target=worker, daemon=True)
            worker_thread.start()
            async with server:
                logger.info("Servidor inicializado exitosamente.")
                await server.serve_forever()
        except Exception as e:
            logger.error(f"Error inicializando el servidor : {e}")
    
    if __name__ == '__main__':
        try:
            asyncio.run(main())
        except Exception as e:
            logger.critical(f"Error fatal: {e}")


Explicación de los cambios:

-  Se configuró el módulo logging con un formato básico y un nivel de
   logging de INFO.
-  Cada función relevante (submit_job, get_results, accept_requests,
   worker, main) ahora tiene bloques try-except para capturar y manejar
   excepciones.
-  En caso de error, se registra un mensaje de error usando logger.error
   y se envía una respuesta al cliente si es necesario.
-  await writer.drain() se añadió después de writer.write() para
   asegurarse de que los datos se envíen completamente al cliente.
-  Se añadieron mensajes de información (logger.info) para indicar el
   éxito de varias operaciones (por ejemplo, trabajo enviado, resultados
   recuperados, servidor iniciado).

2.2 Vamos a refactorizar la función worker para utilizar
concurrent.futures.ProcessPoolExecutor en lugar de multiprocessing.Pool.
Esto nos permitirá manejar los procesos de manera más eficiente y
moderna.

Primero, refactorizaremos la función worker y luego ajustaremos el
código para utilizar ProcessPoolExecutor.

.. code:: ipython3

    import asyncio
    import marshal
    import pickle
    import logging
    from queue import Empty, Queue
    import threading
    import types
    from concurrent.futures import ProcessPoolExecutor
    
    import chunk_mp_mapreduce as mr
    
    # Configurar logging
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    logger = logging.getLogger(__name__)
    
    work_queue = Queue()
    results_queue = Queue()
    results = {}
    
    async def submit_job(job_id, reader, writer):
        try:
            writer.write(job_id.to_bytes(4, 'little'))
            await writer.drain()
            code_size = int.from_bytes(await reader.read(4), 'little')
            my_code = marshal.loads(await reader.read(code_size))
            data_size = int.from_bytes(await reader.read(4), 'little')
            data = pickle.loads(await reader.read(data_size))
            work_queue.put_nowait((job_id, my_code, data))
            logger.info(f"Trabajo {job_id} entregado exitosamente.")
        except Exception as e:
            logger.error(f"Error en entregar el trabajo {job_id}: {e}")
            writer.write(b'\x00\x00\x00\x00')  # Indicar error al cliente
            await writer.drain()
    
    def get_results_queue():
        while results_queue.qsize() > 0:
            try:
                job_id, data = results_queue.get_nowait()
                results[job_id] = data
            except Empty:
                return
    
    async def get_results(reader, writer):
        try:
            get_results_queue()
            job_id = int.from_bytes(await reader.read(4), 'little')
            data = pickle.dumps(None)
            if job_id in results:
                data = pickle.dumps(results[job_id])
                del results[job_id]
            writer.write(len(data).to_bytes(4, 'little'))
            writer.write(data)
            await writer.drain()
            logger.info(f"Resultado para el trabajo {job_id} recuperado exitosamente.")
        except Exception as e:
            logger.error(f"Error en el resultado recuperado: {e}")
            writer.write(b'\x00\x00\x00\x00')  # Indicar error al cliente
            await writer.drain()
    
    async def accept_requests(reader, writer, job_id=[0]):
        try:
            op = await reader.read(1)
            if op[0] == 0:
                await submit_job(job_id[0], reader, writer)
                job_id[0] += 1
            elif op[0] == 1:
                await get_results(reader, writer)
        except Exception as e:
            logger.error(f"Error al aceptar la solicitud: {e}")
    
    def worker():
        with ProcessPoolExecutor() as executor:
            while True:
                try:
                    job_id, code, data = work_queue.get()  # blocking
                    func = types.FunctionType(code, globals(), 'mapper_and_reducer')
                    mapper, reducer = func()
                    future = executor.submit(mr.map_reduce, data, mapper, reducer, 100, mr.reporter)
                    future.add_done_callback(lambda f, job_id=job_id: results_queue.put((job_id, f.result())))
                    logger.info(f"Trabajo {job_id} entregado al ejeecutor.")
                except Exception as e:
                    logger.error(f"Error en el procesamiento en el trabajo del worker {job_id}: {e}")
    
    async def main():
        try:
            server = await asyncio.start_server(accept_requests, '127.0.0.1', 1936)
            worker_thread = threading.Thread(target=worker, daemon=True)
            worker_thread.start()
            async with server:
                logger.info("El servidor se inicia correctamente.")
                await server.serve_forever()
        except Exception as e:
            logger.error(f"Error al iniciar el servidor: {e}")
    
    if __name__ == '__main__':
        try:
            asyncio.run(main())
        except Exception as e:
            logger.critical(f"Error fatal: {e}")


Explicación de los cambios

-  La función worker ahora utiliza
   concurrent.futures.ProcessPoolExecutor.
-  executor.submit se usa para enviar tareas al pool de procesos.
-  future.add_done_callback se usa para agregar una función de callback
   que coloca los resultados en results_queue una vez que la tarea se
   completa.
-  Manejamos excepciones dentro del bucle while en worker para
   asegurarnos de que los errores no detengan el procesamiento de
   trabajos futuros.
-  Utilizamos with ProcessPoolExecutor() as executor: para asegurar que
   el executor se cierre correctamente una vez que el programa termina.

Este enfoque utiliza concurrent.futures.ProcessPoolExecutor para mejorar
la gestión de procesos y hace que el código sea más limpio y moderno
como vimos en clase. Además, con el uso de callbacks, podemos manejar
los resultados de manera más eficiente.

2.3 Vamos a optimizar la comunicación asíncrona utilizando asyncio.Queue
en lugar de queue.Queue para work_queue y results_queue, asegurándonos
de que todas las operaciones de cola sean asíncronas. Esto mejorará la
eficiencia y permitirá un mejor manejo de las tareas en un entorno
asíncrono.

Vamos a refactorizar el código:

.. code:: ipython3

    import asyncio
    import marshal
    import pickle
    import logging
    import threading
    import types
    from concurrent.futures import ProcessPoolExecutor
    
    import chunk_mp_mapreduce as mr
    
    # Configurar logging
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    logger = logging.getLogger(__name__)
    
    work_queue = asyncio.Queue()
    results_queue = asyncio.Queue()
    results = {}
    
    async def submit_job(job_id, reader, writer):
        try:
            writer.write(job_id.to_bytes(4, 'little'))
            await writer.drain()
            code_size = int.from_bytes(await reader.read(4), 'little')
            my_code = marshal.loads(await reader.read(code_size))
            data_size = int.from_bytes(await reader.read(4), 'little')
            data = pickle.loads(await reader.read(data_size))
            await work_queue.put((job_id, my_code, data))
            logger.info(f"Trabajo {job_id} entregado exitosamente.")
        except Exception as e:
            logger.error(f"Error en entregar el trabajo {job_id}: {e}")
            
            writer.write(b'\x00\x00\x00\x00')  # Indicar error al cliente
            await writer.drain()
    
    async def get_results_queue():
        while not results_queue.empty():
            try:
                job_id, data = await results_queue.get()
                results[job_id] = data
            except asyncio.QueueEmpty:
                return
    
    async def get_results(reader, writer):
        try:
            await get_results_queue()
            job_id = int.from_bytes(await reader.read(4), 'little')
            data = pickle.dumps(None)
            if job_id in results:
                data = pickle.dumps(results[job_id])
                del results[job_id]
            writer.write(len(data).to_bytes(4, 'little'))
            writer.write(data)
            await writer.drain()
            logger.info(f"Resultados para trabajos {job_id} recuperados exitosamente.")
        except Exception as e:
            logger.error(f"Error en los resultados esperados: {e}")
            writer.write(b'\x00\x00\x00\x00')  # Indicar error al cliente
            await writer.drain()
    
    async def accept_requests(reader, writer, job_id=[0]):
        try:
            op = await reader.read(1)
            if op[0] == 0:
                await submit_job(job_id[0], reader, writer)
                job_id[0] += 1
            elif op[0] == 1:
                await get_results(reader, writer)
        except Exception as e:
            logger.error(f"Error al aceptar la solicitud: {e}")
    
    async def worker():
        with ProcessPoolExecutor() as executor:
            while True:
                try:
                    job_id, code, data = await work_queue.get()
                    func = types.FunctionType(code, globals(), 'mapper_and_reducer')
                    mapper, reducer = func()
                    loop = asyncio.get_event_loop()
                    future = loop.run_in_executor(executor, mr.map_reduce, data, mapper, reducer, 100, mr.reporter)
                    result = await future
                    await results_queue.put((job_id, result))
                    logger.info(f"Trabajo {job_id} procesados exitosamente.")
                except Exception as e:
                    logger.error(f"Error en el procesamiento de trabajo del worker{job_id}: {e}")
    
    async def main():
        try:
            server = await asyncio.start_server(accept_requests, '127.0.0.1', 1936)
            worker_task = asyncio.create_task(worker())
            async with server:
                logger.info("Servidor iniciado exitosamente.")
                await server.serve_forever()
            await worker_task
        except Exception as e:
            logger.error(f"Error de inicio del servidor: {e}")
    
    if __name__ == '__main__':
        try:
            asyncio.run(main())
        except Exception as e:
            logger.critical(f"Error fatal: {e}")


Explicación de los cambios

-  Cambiamos Queue por asyncio.Queue para work_queue y results_queue.
-  Utilizamos await work_queue.put() y await results_queue.get() para
   operaciones de encolado y desencolado de manera asíncrona.
-  En get_results_queue, usamos await results_queue.get() para manejar
   la cola de resultados de manera asíncrona.
-  En worker, utilizamos asyncio.get_event_loop().run_in_executor() para
   ejecutar mr.map_reduce en el ProcessPoolExecutor de manera asíncrona.
-  Mantuvimos el manejo de errores existente para capturar y registrar
   cualquier excepción que ocurra durante el procesamiento de trabajos y
   la comunicación.
-  Creamos una tarea asíncrona para el trabajador con
   asyncio.create_task(worker()) en lugar de un hilo separado.

Estos cambios optimizan la comunicación asíncrona y aseguran que las
operaciones de cola se manejen de manera eficiente en un entorno
asíncrono.

2.4 Vamos a contenerizar la aplicación usando Docker. El objetivo es
crear un Dockerfile que nos permita construir una imagen de Docker que
ejecute la aplicación. Luego, probaremos esta imagen para verificar que
la aplicación funciona correctamente dentro del contenedor.

.. code:: ipython3

    # Usar una imagen base de Python
    FROM python:3.9-slim
    
    # Establecer el directorio de trabajo
    WORKDIR /app
    
    # Copiar los archivos requeridos al contenedor
    COPY requirements.txt requirements.txt
    COPY chunk_mp_mapreduce.py chunk_mp_mapreduce.py
    COPY main.py main.py
    
    # Instalar las dependencias
    RUN pip install --no-cache-dir -r requirements.txt
    
    # Exponer el puerto en el que la aplicación va a correr
    EXPOSE 1936
    
    # Comando para ejecutar la aplicación
    CMD ["python", "main.py"]


Creamos el archivo requirements.txt. Este archivo contendrá las
dependencias de Python necesarias para nuestra aplicación.

requirements.txt:

.. code:: ipython3

    asyncio

Guardamos el código de la aplicación en un archivo llamado main.py:

.. code:: ipython3

    import asyncio
    import marshal
    import pickle
    import logging
    import threading
    import types
    from concurrent.futures import ProcessPoolExecutor
    
    import chunk_mp_mapreduce as mr
    
    # Configurar logging
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    logger = logging.getLogger(__name__)
    
    work_queue = asyncio.Queue()
    results_queue = asyncio.Queue()
    results = {}
    
    async def submit_job(job_id, reader, writer):
        try:
            writer.write(job_id.to_bytes(4, 'little'))
            await writer.drain()
            code_size = int.from_bytes(await reader.read(4), 'little')
            my_code = marshal.loads(await reader.read(code_size))
            data_size = int.from_bytes(await reader.read(4), 'little')
            data = pickle.loads(await reader.read(data_size))
            await work_queue.put((job_id, my_code, data))
            logger.info(f" ... {job_id} ...")
        except Exception as e:
            logger.error(f"... {job_id}: {e}")
            writer.write(b'\x00\x00\x00\x00')  # Indicar error al cliente
            await writer.drain()
    
    async def get_results_queue():
        while not results_queue.empty():
            try:
                job_id, data = await results_queue.get()
                results[job_id] = data
            except asyncio.QueueEmpty:
                return
    
    async def get_results(reader, writer):
        try:
            await get_results_queue()
            job_id = int.from_bytes(await reader.read(4), 'little')
            data = pickle.dumps(None)
            if job_id in results:
                data = pickle.dumps(results[job_id])
                del results[job_id]
            writer.write(len(data).to_bytes(4, 'little'))
            writer.write(data)
            await writer.drain()
            logger.info(f"Resultados ...{job_id} ...")
        except Exception as e:
            logger.error(f"...: {e}")
            writer.write(b'\x00\x00\x00\x00')  # Indicar error al cliente
            await writer.drain()
    
    async def accept_requests(reader, writer, job_id=[0]):
        try:
            op = await reader.read(1)
            if op[0] == 0:
                await submit_job(job_id[0], reader, writer)
                job_id[0] += 1
            elif op[0] == 1:
                await get_results(reader, writer)
        except Exception as e:
            logger.error(f"...: {e}")
    
    async def worker():
        with ProcessPoolExecutor() as executor:
            while True:
                try:
                    job_id, code, data = await work_queue.get()
                    func = types.FunctionType(code, globals(), 'mapper_and_reducer')
                    mapper, reducer = func()
                    loop = asyncio.get_event_loop()
                    future = loop.run_in_executor(executor, mr.map_reduce, data, mapper, reducer, 100, mr.reporter)
                    result = await future
                    await results_queue.put((job_id, result))
                    logger.info(f"... {job_id} ....")
                except Exception as e:
                    logger.error(f"... {job_id}: {e}")
    
    async def main():
        try:
            server = await asyncio.start_server(accept_requests, '0.0.0.0', 1936)
            worker_task = asyncio.create_task(worker())
            async with server:
                logger.info(".....")
                await server.serve_forever()
            await worker_task
        except Exception as e:
            logger.error(f"...: {e}")
    
    if __name__ == '__main__':
        try:
            asyncio.run(main())
        except Exception as e:
            logger.critical(f"Error fatal: {e}")


Abrimos una terminal y ejecutamos el siguiente comando para construir la
imagen de Docker:

.. code:: ipython3

    docker build -t mapreduce_app .

Después de construir la imagen, podemos ejecutar un contenedor basado en
esta imagen:

.. code:: ipython3

    docker run -p 1936:1936 mapreduce_app

Para verificar que la aplicación funciona correctamente dentro del
contenedor, podemos conectar un cliente al puerto 1936 en el host y
enviar trabajos de prueba.

2.5 Vamos a desplegar la aplicación en un clúster de Kubernetes. Esto
implica crear los archivos de configuración necesarios (Deployment y
Service) para Kubernetes. Estos archivos nos permitirán gestionar la
aplicación y asegurar que se escale y administre correctamente.

.. code:: ipython3

    ### deployment.yaml
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: mapreduce-app
    spec:
      replicas: 3
      selector:
        matchLabels:
          app: mapreduce-app
      template:
        metadata:
          labels:
            app: mapreduce-app
        spec:
          containers:
          - name: mapreduce-app
            image: mapreduce_app:latest
            ports:
            - containerPort: 1936
            resources:
              requests:
                memory: "64Mi"
                cpu: "250m"
              limits:
                memory: "128Mi"
                cpu: "500m"


El archivo de Service define cómo se expone la aplicación a través de un
puerto accesible externamente.

.. code:: ipython3

    ### services.yaml
    apiVersion: v1
    kind: Service
    metadata:
      name: mapreduce-service
    spec:
      selector:
        app: mapreduce-app
      ports:
        - protocol: TCP
          port: 1936
          targetPort: 1936
      type: LoadBalancer


Para que Kubernetes pueda acceder a la imagen de Docker, debemos subirla
a un registro de imágenes (como Docker Hub o Google Container Registry).

.. code:: ipython3

    # Iniciar sesión en Docker Hub
    docker login
    
    # Etiquetar la imagen
    docker tag mapreduce_app:latest <your-dockerhub-username>/mapreduce_app:latest
    
    # Subir la imagen a Docker Hub
    docker push <your-dockerhub-username>/mapreduce_app:latest


Actualizamos el archivo deployment.yaml para usar la imagen del
registro:

.. code:: ipython3

    ...
    containers:
    - name: mapreduce-app
      image: <your-dockerhub-username>/mapreduce_app:latest
      ports:
      - containerPort: 1936
    ...


Usamos kubectl para aplicar los archivos de configuración y desplegar la
aplicación en el clúster

.. code:: ipython3

    kubectl apply -f deployment.yaml
    kubectl apply -f service.yaml

Podemos verificar que los recursos se hayan creado correctamente y que
la aplicación esté corriendo:

.. code:: ipython3

    # Verificar el estado de los pods
    kubectl get pods
    
    # Verificar el estado del servicio
    kubectl get services


2.6 Todo lo pedido se resumen aquí:

.. code:: ipython3

    from concurrent.futures import ProcessPoolExecutor
    import itertools
    import collections
    from typing import Callable, Any, List, Dict, Tuple
    
    def chunk_data(data: List[Any], chunk_size: int) -> List[List[Any]]:
        """Divide los datos en trozos más pequeños."""
        for i in range(0, len(data), chunk_size):
            yield data[i:i + chunk_size]
    
    def map_reduce(
            data: List[Any],
            mapper: Callable[[Any], List[Tuple[Any, Any]]],
            reducer: Callable[[Any, List[Any]], Any],
            chunk_size: int,
            reporter: Callable[[str], None] = None,
            combiner: Callable[[Any, List[Any]], List[Tuple[Any, Any]]] = None,
            partitioner: Callable[[Any], int] = None,
            num_reducers: int = 4) -> Dict[Any, Any]:
        
        if reporter:
            reporter("Inicio de la fase map ")
        
        # Fase de Mapeo
        with ProcessPoolExecutor() as executor:
            chunks = list(chunk_data(data, chunk_size))
            map_results = list(executor.map(mapper, chunks))
    
        if reporter:
            reporter("Fase map completada")
    
        if reporter:
            reporter("Inicio de la fase combine")
        
        # Fase de Combinación (opcional)
        if combiner:
            combined_results = []
            for chunk in map_results:
                combined_chunk = collections.defaultdict(list)
                for key, value in chunk:
                    combined_chunk[key].append(value)
                combined_results.append(
                    list(itertools.chain.from_iterable(combiner(k, v) for k, v in combined_chunk.items()))
                )
            map_results = combined_results
    
        if reporter:
            reporter(" Fase de combine completada")
    
        if reporter:
            reporter("Inicio de la fase shuffle y sort")
        
        # Fase de Barajado y Ordenación
        shuffle_sort = collections.defaultdict(list)
        for result in map_results:
            for key, value in result:
                shuffle_sort[key].append(value)
    
        if partitioner:
            partitioned_data = collections.defaultdict(list)
            for key, values in shuffle_sort.items():
                partitioned_data[partitioner(key) % num_reducers].append((key, values))
        else:
            partitioned_data = {i: [] for i in range(num_reducers)}
            for i, (key, values) in enumerate(shuffle_sort.items()):
                partitioned_data[i % num_reducers].append((key, values))
    
        if reporter:
            reporter(" Fase shuffle y sort completada")
    
        if reporter:
            reporter("Inicio de la fase reduce")
        
        # Fase de Reducción
        reduce_results = {}
        with ProcessPoolExecutor() as executor:
            futures = []
            for partition, kv_pairs in partitioned_data.items():
                futures.append(executor.submit(reduce_partition, kv_pairs, reducer))
            for future in futures:
                reduce_results.update(future.result())
    
        if reporter:
            reporter("Fase reduce completada")
        
        return reduce_results
    
    def reduce_partition(kv_pairs: List[Tuple[Any, List[Any]]], reducer: Callable[[Any, List[Any]], Any]) -> Dict[Any, Any]:
        """Reduce una partición de datos."""
        reduced_data = {}
        for key, values in kv_pairs:
            reduced_data[key] = reducer(key, values)
        return reduced_data


2.7 Posible soluciones

-  Implementar un manejador de señales para limpiar recursos y cerrar el
   servidor de manera ordenada.
-  Utilizar functools.partial para simplificar la creación de funciones
   con múltiples parámetros predefinidos.
-  Utilizar mp.Pool con un inicializador que configure la gestión de
   señales apropiadamente en los procesos hijos.
-  Enviar un trabajo especial (sentinela) a los trabajadores para
   indicarles que deben finaliza y asegurarse de que los hilos
   trabajadores se unen adecuadamente antes de que el programa principal
   termine.
-  Capturar y manejar las excepciones en las funciones asincrónicas y en
   los hilos trabajadoresy utilizar bloques try-except para manejar
   errores en la comunicación entre el cliente y el servidor.
-  Refactorizar el código para separar claramente las responsabilidades
   (por ejemplo, manejar trabajos, manejar resultados, aceptar
   solicitudes) y utilizar nombres de variables y funciones descriptivos
   para mejorar la claridad del código.

