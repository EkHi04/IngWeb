// Elemento donde se mostrará el estado o resultado
const output = document.getElementById("demo");

// Intentar obtener la ubicación
if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(
    (position) => {
        const { latitude, longitude } = position.coords;
        output.innerHTML = `Latitud: ${latitude} <br> Longitud: ${longitude}`;

        // Crear y mostrar el mapa
        const img_url = `https://maps.googleapis.com/maps/api/staticmap?center=${latitude},${longitude}&zoom=14&size=400x300&sensor=false&key=YOUR_KEY`;
        document.getElementById("mapholder").innerHTML = `<img src="${img_url}" alt="Mapa de tu ubicación">`;
    },
    (error) => {
        // Manejo de errores
        const errors = {
        1: "El usuario denegó el permiso de geolocalización.",
        2: "La información de ubicación no está disponible.",
        3: "La solicitud de ubicación ha tardado demasiado.",
        0: "Ha ocurrido un error desconocido."
        };
        output.innerHTML = errors[error.code] || "Error desconocido.";
    }
    );
} else {
    output.innerHTML = "La geolocalización no es compatible con este navegador.";
}


