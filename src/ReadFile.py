from Process import Process

class ReadFile:
    @staticmethod
    def inputFile(fileName):
        processes = []
        with open(fileName, 'r') as archivo:
            for line in archivo:
                datos = line.strip().split(';')  #Separar por punto y coma
                
                #Asignación de los datos del archivo
                etiqueta = datos[0]
                burstTime = int(datos[1])
                arrivalTime = int(datos[2])
                queue = int(datos[3])
                priority = int(datos[4])

                #Creación de los procesos
                process = Process(etiqueta, burstTime, arrivalTime, queue, priority)
                processes.append(process)
                
        return processes

