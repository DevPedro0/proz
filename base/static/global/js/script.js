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
const Ids = ['wellow1', 'pink1', 'blue1', 'red1', 'final1'];
const IdsIMg = ['img1', 'img2', 'img3', 'img4', 'img5']
const section = document.querySelector('.section-func')

document.addEventListener('DOMContentLoaded', () => {

    const Carrossel = () => {

        const elementosDoCarrossel = Ids
            .map(id => document.getElementById(id))
            .filter(elemento => elemento !== null);

        if (elementosDoCarrossel.length > 0) {
            elementosDoCarrossel.forEach(elemento => {
                elemento.addEventListener('click', () => {
                
                    if (Ids.includes(elemento.id)){
                        document.getElementById(elemento.id.replace('1', '')).checked = true;
                    };
                });
            });
        }
    };
    Carrossel();
});


function Organizar(novaOrdem) {
    novaOrdem.forEach((id, index) => {
        let elemento = document.getElementById(id);
       
    });
}

const FuncOct = () => {
    const elementosDoCarrossel = Ids
        .map(id => document.getElementById(id))
        .filter(elemento => elemento !== null);

    elementosDoCarrossel.forEach((elemento, index) => {
        elemento.addEventListener('click', () => {
            const IdPrincipal = document.getElementById(Ids[index]);

            let novaOrdem = [];

            if (IdPrincipal.id === 'pink1') {
                novaOrdem = ['pink1', 'blue1', 'red1', 'final1', 'wellow1'];
                Organizar(novaOrdem)
            } else if (IdPrincipal.id === 'blue1') {
                novaOrdem = ['blue1', 'red1', 'final1', 'wellow1', 'pink1'];
                Organizar(novaOrdem);
            } else if (IdPrincipal.id === 'red1') {
                novaOrdem = ['red1','final1', 'wellow1', 'pink1', 'blue1'];
                Organizar(novaOrdem);
            } else if (IdPrincipal.id === 'final1') {
                novaOrdem = ['final1', 'wellow1', 'pink1', 'blue1', 'red1'];
                Organizar(novaOrdem);
            } else if (IdPrincipal.id === 'wellow1'){
                novaOrdem = ['wellow1', 'pink1', 'blue1', 'red1', 'final1'];
                Organizar(novaOrdem);
            }

            novaOrdem.forEach((id, idx) => {
                const elementoImg = document.getElementById(IdsIMg[idx]);
                elementoImg.style.backgroundImage = `url(../../static/global/img/${id}.jpg)`;
                elementoImg.style.backgroundSize = 'cover';
                elementoImg.style.backgroundPosition = 'center';
            });

            let IdOne = document.getElementById(IdsIMg[0]);
            IdOne.style.backgroundImage = `url(../../static/global/img/${IdPrincipal.id}.jpg)`;
            IdOne.style.backgroundSize = 'cover'; 
            IdOne.style.backgroundPosition = 'center';
            
            // Alterar O Principal DPS
        
        
        });
    });
}

FuncOct();
