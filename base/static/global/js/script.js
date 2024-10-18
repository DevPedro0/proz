const BoxingDisplay = document.querySelector('.Ocult');

        const DisplayFlex = () => {
            // Verifica o display atual e alterna entre 'flex' e 'none'
            if (BoxingDisplay.style.display === 'flex') {
                BoxingDisplay.style.display = 'none';
            } else {
                BoxingDisplay.style.display = 'flex';
            }
};

const Ids = ['yellow', 'pink', 'blue', 'red', 'final'];
const IdsIMg = ['img1', 'img2', 'img3', 'img4', 'img5'];
const section = document.querySelector('.section-func');


function Organizar(novaOrdem) {
  novaOrdem.forEach((id, index) => {
    const elemento = document.getElementById(IdsIMg[index]); 
    if (elemento) {

      elemento.style.backgroundImage = `url(../../static/global/img/${id}.jpg)`;
      elemento.style.backgroundSize = 'cover';
      elemento.style.backgroundPosition = 'center';
    }
  });
}


function FuncOct() {
  const elementosDoCarrossel = Ids.map(id => document.getElementById(id)).filter(Boolean);


  if (elementosDoCarrossel.length > 0) {
    const primeiraImagem = elementosDoCarrossel[0];
    AtualizarImagemPrincipal(primeiraImagem.id);
  }


  elementosDoCarrossel.forEach((elemento, index) => {
    elemento.addEventListener('click', () => {
      const IdPrincipal = Ids[index];
      AtualizarImagemPrincipal(IdPrincipal);

      let novaOrdem = []; 


      switch (IdPrincipal) {
        case 'pink':
          novaOrdem = ['pink', 'blue', 'red', 'final', 'yellow'];
          break;
        case 'blue':
          novaOrdem = ['blue', 'red', 'final', 'yellow', 'pink'];
          break;
        case 'red':
          novaOrdem = ['red', 'final', 'yellow', 'pink', 'blue'];
          break;
        case 'final':
          novaOrdem = ['final', 'yellow', 'pink', 'blue', 'red'];
          break;
        default:
          novaOrdem = ['yellow', 'pink', 'blue', 'red', 'final'];
          break;
      }

      Organizar(novaOrdem); 

      AtualizarMiniaturas(novaOrdem);
    });
  });
}


function AtualizarImagemPrincipal(id) {
  section.style.backgroundImage = `url(../../static/global/img/${id}.jpg)`; 
  section.style.transition = '.4s ease all'; 
  section.style.backgroundSize = 'cover'; 
  section.style.backgroundPosition = 'center'; 
}


function AtualizarMiniaturas(novaOrdem) {
  novaOrdem.forEach((id, idx) => {
    const elementoImg = document.getElementById(IdsIMg[idx]);
    if (elementoImg) {
      elementoImg.style.backgroundImage = `url(../../static/global/img/${id}.jpg)`; 
      elementoImg.style.backgroundSize = 'cover'; 
      elementoImg.style.backgroundPosition = 'center'; 
    }
  });
}

// Inicializa o carrossel e carrega a primeira imagem ao carregar a página
window.addEventListener('load', FuncOct);
