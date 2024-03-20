// REGISTER FORM
$(document).ready(function () {
    let submitBtn = $("#registerSubmit");

    submitBtn.on("click", function () {
        $.ajax({
            url: "http://127.0.0.1:8000/api/accounts/register/",
            type: "POST",
            data: JSON.stringify({
                username: $("#username").val(),
                password: $("#password").val(),
                password2: $("#password2").val(),
            }),
            contentType: 'application/json',
            success: function (data) {
                console.log(data);
                localStorage.setItem("token", data.token);
                location.reload()
            },
        });
    });
});


// LOGIN FORM
$(document).ready(function () {
    let submitBtn = $("#loginSubmit");

    submitBtn.on("click", function () {
        $.ajax({
            url: "http://127.0.0.1:8000/auth/token/login",
            // url: "http://127.0.0.1:8000/api/accounts/login/",
            type: "POST",
            data: JSON.stringify({
                username: $("#username").val(),
                password: $("#password").val(),
            }),
            contentType: 'application/json',
            success: function (data) {
                console.log(data);
                localStorage.setItem("token", data.token);
                location.reload()
            },
        });
    });
});

