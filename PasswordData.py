

class PasswordData():

    def set_data(self, initLine):
        xx = initLine.split()
        self.Letter = xx[1][0]
        self.Password = xx[2]

        self.min = int(xx[0].split('-')[0])
        self.max = int(xx[0].split('-')[1])
        return self
