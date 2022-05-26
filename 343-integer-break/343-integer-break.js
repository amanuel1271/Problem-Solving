/**
 * @param {number} n
 * @return {number}
 */
var integerBreak = function(n) {

    const ans = {};
    const fetchCached = n => {
        if (!(n in ans)){
            ans[n] = helper(n);
        }
        return ans[n];  
    };
    
    const helper = (n) => {
        if (n in ans){
            return ans[n];
        }
        if (n === 2 || n === 3){
            return n-1;
        }
        let maxPossible = 1;
        for(let num1 = 1;num1 <= Math.floor(n/2);num1++){
            let num2 = n - num1;
            let break1 = (num1 <= 3)? num1:fetchCached(num1);
            let break2 = (num2 <= 3)? num2:fetchCached(num2);
            maxPossible = Math.max(maxPossible,break1 * break2);
        }
        ans[n] = maxPossible;
        return ans[n];
    };
    
    return helper(n);
    
};