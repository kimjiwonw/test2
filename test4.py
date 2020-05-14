
def print_pri(m,priority):
    index=m
    max_num=max(priority)
    answer=0

    while True:
        temp = priority.pop(0) 
        if temp < max_num:
            if index ==0: 
                priority.append(temp) 
                index = len(priority)-1 
            else: 
                priority.append(temp) 
                index -= 1 
                            
        else:  
            if index ==0:
                answer += 1
                break  
            
            index -= 1  
            answer +=1  
            max_num=max(priority)
    return answer 

n=int(input("작업 수 : "))
m=int(input("작업 번호 : "))
priority= list(map(int,input("작업 우선순위 : ").split()))
print(print_pri(m,priority),"분")