T = int(input())

for test_case in range(1,T+1):
    n = int(input())
    
    maze = [list(input()) for _ in range(n)] # list로 만들어야 나중에 수정 가능
    
    # 출발 도착 위치 찾기
    start_end = []
    for i in range(n):
        for j in range(n):
            if maze[i][j] == '3':
                start_end.append([i,j])
            elif maze[i][j] == '2':
                start_end.append([i,j])
                
    di = [1,-1,0,0]
    dj = [0,0,1,-1]
    result = 0
    stack = [start_end[0]]
    while stack:
        r,c = stack.pop()
        
        for k in range(4):    
            if 0 <= r+di[k] < n and 0 <= c+dj[k] < n:
                if maze[r+di[k]][c+dj[k]] == '0':
                    stack.append((r+di[k],c+dj[k]))
                    maze[r+di[k]][c+dj[k]] = '1'
                elif maze[r+di[k]][c+dj[k]] == '2':
                    result = 1
                    stack = []
                    break
    
    print(f'#{test_case} {result}')