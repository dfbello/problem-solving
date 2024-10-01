/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    let r = 1;
    let k = 0;
    
    while (r < nums.length){
        
        if (nums[k] === nums[r]){
            r++;
        }else{
            k++;
            nums[k] = nums[r];
        }
    }
    
    return k + 1;
    
};


let num = [0,0,1,1,1,2,2,3,3,3,4];
console.log(removeDuplicates(num));
console.log(num);

