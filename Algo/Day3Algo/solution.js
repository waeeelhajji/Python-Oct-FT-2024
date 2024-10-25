/**
 * - Time: O(n) linear.
 * - Space: O(n) linear.
 * @param {Array<string|number|boolean>} arr
 * @param {string} separator
 * @returns {string}
 */
function join(arr = [], separator = ", ") {
    var joined = "";

    if (!arr.length) {
        return joined;
    }

    // less than arr.length - 1 to stop before last
    for (var i = 0; i < arr.length - 1; i++) {
        joined += arr[i] + separator;
    }
    return joined + arr[arr.length - 1];
}

/**
 * - Time: O(n) linear.
 * - Space: O(n) linear.
 * @param {Array<string|number|boolean>} arr
 * @param {string} separator
 * @returns {string}
 */
function join2(arr = [], separator = ", ") {
    var joined = "";

    if (!arr.length) {
        return joined;
    }

    joined += arr[0];

    for (var i = 1; i < arr.length; i++) {
        // Concatenate separator first to avoid trailing separator
        joined += separator + arr[i];
    }
    return joined;
}

/**
 * - Time: O(n) linear.
 * - Space: O(n) linear.
 * @param {Array<string|number|boolean>} arr
 * @param {string} separator
 * @returns {string}
 */
function join3(arr = [], separator = ", ") {
    var joined = "";

    if (!arr.length) {
        return joined;
    }

    for (var i = 0; i < arr.length; i++) {
        var elem = arr[i];

        joined += i === arr.length - 1 ? elem : elem + separator;

        // without ternary
        // if (i === arr.length - 1) {
        //   joined += elem;
        // } else {
        //   joined += elem + separator;
        // }
    }
    return joined;
}
