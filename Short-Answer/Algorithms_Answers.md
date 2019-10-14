#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a)For the first one, it has 1 while loop, which means it's performing 1 operation for n things. This makes it O(n)

b)This one has nested loops, which is a first sign of 0(n^2)
for n things, it runs the for loop, and while j < n, j \*= 2
You're doing 0(n) for the first loop, 0(n) for the second, so O(n^2) for all of it

c)This function has recursion, so it's a bit up in the air for me. But I think it's only being called n times, and even
at the n-1 call, that's still just a finite n amount of times. So I think this one is linear too, or 0(n)

## Exercise II

Finding a value (f) in a list of floors, knowing that floors > f will break the egg, and egg will be safe on floors < f
This sounds almost like a binary search problem, so I would implement that here
Binary searches are requrired to be a sorted list to work, but since this is a metaphorical building, it would
already be sorted from floor 1 -> floor x (whatever it goes to)
so the list would look something like: floors = [1 , 2, 3, 4, 5, 6, 7, 8, 9]
Using this list, we can run a binary search off it and minimize dropping eggs.
This is a little different then a binary search though, becuase the first floor we find where the egg doesn't break isn't
necessarily the correct answer. Higher floors than that could have the egg intact, too.
So, we're gonna create a variable called highest_nobreak to hold our highest value where the egg did not break
Take the floors array, and find a mid
mid = len(floors) // 2
First things first, drop that egg at the mid floor and see if you got lucky.
if mid == nobreak then highest_nobreak now equals mid
no we can take all the floors higher than the mid, find the mid of those, and drop there
higherFloors = [mid:] this will give us all the higher floors
newMid = len(higherFloors) // 2
and repeat the drop
if newMid == nobreak, then highest_nobreak = newMid.
if it did break, then we know it's got to be in the middle ground. So it's the bottom half of the higherFloors arr
Split that in half, lowerFloors = [:mid] and do the tests there. Keep doing this until you find where it doesn't break, right before it does!

EX
floors = [1, 2, 3, 4, 5, 6, 7, 8, 9]
1st: find mid (5)
drop from mid(5) and see if it breaks.
Did it break?
YES: then half floors less than the mid(5)
Now we have floors = [1, 2, 3, 4,] which the mid is 2
Did it break at 2?
NO: then it's 3 or 4, so take that floors = [3, 4] 2 / 2 =1
now we have mid(4) did it break? No! that's your floor. Yes? then 3 is your floor!

Time Complexity:
The time complexity of this will be that of a binary search, so O(logn) since we're halfing our data every time.
