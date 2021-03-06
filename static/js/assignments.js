/**
 * Created by michal on 21/03/2017.
 */


//-------------------------------------------------------------------------------------//
//                                  MODAL'S FUNCTIONS
//-------------------------------------------------------------------------------------//



// --------------------------------------------
// SHOW MODAL FOR ADDING / EDITING ASSIGNMENTS:
// -------------------------------------------
function showModalAddAssignment(id) {
    var modalAddAssignment = document.getElementById('modalAddAssignment');

    if (id == 'new_assignment_empty_form') {
        // alert('empty form please');
        modalAddAssignment.style.display = "block";
    }
    else {
        var id_in_JSON = JSON.stringify(id);
        $.ajax({
            type: 'POST',
            url: '/get_assignment_by_id',
            contentType: 'application/json',
            data: id_in_JSON,
            success: function (assignment_json_object) {

                var JS_object = JSON.parse(assignment_json_object);

                $('#assignment_title').val(JS_object.title);
                $('#due_date').val(JS_object.due_date);
                $('#max_points').val(JS_object.max_points);
                $('#content').val(JS_object.content);
                if (JS_object.is_team == 0) {
                    $("#is_team").prop('checked', false);
                }
                else {
                    $("#is_team").prop('checked', true);
                }
                $("#add_button").attr("onclick", "add_new_or_edit_assignment('edit_assignment'," + JS_object.id + ")"); // construct custom link
                modalAddAssignment.style.display = "block";
            },
            error: function () {
                alert('error filling edited assignment fields')
            }
        });

        modalAddAssignment.style.display = "block";
    }
};


//-------------------------------------------------------------------------------------//
//                              MODAL'S ADD ASSIGNMENT
//-------------------------------------------------------------------------------------//

//------------------------------------------------//
// ADD NEW ASSIGNMENT OR EDIT ASSIGNMENT BY AJAX:
//------------------------------------------------//
function add_new_or_edit_assignment(choice, id) {

    var modalAddAssignment = document.getElementById('modalAddAssignment');

    // --------------- get values from form -------------------- //
    var assignment_title = $('#assignment_title');
    var is_team = $("#is_team");
    var due_date = $('#due_date');
    var max_points = $('#max_points');
    var content = $('#content');

    if (is_team.prop('checked') == false) {
        is_team = 0
    }
    else {
        is_team = 1
    }

    var new_assignment = {
        assignment_title: assignment_title.val(),
        is_team: is_team,
        max_points: max_points.val(),
        due_date: due_date.val(),
        content: content.val(),
        id: id      // necessary when we want to edit assignment / automatically excluded if we add new assignment
    };

    if (new_assignment["is_team"] == 0) {
        var team_in_table = 'No';
    }
    else {
        var team_in_table = 'Yes'
    }

    var JSON_new_assignment = JSON.stringify(new_assignment);  // convert JS object to JSON string

    // ---------------------------------------------------------------------------------- //
    // ----------- SEND DATA TO CONTROLLER FOR ADDING NEW ASSIGNMENT BY AJAX: ----------- //
    if (choice == 'new_assignment') {
        $.ajax({
            type: 'POST',
            url: '/new_assignment',
            contentType: 'application/json',
            data: JSON_new_assignment,
            success: function (newest_assignment) {         // response_data = sorted to-do list in JSON format
                modalAddAssignment.style.display = "none";
                var new_assignment_js = JSON.parse(newest_assignment);

                $('#assignment_title').val(undefined);
                $("#is_team").prop('checked', false);
                $('#due_date').val(undefined);
                $('#max_points').val(undefined);
                $('#content').val(undefined);
                var rowCount = $('#assignments_table_body tr').length + 1;
                $('#assignments_table_body').append(
                    '<tr id="as' + new_assignment_js['id'] + '"><td>' + rowCount + '.</td>' +
                    '<td>' + new_assignment_js['title'] + '</td>' +
                    '<td>' + team_in_table + '</td>' +
                    '<td><a href="/assignments/' + new_assignment_js['id'] + '"' + ' class="button assignment_buttons">Details</a></td>' +
                    '<td><a onclick="showModalAddAssignment(' + new_assignment_js['id'] + ')" class="button">Edit</a>' +
                    '<a onclick="showModalRemoveAssignment(' + new_assignment_js['id'] + ')"' + ' class="button">Remove</a>' +
                    '<a href="/assignments/' + new_assignment_js['id'] + '/submissions" class="button">Submissions list</a></td></tr>'
                )
            },
            error: function () {
                alert('error adding new thing')
            }
        });
    }
    // ---------------------------------------------------------------------------------- //
    // ------------- SEND DATA TO CONTROLLER FOR EDITING ASSIGNMENT BY AJAX: ------------ //
    else {
        $.ajax({
            type: 'POST',
            url: '/edit_assignment',
            contentType: 'application/json',
            data: JSON_new_assignment,
            success: function () {         // response_data = sorted to-do list in JSON format
                modalAddAssignment.style.display = "none";
                $('#assignment_title').val(undefined);
                $("#is_team").prop('checked', false);
                $('#due_date').val(undefined);
                $('#max_points').val(undefined);
                $('#content').val(undefined);

                //INSERT EDITED DATA TO TABLE WITHOUT REFRESHING:
                $('#as' + id + ' td:nth-child(2)').text(new_assignment["assignment_title"]);
                if (new_assignment["is_team"] == 0) {
                    $('#as' + id + ' td:nth-child(3)').text(team_in_table);
                }
                else {
                    $('#as' + id + ' td:nth-child(3)').text(team_in_table);
                }
            },
            error: function () {
                alert('error adding new thing')
            }
        })
    }
}

//-------------------------------------------------------------------------------------//
//                              MODAL'S REMOVE ASSIGNMENT
//-------------------------------------------------------------------------------------//

function remove_assignment(id) {
    document.getElementById('modalRemoveAssignment').style.display = "none";

    $('#as' + id + '').css('opacity', '0.4').css('textDecoration', 'line-through');

    var id_in_JSON = JSON.stringify(id);

    $.ajax({
        type: 'POST',
        url: '/remove_assignment',
        contentType: 'application/json',
        data: id_in_JSON,
        success: function () {         // response_data = sorted to-do list in JSON format
            console.log('removed by me');
        },
        error: function () {
            alert('error removing thing')

        }
    });
}

//-------------------------------------------------------------------------------------//
//                                  MODAL'S REMOVE CONFIRMATION
//-------------------------------------------------------------------------------------//


// ----------------------  SHOW MODAL REMOVE ------------------------- //
function showModalRemoveAssignment(id) {
    var modalRemoveAssignment = document.getElementById('modalRemoveAssignment');
    modalRemoveAssignment.style.display = "block";
    $('#button_remove_yesAssignment').attr('onclick', 'remove_assignment(' + id + ')');


}
