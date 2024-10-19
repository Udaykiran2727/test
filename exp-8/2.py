import heapq

a, b, c = 5, 10, 7

# Use negative values to simulate a max-heap
pq = []
heapq.heappush(pq, (-a, 'a', a))
heapq.heappush(pq, (-b, 'b', b))
heapq.heappush(pq, (-c, 'c', c))

# Pop the greatest element
_, greatest_label, greatest_value = heapq.heappop(pq)

print(f"{greatest_label} is the greatest with a value of {greatest_value}")

# Now you can use the greatest value in further calculations
result = greatest_value * 2  # Example usage
print(f"The greatest value multiplied by 2 is: {result}")
