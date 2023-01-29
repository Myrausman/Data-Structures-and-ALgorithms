class StudentFileReader:
    def __init__(self, inputSrc):
        self._inputSrc = inputSrc
        self._inputFile = None
    def open(self):
        self._inputFile = open(self._inputSrc,"r")
    def close(self):
        self._inputFile.close()
        self._inputFile=None
    def fetchRecord(self):
        line=self._inputFile.readline().strip()
        if line =="":
            return None
        line=line.split(',')
        student=StudentRecord()
        student.idNum =int (line[0])
        student.firstName= line[1]
        student.lastName=line[2]
        student.classCode=int(line[3])
        student.gpa=float(line[4])

        return student.getRecord()
    def fetchAll(self):
        records = list()
        student = self.fetchRecord()
        while student != None:
            records.append(student)
            student = self.fetchRecord()
        return records
        
class StudentRecord:
    def __init__(self):
        self.idNum = 0
        self.firstName = None
        self.lastName = None
        self.classCode = 0
        self.gpa = 0.0
    # def getRecord(self):
    #     return [self.idNum,self.firstName ,self.lastName ,self.classCode ,self.gpa]
file="students.txt"
# fileopen=open("students.txt","r")
# print(fileopen.readlines())
record=StudentFileReader(file)
record.open()

print(record.fetchAll())        