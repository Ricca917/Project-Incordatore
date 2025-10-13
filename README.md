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

1. Clonare repository con *git clone git@github.com:Ricca917/Project-mirko-incordatore.git*

2. Impostare e attivare il virtual environment con **python - m venv .venv** 

3. Attivare il virtual environment con  **source .venv/Scripts/activate** (windows) 

   - oppure  **source .venv/bin/activate** (linux/macOS)

4. Installare Django e pacchetti aggiuntivi usando il comando **pip install -r requirements.txt** 

    - **requirements.txt** è il file di riferimento contenente la lista dei pacchetti installati e deve 
    essere aggiornato ogni volta che ne viene aggiunto uno con **pip freeze > requirements.txt**

5. Creare le tabelle del Database con **python manage.py migrate**

6. Recuperare i dati del Database dal backup con **python manage.py dumpdata > backup.json** 

7. Popolare il Database con **python manage.py loaddata backup.json**

8. Entrare nella directory *Project-mirko-incordato/mirko_incordatore* e avviare il progetto con **python manage.py runserver**


NOTE:
    - il recupero del db viene fatto solamente perchè non ci sono dati sensibili al suo interno,
    solamente dati inventati a scopo di test.
    In una situazione reale questo tipo di pratica non verrà applicata
---