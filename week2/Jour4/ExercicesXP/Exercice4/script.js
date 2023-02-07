let stock = { 
    "banana": 6, 
    "apple": 0,
    "pear": 12,
    "orange": 32,
    "blueberry":1
}  

let prices = {    
    "banana": 4, 
    "apple": 2, 
    "pear": 1,
    "orange": 1.5,
    "blueberry":10
} 
let shoppingList=["banana","orange","apple"]
function myBill(){
    let prix = 0;
    for(let i of shoppingList)
	{
			if (stock[i] > 0)
			{
				stock[i]=stock[i] - 1;
				console.log("le prix est ", prices[i]);
                console.log("--------------")
                prix += prices[i];
			} 
			else 
			{
				console.log("L'article ", i ,"n'est pas en stock");
			}
     //console.log("Le prix total de votre shoppingList est :"+prix)
	}
}
myBill()