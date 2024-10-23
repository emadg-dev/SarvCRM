document.querySelectorAll(".resizer").forEach(function(resizer) {
    resizer.addEventListener("mousedown", initResize);
});

let startX, startWidth, resizer;

function initResize(event) {
    resizer = event.target;
    startX = event.clientX;
    startWidth = resizer.parentElement.offsetWidth;
    
    // Add mousemove and mouseup event listeners
    document.addEventListener("mousemove", resizeColumn);
    document.addEventListener("mouseup", stopResize);
}

function resizeColumn(event) {
    let newWidth = startWidth + (event.clientX - startX);
    resizer.parentElement.style.width = newWidth + "px";
}

function stopResize() {
    // Remove event listeners
    document.removeEventListener("mousemove", resizeColumn);
    document.removeEventListener("mouseup", stopResize);
}