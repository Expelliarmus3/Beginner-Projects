import random
import time

operator=['+','-','*']
max_operand=12
min_operand=3

def generate_ques():
    opr= random.choice(operator)
    right_oper= random.randint(min_operand,max_operand)
    left_oper= random.randint(min_operand,max_operand)
    ques= str(left_oper)+" "+opr+" "+str(right_oper)
    ans= eval(ques)
    return ques,ans

wrong=0
input("Press enter to start")
print("---------------------")
start_time= time.time()

for i in range(10):
    expr,ans=generate_ques()
    while True:
        guess=input("#"+ str(i+1)+" "+expr+": ")
        if guess== str(ans):
            break
        wrong+=1

end_time= time.time()
total_time= round(end_time-start_time)

print("Woohoo You completed the challenge in",total_time,"seconds")