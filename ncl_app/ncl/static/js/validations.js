function validarLetras(id) {
  let inputId = document.getElementById(id);
  let valueInput = inputId.value;
  let regex = /[^a-zA-Z]/g;
  if (valueInput.match(regex)) {
    inputId.value = valueInput.replace(regex, "");
    alert("Este campo solo puede contener letras.");
  }
}

// Validate numbers with function (error in the first keypress)
function validarNumeros(id) {
  let input = document.getElementById(id);
  input.addEventListener("keypress", function (event) {
    if (event.which < 48 || event.which > 57) {
      if (event.which != 13) {
        // Comprobar si la tecla presionada es Enter
        event.preventDefault();
        alert("Este campo solo puede contener números.");
      }
    }
  });
}

// Validate numbers with class (without error)
const inputs = document.querySelectorAll(".onlyNumbers");

inputs.forEach((input) => {
  input.addEventListener("keydown", (event) => {
    const key = event.key;

    if (!/[\d\.]/.test(key) && key !== "Backspace" && key !== "Tab") {
      event.preventDefault();
    }
  });
});



function validateDate(id) {
  let fechaActual = new Date().toISOString().split("T")[0];
  document.getElementById(id).max = fechaActual;
}