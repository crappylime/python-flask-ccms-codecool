/**
 * Created by michal on 21/03/2017.
 */


//-------------------------------------------------------------------------------------//
//                                  MODAL'S FUNCTIONS
//-------------------------------------------------------------------------------------//

$(document).ready(function() {
    // GET THE MODAL to do: ADD / EDIT  //
    // var modalAdd = document.getElementById('modalAdd');
    // var modalRemove = document.getElementById('modalRemove');

    var all_modals = document.getElementsByClassName('modal');

    window.onclick = function (event) {
        for (var i = 0; i < all_modals.length; i++) {
            if (event.target == all_modals[i])
            all_modals[i].style.display = "none";
        }

    };
    //     alert('click');
    //     var element;
    //     for (element in all_modals) {
    //     element.style.display = "none";
    // }
    // };


    //  window.onclick = function (event) {
    //     if (event.target == modalAdd) {
    //         modalAdd.style.display = "none";
    //     }
    // };



    // When the user clicks anywhere outside of the modal, close it //
    // window.onclick = function (event) {
    //     if (event.target == modalAdd) {
    //         modalAdd.style.display = "none";
    //     }
    // };
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

        if (new_assignment["is_team"] == 0) {
                    var team_in_table = 'No';
                }
                else {var team_in_table = 'Yes'}

        var JSON_new_assignment = JSON.stringify(new_assignment);  // convert JS object to JSON string

        // --------- send values to controller by AJAX: ------------- //
        if (choice == 'new_assignment') {
        $.ajax({
            type: 'POST',
            url: '/new_assignment',
            contentType: 'application/json',
            data: JSON_new_assignment,
            success: function(newest_assignment) {         // response_data = sorted to-do list in JSON format
                modalAdd.style.display = "none";
                var new_assignment_js = JSON.parse(newest_assignment);

                $('#assignment_title').val(undefined);
                $("#is_team").prop('checked', false);
                $('#due_date').val(undefined);
                $('#max_points').val(undefined);
                $('#content').val(undefined);
                var rowCount = $('#assignments_table_body tr').length + 1;
                $('#assignments_table_body').append(
                    '<tr id="as'+ new_assignment_js['id'] +'"><td>' + rowCount + '.</td>' +
                    '<td>' + new_assignment_js['title'] + '</td>' +
                    '<td>' + team_in_table + '</td>' +
                    '<td><a href="/assignments/' + new_assignment_js['id'] + '"' + ' class="button assignment_buttons">Details</a></td>' +
                    '<td><a onclick="showModalAdd(' + new_assignment_js['id'] + ')" class="button">Edit</a>' +
                    '<a onclick="showModalRemove(' + new_assignment_js['id'] +  ')"' + ' class="button">Remove</a>' +
                    '<a href="/assignments/' + new_assignment_js['id'] +  '/submissions" class="button">Submissions list</a></td></tr>'
                )
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
            success: function() {         // response_data = sorted to-do list in JSON format
                modalAdd.style.display = "none";
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
                else {$('#as' + id + ' td:nth-child(3)').text(team_in_table);}


            },
            error: function () {
                alert('error adding new thing')
            }})
        }}

//-------------------------------------------------------------------------------------//
//                              MODAL'S REMOVE ASSIGNMENT
//-------------------------------------------------------------------------------------//

function remove_assignment(id) {
    document.getElementById('modalRemove').style.display = "none";

    $('#as'+ id + '').css('opacity', '0.4').css('textDecoration', 'line-through');

    var id_in_JSON = JSON.stringify(id);

    $.ajax({
            type: 'POST',
            url: '/remove_assignment',
            contentType: 'application/json',
            data: id_in_JSON,
            success: function() {         // response_data = sorted to-do list in JSON format
                console.log('removed by me');},
            error: function () {
                alert('error removing thing')


            }});
}

//-------------------------------------------------------------------------------------//
//                                  MODAL'S REMOVE
//-------------------------------------------------------------------------------------//


// ----------------------  SHOW MODAL REMOVE ------------------------- //
function showModalRemove(id) {
    var modalRemove = document.getElementById('modalRemove');
    modalRemove.style.display = "block";
       $('#button_remove_yes').attr('onclick', 'remove_assignment('+ id +')');


}






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