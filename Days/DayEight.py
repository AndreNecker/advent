class DayEight:

    nop = 'nop'
    acc = 'acc'
    jmp = 'jmp'

    accumulator = 0
    
    indexes_worked = []


    def Get_Accumulator_executed_twice(self, instructions):
        index = 0

        firstInstruction = instructions[index]
        next_idx = self.get_next_jump(index, firstInstruction)

        correct_termination = False
        while (next_idx not in self.indexes_worked):
            self.indexes_worked.append(next_idx)
            if (next_idx >= len(instructions)):
                correct_termination = True
                print('FOUND SOLUTION: ')
                break
            next_idx = self.get_next_jump(next_idx, instructions[next_idx])        
        return correct_termination

    def get_next_jump(self, index, next_instruction):
        if (next_instruction[0] == self.acc):
            self.accumulator = self.accumulator + int(next_instruction[1].strip('+'))
            index = index + 1
        if (next_instruction[0] == self.jmp):
            index = index + int(next_instruction[1].strip('+'))
        if (next_instruction[0] == self.nop):
            index = index + 1
        return index

    def repair_instructions(self, instructions):
        counter = 0
        for instruction in instructions.copy():
            self.accumulator = 0
            self.indexes_worked = []
            correct = False
            if (instruction[0] == self.nop):
                new_instructions = instructions.copy()
                new_instructions[counter] = [self.jmp, new_instructions[counter][1]]
                correct = self.Get_Accumulator_executed_twice(new_instructions)

            if (instruction[0] == self.jmp):
                new_instructions = instructions.copy()
                new_instructions[counter] = [self.nop, new_instructions[counter][1]]
                correct = self.Get_Accumulator_executed_twice(new_instructions)
            if (correct):
                break
            counter = counter + 1
        return correct
            
