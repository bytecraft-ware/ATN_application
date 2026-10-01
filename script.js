console.log("SCRIPT ЗАПУСТИЛСЯ");

const form = document.getElementById("form");

form.addEventListener("submit", async function(event) {
    event.preventDefault();

    console.log("КНОПКА НАЖАТА");

    const application = {
        name: form.querySelector('[name="name"]').value,
        email: form.querySelector('[name="email"]').value,
        telegram: form.querySelector('[name="telegram"]').value,
        age: form.querySelector('[name="age"]').value,
        direction: form.querySelector('[name="direction"]').value,
        reason: form.querySelector('[name="message"]').value
    };

    console.log("ЗАЯВКА:", application);

    try {
        const response = await fetch("http://127.0.0.1:5000/application", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(application)
        });

        console.log("STATUS:", response.status);

        const data = await response.json();

        console.log("ОТВЕТ СЕРВЕРА:", data);

        if (response.ok) {
            alert("Заявка успешно отправлена! ✅");
            form.reset();
        } else {
            alert("Ошибка: " + data.message);
        }

    } catch (error) {
        console.error("ОШИБКА:", error);
        alert("Не удалось подключиться к серверу!");
    }
});
