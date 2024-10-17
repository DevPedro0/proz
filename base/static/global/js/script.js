

const FuncHomePage = () => {
    const ButtonOver = document.getElementById("clickover");
    let BoxingDisplay = document.querySelector('.Ocult');
  
    ButtonOver.addEventListener(
      'click',
      () => {
        BoxingDisplay.style.display = 'flex';
      }
    );
  };
  
  const Ids = ['yellow', 'pink', 'blue', 'red', 'final'];
  const IdsIMg = ['img1', 'img2', 'img3', 'img4', 'img5'];
  const section = document.querySelector('.section-func');
  
  function Organizar(novaOrdem) {
    novaOrdem.forEach((id, index) => {
      const elemento = document.getElementById(id);
      // ... (rest of Organizar function)
    });
  }
  
  function FuncOct() {
    const elementosDoCarrossel = Ids.map(id => document.getElementById(id))
      .filter(elemento => elemento !== null);
  
    // Ensure the first image element exists before setting background
    const firstImg = document.getElementById(IdsIMg[0]);
    if (firstImg) {
      const initialImageId = Ids[0]; // Default to first ID if no click occurred yet
      firstImg.style.backgroundImage = `url(../../static/global/img/${initialImageId}.jpg)`;
      firstImg.style.backgroundSize = 'cover';
      firstImg.style.backgroundPosition = 'center';
    }
  
    elementosDoCarrossel.forEach((elemento, index) => {
      elemento.addEventListener('click', () => {
        const IdPrincipal = document.getElementById(Ids[index]);
  
        section.style.background = `url(../../static/global/img/${elemento.id}.jpg)`;
        section.style.transition = '.4s ease all';
        section.style.backgroundSize = 'cover';
        section.style.backgroundPosition = 'center';
  
        let novaOrdem = [];
  
        // ... (rest of click event handler logic)
  
        novaOrdem.forEach((id, idx) => {
          const elementoImg = document.getElementById(IdsIMg[idx]);
          elementoImg.style.backgroundImage = `url(../../static/global/img/${id}.jpg)`;
          elementoImg.style.backgroundSize = 'cover';
          elementoImg.style.backgroundPosition = 'center';
        });
      });
    });
  }
  
  // Call FuncOct to initialize the carousel with the first image
  window.addEventListener('load', FuncOct);