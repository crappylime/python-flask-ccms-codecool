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
    var modalRemoveMember = document.getElementById('modalRemoveMember');
    // When the user clicks anywhere outside of the modal, close it //
    window.onclick = function (event) {
        if (event.target == modalRemoveTeam || event.target == modalAddTeam || event.target == modalEditTeam || event.target == modalRemoveMember) {
            modalEditTeam.style.display = "none";
            modalRemoveMember.style.display = "none";
            modalRemoveTeam.style.display = "none";
            modalAddTeam.style.display = "none";
            $("#team_members").empty();
            $('#member_list').val('');
            $('#team_name').val('');

        }
    };
});



//-------------------------------------------------------------------------------------//
//                                  MODAL'S REMOVE
//-------------------------------------------------------------------------------------//


// SHOW MODAL
function showModalRemoveTeam(team_id) {
    $('#modalRemoveTeam').css({"display": "block"});
    $('#button_remove_yes').attr('onclick', 'remove_team('+team_id+')');
}

function hideModalRemoveTeam() {
    $('#modalRemoveTeam').css({"display": "block"});
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

function showModalRemoveTeam(team_id) {
    $('#modalRemoveTeam').css({"display": "block"});
    $('#button_remove_yes').attr('onclick', 'remove_team('+team_id+')');
}

function hideModalRemoveTeam() {
    $('#modalRemoveTeam').css({"display": "block"});
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

function showModalRemoveMember(team_id, member_id) {
    $('#modalRemoveMember').css({"display": "block"});
    $('#button_remove_member_yes').attr('onclick', 'remove_member('+team_id+','+ member_id+')');
}

function hideModalRemoveMember(team_id, member_id) {
    $('#modalRemoveMember').css({"display": "none"});
}

function remove_member(team_id, member_id) {
     var myJSON = JSON.stringify({"team_id": team_id, "member_id": member_id})
    $.ajax({
        type: 'POST',
        url: '/remove_member',
        contentType: 'application/json',
        data: myJSON,
        success: function() {
            $('#member_'+member_id.toString()).remove();
            $('#modalRemoveMember').css({"display": "none"});
        },
        error: function () {
            alert('error removing member')
        }
    });
}



//-------------------------------------------------------------------------------------//
//                                  MODAL'S ADD TEAM
//-------------------------------------------------------------------------------------//

function showModalAddTeam() {
    var modalAddTeam = document.getElementById('modalAddTeam');
    modalAddTeam.style.display = "block";
}



    // SHOW MODAL
function AddTeam() {
    var modalAddTeam = document.getElementById('modalAddTeam');

    var team_name = $("#team_name").val();

         var team_name_in_JSON = JSON.stringify(team_name);
         $.ajax({
            type: 'POST',
            url: '/add_team',
            contentType: 'application/json',
            data: team_name_in_JSON,
            success: function(team_json_object) {
                var new_team_js = JSON.parse(team_json_object);

                $('#name').val(new_team_js.name);

                modalAddTeam.style.display = "none";
                $('#team_name').val('')
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
//                              MODAL'S EDIT TEAM
//-------------------------------------------------------------------------------------//

function showModalEditTeam(id) {
    var modalEditTeam = document.getElementById('modalEditTeam');
    modalEditTeam.style.display = "block";
    var team_name = $('#team_name');
    var member_list = $('#member_list');

    var team_id_in_JSON = JSON.stringify(id);
    $.ajax({
        type: 'POST',
        url: '/get_team_by_id',
        contentType: 'application/json',
        data: team_id_in_JSON,
        success: function(team_data_json_object) {
            var new_team_js = JSON.parse(team_data_json_object);
        var students = new_team_js[0];
        var team_name = new_team_js[1];
        $("#team_name_form").attr("value", ""+team_name+"");
        for (var x=0; x<students.length; x++) {
            $("#team_members").append(
            '<option>'+students[x]+'</option>')
        }


        },
        error: function () {
            alert('error filling edit team fields')
        }
    });

    $("#edit_team_button").attr("onclick", "EditTeam("+id+")");
}


function EditTeam(id) {

        var modalEditTeam = document.getElementById('modalEditTeam');

        // --------------- get values from form -------------------- //
        var new_team_name = $('#team_name_form');
        var new_member = $('#member_list');
            var edited_team = {
            name: new_team_name.val(),
            new_member: new_member.val(),
            id: id      // necessary when we want to edit team / automatically excluded if we add new team
        };

        var JSON_edited_team = JSON.stringify(edited_team);  // convert JS object to JSON string
        // --------- send values to controller by AJAX: ------------- //
        $.ajax({
            type: 'POST',
            url: '/edit_team',
            contentType: 'application/json',
            data: JSON_edited_team,
            success: function(edited_data) {
                modalEditTeam.style.display = "none";
                $('#member_list').val('');
                var new_team_data = JSON.parse(edited_data);
                if (typeof new_team_data === 'object'){
                    var team_name = new_team_data[0];
                    var member_name = new_team_data[1];
                    var student_id = new_team_data[2];
                    $('#tbody_team_'+id+'').text(team_name);
                    $('#member_'+member_name.replace(/ /g,'')+'').remove();
                    $('#member_'+student_id+'').remove();
                    $('#team_'+id+'_members').append(
                    '<li id="member_'+member_name.replace(/ /g,'')+'">'+member_name+'</li>'
                    )
                    $('#team_members_table').append(
                    '<tr id="member_'+student_id+'">' +
                    '<td>'+student_id+'</td>' +
                    '<td><a href="users/'+student_id+'">'+member_name+'</a></td>' +
                    '<td><button class="button team_button" onclick="showModalRemoveMember('+id+','+student_id+')">Remove</button></td>' +
                    '</tr>'
                    )
                    ;
                    $("#team_members").empty();
                 } else {
                    team_name = new_team_data;
                     $('#tbody_team_'+id+'').text(team_name);
                     $("#team_members").empty();
                 }
            },
            error: function () {
                alert('error adding new team');
            }});}
