class InputDataReader():
 
    def readFile(self):
        file1 = open('Data/InputNumbers.txt', 'r') 
        Lines = file1.readlines() 

        values = []
        for line in Lines: 
            values.append(line.strip())
        return values


