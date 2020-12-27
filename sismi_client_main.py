import psutil
import requests


client_id = 'abc'
cpu_use = psutil.cpu_percent(interval=1)
mem = psutil.virtual_memory()
disk_use_threshold = 80
disk_use_breach = {}


disks = psutil.disk_partitions()

system_report = {}
system_report["client_id"] = client_id
system_report["cpu_use"] = cpu_use
system_report["memory"] = {"percent": mem.percent, "used": mem.used, "free": mem.free, "total": mem.total,
                           "available": mem.available}
system_report["disk"] = []

for disk in disks:
    this_disk = {}
    this_disk['name'] = disk.mountpoint
    this_disk["use_percent"] = psutil.disk_usage(disk.mountpoint).percent
    system_report["disk"].append(this_disk)


print(system_report)