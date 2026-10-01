# 🔒 Internet Security Project – Improper Platform Usage & Mobile Security Demos
Repository contenente il progetto di Internet Security (Università di Catania), focalizzato sullo studio, la simulazione e la risoluzione di vulnerabilità legate all'uso improprio della piattaforma (Improper Platform Usage, OWASP Mobile Top 10 - M1).

# 📌 Panoramica del Progetto
Il progetto esplora la categoria di rischio *Improper Platform Usage*, che si verifica quando le applicazioni mobile utilizzano in modo errato le funzionalità di sicurezza della piattaforma o falliscono nell'implementare controlli nativi adeguati. Vengono analizzati tre scenari concreti di vulnerabilità associati ad esempi di codice pratici e alle relative contromisure (Fix).

# 🛠️ Demo e Casi Studio Implementati
1. WebView Demo (Phishing & JavaScript Injection)
Descrizione: Viene analizzato l'uso insicuro delle WebView nelle applicazioni mobile.

Attacco: Simulazione di un attacco in cui una WebView carica contenuti non validati o permette l'esecuzione arbitraria di codice JavaScript (es. interazione anomala con i cookie o furto di credenziali attraverso schermate di login contraffatte).

Mitigazione: Configurazione sicura della WebView, disabilitazione di funzionalità JavaScript superflue ove non necessarie e validazione rigorosa degli URL caricati.

2. Clipboard Demo (Data Leakage)
Descrizione: Analisi dei rischi legati all'accesso non controllato alla memoria degli appunti (clipboard) del dispositivo.

Vulnerabilità: Applicazioni terze o script malevoli in background possono leggere dati sensibili (come password, token di sessione o dati personali) copiati in precedenza dall'utente.

Fix: Introduzione di meccanismi di oscuramento/cancellazione della clipboard o restrizioni d'accesso nei sistemi operativi moderni per prevenire la fuga di dati (Data Leakage).

3. Background Monitoring (Privacy & Resource Abuse)
Descrizione: Gestione scorretta dei processi in background o dei servizi di localizzazione/monitoraggio continuo.

Attacco: L'applicazione sfrutta permessi sensibili per tracciare o raccogliere informazioni sull'utente anche quando l'app non è in primo piano, violando la privacy e consumando risorse di sistema.

Fix: Adeguamento alle linee guida di sicurezza per limitare l'esecuzione in background e richiedere solo i permessi strettamente necessari (Principle of Least Privilege).

# 🗂️ Struttura della Repository
La repository raccoglie il codice sorgente delle demo e la documentazione tecnica del progetto:

<img width="338" height="298" alt="image" src="https://github.com/user-attachments/assets/ccd048f6-fb18-43d5-8c74-ca6528719ea8" />

# 🚀 Guida all'Utilizzo
Clona la repository sul tuo ambiente di lavoro locale.

Consulta la relazione tecnica (Relazione.pdf) per i dettagli teorici, i frammenti di codice vulnerabile e le relative patch di sicurezza.

Esegui i singoli moduli di test seguendo le istruzioni specifiche all'interno delle rispettive directory.

# 📚 Riferimenti e Standard di Sicurezza
OWASP Mobile Top 10 – M1: Improper Platform Usage

Documentazione ufficiale di sicurezza Android / iOS sulle WebView e la gestione dei permessi.

# 👤 Autore
Antonio Pistone (Matricola: 1000050018)

Università di Catania – Dipartimento di Matematica e Informatica

Corso di Laurea in Informatica
