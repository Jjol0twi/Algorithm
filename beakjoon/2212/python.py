import sys
input = sys.stdin.readline

n = int(input())    # 센서 개수 입력
k = int(input())    # 집중국 개수 입력
sensors = sorted(set(map(int, input().split())))    # 센서 위치 좌표 입력/정렬 오름차순 + 중복 제거
if len(sensors) <= k:   # 집중국 개수보다 센서 개수가 적으면 최소 거리의 합은 0
    print(0)
    exit()
sensor_distances = sorted([sensors[i+1]-sensors[i] for i in range(len(sensors)-1)])     # 센서 간의 거리
print(sum(sensor_distances[:len(sensor_distances) - (k-1)]))    # k개의 집중국 거리 제외 나머지 거리들의 합
