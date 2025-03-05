import matplotlib.pyplot as plt

class Process:
    def __init__(self, pid, arrival_time, burst_time, priority):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority = priority
        self.start_time = None
        self.completion_time = None
        self.waiting_time = None
        self.turnaround_time = None
        self.response_time = None

class PriorityScheduler:
    def __init__(self):
        self.processes = []

    def add_process(self, pid, arrival_time, burst_time, priority):
        process = Process(pid, arrival_time, burst_time, priority)
        self.processes.append(process)

    def schedule(self):
        self.processes.sort(key=lambda p: (p.arrival_time, p.priority))
        current_time = 0
        total_waiting_time = 0
        total_turnaround_time = 0
        total_response_time = 0

        for process in self.processes:
            if current_time < process.arrival_time:
                current_time = process.arrival_time
            process.start_time = current_time
            process.response_time = process.start_time - process.arrival_time
            process.completion_time = current_time + process.burst_time
            process.turnaround_time = process.completion_time - process.arrival_time
            process.waiting_time = process.turnaround_time - process.burst_time
            total_waiting_time += process.waiting_time
            total_turnaround_time += process.turnaround_time
            total_response_time += process.response_time
            current_time = process.completion_time

        self.avg_waiting_time = total_waiting_time / len(self.processes)
        self.avg_turnaround_time = total_turnaround_time / len(self.processes)
        self.avg_response_time = total_response_time / len(self.processes)

    def display_metrics(self):
        print(f"{'PID':<10}{'Arrival':<10}{'Burst':<10}{'Priority':<10}{'Start':<10}{'Completion':<12}{'Turnaround':<12}{'Waiting':<10}{'Response':<10}")
        for p in self.processes:
            print(f"{p.pid:<10}{p.arrival_time:<10}{p.burst_time:<10}{p.priority:<10}{p.start_time:<10}{p.completion_time:<12}{p.turnaround_time:<12}{p.waiting_time:<10}{p.response_time:<10}")
        print(f"\nAverage Waiting Time: {self.avg_waiting_time:.2f}")
        print(f"Average Turnaround Time: {self.avg_turnaround_time:.2f}")
        print(f"Average Response Time: {self.avg_response_time:.2f}")

    def visualize(self):
        fig, gnt = plt.subplots()
        gnt.set_xlabel('Time')
        gnt.set_ylabel('Processes')
        gnt.set_yticks([10 * (p.pid + 1) for p in self.processes])
        gnt.set_yticklabels([f"P{p.pid}" for p in self.processes])
        gnt.grid(True)

        for p in self.processes:
            gnt.broken_barh([(p.start_time, p.burst_time)], (10 * (p.pid + 1) - 5, 9), facecolors=('tab:blue'))
        
        plt.title('Priority Scheduling Gantt Chart')
        plt.show()

if __name__ == '__main__':
    scheduler = PriorityScheduler()
    pid = 1
    while True:
        try:
            arrival_time = int(input(f"Masukkan arrival time untuk proses {pid}: "))
            burst_time = int(input(f"Masukkan burst time untuk proses {pid}: "))
            priority = int(input(f"Masukkan priority untuk proses {pid}: "))
            if arrival_time < 0 or burst_time <= 0 or priority < 0:
                print("Input tidak valid, masukkan angka positif.")
                continue
            scheduler.add_process(pid, arrival_time, burst_time, priority)
            pid += 1
            more = input("Tambah proses lagi? (y/n): ").lower()
            if more != 'y':
                break
        except ValueError:
            print("Input tidak valid, masukkan angka.")
            continue

    scheduler.schedule()
    scheduler.display_metrics()
    scheduler.visualize()
