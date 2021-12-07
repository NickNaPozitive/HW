from prettytable import PrettyTable as pt
import psutil as pu
import datetime
from collections import namedtuple as nt


# pprint(datetime.datetime.fromtimestamp(pu.boot_time()).strftime("%Y-%m-%d %H:%M:%S"))


def get_cpu():
    counter_cpu = pu.cpu_count(logical=True)
    return counter_cpu


def cpu_freq():
    info = []
    data = pu.cpu_freq(percpu=True)
    for i in data:
        info.append(i[0])
    return info


def cpu_freq_current():
    current = 0
    data = pu.cpu_freq(percpu=True)
    for i in data:
        current += i[0]
    result = current / 12
    return result


def disk_usage():
    dict = {}
    data = pu.disk_usage("/")
    data._asdict()
    dict.update(
        {'total': f"{round((data.total / 1000000000), 2)} Gb",
         'used': f"{round((data.used / 1000000000), 2)} Gb",
         "free": f"{round((data.free / 1000000000), 2)} Gb",
         'percent': f"{data.percent} %",
         }
    )
    return dict


def show(**kwargs):
    i = 1
    my_table = pt()
    my_table.field_names = ["TYPE", "INFO"]
    my_table.add_row(["cores", kwargs['cpu_num']])
    for key in kwargs["cpu_freq"]:
        my_table.add_row([f"freq {i} core", key])
        i += 1
    for key in kwargs["disk_usage"]:
        my_table.add_row([key, kwargs["disk_usage"][key]])

    print(my_table)


def run():
    show(cpu_num=get_cpu(), cpu_freq=cpu_freq(), disk_usage=disk_usage())


if __name__ == '__main__':
    run()
