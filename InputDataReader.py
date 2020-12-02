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
  