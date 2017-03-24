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