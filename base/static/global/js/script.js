const FuncHomePage = () => {
    const ButtonOver = document.getElementById("clickover");
    let BoxingDisplay = document.querySelector('.Ocult');

    ButtonOver.addEventListener(
        'click', 
        () => {
            BoxingDisplay.style.display = 'flex';
        }
    )

};

document.addEventListener('DOMContentLoaded', () => {
    const Carrossel = () => {
        const Ids = ['wellow1', 'pink1', 'blue1', 'red1', 'final1' ];
        let elementosdoCarrossel = Ids.map(id => document.getElementById(id)).filter(naoNull => naoNull !== null);

        if (elementosdoCarrossel.length > 0){
            elementosdoCarrossel.forEach(
                elementoDaLista => {
                    elementoDaLista.addEventListener('click', () => {
                            alert('Clicou');
                            document.getElementById(elementoDaLista.id.replace('1', '')).checked = true;
                        });
                });
        }};

    Carrossel();
});