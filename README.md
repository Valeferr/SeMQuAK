# SeMQuAK – Semantic Modeling of Knowledge Graph Quality

---

## Struttura del progetto

```text
SeMQuAK/
│
├── config/                     # Definizioni statiche, costanti e mapping
│   ├── __init__.py
│   ├── namespaces.py            # RDF namespaces 
│   ├── metrics.py               # Definizioni delle metriche di qualità
│   ├── profile_attributes.py    # Attributi di profilo e relativi predicati
│   └── errors.py                # Gestione e definizione di errori personalizzati
│
├── semquak/                     # core logic
│   ├── __init__.py
│   ├── graph_builder.py         # Creazione e aggiornamento del grafo RDF
│   ├── utils.py                 # Funzioni di utilità
│   ├── extractors.py            # Estrazione dei valori da CSV o da RDF graph
│   └── assessments.py           # Gestione degli assessment (creazione, update, recupero storico)
│
├── output/                      # Cartella di output con grafi serializzati
│   └── graph.ttl                # File Turtle generato
│
├── requirements.txt             # Dipendenze del progetto            TODO
└── README.md                    # Documentazione del progetto
```


