
function validarLetras(id) {
  let inputId = document.getElementById(id);
  let valueInput = inputId.value;
  let regex = /[^a-zA-Z]/g;
  if (valueInput.match(regex)) {
    inputId.value = valueInput.replace(regex, "");
    alert("Este campo solo puede contener letras.");
  }
}

function validarNumeros(id) {
  let input = document.getElementById(id);
  input.addEventListener('keypress', function (event) {
    if (event.which < 48 || event.which > 57) {
      if (event.which != 13) { // Comprobar si la tecla presionada es Enter
        event.preventDefault();
        alert('Este campo solo puede contener números.');
      }
    }
  });
}