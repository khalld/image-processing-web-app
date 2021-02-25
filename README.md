# unict-dmi-imagistrale-multimedia-2020-2021
Progetto multimedia per Università di Catania - Informatica (Magistrale) AA 2020/2021

Image processing tramite python. L'applicativo è gestito con richieste backend con flask e svelteJs per il frontend.

# Setup virtual environment (most safe, not necessary)
All'interno della cartella `python3 -m venv venv` and activate with `source venv/bin/activate` , per trovare tutti i moduli installati `pip3 list`

_*Installare tutti i requirements.txt ( COMPLETARE FILE)  *_

# Svelte.js + Flask
Source:  https://github.com/cabreraalex/svelte-flask-example

A super simple example of using Flask to serve a Svelte app and use it as a backend server.

Run the following for development:

- `python server.py` to start the Flask server.
- `cd client; npm install; npm run autobuild` to automatically build and reload the Svelte frontend when it's changed.

This example just queries the Flask server for a random number.


# Piano di sviluppo
- ~~Introduzione virtual env --> ciò che è scritto qui https://www.youtube.com/watch?v=b9BYA483yVI~~
- ~~Completare procedura venv~~
- ~~Sistemare layout~~
- ~~Import bootstrap per frontEnd~~
- ~~Refactoring delle varie funzioni fin'ora utilizzate (pulizia codice)~~
- ~~Gestione upload immagine: upload --> base64 --> salva l'immagine~~ *Ricorda di dire che si perde qualità! si può salvare un dettaglio dell'immagine in upload tramite lo zoom*
- Impostare logica:
    - un'immagine di default deve essere sempre considerata.
    - se faccio upload di un'immagine devo utilizzare quella e non considero più l'altra --> problema con la cache spiegato sotto
- Import algoritmi:
    - ~~Media~~
    - ~~Mediano~~
    - Bilateral [WORKING]
    - Guided [WORKING]
- Applicazione degli algoritmi all'immagine per cui si è fatto l'upload

## Rotte

    /               Homepage
    /median         Applica filtro mediano
    /mean           Applica filtro di media
    /bilateral      Applica filtro bilaterale
    /guided         Applica filtro guided

## Domande
- Necessario introdurre persistenza con db o necessario solamente creare dei file?
- Chiedere se necessario a livello didattico posso utilizzare delle librerie già pronte, per farle vedere nelle altre lezioni
- é ok usare il png?? controlla eventualmente salva in jpg

- Se modifico l'immagine e faccio l'upload mi ritorna sempre lo stesso per via della cache. ogni volta che si deve testare un'immagine
nuova si deve pulire la cache. (Posso lasciarlo così o devo sistemare necessariamente? non ho idea di come debba fare al momento!)
- secondo me il problema è sulla lib che fa lo zoom perché quando fa upload non richiama nuovamente bene la funzione