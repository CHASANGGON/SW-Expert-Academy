# 1. 그래프를 코드로 표현
# 연결 리스트 - 구현이 어려움..
# 인접 행렬
# 인접 리스트

# 인접 행렬
# - V * V 배열을 활용해서 표현
# - 갈 수 없다면 0, 있다면 1(가중치) 을 저장
# 장점
# - 노드간의 연결 정보를 한 방에 확인 가능
# - 행렬곱을 이용해서 탐색이 쉽게 가능하다!
# - 간선이 많을 수록 유리
# 단점
# - 노드 수가 커지면 메모리가 낭비된다
# - 연결이 안 된 것도 저장
#   -> 노드 수 + 메모리 제한 반드시 확인할 것!

graph = [
    [0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1],
    [0, 1, 0, 0, 0],
    [1, 0, 0, 0, 1],
    [0, 1, 0, 1, 0],
]
# 인접 리스트 (조금 더 권장)
# - V개의 노드가 갈 수 있는 정보만 저장
# 장점
# - 메모리 사용량이 적다
# - 탐색할 때 갈 수 있는 곳만 확인하기 때문에 시간적으로 효율
# 단점
# - 연결 여부를 확인하는 데 시간이 더 걸림

graph = [
    [1, 3],
    [0, 2, 4],
    [1],
    [0, 4],
    [1, 3],
]