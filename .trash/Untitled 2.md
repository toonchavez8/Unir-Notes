Done in 11.0 minutes 32 seconds! Subtitle is in the outputs folder.

------------------------------------

videoplayback

Welcome to this comprehensive course on data structures and algorithms, whether you are preparing

for coding interviews or looking to strengthen your foundational programming skills, this is a great

course for you. Sheldon Chai developed this course. Sheldon will break down the most essential

data structures, like array, string, sets, hash maps, and heaps, and will show you exactly how

and when to use them. You also master core algorithmic patterns, such as two pointers, sliding

windows, binary search, breadth-first search, depth-first search, and backtracking. I'll explain

with clear examples and real interview problems. This course will help you build your intuition

for efficiency and help you recognize which patterns to apply and how to avoid brute-force solutions.

And each concept is taught step-by-step with practical code walkthroughs and tips for common pitfalls.


Lastly, but not least, we have priority cues, also known as heaps. A priority cue is a

special kind of cue where elements are removed in order of priority, not just in the order they

were added. Under the hood, priority cues are usually implemented as binary heaps, which are

just binary trees stored in arrays. There are two main kinds. For a min heap, every parent is

smaller than its children. For a max heap, every parent is larger than its children. In Python,

the default is a min heap, meaning the smallest element comes out first, but we can easily simulate

a max heap by negating the values. That means insertion and removal both take big O of log N time,

which is fast enough for most real-time scheduling or selection problems. Priority cues show up in

a ton of interview problems, especially when you want to repeatedly extract the smallest or largest

item efficiently. You're maintaining a top K or bottom K set of values. You need real-time ranking,

greedy selection, or dexter style pathfinding. You need to sort on the fly, but don't want to pay

the full big O of N log N cost for sorting the entire array. Priority cues are one of the easiest

implementations, often utilizing simple libraries, so the best way to learn these is to get right

into it now with some practice problems. All right, let's put that heap knowledge to work with

this classic problem, finding the K closest points to the origin. We're given a bunch of points

on a 2D plane, and we want to return the K points that are closest to zero zero, using regular

Euclidean distance. Now remember, since we only care about which points are closest, not the actual

distances, we can just compare the squared distances. That saves us from doing a square root for every

point. Let's walk through the code. First, we import heap pop and heap push from Python's

EPQ module. This gives us a nice way to use a min heap where the smallest elements come out first.

Next, we create an empty heap. We'll use this to keep track of all the points sorted by their

distance to the origin. Now we loop through each point in the input list. For every point,

we calculate its squared distance from the origin. That's just x squared plus y squared.

Then we push a tuple into the heap, the distance first, and the point itself second.

Why do we put the distance first? Because heaps in Python use the first item in the tuple

to figure out the priority, so this makes sure the point with the smallest distance will bubble

up to the top. All right, once we've pushed all the points into the heap, we're ready to grab

the top k. We create a result list, and for k times, we pop the smallest element off the heap.

That gives us the point with the next closest distance each time. We don't care about the distance

anymore, so we just extract the point and add it to our result list, and finally, return the result.

So overall, we're using a priority queue to help us efficiently pull out the k closest points

without having to sort the entire list. The heap makes this fast. Each insertion and removal is

logarithmic, and the code stays simple and readable. All right, let's dive into a classic selection

problem using heaps, finding the Keith largest element in an array. So what are we trying to do here?

We're given an unsorted list of numbers, and we need to find the Keith largest.

Not just the Keith item, but the one that would sit in the Keith spot from the end if we sorted it.

Now, since we just learned about heaps, and especially how fast they are at pulling out the largest

or smallest values, this is a great chance to use them in action. Here's what we're doing.

First up, we take all the numbers and negate them. Why? Because Python's heap implementation is

a min heap by default, meaning it always pops out the smallest value, but we want the largest ones

to come out first. So by flipping the signs, we turn it into a max heap. Once we have our max heap,

we call heapify, which rearranges the list so it satisfies the heap structure.

This step only takes linear time, which is a nice bonus. Now, the Keith largest element will be the

one that comes out after we've removed the largest one, K minus one times. So we pop from the heap,

K minus one times. Each pop gives us the current largest number, and finally, we return the number

at the top of the heap. But don't forget to flip the sign back to get the original value.

That's it. Fast, efficient, and no need to sort the entire array, just a smart use of a heap.

based on this transcript create massfive indepth notes provding code examples both in python and in javascript for the algorithims mentioned