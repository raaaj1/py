def schedule_requests(requests, head):
    remaining = requests[:]  # Make a copy of the requests list
    order = []  # To store the order in which requests are served
    total_movement = 0  # Total movement of the disk head

    while remaining:
        # Find the closest request to the current head position
        closest = min(remaining, key=lambda req: abs(req - head))
        
        # Calculate movement
        total_movement += abs(closest - head)
        
        # Move the head to the closest request
        head = closest
        
        # Add to the order of served requests
        order.append(closest)
        
        # Remove the served request
        remaining.remove(closest)

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
