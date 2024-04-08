import heapq
li = [10,9,4,1,2,5,17,4,20,3,1]
heapq.heapify(li)
print(li)

print(heapq.heappop(li))

heapq.heappush(li, 7)
print(li)

heapq._heapify_max(li)
print(li)
