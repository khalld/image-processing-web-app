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
