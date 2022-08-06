/**
 * @param {number[]} nums
 * @return {number}
 */
var findMaxConsecutiveOnes = function(nums) {
    let max_cnt = 0;
    let cnt = 0;
    
    for (let i = 0;i < nums.length;i++){
        if (nums[i] === 0){
            cnt = 0;
            continue;
        }
        cnt++;
        max_cnt = Math.max(max_cnt,cnt)
    }
    
    return max_cnt
};