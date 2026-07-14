# Lab: Hill Climbing Search (Dynamic Version)
# Program by: Samip Khadka
# Roll no: 36
import random

# Input values
values = [2, 5, 8, 12, 10, 15, 11, 13, 9, 14]

# Global maximum
global_max = max(values)

print("=" * 45)
print("HILL CLIMBING SEARCH (DYNAMIC)")
print("=" * 45)

# Display indices
print("\nIndex: ", end="")
for i in range(len(values)):
    print(f"{i:3}", end="")
print()

# Display values
print("Value: ", end="")
for v in values:
    print(f"{v:3}", end="")
print("\n")

# Number of trials
trials = 4

# Random starting points
starts = random.sample(range(len(values)), trials)

for start in starts:

    current = start

    print("-" * 45)
    print(f"\nStart at Index {current}, Value {values[current]}")
    print("Climbing...")

    while True:

        best = current

        # Check left neighbor
        if current > 0 and values[current - 1] > values[best]:
            best = current - 1

        # Check right neighbor
        if current < len(values) - 1 and values[current + 1] > values[best]:
            best = current + 1

        # If no better neighbor exists
        if best == current:
            break

        direction = "left" if best < current else "right"

        print(f"Move {direction} to {best}, Value {values[best]}")

        current = best

    print(f"Peak reached at Index {current}, Value {values[current]}")

    if values[current] == global_max:
        print(" GLOBAL MAXIMUM FOUND!")
    else:
        print(" LOCAL MAXIMUM (not the highest)")

print("\n" + "=" * 45)
print(f"Global Maximum = {global_max}")
print("=" * 45)
print("Program by: Samip Khadka")
print("Roll No: 36")
