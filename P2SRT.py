def srtf_scheduling():
    n = int(input("Enter number of processes: "))
    processes = [tuple(map(int, input(f"Enter arrival and burst time for P{i+1}: ").split())) + (i+1,) for i in range(n)]
    processes.sort(key=lambda x: x[0])

    time, completed, gantt_chart = 0, 0, []
    remaining_time, wt, tat = {p[2]: p[1] for p in processes}, {p[2]: 0 for p in processes}, {p[2]: 0 for p in processes}

    while completed < n:
        available = [p for p in processes if p[0] <= time and remaining_time[p[2]] > 0]
        if available:
            current = min(available, key=lambda x: (remaining_time[x[2]], x[0]))
            gantt_chart.append((time, current[2], time + 1) if not gantt_chart or gantt_chart[-1][1] != current[2] else (gantt_chart[-1][0], current[2], gantt_chart[-1][2] + 1))
            remaining_time[current[2]] -= 1
            time += 1
            if remaining_time[current[2]] == 0:
                completed += 1
                tat[current[2]], wt[current[2]] = time - current[0], time - current[0] - current[1]
        else:
            gantt_chart.append((time, -1, time + 1))
            time += 1

    print("\nGantt Chart:", " ".join([f"{'Idle' if pid == -1 else f'P{pid}'}: [{start},{end}]" for start, pid, end in gantt_chart]))
    print("\n".join([f"P{p[2]}\t{wt[p[2]]}\t{tat[p[2]]}" for p in processes]))
    print(f"\nAvg WT: {sum(wt.values()) / n:.2f}, Avg TAT: {sum(tat.values()) / n:.2f}")

if __name__ == "__main__":
    srtf_scheduling()
