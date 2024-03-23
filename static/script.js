// LOGIN/LOGOUT/REGISTER BUTTONS LOGIC
let login = $("#login")
let register = $("#register")
let logout = $("#logout")
let token = localStorage.getItem("token");

if (token) {
    userLogged()
} else {
    userLogouted()
}

function userLogged() {
    login.hide()
    register.hide()
    logout.show()
}

function userLogouted() {
    login.show()
    register.show()
    logout.hide()
}


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
                if (data && data.token) {
                    localStorage.setItem("token", data.token);
                    console.log("Token:", localStorage.getItem("token"));
                    userLogged()
                } else {
                    console.error("Unexpected response format:", data);
                }
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
            type: "POST",
            data: JSON.stringify({
                username: $("#username").val(),
                password: $("#password").val(),
            }),
            contentType: 'application/json',
            success: function (data) {
                if (data && data.auth_token) {
                    localStorage.setItem("token", data.auth_token);
                    console.log("Token:", localStorage.getItem("token"));
                    userLogged()
                } else {
                    console.error("Unexpected response format:", data);
                }
            },
            error: function (xhr, status, error) {
                console.error("Error:", error);
            }
        });
    });
});


// LOGOUT LOGIC
$(document).ready(function () {
    let logoutBtn = $("#logout");

    logoutBtn.on("click", function () {
        let token = localStorage.getItem("token");

        if (!token) {
            console.error("Token not found in local Memory Storage");
            return;
        }

        $.ajax({
            url: "http://127.0.0.1:8000/auth/token/logout",
            type: "POST",
            headers: {
                "Authorization": "Token " + token
            },
            success: function () {
                localStorage.removeItem("token");
                userLogouted()
                console.log("User's logouted!");
            },
            error: function (xhr, status, error) {
                console.error("error:", error);
            }
        });
    });
});




// REELS LOGIC
document.addEventListener('DOMContentLoaded', function() {
    let currentPageURL = window.location.href;

    if (currentPageURL.includes("http://127.0.0.1:8000/api/")) {
        document.body.style.overflow = 'hidden';

        let token = localStorage.getItem("token");

        if (!token) {
            console.error("Token not found in local Memory Storage");
            return;
        }

        $.ajax({
            url: `http://127.0.0.1:8000/api/reels/`,
            type: 'GET',
            headers: {
                "Authorization": "Token " + token
            },
            success: function (data) {
                if (data) {
                    data.map((item) => {
                        $('body').append(`
                        <section class="section">
                            <div class="reel__container" style="position: relative;">
                                <video autoplay loop muted style="position: absolute; width: 100%; left: 0px; top: 0; bottom: 0; margin: auto 0;">
                                    <source src="${item.video}" type="video/mp4">
                                    Your browser does not support the video tag.
                                </video>
                                <div class="reel__title">
                                    <div class="reel__back-button">
                                        <svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-arrow-narrow-left"
                                            width="24" height="24" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none"
                                            stroke-linecap="round" stroke-linejoin="round">
                                            <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
                                            <line x1="5" y1="12" x2="19" y2="12"></line>
                                            <line x1="5" y1="12" x2="9" y2="16"></line>
                                            <line x1="5" y1="12" x2="9" y2="8"></line>
                                        </svg>
                                        <p class="rexxx">Reels</p>
                                    </div>
                                </div>
                                <div class="reel__content">
                                    <div class="reel__desc">
                                        <div class="reel__user">
                                            <img src="https://i.ibb.co/x36chgX/Untitled.png" class="reel__avatar" />
                                            <p class="reel__username">aisyahnrlh</p>
                                        </div>
                                        <p class="reel__caption">${item.description}</p>
                                    </div>
                                    <div class="reel__options">
                                        <svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-heart" width="24"
                                            height="24" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none"
                                            stroke-linecap="round" stroke-linejoin="round">
                                            <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
                                            <path d="M19.5 13.572l-7.5 7.428l-7.5 -7.428m0 0a5 5 0 1 1 7.5 -6.566a5 5 0 1 1 7.5 6.572">
                                            </path>
                                        </svg>
                                        <p class="reel__likes">${item.video_likes}</p>
                                        <svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-send" width="24"
                                            height="24" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none"
                                            stroke-linecap="round" stroke-linejoin="round">
                                            <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
                                            <line x1="10" y1="14" x2="21" y2="3"></line>
                                            <path d="M21 3l-6.5 18a0.55 .55 0 0 1 -1 0l-3.5 -7l-7 -3.5a0.55 .55 0 0 1 0 -1l18 -6.5"></path>
                                        </svg>
                                    </div>
                                </div>
                            </div>
                        </section>`)
                    })
                }
            }
        })
    }
})

