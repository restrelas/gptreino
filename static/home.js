
function validate(){
    var form = document.getElementById('formulario');
    var msg = document.getElementById('mensagem');
    var idade = document.getElementById('idade');
    
    var valid = true;
    
    var inputs = []
    inputs.push(document.getElementById('nome'));
    inputs.push(document.getElementById('peso'));
    inputs.push(document.getElementById('altura'));
    
    for (var i=0; i < inputs.length; i++){
        if(!inputs[i].value){
            inputs[i].classList.add("invalid");
            msg.innerText = "Preencha todos os campos!";
            valid = false;
        }else{
            inputs[i].classList.remove("invalid");
        }
    }
    
    var sexoF = document.getElementById('feminino');
    var sexoM = document.getElementById('masculino');
    
    if(!sexoF.checked && !sexoM.checked){
        msg.innerText = "Preencha todos os campos!";
        valid = false;
    }

    if (!idade.value){
        idade.classList.add("invalid");
        msg.innerText = "Preencha todos os campos!";
        valid = false;
    }
    else if (idade.value < 18){
        idade.classList.add("invalid");
        msg.innerText = "Idade deve ser maior de 18!";
        valid = false;
    }
    msg.style.display = 'block';
    
    if (valid == true){
        msg.innerText = "Estou criando uma ficha de treino, aguarde um pouco ..."
        
        form.action = '/receber-dados';
        form.submit();
    }
}

function init() {
    var form = document.getElementById('formulario');

    document.getElementById('enviar').addEventListener('click', validate);

    // Pular entre os inputs com enter
    var inputs = form.querySelectorAll('input, select');

    for (var i = 0; i < inputs.length; i++) {
        inputs[i].addEventListener('keydown', function(event) {
            if (event.key === 'Enter') {
                event.preventDefault();

                var index = Array.prototype.indexOf.call(inputs, event.target);
                if (index < inputs.length - 1) {
                    inputs[index + 1].focus();
                }
            }
        });
    }
}

document.addEventListener('DOMContentLoaded', init);