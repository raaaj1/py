from collections import deque

def round_robin():
    n = int(input("Enter the number of processes: "))
    processes = [tuple(map(int, input(f"Enter arrival and burst time for P{i+1}: ").split())) + (i+1,) for i in range(n)]
    quantum = int(input("Enter the time quantum: "))
    processes.sort(key=lambda x: x[0])

    time, gantt_chart, remaining_time = 0, [], {p[2]: p[1] for p in processes}
    waiting_time, turnaround_time = {p[2]: 0 for p in processes}, {p[2]: 0 for p in processes}
    queue = deque()

    while len(queue) or any(remaining_time[p[2]] > 0 for p in processes):
        for p in processes:
            if p[0] <= time and remaining_time[p[2]] > 0 and p not in queue: queue.append(p)
        
        if queue:
            current = queue.popleft()
            exec_time = min(quantum, remaining_time[current[2]])
            gantt_chart.append((time, current[2], time + exec_time) if not gantt_chart or gantt_chart[-1][1] != current[2] else (gantt_chart[-1][0], current[2], gantt_chart[-1][2] + exec_time))
            remaining_time[current[2]] -= exec_time
            time += exec_time

            if remaining_time[current[2]] == 0:
                turnaround_time[current[2]] = time - current[0]
                waiting_time[current[2]] = turnaround_time[current[2]] - current[1]

            if remaining_time[current[2]] > 0: queue.append(current)
        else:
            gantt_chart.append((time, -1, time + 1))
            time += 1

    print(f"\nGantt Chart: {' '.join([f'{('Idle' if pid == -1 else f'P{pid}')}: [{start},{end}]' for start, pid, end in gantt_chart])}")
    print("\nProcess\tWT\tTAT")
    for p in processes:
        pid = p[2]
        print(f"P{pid}\t{waiting_time[pid]}\t{turnaround_time[pid]}")

    avg_wt = sum(waiting_time.values()) / n
    avg_tat = sum(turnaround_time.values()) / n
    print(f"\nAvg Waiting Time: {avg_wt:.2f}\nAvg Turnaround Time: {avg_tat:.2f}")

if __name__ == "__main__":
    round_robin()
