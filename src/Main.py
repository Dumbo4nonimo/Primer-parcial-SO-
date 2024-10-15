from Process import Process
from ReadFile import ReadFile


def printProcesses(processes):
    for process in processes:
        print(process)


def main():
    processes = []
    processes = ReadFile.inputFile("inputs/mlq001.txt") #Se reciben los procesos

    printProcesses(processes)

if __name__ == "__main__":
    main()



