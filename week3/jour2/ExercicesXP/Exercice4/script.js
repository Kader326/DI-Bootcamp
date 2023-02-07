var change1=document.body.children[1].children[3];
console.log(change1)
var change2=document.getElementById("radius")

change2.setAttribute("oninput","val()")
function val(){
        change2v=document.getElementById("radius").value;
	console.log(change2v)
	change2.textContent=change2v;
	console.log(change2)
	return change2v;
}
console.log(change2.value);
var changer=document.body.children[1].children[4];
function calc(){
      var value =eval(change2.value*change2.value*change2.value);
	value=(value*4*(3.14))/3
	change1.value=value;
}	
var changer=document.body.children[1].children[4];
document.getElementById("submit").addEventListener("click",function(event){
	event.preventDefault()
});
changer.setAttribute("onclick","calc()")
