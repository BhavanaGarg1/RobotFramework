#4 digit Random number generation and write to file until 2 kb

import random
import os

output_file = "random_numbers.txt"

with open(output_file, "w") as f:
    while True:
        number = random.randint(1000, 9999)  # 4-digit number
        f.write(str(number) + "\n")          # Write with newline

        # Check if file has reached or exceeded 2 KB (2048 bytes)
        if os.path.getsize(output_file) >= 2048:
            break

print(f"Finished writing to {output_file}. Size: {os.path.getsize(output_file)} bytes.")
