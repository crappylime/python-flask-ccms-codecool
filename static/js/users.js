/**
 * Created by joanna on 21.03.17.
 */
function add_edit_user() {
    var user_id = $('form').attr('id');
    if (user_id == 'new_user') {
        var path = '/new_user';
    }
    else {
        var path = '/edit_user';
    }
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
        role: role,
        id: user_id

    };

    var JSON_new_user = JSON.stringify(new_user);  // convert JavaScript object to JSON string  _____CONVERT_____JavaScript____->____JSON_(string_____

    // --------- send values to controller by AJAX: ------------- //
    $.ajax({
        type: 'POST',
        url: path,
        contentType: 'application/json',
        data: JSON_new_user,
        success: function (response_data) {         // response_data = sorted to-do list in JSON format

            if (response_data == "email taken") {
                alert(response_data);

            }
            else {
                $('#new_user_modal').hide();
                $('input')
                    .val('')
                    .removeAttr('checked')
                    .removeAttr('selected');

                var new_user_data = JSON.parse(response_data); // parse JSON string to JS objects list
                user_string =
                    "<td class='table_index'></td>"
                    +
                    "<td><a href='/users/" + new_user_data['id'] + "'>" + new_user_data['name'] + "</a></td>" +
                    "<td><a href='mailto://" + new_user_data['mail'] + "'>" + new_user_data['mail'] + "</td>" +
                    '<td>' +
                    "<button onclick='showModalAddUser(" + new_user_data['id'] + ")' class='button user_button'>Edit</button>" +
                    '<button class="button user_button" onclick=showModalRemoveUser(' + new_user_data['id'] + ')>Remove</button></td>'
                if (path == '/new_user') {


                    $('#user_table_body').append('<tr id=user' + new_user_data['id'] + ">" +user_string+'</tr>');
                }
                else {
                    $('#user' + user_id).empty();
                    $('#user' + user_id).append(user_string);
                }
                var table_indexes = document.getElementsByClassName('table_index');
            for (var i = 0; i < table_indexes.length; i++) {
                table_indexes[i].innerHTML = (i + 1) + '.';
            }
            }
        },
        error: function () {
            alert('error adding new thing');
        }
    });
}

//-------------------------------------------------------------------------------------//
//                                  MODAL'S FUNCTIONS
//-------------------------------------------------------------------------------------//


$(document).ready(function () {
    // GET THE MODAL to do: ADD / EDIT  //
    var modals = document.getElementsByClassName('modal');


    // When the user clicks anywhere outside of the modal, close it //

    window.onclick = function (event) {
        for (var i = 0; i < modals.length; i++) {
            if (event.target == modals[i]) {
                modals[i].style.display = "none";
            }
        }
    };
});

// SHOW MODAL
function showModalAddUser(id) {
    var modalAdd = document.getElementById('new_user_modal');
    var addForm = modalAdd.getElementsByTagName('form')[0];
    addForm.id = id;
    if (id != "new_user") {
        var id_in_JSON = JSON.stringify(id);
        $.ajax({
            type: 'POST',
            url: '/get_user_by_id',
            contentType: 'application/json',
            data: id_in_JSON,
            success: function (user_json_object) {

                var user_data = JSON.parse(user_json_object);

                $('#firstname').val(user_data.name.split(" ")[0]);
                $('#lastname').val(user_data.name.split(" ")[1]);
                $('#mail').val(user_data.mail);

            }
        });
    }


    modalAdd.style.display = "block";
}


function showModalRemoveUser(user_id) {
    var modalRemove = document.getElementById('modalRemoveUser');
    modalRemove.style.display = "block";
    $('#button_remove_yes').attr('onclick', 'remove_user(' + user_id + ')');

}


function remove_user(user_id) {
    var myJSON = JSON.stringify(user_id);
    $.ajax({
        type: 'POST',
        url: '/users/remove',
        contentType: 'application/json',
        data: myJSON,
        success: function () {
            $('#user' + user_id.toString()).remove();
            $('#modalRemoveUser').css({"display": "none"});
            var table_indexes = document.getElementsByClassName('table_index');
            for (var i = 0; i < table_indexes.length; i++) {
                table_indexes[i].innerHTML = (i + 1) + '.';
            }
        },
        error: function () {
            alert('error removing thing')
        }
    });
}