/* 
  Given an array of integers
  return the first integer from the array that is not repeated anywhere else

  If there are multiple non-repeated integers in the array,
  the "first" one will be the one with the lowest index.
*/

var nums1 = [3, 5, 4, 3, 4, 6, 5];
var expected1 = 6;

var nums2 = [3, 5, 5];
var expected2 = 3;

var nums3 = [3, 3, 5];
var expected3 = 5;

var nums4 = [5];
var expected4 = 5;

var nums5 = [];
var expected5 = null;

/**
 * Finds the first int from the given array that has no duplicates. I.e., the
 *    item at the lowest index that doesn't appear again in the given array.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} nums
 * @returns {number|null} The first int value from the given array that has no
 *    dupes or null if there is none.
 */
function firstNonRepeated(nums) { }

/*****************************************************************************/