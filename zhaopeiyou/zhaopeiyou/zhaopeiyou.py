
for a in range(1,50):
    for b in range(1,50):
        for c in range(1,50):
            if(a * b * c == 36):
                print(a,b,c)

#import sys
#def calcs(t):
#    #return t + 0.5 * 2*t*t
#    return t + t*t

#inputstr = '2 1 2'#input('numbers seprated by space :')
#nums = inputstr.split(" ")
#nums = [int(i) for i in nums]
#n = nums[0]
#for i in range(1,n):
#    s = calcs(nums[i])
#    #print(str(s) + ' ')
#    sys.stdout.write(str(s) + ' ')

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