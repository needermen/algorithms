# time spent 
# 30 minutes

# materials
# https://www.rapidtables.com/convert/number/decimal-to-binary.html

# how to run
# pyhton lesson_1.py

# solution
def solution(N):
    maxCount = 0;
    count = -1;
    while N > 0:
        a = N % 2;
        N = (N - a) / 2;
        if a == 1:
            if maxCount < count:
                maxCount = count;
            count = 0;
        else:
            if count != -1:
                count += 1;  
            
    return maxCount


# printing
print(solution(1041))