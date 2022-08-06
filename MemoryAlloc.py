import os
import psutil

process = psutil.Process(os.getpid())
resident_mem = process.memory_info().rss/1024/1024    # Resident Set Size
virtual_mem = process.memory_info().vms/1024/1024     # Virtual memory size
print('Resident Memory : ', resident_mem, 'MBs')
print('Resident Memory : ', virtual_mem, 'MBs')
