def fifo_page_replacement(pages, capacity):
    """
    FIFO Page Replacement Algorithm
    """
    memory = []
    page_faults = 0

    for page in pages:
        if page not in memory:
            page_faults += 1
            if len(memory) == capacity:
                memory.pop(0)  # Remove the oldest page
            memory.append(page)
    return page_faults


def lru_page_replacement(pages, capacity):
    """
    LRU Page Replacement Algorithm
    """
    page_map = {}  # Page -> Last used index
    page_faults = 0

    for i, page in enumerate(pages):
        if page not in page_map:
            page_faults += 1
            if len(page_map) == capacity:
                # Find the least recently used page
                lru_page = min(page_map, key=page_map.get)
                del page_map[lru_page]
        page_map[page] = i  # Update the last used index
    return page_faults


def optimal_page_replacement(pages, capacity):
    """
    Optimal Page Replacement Algorithm
    """
    memory = []
    page_faults = 0

    for i, page in enumerate(pages):
        if page not in memory:
            page_faults += 1
            if len(memory) == capacity:
                # Find the page to replace
                farthest = -1
                page_to_replace = None
                for mem_page in memory:
                    if mem_page not in pages[i + 1:]:
                        page_to_replace = mem_page
                        break
                    else:
                        next_use = pages[i + 1:].index(mem_page)
                        if next_use > farthest:
                            farthest = next_use
                            page_to_replace = mem_page
                memory.remove(page_to_replace)
            memory.append(page)
    return page_faults


def main():
    """
    Main function to handle input and output.
    """
    # Input number of frames
    capacity = int(input("Enter number of frames: "))

    # Input number of pages
    n = int(input("Enter number of pages: "))

    if capacity <= 0 or n <= 0:
        print("Number of frames and pages must be greater than zero.")
        return

    # Input the page reference string
    print("Enter the page reference string (space-separated): ", end="")
    pages = list(map(int, input().split()))

    # Choose the algorithm
    print("\nChoose the algorithm (1 for FIFO, 2 for LRU, 3 for Optimal): ", end="")
    choice = int(input())

    if choice == 1:
        page_faults = fifo_page_replacement(pages, capacity)
        print("FIFO Page Faults:", page_faults)
    elif choice == 2:
        page_faults = lru_page_replacement(pages, capacity)
        print("LRU Page Faults:", page_faults)
    elif choice == 3:
        page_faults = optimal_page_replacement(pages, capacity)
        print("Optimal Page Faults:", page_faults)
    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()
