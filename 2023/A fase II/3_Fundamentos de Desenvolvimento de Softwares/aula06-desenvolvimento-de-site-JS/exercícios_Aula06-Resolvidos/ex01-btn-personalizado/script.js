const btn = document.querySelector("#btn");
let quebrado = false;
let contaCliques = 0;

btn.addEventListener("mouseover",()=>{
    if(!quebrado){
        btn.style.background="green";
        btn.style.color="white";
    } 
});

btn.addEventListener("mouseout",()=>{
    if(!quebrado){
        btn.style.background="";
        btn.style.color="black";
    }   
});

btn.addEventListener("click",()=>{
    btn.style.background="yellow";
    contaCliques++;
    if(contaCliques >= 5){
        btn.style.background="red";
        btn.innerHTML="Quebrei";
        quebrado = true;
    }
    
});
