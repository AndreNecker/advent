class DaySeven:
    
    shiny_gold = 'shiny gold'
    colors_containing_gold = []
    colors_not_containging_gold = []
    
    def count_bags(self, bagsInputsDict):
        count = 0
        for bag in bagsInputsDict:
            if (self.contains_gold(bag, bagsInputsDict)):    
                count  = count + 1
        return count

    def contains_gold(self, bag, bagsInputsDict):
        if (bag in bagsInputsDict):
            bags_in_bag = bagsInputsDict[bag]
            is_valid = False
            for inner_bag in bags_in_bag:
                if (inner_bag[0] == self.shiny_gold):
                    is_valid = True
                else:
                    is_valid = self.contains_gold(inner_bag[0], bagsInputsDict)
                if (is_valid):
                    return True
        return False

    def count_bags_in_gold(self, bagsInputsDict):
        bags_in_gold = bagsInputsDict[self.shiny_gold]
        
        count = self.get_bags_count(bags_in_gold, bagsInputsDict)
        return count

    def get_bags_count(self, bags, bagsInputsDict):
        count = 0
        for inner_bag in bags:
            count = count + inner_bag[1]
            if(inner_bag[0] in bagsInputsDict):
                inner_inner_bags = bagsInputsDict[inner_bag[0]]
                xx = self.get_bags_count(inner_inner_bags, bagsInputsDict)
                count = count + (inner_bag[1] * xx)
            
        return count

