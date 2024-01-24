import subprocess


def get_info():
    info_lines = subprocess.check_output("sensors").decode("utf-8").split("\n")
    result = []
    count = 0
    for i in info_lines:
        if "fan" in i:
            result.append("Fan Speed: " + i.split(":")[-1].strip())

        if "Core" in i:
            result.append("Core %d: " % count + i.split(":")[-1].split("(")[0].strip())
            count += 1

    return result
