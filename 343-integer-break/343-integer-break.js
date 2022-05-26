/**
 * @param {number} n
 * @return {number}
 */
var integerBreak = function(n) {

    const ans = {};
    
    
    const helper = (n) => {
        if (n in ans){
            return ans[n];
        }
        if (n === 2){
            return 1;
        }
        else if (n === 3){
            return 2;
        }
        
        const fetchCached = n => {
            let res = 0;
            if (n in ans){
                res = ans[n];
            }
            else{
                ans[n] = helper(n);
                res = ans[n];
            }
            return res;  
        };
        
        let maxPossible = 1;
        for(let num1 = 1;num1 <= Math.floor(n/2);num1++){
            const num2 = n - num1;
            let break1 = 0;
            let break2 = 0;
            
            break1 = (num1 <= 3)? num1:fetchCached(num1);
            break2 = (num2 <= 3)? num2:fetchCached(num2);
            maxPossible = Math.max(maxPossible,break1 * break2);
        }
        ans[n] = maxPossible;
        return ans[n];
    };
    
    return helper(n);
    
};