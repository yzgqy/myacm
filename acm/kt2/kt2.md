1

数学公式

Description

Implement pow(A, B) % C.In other words, given A, B and C, find (A^B)%C


Input

The first line of input consists number of the test cases. The following T lines consist of 3 numbers each separated by a space and in the following order:A B C'A' being the base number, 'B' the exponent (power to the base number) and 'C' the modular.Constraints:1 ≤ T ≤ 70,1 ≤ A ≤ 10^5,1 ≤ B ≤ 10^5,1 ≤ C ≤ 10^5


Output

In each separate line print the modular exponent of the given numbers in the test case.


Sample Input 1 

3
3 2 4
10 9 6
450 768 51

Sample Output 1

1
4
34

2

点的凸包

Description

Convex Hull of a set of points, in 2D plane, is a convex polygon with minimum area such that each point lies either on the boundary of polygon or inside it. Now given a set of points the task is to find the convex hull of points.


Input

The first line of input contains an integer T denoting the no of test cases. Then T test cases follow. Each test case contains an integer N denoting the no of points. Then in the next line are N*2 space separated values denoting the points ie x and y.Constraints:1<=T<=100,1<=N<=100,1<=x,y<=1000


Output

For each test case in a new line print the points x and y of the convex hull separated by a space in sorted order where every pair is separated from the other by a ','. If no convex hull is possible print -1.


Sample Input 1 

2
3
1 2 3 1 5 6
3
1 2 4 4 5 1

Sample Output 1

1 2, 3 1, 5 6
1 2, 4 4, 5 1

3

Searching_1

Description

Dilpreet wants to paint his dog- Buzo's home that has n boards with different lengths[A1, A2,..., An]. He hired k painters for this work and each painter takes 1 unit time to paint 1 unit of the board.The problem is to find the minimum time to get this job done under the constraints that any painter will only paint continuous sections of boards, say board {2, 3, 4} or only board {1} or nothing but not board {2, 4, 5}.

Constraints:1<=T<=100,1<=k<=30,1<=n<=50,1<=A[i]<=500


Input

The first line consists of a single integer T, the number of test cases. For each test case, the first line contains an integer k denoting the number of painters and integer n denoting the number of boards. Next line contains n- space separated integers denoting the size of boards.


Output

For each test case, the output is an integer displaying the minimum time for painting that house.

Sample Input 1 

2
2 4
10 10 10 10
2 4
10 20 30 40

Sample Output 1

20
60


4

Searching_2

Description

Find the count of numbers less than N having exactly 9 divisors

1<=T<=1000,1<=N<=10^12


Input

First Line of Input contains the number of testcases. Only Line of each testcase contains the number of members N in the rival gang.


Output

Print the desired output.


Sample Input 1 

2
40
5

Sample Output 1

1
0