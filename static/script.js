//****************************************************************
//here are functions handling EMPLOYEES
function edit_employee(id) {
    sel = window.prompt("Which name do you want to edit?", "first/last");
    new_name = window.prompt("Choose new name: ", "New name");
    if (new_name != null && new_name != "") {
        fetch('http://127.0.0.1:443/back/edit-employee', {
          method: 'PUT',
          headers: {
            'Content-Type': 'text/plain;charset=utf-8',
            'ID': id,
            'SEL': sel
          },
          body: new_name
        }).then(() => {
            window.location.reload(); // Reload the page after successful deletion
        });
    };
}

function add_employee() {
    first_name = document.getElementById('first-name').value
    last_name = document.getElementById('last-name').value
    if (first_name != null && first_name != "" && last_name != null && last_name != "") {
        fetch('http://127.0.0.1:443/back/add-employee', {
          method: 'POST',
          headers: {
            'Content-Type': 'text/plain;charset=utf-8',
            'FN': first_name,
            'LN': last_name
          }
        }).then(() => {
            window.location.reload(); // Reload the page after successful deletion
        });
    };
}

function remove_employee(id) {
    confirm = window.confirm("Are you sure?");
    if (confirm) {
        fetch('http://127.0.0.1:443/back/remove-employee', {
          method: 'DELETE',
          headers: {
            'Content-Type': 'text/plain;charset=utf-8',
            'ID': id
          }
        }).then(() => {
            window.location.reload(); // Reload the page after successful deletion
        });
    };
}

//****************************************************************
//here are functions handling ANIMALS
function edit_animal(id) {
    sel = window.prompt("Which property do you want to edit?", "name/species/enclosure");
    new_value = window.prompt("Choose new value: ", "New value");
    if (new_value != null && new_value != "") {
        fetch('http://127.0.0.1:443/back/edit-animal', {
          method: 'PUT',
          headers: {
            'Content-Type': 'text/plain;charset=utf-8',
            'ID': id,
            'SEL': sel
          },
          body: new_value
        }).then(() => {
            window.location.reload(); // Reload the page after successful deletion
        });
    };
}

function add_animal() {
    name = document.getElementById('name').value
    species = document.getElementById('species').value
    enclosure = document.getElementById('enclosure').value
    if (name != null && name != "" && species != null && species != "") {
        fetch('http://127.0.0.1:443/back/add-animal', {
          method: 'POST',
          headers: {
            'Content-Type': 'text/plain;charset=utf-8',
            'NM': name,
            'SP': species,
            'ENC':enclosure
          }
        }).then(() => {
            window.location.reload(); // Reload the page after successful deletion
        });
    };
}

function remove_animal(id) {
    confirm = window.confirm("Are you sure?");
    if (confirm) {
        fetch('http://127.0.0.1:443/back/remove-animal', {
          method: 'DELETE',
          headers: {
            'Content-Type': 'text/plain;charset=utf-8',
            'ID': id
          }
        }).then(() => {
            window.location.reload(); // Reload the page after successful deletion
        });
    };
}


//****************************************************************
//here are functions handling ENCLOSURES
function edit_enclosure(id) {
    sel = window.prompt("Which property do you want to edit?", "location/inhabitant");
    new_value = window.prompt("Choose new value: ", "New value");
    if (new_value != null && new_value != "") {
        fetch('http://127.0.0.1:443/back/edit-enclosure', {
          method: 'PUT',
          headers: {
            'Content-Type': 'text/plain;charset=utf-8',
            'ID': id,
            'SEL': sel
          },
          body: new_value
        }).then(() => {
            window.location.reload(); // Reload the page after successful deletion
        });
    };
}

function add_enclosure() {
    loc = document.getElementById('location').value
    inhabitant = document.getElementById('inhabitant').value
    if (location != null && location != "") {
        fetch('http://127.0.0.1:443/back/add-enclosure', {
          method: 'POST',
          headers: {
            'Content-Type': 'text/plain;charset=utf-8',
            'LC': loc,
            'INH': inhabitant
          }
        }).then(() => {
            window.location.reload(); // Reload the page after successful deletion
        });
    };
}

function remove_enclosure(id) {
    confirm = window.confirm("Are you sure?");
    if (confirm) {
        fetch('http://127.0.0.1:443/back/remove-enclosure', {
          method: 'DELETE',
          headers: {
            'Content-Type': 'text/plain;charset=utf-8',
            'ID': id
          }
        }).then(() => {
            window.location.reload(); // Reload the page after successful deletion
        });
    };
}

