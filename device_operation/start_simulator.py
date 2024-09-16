import subprocess
import winreg

from .get_adb_address import get_simulator_port
from .mumu_manager_api import mumu12_control_api_backend
from .bluestacks_module import find_display_name, read_registry_key
from .device_config import load_data


def start_simulator_uuid(uuid):
    return subprocess.Popen(load_data(uuid)['latest_command_line'])


def start_simulator_classic(simulator_type, multi_instance=None, return_status=False):
    if simulator_type in ["bluestacks_nxt","bluestacks_nxt_cn"]:
        if simulator_type != "bluestacks_nxt":
            region = "cn"
        if multi_instance is None and region == "cn":
            multi_instance = "BlueStacks"
        elif multi_instance is None:
            multi_instance = "BlueStacks App Player"

        def bst_read_registry_key(region):
            key_path = f"SOFTWARE\\BlueStacks_nxt{region}"
            value_name = "InstallDir"
            try:
                with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path, 0, winreg.KEY_READ) as key:
                    value, _ = winreg.QueryValueEx(key, value_name)
                return value + 'HD-Player.exe'
            except FileNotFoundError:
                return None

        command = f""" "{bst_read_registry_key(region)}" --instance {find_display_name(multi_instance, read_registry_key(region))}"""
        subprocess.Popen(command,shell=True)
        if return_status == True:
            return ["starting",get_simulator_port(simulator_type, multi_instance)]
        else:
            return get_simulator_port(simulator_type, multi_instance)
    if simulator_type in ["mumu", "mumu_global"]:
        if multi_instance == None:
            multi_instance = 0
        if return_status == True:
            return [mumu12_control_api_backend(simulator_type, multi_instance, 'get_launch_status'),get_simulator_port(simulator_type, multi_instance)]
        else:
            return mumu12_control_api_backend(simulator_type, multi_instance, 'start')
