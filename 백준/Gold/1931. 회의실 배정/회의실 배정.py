#참고 https://st-lab.tistory.com/145
N=int(input())

meeting=[]

for i in range(N): 
    start, end = map(int,input().split())
    meeting.append((start,end))

meeting.sort(key=lambda x:(x[1],x[0])) #종료 시간순으로 오름차순, 같으면 시작시간 순으로 오름차순

count=0
time=0
for (start,end) in meeting:
    if start>=time: # 만약 이전 end time이 현재 start 타임보다 작으면 (회의시간이 겹치지 않으면)
        count+=1
        time=end

print(count)

