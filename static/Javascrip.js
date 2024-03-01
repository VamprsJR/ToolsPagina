function cambiarModo() {
    var body = document.body;
    var iconoModo = document.getElementById('iconoModo');

    body.classList.toggle('modo-oscuro');
    iconoModo.classList.toggle('sol');
    iconoModo.classList.toggle('luna');
}
