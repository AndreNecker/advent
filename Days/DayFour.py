import re

class DayFour:

    def count_passports(self, passports):
        bla = [passport.split(' ') for passport in passports]
        valid_passport_count = 0
        for xx in bla:
            valueKeys = [x.split(':') for x in xx]
            allKeys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

            passportValid = True
            for neededKey in allKeys:
                found = False
                for valueKey in valueKeys:
                    if (valueKey[0] == neededKey):
                        found = self.data_are_valid(neededKey, valueKey[1])
                        break
                if (found == False):
                    print(neededKey+ ' not found')
                if (found == False):
                    passportValid = False
                    break
            if (passportValid):
                print('Found one')
                valid_passport_count = valid_passport_count + 1
        return valid_passport_count

    def data_are_valid(self, key, value):
        valid = True
        if (key == 'byr'):
            birth_year = int(value)
            valid = birth_year <= 2002 and birth_year >= 1920 
                
        if (key == 'iyr'):
            issuer_year = int(value)
            valid = issuer_year <= 2020 and issuer_year >= 2010
                
        if (key == 'eyr'):
            issuer_year = int(value)
            valid = issuer_year <= 2030 and issuer_year >= 2020
        
        if (key == 'hgt'):
            unit = value[-2:]
            valid = unit == 'cm' or unit == 'in'
            if (valid):
                height = int(value[:-2])
                valid = (unit == 'cm' and height >= 150 and height <= 193) or (unit == 'in' and height >=59 and height <= 76)
        
        if (key == 'hcl'):
           valid = value[0] == '#' and len(value) == 7
        
        if (key == 'ecl'):
            valid_valued = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
            valid = valid_valued.__contains__(value)
        
        if (key == 'pid'):
            regex = '\d\d\d\d\d\d\d\d\d'
            xx = re.match(regex, value)
            valid = False
            if (xx):
                valid = xx.pos == 0 and len(value) == 9
        
        if (valid == False):
            print(key+ ' ' + value)
        return valid

       
    