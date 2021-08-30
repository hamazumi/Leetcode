/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var findKthLargest = function(nums, k) {
    let rs = nums.sort(function(a, b){return a - b})
    console.log(rs)
    return rs[nums.length - k ]
    
};
