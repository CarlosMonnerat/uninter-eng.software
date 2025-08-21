const campo1 = document.querySelector("#campo1");
const campo2 = document.querySelector("#campo2");
const seletor = document.querySelector("#seletor");
const botao = document.querySelector("#igual");
let resposta = document.querySelector("#resposta");

// botao.addEventListener("click",calcular);
seletor.addEventListener("change",calcular);
campo1.addEventListener("keyup", calcular);
campo2.addEventListener("keyup", calcular);

function calcular(){
    if(campo1.value ==="" && campo2.value ===""){
        resposta.classList.add("error");
        resposta.innerHTML="Preencha os campos corretamente e tente novamente!";
    }else{
        resposta.classList.remove("error");
        const valor1 = parseInt(campo1.value);
        const valor2 = parseInt(campo2.value);
        const selecao = seletor.value;
        
        if(selecao=="Somar"){
            const res = valor1 + valor2;
            resposta.innerHTML=res;
        }else if(selecao=="Subtrair"){
            const res = valor1 - valor2;
            resposta.innerHTML=res;
        }else if(selecao=="Multiplicar"){
            const res = valor1 * valor2;
            resposta.innerHTML=res;
        }else if(selecao=="Dividir"){
            const res = valor1 / valor2;
            resposta.innerHTML=res;
        }
    }

    
}
    
    
    
