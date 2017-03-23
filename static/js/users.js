/**
 * Created by joanna on 21.03.17.
 */
function add_edit_user(user_id) {

        // if (user_id == 'new_user') {
        //     var path = '/add_todo';
        // }
        // else {
            var path = '/add_user';
        // }

        // --------------- get values from form -------------------- //
        var firstname = $('#firstname');
        var lastname = $("#lastname");
        var email = $('#email');
        var password = $('#password');
        var role = document.getElementsByTagName('table')[0].id;

        var new_user = {       // JavaScript object
            firstname: firstname.val(),
            lastname: lastname.val(),
            email: email.val(),
            password: password.val(),
            role: role

        };
        var JSON_new_user = JSON.stringify(new_user);  // convert JavaScript object to JSON string  _____CONVERT_____JavaScript____->____JSON_(string_____

        // --------- send values to controller by AJAX: ------------- //
        $.ajax({
            type: 'POST',
            url: path,
            contentType: 'application/json',
            data: JSON_new_user,
            success: function(response_data) {         // response_data = sorted to-do list in JSON format
                var new_user_data = $.parseJSON(response_data); // parse JSON string to JS objects list
                $("#main_table_body").empty();
                modalAdd.style.display = "none";
                $('#name_in_form').val(undefined);   //clear modal form from typed info
                $('#priority_select').val(1);
                $("#done").prop('checked', false);
                $('#due_date').val(undefined);
            },
            error: function () {
                alert('error adding new thing')
            }});
    }

    //-------------------------------------------------------------------------------------//
//                                  MODAL'S FUNCTIONS
//-------------------------------------------------------------------------------------//


$(document).ready(function() {
    // GET THE MODAL to do: ADD / EDIT  //
    var modals = document.getElementsByClassName('modal');


    // When the user clicks anywhere outside of the modal, close it //

    window.onclick = function (event) {
        for (var i=0;i<modals.length;i++) {
            if (event.target == modals[i]) {
                modals[i].style.display = "none";
            }
        }    };
});

    // SHOW MODAL
function showModalAdd(id) {
    var modalAdd = document.getElementById('new_user');

    modalAdd.style.display = "block";
    var addForm = modalAdd.getElementsByTagName('form')[0];
    addForm.id = id;
}


function showModalRemove(user_id) {
    var modalRemove = document.getElementById('modalRemove');
    modalRemove.style.display = "block";
    $('#button_remove_yes').attr('onclick', 'remove_user('+user_id+')');

}


function remove_user(user_id) {
     var myJSON = JSON.stringify(user_id);
    $.ajax({
        type: 'POST',
        url: '/users/remove',
        contentType: 'application/json',
        data: myJSON,
        success: function() {
            $('#user'+user_id.toString()).remove();
            $('#modalRemove').css({"display": "none"});
            var table_indexes = document.getElementsByClassName('table_index');
            for (var i=0;i<table_indexes.length;i++) {
                table_indexes[i].innerHTML = (i + 1)+'.';
            }
        },
        error: function () {
            alert('error removing thing')
        }
    });
}