#sumabc = []
#for a in range(1,50):# assume child < 50
#    for b in range(1,50):
#        for c in range(1,50):
#            if(a * b * c == 36):
#                abc = [a,b,c]
#                abc.sort()
#                sumabc.append([a + b + c,abc])
#d = dict()
#for k,x in sumabc:
#    if(k in d):
#        if(x not in d[k]):
#            d[k].append(x)
#    else:
#        d[k] = [x]

#for k in d.keys():
#    if(len(d[k]) > 1):
#        print(k,d[k])

 #in result, there's only one a,b,c
 #that has at least 2 combinations

import sys
def calcs(t):
    #formula: v0t + 1/2 a t^2
    # v0 = 1, a = 2
    return t + t * t

inputstr = input('numbers seprated by space :')
nums = inputstr.split(" ")
#convert to int
nums = [int(i) for i in nums]
t = nums[0] # first number as T
# remaining number as time
for i in range(1,t + 1):
    s = calcs(nums[i])
    sys.stdout.write(str(s) + ' ')

#inputstr = '2 1 2'#input('numbers seprated by space :')


#inputstr = input('numbers seprated by , :')
#nums = inputstr.split(",")
#nums = [float(i) for i in nums]
#print('original:')
#print(nums)
#nums.remove(max(nums))
#nums.remove(min(nums))
#print('removed min max:')
#print(nums)
#print('ave:')
#print(sum(nums) / float(len(nums)))