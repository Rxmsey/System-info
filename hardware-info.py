import subprocess

def get_cpu_info():
    # Use the wmic command to retrieve information about the CPU
    output = subprocess.check_output(["wmic", "cpu", "get", "name"]).strip()
    print("CPU: " + output.decode())

def get_gpu_info():
    # Use the dxdiag command to retrieve information about the GPU
    output = subprocess.check_output(["dxdiag", "/t", "dxdiag.txt"])
    with open("dxdiag.txt", "r") as f:
        lines = f.readlines()
    for line in lines:
        if "Card name" in line:
            print("GPU: " + line.strip())

def get_ram_info():
    # Use the wmic command to retrieve information about the RAM
    output = subprocess.check_output(["wmic", "memorychip", "get", "capacity"]).strip()
    print("RAM: " + output.decode())

def get_battery_info():
    # Use the powercfg command to retrieve information about the battery
    output = subprocess.check_output(["powercfg", "/batteryreport"])
    with open("battery-report.html", "r") as f:
        lines = f.readlines()
    for line in lines:
        if "Design capacity" in line:
            print("Battery: " + line.strip())

def main():
    get_cpu_info()
    get_gpu_info()
    get_ram_info()
    get_battery_info()

if __name__ == "__main__":
    main()
