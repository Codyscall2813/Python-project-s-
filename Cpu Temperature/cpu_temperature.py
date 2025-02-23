import psutil


def get_cpu_temperature() -> float | str:
    try:
        temperatures = psutil.sensors_temperatures()
        if 'coretemp' in temperatures:
            temperature = temperatures['coretemp'][0].current
            return temperature if isinstance(temperature, (int, float)) else "NA"
        else:
            return "NA"
    except (AttributeError, IndexError, KeyError):
        return "NA"


def get_ram_and_cpu_util() -> list:
    memory_stats = psutil.virtual_memory()
    return [
        memory_stats[0] // (1024 * 1024),
        memory_stats[2],
        psutil.cpu_percent(interval=4, percpu=True)
    ]


cpu_temperature = get_cpu_temperature()
system_utils = get_ram_and_cpu_util()

if isinstance(system_utils[2], list):
    cpu_percentage = ", ".join(f"{cpu:.2f}%" for cpu in system_utils[2])
else:
    cpu_percentage = f"{system_utils[2]:.2f}%"

print(f"Current CPU Temperature in Celsius is {
      cpu_temperature}°C, with percentage utilized being at {cpu_percentage}")
print(f"Current RAM utilization is {system_utils[1]}% of {system_utils[0]} MB")
