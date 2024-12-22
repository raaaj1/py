def schedule_requests(requests, head):
    order = requests  # Requests are served in the order they arrive
    total_movement = 0

    for req in order:
        total_movement += abs(req - head)
        head = req

    return order, total_movement


def main():
    # Step 1: Input number of requests
    n = int(input("Enter the number of disk requests: "))

    # Step 2: Input the requests
    print("Enter the disk requests (space-separated): ", end="")
    requests = list(map(int, input().split()))

    # Step 3: Input initial head position
    head = int(input("Enter the initial position of the disk head: "))

    # Step 4: Call the scheduling function
    order, total_movement = schedule_requests(requests, head)

    # Step 5: Output the results
    print("\nRequest Order: ", " ".join(map(str, order)))
    print(f"Total Head Movement: {total_movement}")


if __name__ == "__main__":
    main()
