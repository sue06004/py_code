import sys
input = sys.stdin.readline

def time_sub(time1,time2):
    if int(time2[3:])<int(time1[3:]):
        s=str(int(time2[3:])-int(time1[3:])+60)
        tmp=str(int(time2[:2])-1)
        if len(tmp)==1:
            tmp="0"+tmp
        time2=list(time2)
        time2[:2]=list(tmp)
        time2="".join(time2)
    else:
        s=str(int(time2[3:])-int(time1[3:]))
    m=str(int(time2[:2])-int(time1[:2]))
    res=""
    if len(m)==1:
        res+="0"
    res+=m+":"
    if len(s)==1:
        res+="0"
    res+=s
    return res

def time_plus(time1,time2):
    m=int(time1[:2])+int(time2[:2])
    s=int(time1[3:])+int(time2[3:])
    if s>=60:
        s-=60
        m+=1
    if m>=10:
        m=str(m)
    else:
        m="0"+str(m)
    if s>=10:
        s=str(s)
    else:
        s="0"+str(s)
    return m+":"+s
N=int(input())
score_1,score_2=0,0
tmp=0
win_team=0
win_time_1,win_time_2="00:00","00:00"
team,time="",""
for _ in range(N):
    team,time=input().split()
    if team=="1":
        score_1+=1
    elif team=="2":
        score_2+=1
    if score_1==score_2:
        if team=="1":
            win_time_2=time_plus(win_time_2,time_sub(tmp,time))
        elif team=="2":
            win_time_1=time_plus(win_time_1,time_sub(tmp,time))
    elif abs(score_1-score_2)==1:
        if (team=="1" and score_1-1==score_2) or\
            (team=="2" and score_1==score_2-1):
            tmp=time
        
        
if score_1>score_2:
    win_time_1=time_plus(win_time_1,time_sub(tmp,"48:00"))
elif score_1<score_2:
    win_time_2=time_plus(win_time_2,time_sub(tmp,"48:00"))

print(win_time_1)
print(win_time_2)
