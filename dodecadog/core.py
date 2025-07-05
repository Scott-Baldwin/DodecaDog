# default
import sys, platform, logging

# 3rd party
import psutil

# constants
NAME = "Template App"
VERSION = "0.1.2"


class AppClass:
    """
    App class to store values and perform operations.
    """

    def __init__(self):
        self.a = 0
        self.b = 0

    def go(self):
        return round(self.a * self.b, 2)

    def set_a(self, a):
        self.a = a

    def set_b(self, b):
        self.b = b


# %% custom logging function
def print_log(msg, log=logging.info):
    print(msg)
    log(msg)


# %% system info for logs
def print_system_info(p=print_log):
    p("=" * 40 + " SYS " + "=" * 40)
    p(f"File/Script: {__file__}")
    p(f"File version: {VERSION}")
    py_version = sys.version.split()[0]
    p(f"Python Version: {py_version}")
    uname = platform.uname()
    p(f"System: {uname.system}")
    p(f"Node Name: {uname.node}")
    p(f"Release: {uname.release}")
    p(f"Version: {uname.version}")
    p(f"Machine: {uname.machine}")
    p(f"Processor: {uname.processor}")

    p("=" * 40 + " CPU " + "=" * 40)
    p(f"Physical cores: {psutil.cpu_count(logical=False)}")
    p(f"Total cores: {psutil.cpu_count(logical=True)}")
    p(f"Max Frequency: {psutil.cpu_freq().max / 1000:.1f}Ghz")

    p("=" * 40 + " RAM " + "=" * 40)
    p(f"Total: {get_bytes_size(psutil.virtual_memory().total)}")
    p(f"Available: {get_bytes_size(psutil.virtual_memory().available)}")

    p("=" * 40 + " END " + "=" * 40)


def get_bytes_size(bytes, suffix="B"):
    """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor
