def SCAN(requests, initial_position, disk_size):
    """
    SCAN disk scheduling algorithm.
    """
    # Sort the requests
    requests.sort()

    # Separate requests into left and right of the initial position
    left = [req for req in requests if req < initial_position]
    right = [req for req in requests if req >= initial_position]

    # Reverse the left side for servicing in decreasing order
    left.reverse()

    total_distance = 0
    current_position = initial_position

    # Serve the left side
    for req in left:
        total_distance += abs(current_position - req)
        current_position = req

    # Account for the disk edge (move to 0)
    if left:
        total_distance += abs(current_position - 0)
        current_position = 0

    # Serve the right side
    for req in right:
        total_distance += abs(current_position - req)
        current_position = req

    return total_distance


def main():
    """
    Main function to handle input and output.
    """
    # Input the number of disk requests
    n = int(input("Enter the number of disk requests: "))

    # Input the disk requests
    print("Enter the disk requests (track numbers): ", end="")
    requests = list(map(int, input().split()))

    # Input the initial disk arm position
    initial_position = int(input("Enter the initial disk arm position: "))

    # Input the disk size
    disk_size = int(input("Enter the disk size (maximum track number): "))

    # Call the SCAN function
    total_distance = SCAN(requests, initial_position, disk_size)

    # Output the total seek distance
    print("Total seek distance (SCAN):", total_distance)


if __name__ == "__main__":
    main()
