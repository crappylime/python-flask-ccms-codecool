//---------------------------------------------------------------//
//               SUBMISSIONS MODALS FUNCTIONS
//---------------------------------------------------------------//

$(document).ready(function() {
    // GET THE MODAL for actions: ADD, GRADE  //
    var modal = document.getElementsByClassName('modal');

    // user who clicks anywhere outside of the modal closes all modals //
    window.onclick = function (event) {
      for (var i = 0; i < modal.length; i++) {
          if (event.target == modal[i]) {
              modal[i].style.display = "none";
          }
      }
    };
});


function showModal(id) {
    var modal = document.getElementById(id);

    modal.style.display = "block";
}
