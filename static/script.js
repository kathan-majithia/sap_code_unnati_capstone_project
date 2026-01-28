const form = document.getElementById("uploadForm");
const resultDiv = document.getElementById("result");

form.addEventListener("submit", async (e) => {
    e.preventDefault();

    resultDiv.classList.add("hidden");
    resultDiv.innerHTML = "Analyzing signatures...";

    const formData = new FormData(form);

    const response = await fetch("/predict", {
        method: "POST",
        body: formData
    });

    const data = await response.json();

    resultDiv.innerHTML = `
        <h3>🔍 Analysis Result</h3>
        <p><b>Signature A Confidence:</b> ${data.img1_conf}%</p>
        <p><b>Signature B Confidence:</b> ${data.img2_conf}%</p>
        <hr>
        <p>✅ <b>${data.real}</b> is REAL</p>
        <p>❌ <b>${data.forged}</b> is FORGED</p>
    `;

    resultDiv.classList.remove("hidden");
});

const img1Input = document.getElementById("img1");
const img2Input = document.getElementById("img2");

img1Input.addEventListener("change", () => {
    document.getElementById("file-name-1").textContent =
        img1Input.files.length ? img1Input.files[0].name : "No file selected";
});

img2Input.addEventListener("change", () => {
    document.getElementById("file-name-2").textContent =
        img2Input.files.length ? img2Input.files[0].name : "No file selected";
});
