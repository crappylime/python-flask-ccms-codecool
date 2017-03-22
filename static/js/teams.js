/**
 * Created by ihni on 21.03.17.
 */

function remove_team(team_id) {
     var myJSON = JSON.stringify(team_id);
    $.ajax({
        type: 'POST',
        url: '/teams/remove',
        contentType: 'application/json',
        data: myJSON,
        success: function() {
            $('#team_'+team_id.toString()).remove();
            $('#modalRemove').css({"display": "none"});
        },
        error: function () {
            alert('error removing thing')
        }
    });
}