var updateBtns = document.getElementsByClassName('update-cart')

for (i = 0; i < updateBtns.length; i++) {
	updateBtns[i].addEventListener('click', function(){
		var productId = this.dataset.product
		var action = this.dataset.action
		console.log('productId:', productId, 'Action:', action)
		console.log('USER:', user)

        addCookieItem(productId, action)
	})
}

function addCookieItem(productId, action){
	console.log('User is not authenticated')
	
	if(productId == 'undefined'){
		console.log('Product Id is undefined')

	}
	else {
		if (action == 'add'){
			if (cart[productId] == undefined){
				cart[productId] = {'quantity':1}
	
			}else{
				cart[productId]['quantity'] += 1
			}
		}
	
		if (action=="subtract"){
			cart[productId]['quantity'] -= 1
	
			if (cart[productId]['quantity'] <= 0){
				console.log('Item should be deleted')
				delete cart[productId];
			}
		}
	
		if (action == 'remove'){
			delete cart[productId];
		}
		
		console.log('CART:', cart)
		document.cookie ='cart=' + JSON.stringify(cart) + ";domain=;path=/"
	
		location.reload()
	}
}