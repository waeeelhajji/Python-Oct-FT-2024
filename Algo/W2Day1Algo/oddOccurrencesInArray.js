// https://app.codility.com/programmers/lessons/2-arrays/odd_occurrences_in_array/

/* 
Given a non-empty array of odd length containing ints where every int but one
has a matching pair (another int that is the same)
return the only int that has no matching pair.
*/

var nums1 = [1];
var expected1 = 1;

var nums2 = [5, 4, 5];
var expected2 = 4;

var nums3 = [5, 4, 3, 4, 3, 4, 5];
var expected3 = 4; // there is a pair of 4s but one 4 has no pair.

var nums4 = [5, 2, 6, 2, 3, 1, 6, 3, 2, 5, 2];
var expected4 = 1;

function oddOccurrencesInArray(nums) { }

console.log(oddOccurrencesInArray(nums1), "should equal", expected1);
console.log(oddOccurrencesInArray(nums2), "should equal", expected2);
console.log(oddOccurrencesInArray(nums3), "should equal", expected3);
console.log(oddOccurrencesInArray(nums4), "should equal", expected4);

/*****************************************************************************/