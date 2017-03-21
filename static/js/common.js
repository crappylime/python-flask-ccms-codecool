/**
 * Created by michal on 21/03/2017.
 */


//-------------------------------------------------------------------------------------//
//                                  MODAL'S FUNCTIONS
//-------------------------------------------------------------------------------------//

$(document).ready(function() {
    // GET THE MODAL to do: ADD / EDIT  //
    var modalAdd = document.getElementById('modalAdd');

    // When the user clicks anywhere outside of the modal, close it //
    window.onclick = function (event) {
        if (event.target == modalAdd) {
            modalAdd.style.display = "none";
        }
    };
});

    // SHOW MODAL
function showModalAdd() {
    var modalAdd = document.getElementById('modalAdd');
    modalAdd.style.display = "block";
}


//-------------------------------------------------------------------------------------//
//                                  MODAL'S REMOVE
//-------------------------------------------------------------------------------------//

$(document).ready(function() {
    var modalAdd = document.getElementById('modalRemove');

    // When the user clicks anywhere outside of the modal, close it //
    window.onclick = function (event) {
        if (event.target == modalAdd) {
            modalAdd.style.display = "none";
        }
    };
});

    // SHOW MODAL
function showModalRemove() {
    var modalAdd = document.getElementById('modalRemove');
    modalAdd.style.display = "block";
}