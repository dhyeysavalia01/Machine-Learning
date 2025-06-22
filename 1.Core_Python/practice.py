# Practice: Write a mean, median, mode function

from collections import Counter

def MEAN(random_list):
    return (sum(random_list)/len(random_list))

def MEDIAN(random_list):
    sorted_list = sorted(random_list)

    if(len(sorted_list)%2==0):
        temp = sorted_list[len(sorted_list)//2]
        temp2 = sorted_list[(len(sorted_list)//2) - 1]
        avg = (temp + temp2) / 2
        return avg

    else:
        flag = sorted_list[len(sorted_list)//2]
        return flag
    
def MODE(random_list):
     counter_variable = Counter(random_list)
     common = counter_variable.most_common(2)
     return common




    

random_list = [5, 3, 8, 3, 9, 1, 3, 1]
print("mean =",MEAN(random_list))

print("median =",MEDIAN(random_list))

print("mode =",MODE(random_list))