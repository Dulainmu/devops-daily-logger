import os
from datetime import date

log = input("What did you learn today? ")
today = date.today().isoformat()

if not os.path.exists("logs"):
    os.mkdir("logs")

with open(f"logs/{today}.txt", "w") as file:
    file.write(log)

print(f"Log saved to logs/{today}.txt")
