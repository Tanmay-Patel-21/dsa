/*
You are given a number of steps (n), you can climb the steps one or two at a time ,
you have to find total number of ways in which you can climb all the steps

Example input 1: 2
Example output 1: 2
Explaination: We can climb the stairs in following possible ways:
1 1
2

Example input 1: 5
Example output 1: 8
Explaination: We can climb the stairs in following possible ways:
1 1 1 1 1
2 1 1 1
1 2 1 1
1 1 2 1
1 1 1 2
1 2 2
2 1 2
2 2 1
*/

function getTotWayToClimbSteps(n) {
  let totWays = 1;
  let noTwo = Math.floor(n / 2);
  while (noTwo > 0) {
    let noOne = n - noTwo * 2;
    totWays += noTwo * noOne + 1;
    noTwo--;
  }
  return totWays;
}

console.log(getTotWayToClimbSteps(10));
