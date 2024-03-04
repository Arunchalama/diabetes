document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("diabetes-form");
    const resultDiv = document.getElementById("result");

    form.addEventListener("submit", async function (e) {
        e.preventDefault();

        // Clear the previous result
        resultDiv.innerHTML = "";

        const formData = new FormData(form);
        const response = await fetch("/", {
            method: "POST",
            body: formData,
        });

        if (response.ok) {
            const result = await response.text();
            // Display the result in the existing result container
            resultDiv.innerHTML = `<p>${result}</p>`;
        } else {
            resultDiv.innerHTML = "<p>Failed to predict.</p>";
        }
    });
});
