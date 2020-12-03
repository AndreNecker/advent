class DayThree():

    def count_trees(self, tree_map, addLines, addColumns):
        countedTrees = 0        
        lineCount = 0
        columnCount = 0        
        lengthCols = len(tree_map[0])

        while( len(tree_map) > lineCount):
            if columnCount >= lengthCols:
                columnCount = columnCount - lengthCols

            if (tree_map[lineCount][columnCount]):
                countedTrees = countedTrees + 1
            print ('line ' + str(lineCount) + ' count ' + str(countedTrees) + ' col ' + str(columnCount))
            lineCount = lineCount + addLines
            columnCount = columnCount + addColumns
        return countedTrees
        