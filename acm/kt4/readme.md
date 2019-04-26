1、订单问题
```angular2html
Description

Rahul and Ankit are the only two waiters in Royal Restaurant. Today, the restaurant received N orders. The amount of tips may differ when handled by different waiters, if Rahul takes the ith order, he would be tipped Ai rupees and if Ankit takes this order, the tip would be Bi rupees.In order to maximize the total tip value they decided to distribute the order among themselves. One order will be handled by one person only. Also, due to time constraints Rahul cannot take more than X orders and Ankit cannot take more than Y orders. It is guaranteed that X + Y is greater than or equal to N, which means that all the orders can be handled by either Rahul or Ankit. Find out the maximum possible amount of total tip money after processing all the orders.


Input

• The first line contains one integer, number of test cases.

• The second line contains three integers N, X, Y.

• The third line contains N integers. The ith integer represents Ai.

• The fourth line contains N integers. The ith integer represents Bi.


Output

Print a single integer representing the maximum tip money they would receive.


Sample Input 1 

1
15 3 3
1 2 3 4 5
5 4 3 2 1
Sample Output 1

21
```
2、数组查询
```angular2html
Description

Given an array, the task is to complete the function which finds the maximum sum subarray, where you may remove atmost one element to get the maximum sum.


Input

第一行为测试用例个数T；后面每两行表示一个用例，第一行为用例中数组长度N，第二行为数组具体内容。


Output

每一行表示对应用例的结果。


Sample Input 1 

1
5
1 2 3 -4 5
Sample Output 1

11
Hint

例如，对一个数组A[] = {1, 2, 3, -4, 5}，要移除-4得到最大和的子数组，和为11.

```
3、按照要求保留数组元素使得和最大
```angular2html
Description

Given an array of N numbers, we need to maximize the sum of selected numbers. At each step, you need to select a number Ai, delete one occurrence of Ai-1 (if exists) and Ai each from the array. Repeat these steps until the array gets empty. The problem is to maximize the sum of selected numbers. 必须从大到小选择元素。


Input

The first line of the input contains T denoting the number of the test cases. For each test case, the first line contains an integer n denoting the size of the array. Next line contains n space separated integers denoting the elements of the array. 数组元素已经按照从小到大顺序排列。


Output

For each test case, the output is an integer displaying the maximum sum of selected numbers.


Sample Input 1 

1
3
1 2 3
Sample Output 1

4
```
4、生活日常之蔬菜购买
```angular2html
Description

Rahul wanted to purchase vegetables mainly brinjal, carrot and tomato. There are N different vegetable sellers in a line. Each vegetable seller sells all three vegetable items, but at different prices. Rahul, obsessed by his nature to spend optimally, decided not to purchase same vegetable from adjacent shops. Also, Rahul will purchase exactly one type of vegetable item (only 1 kg) from one shop. Rahul wishes to spend minimum money buying vegetables using this strategy. Help Rahul determine the minimum money he will spend.


Input

First line indicates number of test cases T. Each test case in its first line contains N denoting the number of vegetable sellers in Vegetable Market. Then each of next N lines contains three space separated integers denoting cost of brinjal, carrot and tomato per kg with that particular vegetable seller.


Output

For each test case, output the minimum cost of shopping taking the mentioned conditions into account in a separate line.

Constraints:1 <= T <= 101 <= N <= 100000 Cost of each vegetable(brinjal/carrot/tomato) per kg does not exceed 10^4


Sample Input 1 

1
3
1 50 50
50 50 50
1 50 50
Sample Output 1

52
```