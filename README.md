# unict-dmi-imagistrale-multimedia-2020-2021
Progetto multimedia per Università di Catania - Informatica (Magistrale) AA 2020/2021

Image processing tramite python. L'applicativo è gestito con richieste backend con flask e svelteJs per il frontend.
Template di partenza https://github.com/cabreraalex/svelte-flask-example

# Svelte.js + Flask

A super simple example of using Flask to serve a Svelte app and use it as a backend server.

Run the following for development:

- `python server.py` to start the Flask server.
- `cd client; npm install; npm run autobuild` to automatically build and reload the Svelte frontend when it's changed.

This example just queries the Flask server for a random number.


# Piano di sviluppo
- ~~Import bootstrap per frontEnd~~
- ~~Refactoring delle varie funzioni fin'ora utilizzate (pulizia codice)~~
- Import algoritmi:
    - ~~Media~~
    - ~~Mediano~~
    - Guided
    - Bilateral
- Gestione upload immagine
- Applicazione degli algoritmi all'immagine per cui si è fatto l'upload

## Rotte

    /               Homepage
    /median         Applica mediano all'immagine di test
    /mean           Applica filtro di media all'immagine di test

    
