# PromAtlas

Piattaforma unificata di **Rischio Territoriale e Settoriale** basata esclusivamente su dati open italiani.

PromAtlas integra tre casi d'uso:

1. **Italia Credit Risk Atlas**  
   Mappa interattiva del rischio di credito per settore e territorio (dati Banca d'Italia).

2. **Municipal Fiscal Risk Scanner**  
   Score di rischio finanziario dei Comuni italiani (OpenBilanci, BDAP – MEF).

3. **Sector Resilience Radar**  
   Indice di resilienza settoriale per banche e investitori (ISTAT, BdI).

Tutto gira in locale, con un semplice front-end Streamlit e un database analitico file-based (DuckDB/SQLite).

---

## Obiettivo

Costruire un **ecosistema dati unico** per analizzare:

- rischio di credito (per territorio e settore),
- rischio fiscale degli enti locali,
- resilienza dei settori produttivi,

su una struttura comune **territorio × settore × anno**.

È pensato come **MVP serio** e immediatamente utilizzabile/pitchabile in Prom.

---

## Struttura della repo

```bash
PromAtlas/
├─ README.md
├─ pyproject.toml          # oppure requirements.txt
├─ .gitignore
├─ data/
│  ├─ raw/
│  │  ├─ bdi/
│  │  ├─ istat/
│  │  ├─ bdap/
│  │  └─ openbilanci/
│  ├─ interim/
│  └─ processed/
├─ src/
│  └─ promatlas/
│     ├─ __init__.py
│     ├─ config/
│     │  ├─ __init__.py
│     │  └─ settings.py
│     ├─ etl/
│     │  ├─ __init__.py
│     │  ├─ bdi_credit.py
│     │  ├─ istat_sectors.py
│     │  ├─ istat_territory.py
│     │  ├─ bdap_bilanci.py
│     │  └─ openbilanci.py
│     ├─ db/
│     │  ├─ __init__.py
│     │  ├─ schema.py
│     │  └─ load.py
│     ├─ features/
│     │  ├─ __init__.py
│     │  ├─ credit_risk.py
│     │  ├─ municipal_fiscal.py
│     │  └─ sector_resilience.py
│     └─ app/
│        ├─ __init__.py
│        └─ main.py
├─ scripts/
│  ├─ download_all_data.py
│  ├─ build_all.py
│  └─ run_app.sh
└─ tests/
   ├─ __init__.py
   └─ test_basic.py
```

## Requisiti

- Python 3.11+
- git
- ambiente virtuale (consigliato: venv)

## Setup ambiente

```bash
git clone <URL-della-repo> PromAtlas
cd PromAtlas

python -m venv .venv
source .venv/bin/activate   # su Windows: .venv\\Scripts\\activate

# Se usi pyproject.toml
pip install -e ".[dev]"

# Oppure, se usi requirements.txt
# pip install -r requirements.txt
```

## Dati utilizzati

PromAtlas usa esclusivamente dati pubblici (non inclusi nella repo):

**Banca d'Italia**

- Condizioni e rischiosità del credito (STACORIS)
- Tabelle su qualità del credito per settore/territorio

**ISTAT**

- Competitività dei settori produttivi (indicatori di redditività, produttività, export, ecc.)
- Dati territoriali (popolazione, codici ISTAT, se necessari)

**MEF – BDAP**

- Bilanci degli enti territoriali

**OpenBilanci**

- Bilanci dei Comuni italiani (serie storiche)

I file scaricati vengono salvati sotto `data/raw/` e **NON** vengono versionati (`.gitignore`).

## Flusso di lavoro (alto livello)

### Download open data

Esegui lo script di download (in fase di sviluppo):

```bash
python scripts/download_all_data.py
```

Lo script:

- crea la struttura `data/raw/<fonte>/`,
- scarica i file CSV/XLSX necessari per i 3 use case.

### Costruzione database analitico

```bash
python scripts/build_all.py
```

Lo script:

- legge i file in `data/raw/`,
- applica le logiche di ETL (pulizia, mapping codici, costruzione dimensioni),
- scrive le tabelle finali (dimensioni + fact) in un DB locale
  (es. `data/processed/promatlas.duckdb`).

### Avvio dell'applicazione (MVP)

```bash
streamlit run src/promatlas/app/main.py
```

L'interfaccia offre:

- Credit Risk Atlas (use case 1) – prima funzionalità a essere sviluppata
- Municipal Fiscal Risk (use case 2) – in sviluppo
- Sector Resilience Radar (use case 3) – in sviluppo
- Vista integrata territorio × settore × anno (fase successiva)

## Roadmap di sviluppo (sintesi)

### Fase 1 – Infrastruttura

- definizione schema DB (dimensioni e fact)
- setup ETL per Banca d'Italia (use case 1)
- MVP “Italia Credit Risk Atlas” (mappe + serie storiche)

### Fase 2 – Estensione settori

- ETL ISTAT settori produttivi
- costruzione “Sector Resilience Radar”

### Fase 3 – Estensione Comuni

- ETL BDAP/OpenBilanci
- costruzione “Municipal Fiscal Risk Scanner”

### Fase 4 – Integrazione

- vista unica territorio × settore × anno
- pagina di confronto e analisi incrociate

## Stato attuale

- [x] Struttura repo
- [ ] Script download dati
- [ ] Schema DB e tabelle di base
- [ ] MVP “Italia Credit Risk Atlas”
- [ ] Modulo “Sector Resilience Radar”
- [ ] Modulo “Municipal Fiscal Risk”
- [ ] Vista integrata

## Contributi

Per ora il progetto è orientato ad uso interno / MVP. Quando la struttura sarà più stabile, si potrà:

- documentare meglio le fonti e le scelte metodologiche,
- valutare quali parti rendere open-source.
