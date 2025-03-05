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

class PriorityScheduler:
    def __init__(self):
        self.processes = []

    def add_process(self, pid, arrival_time, burst_time, priority):
        process = Process(pid, arrival_time, burst_time, priority)
        self.processes.append(process)

    def schedule(self):
        self.processes.sort(key=lambda p: (p.arrival_time, p.priority))
        current_time = 0

        for process in self.processes:
            if current_time < process.arrival_time:
                current_time = process.arrival_time
            process.start_time = current_time
            process.completion_time = current_time + process.burst_time
            process.turnaround_time = process.completion_time - process.arrival_time
            process.waiting_time = process.turnaround_time - process.burst_time
            current_time = process.completion_time

    def display_metrics(self):
        print(f"{'PID':<10}{'Arrival':<10}{'Burst':<10}{'Priority':<10}{'Start':<10}{'Completion':<12}{'Turnaround':<12}{'Waiting':<10}")
        for p in self.processes:
            print(f"{p.pid:<10}{p.arrival_time:<10}{p.burst_time:<10}{p.priority:<10}{p.start_time:<10}{p.completion_time:<12}{p.turnaround_time:<12}{p.waiting_time:<10}")

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
    scheduler.add_process(1, 0, 5, 2)
    scheduler.add_process(2, 1, 3, 1)
    scheduler.add_process(3, 2, 8, 3)
    scheduler.add_process(4, 3, 6, 2)

    scheduler.schedule()
    scheduler.display_metrics()
    scheduler.visualize()
