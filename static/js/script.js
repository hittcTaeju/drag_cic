const dropzone = document.getElementById("dropzone");

dropzone.addEventListener("dragover", (event) => {
    event.preventDefault();
    dropzone.classList.add("dragover");
});

dropzone.addEventListener("dragleave", () => {
    dropzone.classList.remove("dragover");
});

dropzone.addEventListener("drop", (event) => {
    event.preventDefault();
    dropzone.classList.remove("dragover");

    const files = event.dataTransfer.files;
    const formData = new FormData();

    for (let i = 0; i < files.length; i++) {
        formData.append("file", files[i]);
    }

    fetch("/upload", {
        method: "POST",
        body: formData
    }).then(response => response.text())
      .then(result => alert(result))
      .catch(error => console.error("Error:", error));
});
