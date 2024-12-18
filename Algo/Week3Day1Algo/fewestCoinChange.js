/* 
  Given an int to represent how much change is needed
  calculate the fewest number of coins needed to create that change,
  using the standard US denominations

-*****Cent
1¢	penny

-*****Five cents
5¢	nickel

-*****Ten cents
10¢	dime

-*****Quarter dollar
25¢	quarte


*/

var cents1 = 25;
var expected1 = { quarter: 1 };

var cents2 = 50;
var expected2 = { quarter: 2 };

var cents3 = 9;
var expected3 = { nickel: 1, penny: 4 };

var cents4 = 99;
var expected4 = { quarter: 3, dime: 2, penny: 4 };

/**
 * Calculates the fewest coins of the standard American denominations needed
 *    to reach the given cents amount.
 * - Time: O(?).
 * - Space: O(?).
 * @param {number} cents
 * @param {string} sick
 * @returns {Object<string, number>} - A denomination table where the keys are
 *    denomination names and the value is the amount of that denomination
 *    needed.
 */
function fewestCoinChange(cents) { }

/*****************************************************************************/