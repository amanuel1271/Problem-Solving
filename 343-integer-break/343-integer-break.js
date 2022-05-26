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
        
        let maxx = 1;
        for(let num1 = 1;num1 <= Math.floor(n/2);num1++){
            const num2 = n - num1;
            let break1 = 0;
            let break2 = 0;
            
            if (num1 <= 3){
                break1 = num1;
            }
            else{
                if (num1 in ans){
                    break1 = ans[num1];
                }
                else{
                    ans[num1] = helper(num1);
                    break1 = ans[num1];
                }
                    
            }
            if (num2 <= 3){
                break2 = num2;
            }
            else{
                if (num2 in ans){
                    break2 = ans[num2];
                }
                else{
                    ans[num2] = helper(num2);
                    break2 = ans[num2];
                }
                    
            }
            maxx = Math.max(maxx,break1 * break2);
        }
        
        ans[n] = maxx;
        return ans[n];
    };
    
    return helper(n);
    
};