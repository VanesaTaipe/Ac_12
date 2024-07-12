def philosopher(left_fork, right_fork, philosopher_number):
    while True:
        with left_fork:
            with right_fork:
                print(f"Filósofo {philosopher_number} está comiendo.")
                time.sleep(0.5)
        print(f"Filósofo {philosopher_number} está pensando.")

forks = [threading.Lock() for _ in range(5)]
philosophers = [threading.Thread(target=philosopher, args=(forks[i % 5], forks[(i + 1) % 5], i)) for i in range(5)]
for p in philosophers:
    p.start()
