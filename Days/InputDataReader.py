

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



  






















  
class PasswordData():

    def set_data(self, initLine):
        xx = initLine.split()
        self.Letter = xx[1][0]
        self.Password = xx[2]

        self.min = int(xx[0].split('-')[0])
        self.max = int(xx[0].split('-')[1])
        return self
