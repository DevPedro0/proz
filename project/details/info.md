# Demonstração Educacional de Keylogger (Projeto Escolar)

> **Aviso ético e legal**
> Este projeto foi desenvolvido **exclusivamente para fins educacionais**, com o objetivo de demonstrar, de forma controlada, **como ataques funcionam** para melhorar a conscientização em **cibersegurança**. O uso de keyloggers fora de ambientes autorizados é ilegal e antiético.

---

## 1. Objetivo do Projeto

Demonstrar o funcionamento **conceitual** de um ataque do tipo *keylogger*, explicando:

* Como a captura de teclas pode ocorrer em nível de software;
* Como dados podem ser registrados localmente;
* Por que esse tipo de técnica representa um risco à segurança da informação;
* A importância de práticas defensivas e prevenção.

Nenhuma funcionalidade de **exfiltração**, **web scraping** ou envio remoto de dados foi implementada, respeitando princípios de cibersegurança.

---

## 2. Visão Geral do Funcionamento

Quando o projeto é executado, ocorre o seguinte fluxo lógico:

0. Primeiramente, deve-se criar o ambiente virtual (`venv`) -> Rode o seguinte: (*py -m venv venv*) e siga sua respectiva ativação no diretório do Ambiente Virtual (*venv\scripts\activate*)
  **OBS** Necessita de python Instalado <https://www.python.org/> para Instalação do Python;
  **OBS** Arquivo (`requirements.txt`) Obtém todas as Funcionalidades do Projeto, logo, após o Ambiente Virtual ser ativado, faça (*pip install -r requirements.txt*)

1. O arquivo principal (`main.py`) é iniciado dentro de um ambiente virtual (*venv*);
2. As dependências listadas em `requirements.txt` já estão previamente instaladas;
3. O programa passa a **monitorar eventos de teclado** do sistema;
4. Cada tecla pressionada é registrada juntamente com:

   * A tecla capturada;
   * O horário exato do evento;
5. Essas informações são armazenadas localmente em um arquivo chamado `data.py`.

---

## 3. Registro de Dados

O arquivo `data.py` funciona como um **repositório local de eventos**, contendo:

* Timestamp (data e hora do pressionamento);
* Identificação da tecla digitada.

Esse registro permite demonstrar como informações aparentemente simples podem, quando acumuladas, revelar:

* Senhas;
* Mensagens privadas;
* Dados sensíveis.

---

## 4. Por que o Web Scraping Não Foi Implementado

Inicialmente, havia a ideia de simular uma etapa de **coleta ou envio de dados via web scraping**, porém isso foi **intencionalmente descartado** por motivos de segurança:

* Evitar a simulação de exfiltração de dados reais;
* Não reproduzir comportamentos próximos a *malware ativo*;
* Manter o projeto dentro de limites acadêmicos e éticos;
* Reduzir riscos legais e técnicos.

Assim, o projeto permanece **local, controlado e demonstrativo**.

---

## 5. Relação com Cibersegurança

Este projeto ajuda a compreender:

* Como ataques baseados em *spyware* funcionam;
* Por que antivírus e sistemas de detecção comportamental são importantes;
* A relevância de permissões de sistema e isolamento de processos;
* A necessidade de boas práticas como:

  * Uso de antivírus;
  * Princípio do menor privilégio;
  * Ambientes virtuais e sandboxing;
  * Conscientização do usuário.

---

## 6. Limitações do Projeto

* Não realiza envio de dados para servidores externos;
* Não possui persistência no sistema;
* Não executa técnicas de evasão;
* Não opera de forma oculta ou stealth;
* Finalidade exclusivamente didática.

---

## 7. Conclusão

O projeto demonstra, de forma **segura e controlada**, como um keylogger pode funcionar em nível básico, reforçando a importância da **cibersegurança defensiva**. Ao compreender o ataque, torna-se possível projetar melhores mecanismos de proteção.

Este tipo de abordagem é comum em cursos e laboratórios de segurança da informação, sempre respeitando princípios legais, éticos e acadêmicos.

---

**Projeto desenvolvido para fins educacionais.**
