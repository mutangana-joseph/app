const handleActive = (elements) => {
    elements.forEach(el => {
        el.addEventListener("click", () => {
            elements.forEach(item => item.classList.remove("active"));
            el.classList.add("active");
        });
    });
};

handleActive(document.querySelectorAll(".card"));
handleActive(document.querySelectorAll(".topCard"));
  