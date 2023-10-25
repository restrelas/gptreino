function init() {
    document.getElementById('enviar').addEventListener('click', function() {
        // Exibir mensagem de "processando"
        document.getElementById('processando').style.display = 'block';

        // Submeter o formulário for the processing page
        document.getElementById('formulario').action = '/receber-dados';
        document.getElementById('formulario').submit();
        });
}

document.addEventListener('DOMContentLoaded', init);