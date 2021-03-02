# unict-dmi-imagistrale-multimedia-2020-2021
Progetto multimedia per Università di Catania - Informatica (Magistrale) AA 2020/2021
Image processing tramite python. L'applicativo è gestito con richieste backend con flask e svelteJs per il frontend.
Tested with:

- Python 3.9.2
- Node 12.16.2

Librerie da installare con pip
Pillow
numpy
opencv

# Setup virtual environment (most safe, not necessary)
All'interno della cartella `python3 -m venv venv` and activate with `source venv/bin/activate` , per trovare tutti i moduli installati `pip3 list`

# Svelte.js + Flask
Source:  https://github.com/cabreraalex/svelte-flask-example

A super simple example of using Flask to serve a Svelte app and use it as a backend server.

Run the following for development:

- `python server.py` to start the Flask server.
- `cd client; npm install; npm run autobuild` to automatically build and reload the Svelte frontend when it's changed.

# Piano di sviluppo
- ~~Import bootstrap per frontEnd~~ --> Controllare spinner
- Refactoring delle varie funzioni fin'ora utilizzate (pulizia codice)
    - Mean / median da fare con kernel dinamico, al momento 3x3
    - Guided filter [Prioritario]
- ~~Gestione upload immagine: upload --> base64 --> salva l'immagine~~ *Nota: si perde qualità! si può salvare un dettaglio dell'immagine in upload tramite lo zoom, libreria integrata da citare*

- Impostare logica:
    - un'immagine di default deve essere sempre considerata.
    - se faccio upload di un'immagine devo utilizzare quella e non considero più l'altra --> problema con la cache spiegato sotto
- Import algoritmi:
    - ~~Media~~     --> FISSO CON KERNEL 3X3 
    - ~~Mediano~~   --> FISSO CON KERNEL 3X3
    - ~~Bilateral~~ --> OK con .md file
    - Guided [WORKING]
## Rotte

    /               Homepage
    /median         Applica filtro mediano
    /mean           Applica filtro di media
    /bilateral      Applica filtro bilaterale
    /guided         Applica filtro guided

## BUG da risolvere
- Non si può caricare ed elaborare più di una immagine senza riavviare
    - Se modifico l'immagine e faccio l'upload mi ritorna sempre lo stesso per via della cache. ogni volta che si deve testare un'immagine --> è fondamentale per la consegna del progetto fixare questa parte? potrei dedicarmi a qualcos altro eventualmente.

## Domande
- Necessario introdurre persistenza con db o necessario solamente creare dei file?
- Chiedere se necessario a livello didattico posso utilizzare delle librerie già pronte, per farle vedere nelle altre lezioni
- Quanti altri algoritmi devo introdurre?
- Devo fare un paper con tutti gli algoritmi usati? O basta un file .md? (esempio bilateral filter)
- Altre funzionalità da introdurre?