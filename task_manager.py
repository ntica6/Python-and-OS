import psutil
import time

print(psutil.cpu_count())

processes =list(psutil.process_iter(["name", "memory_percent", "cpu_percent"]))
for p in processes:
    p.cpu_percent(interval = None)

time.sleep(5)
print(f"{"Name":<35}{"Memory(%)":<15}{"CPU(%)":<15}")
for p in processes:
    print(f"{p.name():<35}{p.memory_percent():<15.2f}{p.cpu_percent(interval=None):<15}")