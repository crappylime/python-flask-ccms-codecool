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

// $(document).ready(function() {
//     var modalAdd = document.getElementById('modalRemove');
//
//     // When the user clicks anywhere outside of the modal, close it //
//     window.onclick = function (event) {
//         if (event.target == modalAdd) {
//             modalAdd.style.display = "none";
//         }
//     };
// });
//
//     // SHOW MODAL
// function showModalRemove() {
//     var modalAdd = document.getElementById('modalRemove');
//     modalAdd.style.display = "block";
// }

//-------------------------------------------------------------------------------------//
//                              MODAL'S ADD ASSIGNMENT
//-------------------------------------------------------------------------------------//

// add new/edit to-do item (depends on 'choice' parameter: 'new_to_do' / 'edit_to_do'
function add_new_edit_to_do(choice, id) {

        var modalAdd = document.getElementById('modalAdd');

        if (choice == 'new_assignment') {
            var path = '/new_assignment';
        }
        else {
            var path = '/edit_assignment';
        }

        // --------------- get values from form -------------------- //
        var assignment_title = $('#assignment_title');
        var is_team = $("#is_team");
        var due_date = $('#due_date');
        var max_points = $('#max_points');
        var content = $('#content');


        if (is_team.prop('checked') == false) {
            is_team = 0}
        else {is_team = 1}

        var new_assignment = {
            assignment_title: assignment_title.val(),
            is_team: is_team,
            max_points: max_points.val(),
            due_date: due_date.val(),
            content: content.val(),
            id: id
        };
        var JSON_new_assignment = JSON.stringify(new_assignment);  // convert JS object to JSON string

        // --------- send values to controller by AJAX: ------------- //
        $.ajax({
            type: 'POST',
            url: '/new_assignment',
            contentType: 'application/json',
            data: JSON_new_assignment,
            success: function() {         // response_data = sorted to-do list in JSON format
                modalAdd.style.display = "none";
            },
            error: function () {
                alert('error adding new thing')
            }});
    }

     // success: function(response_data) {         // response_data = sorted to-do list in JSON format
     //            var parsed_response_data = $.parseJSON(response_data); // parse JSON string to JS objects list
     //            $("#main_table_body").empty();
     //            modalAdd.style.display = "none";
     //            $('#name_in_form').val(undefined);   //clear modal form from typed info
     //            $('#priority_select').val(1);
     //            $("#done").prop('checked', false);
     //            $('#due_date').val(undefined);
     //            print_table(parsed_response_data)