

var button = document.querySelector("#submit_input");
button.addEventListener("click",updateItem);

// alert('hi');

function updateItem(){
	var form = document.querySelector("#form_submit");
	var output = document.querySelector("#output");
	var str = "";
	output.innerHTML = "";
	for (var i = 0; i<form.length-1; i++){
		str += form[i].value;
	}
	output.innerHTML=str;
}
