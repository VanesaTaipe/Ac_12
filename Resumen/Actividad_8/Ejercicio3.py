import dask.dataframe as dd

def parallel_csv_processing(file_paths):
    df = dd.read_csv(file_paths)
    average_value = df['Salary'].mean().compute()
    #El método compute() se utiliza para ejecutar el cálculo y obtener el resultado.
    return average_value

file_paths = ['file1.csv', 'file2.csv', 'file3.csv']
average = parallel_csv_processing(file_paths)
print(f"Average value: {average}")
