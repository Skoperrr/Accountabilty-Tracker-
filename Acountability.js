document.getElementById('submit').addEventListener("click",async function(){
let Task= document.getElementById("task"); 
let StartDate= document.getElementById("start-date");
let DueDate= document.getElementById("due-date");


if(Task.value=="" || StartDate.value=="" || DueDate.value==""){
    alert("Please fill in all fields.");
    return;
 
}})







