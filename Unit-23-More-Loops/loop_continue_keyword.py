for num in range(1, 30):
    if num % 3 == 0:
        # Skips any following statements from happening
        # continue to the next sequence in the loop
        continue

    print(f"NOT Multiple of 3 - {num}")