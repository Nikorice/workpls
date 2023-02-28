// Add event listener to form submission
document.querySelectorAll("form").forEach(function(form) {
    form.addEventListener("submit", function(event) {
        event.preventDefault();
        var formData = new FormData(form);
        var xhr = new XMLHttpRequest();
        xhr.open("POST", form.action);
        xhr.onload = function() {
            document.open();
            document.write(xhr.responseText);
            document.close();
        };
        xhr.send(formData);
    });
});
