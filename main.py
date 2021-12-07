from prettytable import PrettyTable as pt
import psutil as pu
from pprint import pprint as pp
import datetime
from collections import namedtuple as nt


def get_cpu():
    dict = {}
    j = 1
    current = 0

    counter_cpu = pu.cpu_count(logical=True)
    data_freq = pu.cpu_freq(percpu=True)
    dict.update({
        'cores': counter_cpu
    })
    for i in data_freq:
        dict.update({
            f'core {j}': i[0]
        })
        j += 1
    for i in data_freq:
        current += i[0]
    result = current / 12
    dict.update({
        'freq_current': round(result, 4)
    })
    return dict


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


def network_info():
    dict = {}
    data = pu.net_io_counters()
    data._asdict()
    dict.update(
        {'bytes_sent': f"{round((data.bytes_sent / 1000000000), 3)} Gb",
         'bytes_recv': f"{round((data.bytes_recv / 1000000000), 3)} Gb",
         }
    )

    return dict


def show(**kwargs):
    i = 1
    my_table = pt()
    my_table.field_names = ["TYPE", "INFO"]
    for key, value in kwargs["get_cpu"].items():
        if key == 'cores':
            my_table.add_row(["cores", value])
        elif key == 'freq_current':
            my_table.add_row(["freq_current", value])
        else:
            my_table.add_row([key, value])
    for key in kwargs["disk_usage"]:
        my_table.add_row([key, kwargs["disk_usage"][key]])
    for key in kwargs["network_info"]:
        my_table.add_row([key, kwargs["network_info"][key]])

    print(my_table)


def run():
    show(get_cpu=get_cpu(), disk_usage=disk_usage(), network_info=network_info())


if __name__ == '__main__':
    run()
