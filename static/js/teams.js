/**
 * Created by ihni on 21.03.17.
 */
//-------------------------------------------------------------------------------------//
//                                  MODAL'S FUNCTIONS
//-------------------------------------------------------------------------------------//

$(document).ready(function() {
    // GET THE MODAL to do: ADD / EDIT  //
    var modalAddTeam = document.getElementById('modalAddTeam');
    var modalRemoveTeam = document.getElementById('modalRemoveTeam');
    var modalEditTeam = document.getElementById('modalEditTeam');
    // When the user clicks anywhere outside of the modal, close it //
    window.onclick = function (event) {
        if (event.target == modalRemoveTeam || event.target == modalAddTeam || event.target == modalEditTeam) {
            modalRemoveTeam.style.display = "none";
            modalAddTeam.style.display = "none";
            modalEditTeam.style.display = "none";
        }
    };
});



//-------------------------------------------------------------------------------------//
//                                  MODAL'S REMOVE
//-------------------------------------------------------------------------------------//


// SHOW MODAL
function showModalRemoveTeam(team_id) {
    var modalRemove = document.getElementById('modalRemoveTeam');
    modalRemove.style.display = "block";
    $('#button_remove_yes').attr('onclick', 'remove_team('+team_id+')');
}

function hideModalRemoveTeam() {
    var modalRemoveTeam = document.getElementById('modalRemoveTeam');
    modalRemoveTeam.style.display = "none";
}

function remove_team(team_id) {
     var myJSON = JSON.stringify(team_id);
    $.ajax({
        type: 'POST',
        url: '/teams/remove',
        contentType: 'application/json',
        data: myJSON,
        success: function() {
            $('#team_'+team_id.toString()).remove();
            $('#modalRemoveTeam').css({"display": "none"});
        },
        error: function () {
            alert('error removing thing')
        }
    });
}





//-------------------------------------------------------------------------------------//
//                                  MODAL'S ADD/EDIT
//-------------------------------------------------------------------------------------//

function showModalAddTeam() {
    var modalAddTeam = document.getElementById('modalAddTeam');
    modalAddTeam.style.display = "block";
}

function showModalEditTeam(id) {
    var modalEditTeam = document.getElementById('modalEditTeam');
    modalEditTeam.style.display = "block";
    var team_name = $('#team_name');
    var member_list = $('#member_list');

    var team_id_in_JSON = JSON.stringify(id);
    alert(team_id_in_JSON)
    $.ajax({
        type: 'POST',
        url: '/get_team_by_id',
        contentType: 'application/json',
        data: team_id_in_JSON,
        success: function(team_data_json_object) {
            var new_team_js = JSON.parse(team_data_json_object);
            console.log(new_team_js);
        students = new_team_js[0][0]
        members = new_team_js[0][1]


        },
        error: function () {
            alert('error filling add team fields')
        }
    });

    $("#edit_team_button").attr("onclick", "EditTeam("+id+")");
}

    // SHOW MODAL
function AddTeam() {
    var modalAddTeam = document.getElementById('modalAddTeam');

    var team_name = $("#team_name").val();

         var team_name_in_JSON = JSON.stringify(team_name);
         $.ajax({
            type: 'POST',
            url: '/add_team', //TODO
            contentType: 'application/json',
            data: team_name_in_JSON,
            success: function(team_json_object) {
                var new_team_js = JSON.parse(team_json_object);

                $('#name').val(new_team_js.name);

                modalAddTeam.style.display = "none";
                $("#team_table_body").append(
                    '<tr id="team_'+ new_team_js['id'] +'">' +
                    '<td>'+new_team_js['id']+'</td>' +
                    '<td>' + new_team_js['name'] + '</td>' +
                    '<td><ol></ol></td>' +
                    '<td>' +
                        '<a href="/teams/' + new_team_js['id'] + '"' + ' class="button team_button">Details</a>' +
                        '<button class="button team_button" onclick="showModalEditTeam(' +new_team_js['id'] +')">Edit</button>' +
                        '<button class="button team_button" onclick="showModalRemoveTeam(' +new_team_js['id'] +')">Remove</button>' +
                    '</td>')
            },
            error: function () {
                alert('error filling add team fields')
            }
    });

};





//-------------------------------------------------------------------------------------//
//                              MODAL'S ADD TEAM
//-------------------------------------------------------------------------------------//


function EditTeam(id) {

        var modalEditTeam = document.getElementById('modalEditTeam');

        // --------------- get values from form -------------------- //
        var team_name = $('#team_name');
        var member_list = $('#member_list');

            var edited_team = {
            name: team_name.val(),
            id: id      // necessary when we want to edit team / automatically excluded if we add new team
        };

        var JSON_new_team = JSON.stringify(new_team);  // convert JS object to JSON string

        // --------- send values to controller by AJAX: ------------- //
        if (choice == 'new_team') {
        $.ajax({
            type: 'POST',
            url: '/teams/new',
            contentType: 'application/json',
            data: JSON_new_team,
            success: function(newest_team) {         // response_data = sorted to-do list in JSON format
                modalAdd.style.display = "none";
                var new_team_js = JSON.parse(newest_team);

                $('#name').val(JS_object.name);//TODO
                $('#member_list').val(JS_object.name);
                $('#team_assignments_list').val(JS_object.name);

                var rowCount = $('#teams_table_body tr').length + 1;
                $('#teams_table_body').append(
                    '<tr id="team_'+ new_team_js['id'] +'"><td>' + rowCount + '.</td>' +
                    '<td>' + new_team_js['name'] + '</td>' +
                    '<td>' + team_in_table + '</td>' +
                    '<td><a href="/assignments/' + new_assignment_js['id'] + '"' + ' class="button assignment_buttons">Details</a></td>' +
                    '<td><a onclick="showModalAdd(' + new_assignment_js['id'] + ')" class="button">Edit</a>' +
                    '<a href="/assignments/' + new_assignment_js['id'] +  '/remove' + '"' + ' class="button">Remove</a>' +
                    '<a href="/assignments/' + new_assignment_js['id'] +  '/submissions" class="button">Submissions list</a></td></tr>'
                )
            },
            error: function () {
                alert('error adding new team')
            }});}}
