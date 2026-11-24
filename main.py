"""The Robot Pickup Line Championship — entry for make.fun.

Writes one line to /output/entry.txt.
The line is the funniest one-line pickup line a robot could use, 200 characters or fewer.
"""
import os

LINE = "Are you Wi-Fi? Because I feel a strong connection, and my signal drops every time you leave the room."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
