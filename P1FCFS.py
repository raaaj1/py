class Process:
    def __init__(self, pid, arrival, burst):
        self.id, self.arrival, self.burst = pid, arrival, burst
        self.completion = self.turnaround = self.waiting = 0

def fcfs_scheduling(processes):
    current_time = 0
    gantt_chart = []
    for p in processes:
        current_time = max(current_time, p.arrival)
        gantt_chart.append((p.id, current_time))
        p.completion = current_time + p.burst
        p.turnaround, p.waiting = p.completion - p.arrival, p.turnaround - p.burst
        current_time += p.burst
    return gantt_chart

def main():
    n = int(input("Enter number of processes: "))
    processes = [Process(i+1, *map(int, input(f"Enter arrival and burst for P{i+1}: ").split())) for i in range(n)]
    processes.sort(key=lambda p: p.arrival)
    
    gantt_chart = fcfs_scheduling(processes)
    print("\nGantt Chart:", "".join(f"| P{p[0]} " for p in gantt_chart) + "|")
    print("0", "".join(f"{p[1]:>4} " for p in gantt_chart))
    
    avg_wt = sum(p.waiting for p in processes) / n
    avg_tat = sum(p.turnaround for p in processes) / n
    print(f"\nAverage Waiting Time: {avg_wt:.2f}\nAverage Turnaround Time: {avg_tat:.2f}")

if __name__ == "__main__":
    main()
