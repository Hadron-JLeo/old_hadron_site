""" Currently only calculates from one rank to another """


tiers_dict = {
    # Amount of shards needed to upgrade to the next rank
    'SSS+' : 0, # Highest Rank
    'SSS' : (25 * 20),
    'SS' : (16 * 20),
    'S' : (9 * 20),
    'A' : (3 * 20),
    'B' : (0 * 20)
}

tiers_list = list(tiers_dict.keys())

def get_prev_tier(tier):
    """ Get previous tier of input. E.g.: 'A' -> 'B' """
    key_list = tiers_list
    cur_index = (key_list.index(tier) + 1)
    prev_tier = key_list[cur_index] 
    
    return prev_tier


def calculate_remaining_shards(next_tier, cur_level=0, shards_inside=0):
    """ Will calculate remaining shards to next rank"""
    # cur_level = 0-19
    # next_tier = a-sss+
    # cur_tier = b-sss
    # shard_inside : int
    per_level = 20
    
    cur_tier = get_prev_tier(next_tier)
    full_shards = tiers_dict.get(cur_tier)
    

    remaining_shards = full_shards - (int((full_shards/20) * cur_level) + shards_inside)
    return remaining_shards

#res = calculate_remaining_shards('SS', 11, 6)
#print(res)


def calculate_shards_till_max(cur_tier, cur_level, shards_inside):
    rem=0
    temp_level=0
    start_tier=cur_tier
    
    def calc_shards(my_tier, cur_level=0, shards_inside=0):
        """ Will calculate remaining shards to next rank"""
        per_level = 20
    
        cur_tier = my_tier
        full_shards = tiers_dict.get(cur_tier)
    

        remaining_shards = full_shards - (int((full_shards/20) * cur_level) + shards_inside)
        #print(remaining_shards)
        return remaining_shards

    
    for tier in reversed(tiers_list[0:tiers_list.index(cur_tier)+1]):
        #print(tier)
        cur_index = tiers_list.index(start_tier)
        if tier==cur_tier:
            temp_level=cur_level
        else:
            temp_level=0
            
            
        if tiers_list[cur_index]==tiers_list[-1]:
            break
        else:
            rem = rem + calc_shards(start_tier, temp_level)
            if not(tiers_list[cur_index] == tiers_list[-1]):
                start_tier=(tiers_list[cur_index-1])
        #print(rem)
        
        #print(start_tier)
    rem=rem-shards_inside
    return rem

#calculate_shards_till_max('S', 10, 0)



