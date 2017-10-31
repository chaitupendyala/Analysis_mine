import time
previous_category = ''
overall_switching=0
old_rate = 0
threshold = .3
start_time = None
number_of_switches = 0.0
def switch(visit_time,category):
    total_time = 0.0
    if previous_category.upper() != category.upper():
        previous_category = category
        number_of_switches+=1
        old_rate = overall_switching
        overall_switching = (1/number_of_switches)
        if overall_switching > threshold:
            threshold += .001
            return [overall_switching,"Switch To Internal"]
        else:
            if overall_switching < old_rate:
                threshold -= (old_rate - overall_switching)
            return [overall_switching,"Switch To Internal"]
    else:    
        return [overall_switching,"Switch To Internal"]
