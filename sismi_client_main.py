import psutil
print(psutil.cpu_percent(interval=1))
mem = psutil.virtual_memory()
print(mem.percent)

disks = psutil.disk_partitions()
for disk in disks:
    if 'snap' not in disk.mountpoint:
        print(disk.mountpoint, " ------> ", psutil.disk_usage(disk.mountpoint).percent)