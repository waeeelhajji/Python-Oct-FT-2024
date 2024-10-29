/**
 * Converts the given arrays of keys and values into an object.
 * - Time: O(n) linear, because 1 loop to access elements from both arrays.
 * - Space: O(n).
 * @param {Array<string>} keys
 * @param {Array<any>} values
 * @returns {Object} The object with the given keys and values.
 */
function zipArraysIntoMap(keys = [], values = []) {
    var hashMap = {};

    for (var i = 0; i < keys.length; i++) {
        var key = keys[i];
        var val = values[i];

        hashMap[key] = val;
    }
    return hashMap;
}