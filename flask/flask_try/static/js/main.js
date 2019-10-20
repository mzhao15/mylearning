
var trig = document.getElementsByClassName("mr-2")[0];

trig.addEventListener("click",myFunc);
// console.log("hi");
// alert("hi");

function myFunc(){
	var newvar = document.getElementById("what");
	newvar.innerHTML = this.innerHTML;
}