import collections

my_deque = collections.deque([10, 20, 30, 40, 50])

my_deque.append(60)

print( "The deque after appending at right: " )
print( my_deque )
 
my_deque.appendleft(70)
print( "The deque after appending at left: " )
print( my_deque )

my_deque.pop()
print( "The deque after removing from right: " )
print( my_deque )

my_deque.popleft()

print("The deque after removing from left: " )
print( my_deque )
