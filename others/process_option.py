import win32api
import ctypes
import psutil
# 导入打开进程权限
from win32con import PROCESS_ALL_ACCESS


def get_pid(app_name):
    app_pid = []
    for i in psutil.pids():
        proc = psutil.Process(i)
        if proc.name() == app_name:
            app_pid.append(i)
    return app_pid


class ProcessOption:
    def __init__(self, pid):
        self._kernel32 = ctypes.windll.LoadLibrary("kernel32.dll")  # 加载动态链接库
        self._process = win32api.OpenProcess(PROCESS_ALL_ACCESS, False, pid)  # 获取进程句柄

    def read_process_memory(self, address, read_size):
        """
        读取进程中内存值
        :param address: 内存地址
        :param read_size: 读取大小
        :return:
        """
        tmp_value = ctypes.c_ulong()
        self._kernel32.ReadProcessMemory(int(self._process), address, ctypes.byref(tmp_value), read_size, None)  # 读内存
        return tmp_value.value

    def write_process_memory(self, address, data, write_size):
        """
        修改进程中的内存值
        :param address: 内存地址
        :param data: 数据
        :param write_size: 写入大小
        :return:
        """
        tmp_value = ctypes.c_long(data)  # 设定修改的数据
        self._kernel32.WriteProcessMemory(int(self._process), address, ctypes.byref(tmp_value), write_size, None)

    def close(self):
        win32api.CloseHandle(self._process)


if __name__ == '__main__':
    proc_id = get_pid("Game.exe")[0]
    print(proc_id)
    handle = ProcessOption(proc_id)
    value = handle.read_process_memory(0x28CCC9F4, 4)
    if value < 1000:
        handle.write_process_memory(0x28CCC9F4, value * 10, 4)
    handle.close()
    print(value)
