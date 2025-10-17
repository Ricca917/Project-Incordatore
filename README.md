** Mirko Incordatore**

---

### 2. Descrizione del Progetto

App Web che permette di prenotare incordature in modo facile e intuitivo

---

### 3. Target

L’app si rivolge a:  

- Giocatori di tennis amatoriali e professionisti che: 

- vogliono incordature professionali, veloci e personalizzate

- chiedono punti di ritiro specifici (tennis club)

---

### 4. Mission

Piattaforma che permette all'incordatore di gestire facilmente le prenotazioni

in modo da organizzare bene il lavoro e aumentare la produttività

Aiutare i clienti a prenotare incordatura,

ritiro prodotto e pagamento in modo facile e intuitivo

---

### 5. Funzionalità Principali (Roadmap)

- ✅ **Fase Uno:**  Struttura base backend, Prenotazione, Servizi e Punti di Ritiro — *Completata*

- ✅ **Fase Due:** Login e Registrazione Utenti — *Completata*

- ⏳ **Fase Tre** Inserimento sistema Pagamenti — *In Arrivo*

- ⏳ **Fase Quattro** Sviluppo Frontend React — *In Arrivo*

- ⏳ **Fase Cinque** Sviluppo App Mobile — *In Arrivo* 

---

### 6. Architettura Software

- **Frontend Web:** React  

- **Mobile:** React Native  

- **Backend:** Python 3.13.8 / Django   

- **Database:** SQLite 

- **API REST** per la comunicazione tra frontend e backend

---

### Istruzioni per l'uso

1. Clonare repository con *git clone git@github.com:Ricca917/Project-mirko-incordatore.git*

2. Impostare e attivare il virtual environment con **python -m venv .venv** 

3. Attivare il virtual environment con  **source .venv/Scripts/activate** (windows) 

   - oppure  **source .venv/bin/activate** (linux/macOS)

4. Installare Django e pacchetti aggiuntivi usando il comando **pip install -r requirements.txt** 

    - **requirements.txt** è il file di riferimento contenente la lista dei pacchetti installati e deve 
    essere aggiornato ogni volta che ne viene aggiunto uno con **pip freeze > requirements.txt**

5. Creare le tabelle del Database con **python manage.py migrate**

6. Popolare il Database usando i dati d'esempio con **python manage.py loaddata backup.json**

7. Entrare nella directory *Project-mirko-incordato/mirko_incordatore* e avviare il progetto con **python manage.py runserver**

 -  **NOTE**: Il recupero del db viene fatto solamente perchè non ci sono dati sensibili al suo interno,
    solamente dati inventati a scopo di test.
    In una situazione reale questo tipo di pratica non verrà applicata

    Il nome all'interno del progetto è uno di fantasia per via della privacy,
    verranno usati quelli originali a sviluppo inoltrato

---