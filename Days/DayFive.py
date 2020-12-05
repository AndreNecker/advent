
class DayFive:

    def get_seat_number(self, input):
       
        dict = {}
        highest_numner = 0
        for seat in input:
            row = int(seat[0], 2)
            col = int(seat[1], 2)

            if (row in dict):
                seatedcols = dict[row]
                seatedcols.append(col)
            else:
                seatedcols = []
                seatedcols.append(col)
                dict[row] = seatedcols

            seat_id = (8 * row) + col
           # print('row: ' + str(row) + ' col:' + str(col) + ' seatid:' + str(seat_id))
            if (highest_numner < seat_id):
                highest_numner = seat_id
           #     print(' new highest number: ' + str(highest_numner))
        
        for row in dict:
            print(str(row))
            print(dict[row])
            needed_keys = {0, 1, 2, 3, 4, 5, 6, 7}
            for key in needed_keys:
                if (key not in dict[row]):
                    seat_id = (8 * row) + col
                    print('row: ' + str(row) + ' col:' + str(key) + ' seatid:' + str(seat_id))


        return highest_numner
