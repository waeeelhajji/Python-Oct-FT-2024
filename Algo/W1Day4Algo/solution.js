/**
 * - Time: O(n/2) -> O(n) linear.
 * - Space: O(1) constant.
 * @param {string} str
 * @returns {boolean}
 */
function isPalindrome(str = "") {
    for (var i = 0; i < Math.floor(str.length / 2); i++) {
        // Looping inwards from both sides.
        var leftChar = str[i];
        var rightChar = str[str.length - 1 - i];

        if (leftChar !== rightChar) {
            return false; // early exit
        }
    }
    return true;
}

/**
 * - Time: O(3n) -> O(n) linear. Each method used is looping.
 * - Space: O(2n) linear. Split and join both create a copy.
 * @param {string} str
 * @returns {boolean}
 */