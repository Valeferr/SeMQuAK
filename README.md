# SeMQuAK – Semantic Modeling of Quality Assessment in Knowledge Graphs
**SeMQuAK** è un framework sviluppato in Python progettato per la semantificazione automatica delle valutazioni di qualità dei Knowledge Graph (KG). Il progetto nasce come parte di una tesi di **laurea triennale in Informatica presso l'Università degli Studi di Salerno** ([ISISLab](https://www.isislab.it/)) e si propone come modulo da integrare nel progetto di ricerca: [KGHeartBeat](https://github.com/isislab-unisa/KGHeartBeat).

---

## 📖 Abstract e Obiettivo

La valutazione automatica della qualità dei Knowledge Graph produce periodicamente enormi moli di dati. Strumenti come KGHeartBeat monitorano oltre 1600 dataset della LOD Cloud, rilasciando settimanalmente report in formato CSV. Sebbene il formato tabellare sia facile da leggere, presenta limiti significativi:

* **Visione frammentata**: I dati sono isolati in file statici.
* **Scarsa interoperabilità**: Difficoltà nell'integrare le metriche con altre risorse semantiche.
* **Tracciabilità limitata**: Difficile monitorare l'evoluzione temporale della qualità in modo strutturato.

SeMQuAK risolve questi problemi trasformando i risultati delle valutazioni da semplici file CSV a una rappresentazione semantica conforme ai principi dei **Linked Data**.

---
## Struttura del progetto

```text
SeMQuAK/
│
├── config/                     # Definizioni statiche, costanti e mapping
│   ├── __init__.py
│   ├── namespaces.py                   # RDF namespaces 
│   ├── metrics.py                      # Definizioni delle metriche di qualità
│   ├── profile_attributes.py           # Attributi di profilo e relativi predicati
│   └── errors.py                       # Gestione e definizione di errori personalizzati
│
├── semquak/                     # core logic
│   ├── __init__.py
│   ├── graph_builder.py                # Creazione e aggiornamento del grafo RDF
│   ├── utils.py                        # Funzioni di utilità
│   ├── extractors.py                   # Estrazione dei valori da CSV o da RDF graph
│   └── assessments.py                  # Gestione degli assessment (creazione, update, recupero storico)
│
├── output/                      # Cartella di output con grafi serializzati
│   └── kgs_quality.ttl                 # File Turtle generato
│
├── requirements.txt             # Dipendenze del progetto            TODO
└── README.md                    # Documentazione del progetto
```

---
## ⚙️ Come Funziona

SeMQuAK implementa una **pipeline ETL** (Extract, Transform, Load) specializzata:
1. **Extract** (Estrazione): Il modulo legge i file CSV generati dai tool di valutazione (es. KGHeartBeat).
2. **Transform** (Trasformazione):
    * *Normalizzazione*: Pulisce i dati, gestisce errori HTTP (es. 404, 500) mappandoli su URI specifici e valuta i datatype (XSD).
    * *Mapping Ontologico*: Mappa le metriche su vocabolari standard come DQV (Data Quality Vocabulary), PROV-O (Provenance Ontology) e DCAT.
    * *Gestione Versionamento*: Confronta il nuovo assessment con lo storico nel grafo. Se i valori sono invariati, aggiorna solo i timestamp, evitando duplicazione di dati ridondanti (Logica implementata in assessment.py).
3. **Load** (Caricamento): Produce un grafo RDF unificato (file .ttl) interrogabile via SPARQL.

---
## 🛠️ Tecnologie Utilizzate

* Linguaggio: Python 3.11
* Librerie Principali:
    1. *rdflib*: Per la creazione e manipolazione del grafo RDF.
    2. *pandas*: Per la manipolazione efficiente dei dati tabellari CSV.
* Ontologie: DQV, PROV, DCAT, SKOS, RDF-S.