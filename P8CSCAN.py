def CSCAN(requests, head, disk_size=183):
    """
    Function to implement the C-SCAN disk scheduling algorithm.
    """
    seek_count = 0
    distance = 0
    cur_track = 0
    left = [0]  # Starting boundary
    right = [disk_size - 1]  # Ending boundary
    seek_sequence = []

    # Divide requests into left and right of the head
    for request in requests:
        if request < head:
            left.append(request)
        if request > head:
            right.append(request)

    # Sort left and right lists
    left.sort()
    right.sort()

    # Serve the right side first
    for cur_track in right:
        seek_sequence.append(cur_track)
        distance = abs(cur_track - head)
        seek_count += distance
        head = cur_track

    # Jump to the beginning (circular behavior)
    head = 0
    seek_count += (disk_size - 1)

    # Serve the left side
    for cur_track in left:
        seek_sequence.append(cur_track)
        distance = abs(cur_track - head)
        seek_count += distance
        head = cur_track

    # Print results
    print("Total number of seek operations =", seek_count)
    print("Seek Sequence is:")
    print(" ".join(map(str, seek_sequence)))


def main():
    """
    Main function to handle input and output.
    """
    # Input number of requests
    n = int(input("Enter the number of requests: "))

    # Input requests
    print("Enter the requests (space-separated): ", end="")
    requests = list(map(int, input().split()))

    # Input initial head position
    head = int(input("Enter the initial position of the head: "))

    # Call the CSCAN function
    CSCAN(requests, head)


if __name__ == "__main__":
    main()
