import os
import psutil

process = psutil.Process(os.getpid())
resident_mem = process.memory_info().rss    # Resident Set Size
virtual_mem = process.memory_info().vms     # Virtual memory size
