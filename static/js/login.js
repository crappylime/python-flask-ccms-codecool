function validateLogin(event) {
    event.preventDefault();
    var email = document.getElementById("email").value;
    var password = document.getElementById("password").value;
    if (!/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(email))
    {
        document.getElementById("email_format_error").style.display = 'block';
        return false;
    } else {
        document.getElementById("email_format_error").style.display = 'none';
    }
    if (password.length < 5) {
        document.getElementById("password_error").style.display = 'block';
        return false;
    }
    // else {
    //     window.location = "/login";
    //     return true;
    // }
}

