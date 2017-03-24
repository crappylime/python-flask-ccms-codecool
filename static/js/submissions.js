//---------------------------------------------------------------//
//               SUBMISSIONS MODALS FUNCTIONS
//---------------------------------------------------------------//

$(document).ready(function() {
    // GET THE MODAL for actions: ADD, GRADE  //
    var modal = document.getElementById('addSubmission');

    // user who clicks anywhere outside of the modal closes it //
    window.onclick = function (event) {
      if (event.target == modal) {
          modal.style.display = "none";
      }
    };
});


function showModal(id) {
    var modal = document.getElementById('addSubmission');
    modal.style.display = "block";
    $("#add_submission_save_button").attr("onclick","addSubmission(" + id + ")"); // construct custom link
    $("#grade_submission_save_button").attr("onclick","addSubmission(" + id + ")");
}


function addSubmission(id) {
    var submission_link = $('#submission_link').val();
    var submission_content_list = [submission_link, id];
    var JSON_new_submission = JSON.stringify(submission_content_list);  // convert JS object to JSON string

    $.ajax({
        type: 'POST',
        url: '/add_submission',
        contentType: 'application/json',
        data: JSON_new_submission,
        success: function(last_submission) {         // response_data = sorted to-do list in JSON format
            var modal = document.getElementById('addSubmission');
            modal.style.display = "none";
            var new_submission_js = JSON.parse(last_submission);
            $('#submission_link').val(undefined);
            var rowCount = $('#submission_table tr').length + 1;
            $('#submission_table').append(
                '<tr><td>' + rowCount + '.</td>' +
                '<td><a href="/assignments/' + new_submission_js['assignment'] + '"' + '>' + new_submission_js['assignment_title'] + '</a></td>' +
                '<td>submitted</td>' +
                '<td><a href="/submissions/' + new_submission_js['id'] + '"' + ' class="button">View submission</a></td>' +
                '<td>– –/' + new_submission_js['assignment_max_points'] + '</td></tr>'
            );
            $('#ass' + new_submission_js['assignment']).remove();
        },
        error: function () {
            alert('Some weird error!');
        }});
    modal.style.display = "block";
}


$(document).ready(function() {
    // GET THE MODAL for actions: ADD, GRADE  //
    var grade_modal = document.getElementById('gradeSubmission');

    // user who clicks anywhere outside of the grade_modal closes it //
    window.onclick = function (event) {
      if (event.target == grade_modal) {
          grade_modal.style.display = "none";
      }
    };
});


function showGradeModal(id) {
    var grade_modal = document.getElementById('gradeSubmission');
    grade_modal.style.display = "block";
    $("#grade_submission_save_button").attr("onclick","gradeSubmission(" + id + ")");
    $('#points').attr('value', '')
}


function gradeSubmission(id) {
    var points = $('#points').val();
    var grade_submission_content_list = [points, id];
    var JSON_new_submission_grade = JSON.stringify(grade_submission_content_list);  // convert JS object to JSON string

    $.ajax({
        type: 'POST',
        url: '/grade_submission',
        contentType: 'application/json',
        data: JSON_new_submission_grade,
        success: function(last_submission) {         // response_data = sorted to-do list in JSON format
            var grade_modal = document.getElementById('gradeSubmission');
            grade_modal.style.display = "none";
            var graded_submission_js = JSON.parse(last_submission);
          },
          error: function () {
              alert('You cannot give so much points!');
          }});
      grade_modal.style.display = "block";
  }
