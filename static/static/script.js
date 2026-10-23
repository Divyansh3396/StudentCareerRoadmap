function showLoading(){
document.getElementById("loader").style.display="block";
}

function hideLoading(){
document.getElementById("loader").style.display="none";
}

window.onload=function(){
hideLoading();
}

function confirmSubmit(){
return confirm("Are you sure you want to submit?");
}