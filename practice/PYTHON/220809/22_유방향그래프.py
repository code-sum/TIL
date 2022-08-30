# https://www.notion.so/hphk-edu/22-edea5d6c9e9946c1924dbee716cb9df7

from pprint import pprint
import sys
sys.stdin = open("21_무방향그래프.txt")

# 첫째 줄에 정점의 개수 N과 간선의 개수 M
N, M = map(int, input().split())

# 인접 행렬 만들기
graph = [[0] * (N+1) for _ in range(N+1)]

for _ in range(M):
    v1, v2 = map(int, input().split())
    graph[v1][v2] = 1

pprint(graph)

# 인접 리스트 만들기
graph = [[] for _ in range(N+1)]

for _ in range(M):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)

pprint(graph)