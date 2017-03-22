/**
 * Created by joanna on 21.03.17.
 */
function add_edit_user(choice, user_id) {

        if (choice == 'new_to_do') {
            var path = '/add_todo';
        }
        else {
            var path = '/edit_todo';
        }

        // --------------- get values from form -------------------- //
        var name = $('#name_in_form');
        var done = $("#done");
        var priority = $('#priority_select');
        var date = $('#due_date');

        if (done.prop('checked') == false) {
            done = 'unchecked'}
        else {done = 'checked'}

        var new_todo = {       // JavaScript object
            name: name.val(),
            done: done,
            priority: priority.val(),
            due_date: date.val(),
            id: id
        };
        var JSON_todo = JSON.stringify(new_todo);  // convert JavaScript object to JSON string  _____CONVERT_____JavaScript____->____JSON_(string_____

        // --------- send values to controller by AJAX: ------------- //
        $.ajax({
            type: 'POST',
            url: path,
            contentType: 'application/json',
            data: JSON_todo,
            success: function(response_data) {         // response_data = sorted to-do list in JSON format
                var parsed_response_data = $.parseJSON(response_data); // parse JSON string to JS objects list
                $("#main_table_body").empty();
                modalAdd.style.display = "none";
                $('#name_in_form').val(undefined);   //clear modal form from typed info
                $('#priority_select').val(1);
                $("#done").prop('checked', false);
                $('#due_date').val(undefined);

                print_table(parsed_response_data)
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
    var modalAdd = document.getElementById(id);
    modalAdd.style.display = "block";
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