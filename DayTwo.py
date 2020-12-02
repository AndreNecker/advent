
class DayTwo():

    def is_valid(self, line, partTwo):    
        valid = 0
        if (partTwo == 0):
            count_letter = 0
            for password_letter in line.Password:
                if password_letter == line.Letter:
                    count_letter = count_letter + 1 
            valid = 0
            if count_letter >= line.min and count_letter <= line.max:
                valid = 1
        if (partTwo == 1):
            if (line.Password[line.min-1] == line.Letter or line.Password[line.max-1] == line.Letter) and line.Password[line.min-1] != line.Password[line.max-1]:
                valid = 1        
        return valid
        

    def read_day_two(self, data, partTwo):
     
        count_valid_passwords = 0
        for line in data:
            valid = self.is_valid(line, partTwo)
            if valid == 1:
                count_valid_passwords = count_valid_passwords + 1
        return count_valid_passwords
           