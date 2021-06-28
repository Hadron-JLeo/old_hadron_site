import browser
import shards

""" STATIC """
calc_btn = browser.document.getElementById("calc_btn")
calc_btn2 = browser.document.getElementById("calc_btn2")
my_display = browser.document.getElementById("needed_shards_display")
display_text = my_display.text #"The amount of shards needed: "

""" UTILITY METHODS ---------------------------------------"""
def get_field_val(field_id:str):
    """ Get value of field. Para: id(str)"""
    return browser.document.getElementById(field_id).value

def refresh_values(option=1):
    """ Get current values from input fields. No Para."""
    tier = "tier_input"
    lvl = "cur_level"
    rem = "remaining_shards"

    if option == 1:
        pass
    elif option == 2:
        tier = "my_input"
        lvl = "cur_level2"
        rem = "remaining_shards2"
    else:
        print("problem")

    next_tier = get_field_val(tier)
    cur_level = get_field_val(lvl)
    remaining_shards = get_field_val(rem)

    return next_tier, cur_level, remaining_shards

def nullify(val):
    if (val == None):
        val = 0
    return int(val)

""" UTILITY METHODS END -----------------------------------"""

def main(ev):
    """ Para used to identify as event """
    next_tier, cur_level, remaining_shards = str(refresh_values(1)[0]).upper, refresh_values(1)[1], refresh_values(1)[2]
    cur_level = nullify(cur_level)
    remaining_shards = nullify(remaining_shards)
    res=str(shards.calculate_remaining_shards(next_tier, cur_level, remaining_shards))

    my_display.text = display_text + " " + res
    #browser.alert(res)

def max_tier(ev):
    """ Will calculate shards remaining till max tier (SSS+) """
    next_tier, cur_level, remaining_shards = str(refresh_values(2)[0]).upper(), refresh_values(2)[1], refresh_values(2)[2]
    cur_level = nullify(cur_level)
    remaining_shards = nullify(remaining_shards)

    res=str(shards.calculate_shards_till_max(next_tier, cur_level, remaining_shards))
    my_display.text = display_text + " " + res

#output(next_tier)
#output(shards.calculate_shards_till_max('S', 10, 0))

calc_btn.bind("click", main)
calc_btn2.bind("click", max_tier)
