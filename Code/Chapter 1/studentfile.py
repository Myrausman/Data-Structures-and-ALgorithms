class StudentFileReader:
    def __init__(self, inputSrc):
        self._inputSrc = inputSrc
        self._inputFile = None

    def open(self):
        self._inputFile = open(self._inputSrc, "r")

    def close(self):
        self._inputFile.close()
        self._inputFile = None

    def fetchAll(self):
        theRecords = list()
        student = self.fetchRecord()
        while student != None:
            theRecords.append(student)
            student = self.fetchRecord()
        return theRecords

    def fetchRecord(self):
        line = self._inputFile.readline()
        if line=="":
            return None
        student = StudentRecord()
        student.idNum = int(line)
        student.firstName = self._inputFile.readline().rstrip()
        student.lastName = self._inputFile.readline().rstrip()
        student.classCode = int(self._inputFile.readline())
        student.gpa = float(self._inputFile.readline())
        return student

    def fetchAllRecordCSV(self):
        theRecords = list()
        student = self.fetchRecordCSV()
        while student != None:
            theRecords.append(student)
            student = self.fetchRecordCSV()
        return theRecords


    def fetchRecordCSV(self):
        line = self._inputFile.readline()
        if line == "":
            return None
        line= line.strip().split(',')
        student = StudentRecord()
        student.idNum = int(line[0])
        student.firstName = line[1]
        student.lastName = line[2]
        student.classCode = int(line[3])
        student.gpa = float(line[4])
        return student




class StudentRecord:
    def __init__(self):
        self.idNum = 0
        self.firstName = None
        self.lastName = None
        self.classCode = 0
        self.gpa = 0.0
