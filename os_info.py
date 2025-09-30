import psutil

memory_info = psutil.virtual_memory()
memory_bytes = memory_info.total
memory_gigabytes = memory_bytes / (1024 ** 3)
no_physical_cores = psutil.cpu_count(logical = False)
no_logical_cores =  psutil.cpu_count(logical = True)
total_cpu_usage = psutil.cpu_percent(interval = 1)
current_process = psutil.Process()
no_threads = current_process.num_threads()
print(total_cpu_usage)
#no_threads_in_current_process

print(f"{"Memory Total(GB)":<30}{"Total CPU Usage(%)":<30}{"Number of Physical Cores":<30}{"Number of Logical Cores":<30}{"Number of Threads in Current Process":<30}")
print(f"{memory_gigabytes:<30.2f}{no_physical_cores:<30}{no_logical_cores:<30}{total_cpu_usage:<30}{no_threads:<30} ")
