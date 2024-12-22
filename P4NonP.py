from collections import deque
from typing import List, Tuple


# Class to store process information
class Process:
    def __init__(self, pid, arrival, burst, priority):
        self.id = pid             # Process ID
        self.arrival = arrival    # Arrival Time
        self.burst = burst        # Burst Time
        self.priority = priority  # Priority
        self.remaining_burst = burst  # Remaining Burst Time
        self.completion = 0       # Completion Time
        self.turnaround = 0       # Turnaround Time
        self.waiting = 0          # Waiting Time


# Function to implement Non-preemptive Priority scheduling
def priority_scheduling(processes: List[Process]) -> List[Tuple[int, int]]:
    gantt_chart = []  # List of tuples (Process ID, Time)
    current_time = 0

    # Sort processes by arrival time, then by priority (lower priority number means higher priority)
    processes.sort(key=lambda p: (p.arrival, p.priority))

    # List to store completed processes
    completed = []
    while len(completed) < len(processes):
        # Find the process with the highest priority (smallest priority number)
        ready_queue = [p for p in processes if p.arrival <= current_time and p not in completed]
        ready_queue.sort(key=lambda p: p.priority)

        if ready_queue:
            process = ready_queue[0]
            gantt_chart.append((process.id, current_time))
            current_time += process.burst
            process.completion = current_time
            process.turnaround = process.completion - process.arrival
            process.waiting = process.turnaround - process.burst
            completed.append(process)
        else:
            current_time += 1  # Idle time if no process is ready

    return gantt_chart


# Function to implement Round-Robin scheduling
def round_robin(processes: List[Process], quantum: int) -> List[Tuple[int, int]]:
    gantt_chart = []  # List of tuples (Process ID, Time)
    current_time = 0
    queue = deque()

    # Sort processes by arrival time
    processes.sort(key=lambda p: p.arrival)

    i = 0
    while i < len(processes) and processes[i].arrival <= current_time:
        queue.append(processes[i])
        i += 1

    while queue:
        process = queue.popleft()
        if process.remaining_burst > quantum:
            gantt_chart.append((process.id, current_time))
            current_time += quantum
            process.remaining_burst -= quantum
        else:
            gantt_chart.append((process.id, current_time))
            current_time += process.remaining_burst
            process.remaining_burst = 0
            process.completion = current_time
            process.turnaround = process.completion - process.arrival
            process.waiting = process.turnaround - process.burst

        # Add processes that have arrived to the queue
        while i < len(processes) and processes[i].arrival <= current_time:
            queue.append(processes[i])
            i += 1

        # If the process is not finished, add it back to the queue
        if process.remaining_burst > 0:
            queue.append(process)

    return gantt_chart


# Function to display the Gantt chart
def display_gantt_chart(gantt_chart: List[Tuple[int, int]]):
    print("\nGantt Chart:")
    for entry in gantt_chart:
        print(f"| P{entry[0]} ", end="")
    print("|")

    print("0 ", end="")
    for entry in gantt_chart:
        print(f"{entry[1]:>4} ", end="")
    print()


# Function to display process details
def display_process_details(processes: List[Process]):
    print("\nProcess\tArrival\tBurst\tPriority\tCompletion\tTurnaround\tWaiting")
    for p in processes:
        print(f"P{p.id}\t{p.arrival}\t{p.burst}\t{p.priority}\t\t{p.completion}\t\t{p.turnaround}\t\t{p.waiting}")


# Main function
def main():
    n = int(input("Enter the number of processes: "))
    quantum = int(input("Enter the time quantum (for Round-Robin): "))
    
    processes = []
    for i in range(n):
        arrival, burst, priority = map(int, input(f"Enter arrival time, burst time and priority for process {i + 1} (space-separated): ").split())
        processes.append(Process(i + 1, arrival, burst, priority))

    # Non-preemptive Priority Scheduling
    print("\nNon-preemptive Priority Scheduling:")
    priority_gantt_chart = priority_scheduling(processes.copy())
    display_process_details(processes)
    display_gantt_chart(priority_gantt_chart)

    # Round-Robin Scheduling
    print("\nRound-Robin Scheduling:")
    round_robin_gantt_chart = round_robin(processes.copy(), quantum)
    display_process_details(processes)
    display_gantt_chart(round_robin_gantt_chart)

    # Calculate and display average waiting time and turnaround time
    total_waiting = sum(p.waiting for p in processes)
    total_turnaround = sum(p.turnaround for p in processes)

    avg_waiting_time = total_waiting / n
    avg_turnaround_time = total_turnaround / n

    print(f"\nAverage Waiting Time: {avg_waiting_time:.2f}")
    print(f"Average Turnaround Time: {avg_turnaround_time:.2f}")


if __name__ == "__main__":
    main()
