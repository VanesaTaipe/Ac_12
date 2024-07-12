import concurrent.futures
import os

def count_words_in_file(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
    word_count = len(text.split())
    return (file_path, word_count)
#El método split() divide el texto en palabras utilizando espacios en blanco como separadores
#y len() devuelve la cantidad de elementos resultantes.

def parallel_word_count(file_paths):
    results = {}
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_to_file = {executor.submit(count_words_in_file, file_path): file_path for file_path in file_paths}
        for future in concurrent.futures.as_completed(future_to_file):
            file_path = future_to_file[future]
            try:
                file_path, count = future.result()
                results[file_path] = count
            except Exception as exc:
                print(f"{file_path} generated an exception: {exc}")
    return results

file_paths = ["file1.txt", "file2.txt", "file3.txt"]
word_counts = parallel_word_count(file_paths)
print(word_counts)
#administrador de contexto para crear un grupo de subprocesos (threads)
#que ejecutarán las tareas en paralel
