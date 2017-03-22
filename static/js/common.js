/**
 * Created by michal on 21/03/2017.
 */


//-------------------------------------------------------------------------------------//
//                                  MODAL'S FUNCTIONS
//-------------------------------------------------------------------------------------//

$(document).ready(function() {
    // GET THE MODAL to do: ADD / EDIT  //
    var modalAdd = document.getElementById('modalAdd');
    var modalRemove = document.getElementById('modalRemove');
    // When the user clicks anywhere outside of the modal, close it //
    window.onclick = function (event) {
        if (event.target == modalRemove || event.target == modalAdd) {
            modalRemove.style.display = "none";
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


    // SHOW MODAL
function showModalRemove(team_id) {
    var modalRemove = document.getElementById('modalRemove');
    modalRemove.style.display = "block";
    $('#button_remove_yes').attr('onclick', 'remove_team('+team_id+')');

}