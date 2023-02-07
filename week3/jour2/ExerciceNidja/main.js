//Première partie
//La fonction calculatetip ne prenant aucun paramètre
function  calculateTip(){
	//Création de la variable billAmount
		var billAmount=document.getElementById("billamt").value;
		billAmount=parseInt(billAmount);
		console.log(billAmount)
		//Création de la variable serviceQuality
		var serviceQuality=document.getElementById("serviceQual").value;
		serviceQuality=Number(serviceQuality);
		console.log(serviceQuality)
		//numberOfPeople
		var numberOfPeople=document.getElementById("peopleamt").value;
		numberOfPeople=parseInt(numberOfPeople)
		console.log(numberOfPeople);
		//Les conditions
		if(!billAmount ||serviceQuality===0){
			alert("there are invalids inputs check the bill amount or service quality")
		}else{
			if(!numberOfPeople||numberOfPeople<1){
					numberOfPeople=1;
					console.log(numberOfPeople);		
			}
			var total=((billAmount*serviceQuality)/numberOfPeople);	
			total.toFixed(2)
			console.log(total)
			document.getElementById("totalTip").style.display="block";
			document.getElementById("tip").innerHTML=total;	
		}
	} 

document.getElementById("totalTip").style.display="none"
//Deuxième partie
		document.getElementById("calculate").addEventListener("click",function(event){
		event.preventDefault()
		});
		document.getElementById("calculate").setAttribute("onclick","calculateTip()")


//Exercice 3 : Coordonées de géolocalisation
//Utilisation de tout ce que nous avons appris en classe
var locate=document.getElementById("result");
function geo(){
	if(navigator.geolocation){
		navigator.geolocation.getCurrentPosition(showPosition,showError);
	}else{
		locate.innerHTML="Geolocation is not supported on this browser update it"	
	}
	function showPosition(position){
		locate.innerHTML="Latitude:"+ position.coords.latitude+"<br>Longitude:"+position.coords.longitude;
	}
	function showError(error){
		switch(error.code){
			case error.PERMISSION_DENIED:
				locate.innerHTML="locate denied by user."
				break;
			case error.POSITION_UNAVAILABLE:
				locate.innerHTML="locate info is unavailable."
				break;
			case error.TIMEOUT:
				locate.innerHTML="TimeOUT"
				break;
			case error.UNKNOWN_ERROR:
				locate.innerHTML="Unknown error occur"	
		}
	}
}