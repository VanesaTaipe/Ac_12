from multiprocessing import Pool

def sum_segment(segment):
    return sum(segment)

if __name__ == "__main__":
    data = list(range(10))  # Lista de un millón de elementos
    num_processes = 4
    segment_size = len(data) // num_processes

    segments = [data[i * segment_size:(i + 1) * segment_size] for i in range(num_processes)]

    with Pool(num_processes) as pool:
        results = pool.map(sum_segment, segments)

    total_sum = sum(results)
    print(f"Total sum: {total_sum},{results}")
