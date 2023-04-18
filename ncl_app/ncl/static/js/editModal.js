function editModal(data) {
  
  const keys = Object.keys(data);
  
  for (const key of keys) {
    const input = document.querySelector(`#id_edit-${key}__edit`);
    console.log(input)
    if (input) {
      if (input.tagName === 'SELECT') {
        input.querySelectorAll('option').forEach(option => option.selected = false);
        const options = input.options;
        for (const option of options) {
          if (data[key].indexOf(option.value) !== -1) {
            option.selected = true;
          }
        }
      } else {
        input.value = data[key];
      }
    }
  }
}