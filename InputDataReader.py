from PasswordData  import PasswordData

class InputDataReader():
 
    def read_day_one(self):
        file1 = open('Data/InputDayOne.txt', 'r') 
        Lines = file1.readlines() 

        values = []
        for line in Lines: 
            values.append(line.strip())
        return values
           

    def read_day_two(self):
        file1 = open('Data/InputDayTwo.txt', 'r') 
        Lines = file1.readlines() 
        xx = [PasswordData().set_data(val) for val in Lines]
        return xx

    def read_day_three(self):
        file1 = open('Data/InputDayThree.txt', 'r') 
        Lines = file1.readlines() 
        boolLines = []

        for line in Lines:
            boolCols = []
            for column in line:
                if (column == '#'):
                    boolCols.append(True)
                if (column == '.'):
                    boolCols.append(False)
            boolLines.append(boolCols)
        return boolLines

    def read_day_four(self):
        file1 = open('Data/InputDayFour.txt', 'r') 
        Lines = file1.readlines() 
        
        passports = []
        passport = ''
        for line in Lines:
            line_stripped = line.strip()
            passport = passport + ' ' + line_stripped

            if (len(line_stripped) == 0):
                passports.append(passport)
                passport = ''

        if (len(passport) > 0):
            passports.append(passport)
        return passports


  