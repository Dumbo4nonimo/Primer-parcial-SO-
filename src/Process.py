class Process:
    def __init__(self, etiqueta, burstTime, arrivalTime, queue, priority):
        self.etiqueta = etiqueta
        self.burstTime = burstTime
        self.arrivalTime = arrivalTime
        self.queue = queue
        self.priority = priority

    def __repr__(self): #Metodo de representacion, permite ver a los objetos mas legiblemente
        return f"Process({self.etiqueta}, {self.burstTime}, {self.arrivalTime}, {self.queue}, {self.priority})"




