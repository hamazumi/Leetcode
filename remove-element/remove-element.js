/**
 * @param {number[]} nums
 * @param {number} val
 * @return {number}
 */
var removeElement = function(nums, val) {
    var i = 0;
    var len = nums.length;
    
    while (i < len) {
        if (nums[i] === val) {
            // remove number from list
            nums.splice(i, 1);
            // adjust list length
            // (could also set len = nums.length)
            len--;
        } else {
            // only increment index if
            // number is not a match
            i++;
        }
    }
    
    return len;
};