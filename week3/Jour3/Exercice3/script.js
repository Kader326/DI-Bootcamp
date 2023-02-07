var select1= document.getElementById("box")
select1.setAttribute('draggable','true');
select1.setAttribute('ondragstart','dragStart(event)');
var select2= document.getElementById("target")
select2.setAttribute('ondrop','dragDrop(event)');
select2.setAttribute("ondragover","allowDrop(event)");
select2.setAttribute("ondragenter","allowDrop(event)");
select2.setAttribute("ondragleave","allowDrop(event)");
function allowDrop(event) {
  event.preventDefault(); 
}

function allowEnter(event) {
  event.target.classList.add('over');
}

function allowLeave(event) {
  event.target.classList.remove('over');
}

function dragStart(event) {
console.log("target:",  event.target)
console.log("box: ",  event.target.id )
event.dataTransfer.setData("text", event.target.id);
}

function dragDrop(event) {

event.preventDefault();
  
let data = event.dataTransfer.getData("text");
console.log("data: ",  data) 
  
let box = document.getElementById(data)
event.target.appendChild(box);
}