def tower_of_hanoi(n, source, target, auxiliary):
    """
    Solve the Tower of Hanoi problem.

    Parameters:
        n (int): Number of disks.
        source (str): The source rod.
        target (str): The target rod.
        auxiliary (str): The auxiliary rod.
    """
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return

    # Move n-1 disks from source to auxiliary using target as auxiliary
    tower_of_hanoi(n - 1, source, auxiliary, target)

    # Move the nth disk from source to target
    print(f"Move disk {n} from {source} to {target}")

    # Move the n-1 disks from auxiliary to target using source as auxiliary
    tower_of_hanoi(n - 1, auxiliary, target, source)

# Example usage
number_of_disks = 3
print(f"Solving Tower of Hanoi with {number_of_disks} disks:")
tower_of_hanoi(number_of_disks, 'A', 'C', 'B')
