const flash = document.querySelectorAll(".flash")

if (flash) {
    setTimeout(() => {
        document.querySelectorAll(".flash").forEach(flash => {
            flash.style.opacity = "0";
            setTimeout(() => flash.remove(), 100);
        });
    }, 5000);

}