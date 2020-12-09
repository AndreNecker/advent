

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


    def read_day_five(self):
        file1 = open('Data/InputDayFive.txt', 'r') 
        Lines = file1.readlines()
        seats = []
        for line in Lines:
            line_stripped = line.strip()
            line_stripped = line_stripped.replace('F', '0').replace('B', '1').replace('R', '1').replace('L', '0')
            seats.append([line_stripped[:7], line_stripped[-3:] ] )
        return seats

    def read_day_six_per_group(self):
        file1 = open('Data/InputDaySix.txt', 'r') 
        Lines = file1.readlines()
        votes = []
        vote_group = ''
        for line in Lines:
            line_stripped = line.strip()
            if (len(line_stripped) == 0):
                votes.append(vote_group)
                vote_group = ''
            vote_group = vote_group + line_stripped
        if (len(vote_group) > 0):
            votes.append(vote_group)
        return votes

        
    def read_day_six_per_person_per_group(self):
        file1 = open('Data/InputDaySix.txt', 'r') 
        Lines = file1.readlines()
        votes = []
        vote_group = []
        for line in Lines:
            line_stripped = line.strip()
            if (len(line_stripped) == 0 and len(vote_group)):
                votes.append(vote_group)
                vote_group = []
            if (len(line_stripped) > 0):
                vote_group.append(line_stripped)
        if (len(vote_group) > 0):
            votes.append(vote_group)
        return votes

    def read_day_seven(self):
        file1 = open('Data/InputDaySeven.txt', 'r') 
        Lines = file1.readlines()
        xx = {}
        for line in Lines:
            line_stripped = line.strip()
            splitted = line_stripped.split()
            if (len(splitted) > 7):
                value = [[splitted[5] + ' ' + splitted[6], int(splitted[4])]]
                if (len(splitted) > 9):
                    value.append([splitted[9] + ' ' + splitted[10], int(splitted[8])])
                if (len(splitted) > 12):
                    value.append([splitted[13] + ' ' + splitted[14], int(splitted[12])])
                if (len(splitted) > 17):
                    value.append([splitted[17] + ' ' + splitted[18], int(splitted[16])])
                if (len(splitted) > 20):
                    value.append([splitted[20] + ' ' + splitted[21], int(splitted[19])])
                xx[splitted[0] + ' ' + splitted[1]] = value
        return xx

    def read_day_eight(self):
        file1 = open('Data/InputDayEight.txt', 'r') 
        Lines = file1.readlines()

        instructions =  [line.split() for line in Lines]
        return instructions

    def read_day_nine(self):
        file1 = open('Data/InputDayNine.txt', 'r') 
        Lines = file1.readlines()

        numbers = [int(line) for line in Lines]
        return numbers



















  
class PasswordData():

    def set_data(self, initLine):
        xx = initLine.split()
        self.Letter = xx[1][0]
        self.Password = xx[2]

        self.min = int(xx[0].split('-')[0])
        self.max = int(xx[0].split('-')[1])
        return self
