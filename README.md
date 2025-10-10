### 1. Titolo del Progetto

** Mirko Incordatore**

---

### 2. Descrizione del Progetto

Applicazione Web che permette di prenotare incordature e luogo di ritiro
in modo facile e intuitivo

---

### 3. Target

L’app si rivolge principalmente a:  
Giocatori di tennis amatoriali/professionisti che:
    - vogliono incordature professionali e veloci
    - chiedono punti di ritiro specifici

---

### 4. Mission

Avere una piattaforma che permette all'incordatore di gestire facilmente
le prenotazioni, in modo da organizzare bene il lavoro e aumentare la produttività.

Aiutare i clienti a prenotare incordatura,
ritiro prodotto e pagamento in modo facile e intuivito

---

### 5. Funzionalità Principali (Roadmap)

    - **Fase Uno:** Creazione del software gestionale  
    - **Fase Due:** Inserimento ruoli Admin/utente/anonimo con relativi permessi

---

### 6. Architettura Software

    - **Frontend Web:** React  
    - **Mobile:** React Native  
    - **Backend:** Python 3.13.8 /Django   
    - **Database:** SQLite 
    - **API REST** per la comunicazione tra frontend e backend
    - **Ollama** per supportare  il cliente durante l'esperienza 

---

### 7. Note

    - V 1.0: sarà fatta esclusivamente coma backend Django
    - V 2.0: frontend dedicato in React
    - V x.0: versione mobile usando React Native

---

### Istruzioni per l'uso

1. Clonare repository con **git clone git@github.com:Ricca917/Project-mirko-incordatore.git**

2. Impostare e attivare il virtual environment con **python - m venv .venv** 

3. Attivare il virtual environment con  **source .venv/Scripts/activate** (windows) 

   oppure  **source .venv/bin/activate** (linux/macOS)

4. Installare Django con **pip install django**

5. Installare pacchetti aggiuntivi Django con:

   **pip install django djangorestframework django-cors-headers djangorestframework-simplejwt python-dotenv whitenoise**

   - **djangorestframework** -> per le chiamate API REST
   - **django-cors-headers** -> per gestire il CORS
   - **djangorestframework**-simplejwt -> autenticazione tramite JWT
   - **python-dotenv** -> variabili d'ambiente (chiavi API, credenziali, configurazioni ecc..)
   - **whitenoise** -> per i file statici (CSS,JS, immagini)

5. Entrare nella directory del progetto e avviarlo con **python manage.py runserver**

---