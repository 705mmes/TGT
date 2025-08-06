if (document.getElementById("registerBtn")) {
	let btn = document.getElementById("registerBtn");
	btn.onclick = sendForm();
}

async function sendForm() {
	const url = window.location.pathname;
	console.log(url);
}