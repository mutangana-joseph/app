
const password = document.getElementById("password");
const showPassword = document.getElementById("show-password");
const newPassword = document.getElementById("newPassword");
const hover = document.getElementById("hover")


if (showPassword) {
    showPassword.addEventListener('click', function () {
        showPassword.classList.toggle('fa-eye');
        showPassword.classList.toggle('fa-eye-slash');
        hover.textContent='Hide password';
        if (password.type === 'password') {
           
            password.type = 'text';
            newPassword.type = 'text';
        }
        else {
            password.type = 'password';
            newPassword.type = 'password';
            hover.textContent='Show password';
        }

    });
}









