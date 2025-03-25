function toggleContent(id, element) {
    const content = document.getElementById(id);
    const plus = element.querySelector(".plus");
    if (content.classList.contains("content-hidden")) {
        content.classList.remove("content-hidden");
        content.classList.add("content-visible", "fade-in");
        setTimeout(() => content.classList.add("show"), 10); // Thêm lớp show để hiện từ từ
        plus.textContent = "−";
    } else {
        content.classList.remove("content-visible", "fade-in", "show");
        content.classList.add("content-hidden");
        plus.textContent = "+";
    }
}
document.addEventListener("mousedown", function (e) {
    e.preventDefault();
});
