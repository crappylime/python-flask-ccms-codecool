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
function showModalAdd(id) {
    var modalAdd = document.getElementById('modalAdd');

    if (id == 'new_assignment_empty_form') {
        // alert('empty form please');
        modalAdd.style.display = "block";
    }
    else {
         var id_in_JSON = JSON.stringify(id);
         $.ajax({
            type: 'POST',
            url: '/get_assignment_by_id',
            contentType: 'application/json',
            data: id_in_JSON,
            success: function(assignment_json_object) {

                var JS_object = JSON.parse(assignment_json_object);

                $('#assignment_title').val(JS_object.title);
                $('#due_date').val(JS_object.due_date);
                $('#max_points').val(JS_object.max_points);
                $('#content').val(JS_object.content);
                if (JS_object.is_team == 0) {
                    $("#is_team").prop('checked', false);
                }
                else {$("#is_team").prop('checked', true);}
                $("#add_button").attr("onclick","add_new_or_edit_assignment('edit_assignment'," + JS_object.id + ")"); // construct custom link
                modalAdd.style.display = "block";
            },
            error: function () {
                alert('error filling edited assignment fields')
            }
    });

    modalAdd.style.display = "block";
}};





//-------------------------------------------------------------------------------------//
//                              MODAL'S ADD ASSIGNMENT
//-------------------------------------------------------------------------------------//


function add_new_or_edit_assignment(choice, id) {

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
            id: id      // necessary when we want to edit assignment / automatically excluded if we add new assignment
        };
        var JSON_new_assignment = JSON.stringify(new_assignment);  // convert JS object to JSON string

        // --------- send values to controller by AJAX: ------------- //
        if (choice == 'new_assignment') {
        $.ajax({
            type: 'POST',
            url: '/new_assignment',
            contentType: 'application/json',
            data: JSON_new_assignment,
            success: function() {         // response_data = sorted to-do list in JSON format
                modalAdd.style.display = "none";
                $('#assignment_title').val(undefined);
                $("#is_team").prop('checked', false);
                $('#due_date').val(undefined);
                $('#max_points').val(undefined);
                $('#content').val(undefined);
            },
            error: function () {
                alert('error adding new thing')
            }});
    }
        else {
        $.ajax({
            type: 'POST',
            url: '/edit_assignment',
            contentType: 'application/json',
            data: JSON_new_assignment,
            success: function(edited_assignment) {         // response_data = sorted to-do list in JSON format
                modalAdd.style.display = "none";
                $('#assignment_title').val(undefined);
                $("#is_team").prop('checked', false);
                $('#due_date').val(undefined);
                $('#max_points').val(undefined);
                $('#content').val(undefined);

                //INSERT EDITED DATA TO TABLE WITHOUT REFRESHING:
                $('#' + id + ' td:nth-child(2)').text(new_assignment["assignment_title"]);
                if (new_assignment["is_team"] == 0) {
                    $('#' + id + ' td:nth-child(3)').text("No");
                }
                else {$('#' + id + ' td:nth-child(3)').text("Yes");}


            },
            error: function () {
                alert('error adding new thing')
            }});


        }}

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


//------------------------------    TRASH       -----------------------------------------------//


     // success: function(response_data) {         // response_data = sorted to-do list in JSON format
     //            var parsed_response_data = $.parseJSON(response_data); // parse JSON string to JS objects list
     //            $("#main_table_body").empty();
     //            modalAdd.style.display = "none";
     //            $('#name_in_form').val(undefined);   //clear modal form from typed info
     //            $('#priority_select').val(1);
     //            $("#done").prop('checked', false);
     //            $('#due_date').val(undefined);
     //            print_table(parsed_response_data)