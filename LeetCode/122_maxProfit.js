
var maxProfit = function(prices){
	let profit = 0;
	
	let i = 0;
	while (i < prices.length - 1){
		let dayprofit = prices[i+1] - prices[i];
		if (dayprofit < 0){
			i++;
		}else{
			profit += dayprofit;
			i++;
		}

	}


	return profit;
};


let priceArr = [7,1,5,3,2,6,4];


console.log(maxProfit(priceArr), priceArr);
