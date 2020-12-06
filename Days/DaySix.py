class DaySix:

    def get_number_of_votes(self, groups):        
        count_votes_per_group = []
        for group in groups:
            group_votes = []
            for vote in group:
                if (vote not in group_votes):
                    group_votes.append(vote)
            count_votes_per_group.append(len(group_votes))
        
        count = 0
        for group_count in count_votes_per_group:
            count = count + group_count
        return count
    
    def get_number_of_votes_per_group(self, groups):
        count_votes_per_group = []
        for group in groups:
            votes_in_all_groups = []
            for vote in group:
                if (len(votes_in_all_groups) == 0):
                    votes_in_all_groups = list(vote)
                else:
                    for yet_common_vote in votes_in_all_groups.copy():
                        if (yet_common_vote not in vote):
                            votes_in_all_groups.remove(yet_common_vote)
                    if(len(votes_in_all_groups)==0):
                        break
            count_votes_per_group.append(len(votes_in_all_groups))

        
        count = 0
        for group_count in count_votes_per_group:
            count = count + group_count
        return count

