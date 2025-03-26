def solution(places):
    answer = []
    
    for place in places:
        ans = 1
        for i in range(len(place)):
            if ans == 0:
                break
            for j in range(len(place)):
                if place[i][j] == "P":
                    ans = ans and check_single_person(i,j, place)
                    if ans == 0:
                        break
        answer.append(ans)
                    
    return answer

def check_single_person(y,x, place):
    
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    
    levels = [[(y, x)]]
    cnt = 0
    
    while cnt < 2:
        levels.append([])
        if len(levels[-2]) == 0:
            break
        for pos in levels[cnt]:
            cy = pos[0]
            cx = pos[1]
        
            for i in range(len(dx)):
                if cx+dx[i] >= 0 and cy+dy[i] >= 0 and cx+dx[i] < 5 and cy+dy[i] < 5:
                    if cy+dy[i] == y and cx+dx[i] == x:
                        continue
                    if place[cy+dy[i]][cx+dx[i]] == "P":
                        return 0
                    if place[cy+dy[i]][cx+dx[i]] == "O":
                        levels[-1].append((cy+dy[i],cx+dx[i]))
            cnt += 1
    return 1