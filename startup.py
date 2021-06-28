import os
import time

# delay between each execution statement
delay = 20

# files to be opened (add .exe files)
open = [
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    r"C:\ST\STM32CubeIDE_1.6.1\STM32CubeIDE\stm32cubeide.exe",
    r"C:\Users\vicadmin\AppData\Local\Programs\Microsoft VS Code\Code.exe",
    r"C:\Users\vicadmin\AppData\Local\slack\slack.exe"
]

# Print iterations progress
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Print New Line on Complete
    if iteration == total: 
        print()


print("Begging Startup...")
print("Opening:")

for a in open:
    print(a)

input("Press ENTER to Continue...")
print("===========================")

for x in open:
    print("Executing | " + x)
    os.startfile(x)
    printProgressBar(0, delay, prefix = 'Progress:', suffix = 'Complete', length = 50)
    for i in range(delay):
        printProgressBar(i + 1, delay, prefix = 'Progress:', suffix = 'Complete', length = 50)
        time.sleep(1)

input("Startup Compleated, Press ENTER to Exit.")

exit()