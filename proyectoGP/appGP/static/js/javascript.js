document.addEventListener('DOMContentLoaded', () => {

    // 1. Destacar el menú activo
    document.querySelectorAll('#menu li a').forEach(link => {
        link.addEventListener('click', (event) => {
            document.querySelectorAll('#menu li').forEach(li => li.classList.remove('selected'));
            event.target.parentElement.classList.add('selected');
        });
    });

// 2. Efectos de transición en el contenido al hacer clic en el menú
document.querySelectorAll('#menu li a').forEach(link => {
    link.addEventListener('click', (event) => {
        event.preventDefault();
        const contentBody = document.querySelector('#content-body');

        contentBody.classList.add('fade'); // Clase opcional en tu CSS para la transición

        fetch(link.href)
            .then(response => response.text())
            .then(html => {
                // Crear un DOM temporal para poder manipular la respuesta
                const tempDoc = new DOMParser().parseFromString(html, 'text/html');

                // Selecciona solo el contenido que necesitas, excluyendo el menú y otras partes
                const newContent = tempDoc.querySelector('#content-body');

                // Solo actualizar el contenido de la página, sin el menú ni encabezados
                if (newContent) {
                    contentBody.innerHTML = newContent.innerHTML;
                }

                contentBody.classList.remove('fade');
            })
            .catch(error => {
                console.error('Error al cargar el contenido:', error);
            });
    });
});

// 3. Mensajes emergentes personalizados
if (!sessionStorage.getItem('alertShown')) {
    window.onload = () => {
        alert('¡Bienvenido a Proyecto Base!');
        sessionStorage.setItem('alertShown', 'true'); // Marca que el mensaje ya fue mostrado
    };
}


    // 6. Interacciones con efectos al pasar el ratón por encima de los elementos del sidebar
    document.querySelectorAll('.sidebar_item').forEach(item => {
        item.addEventListener('mouseover', () => {
            item.style.backgroundColor = '#f9f9f9'; // Cambia el color de fondo
            item.style.transition = 'background 0.3s ease';
        });
        item.addEventListener('mouseout', () => {
            item.style.backgroundColor = 'transparent'; // Restaura el color de fondo
        });
    });
    document.addEventListener("DOMContentLoaded", function() {
        const menuLinks = document.querySelectorAll("#menu a");
    
        menuLinks.forEach(link => {
            link.addEventListener("click", function(event) {
                event.preventDefault();  // Previene el comportamiento por defecto del enlace (recarga)
    
                // Llamada AJAX o carga dinámica de contenido
                const url = link.getAttribute("href");
    
                // Evitar duplicación del contenido cargado (si es necesario)
                if (!document.querySelector(`#content[data-url="${url}"]`)) {
                    fetch(url)  // Realiza la llamada al URL
                        .then(response => response.text())
                        .then(data => {
                            const contentDiv = document.querySelector("#content");
                            contentDiv.innerHTML = data;  // Carga el contenido nuevo
                            contentDiv.setAttribute("data-url", url);  // Marca el contenido cargado
                        })
                        .catch(error => console.error("Error al cargar el contenido:", error));
                }
            });
        });
    });

    document.addEventListener("DOMContentLoaded", function () {
        const menuLinks = document.querySelectorAll("#menu a");
    
        menuLinks.forEach(link => {
            link.addEventListener("click", function (event) {
                event.preventDefault();  // Evita la recarga completa de la página
    
                // Obtén la URL del enlace
                const url = link.getAttribute("href");
    
                // Verifica si el contenido ya ha sido cargado
                if (!document.querySelector(`#content[data-url="${url}"]`)) {
                    // Realiza la llamada al servidor para obtener el contenido del enlace
                    fetch(url)
                        .then(response => response.text())
                        .then(data => {
                            const contentDiv = document.querySelector("#content");
                            
                            // Limpia el contenido anterior
                            contentDiv.innerHTML = data;
    
                            // Establece un atributo personalizado para evitar duplicación
                            contentDiv.setAttribute("data-url", url);
                        })
                        .catch(error => {
                            console.error("Error al cargar el contenido:", error);
                        });
                }
            });
        });
    });
    
    

});
