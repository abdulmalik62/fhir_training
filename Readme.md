# 🏥 Healthcare Interoperability Training

> A two-week onboarding deep-dive into healthcare data interoperability — covering FHIR, C-CDA, TEFCA, SMART on FHIR, Bulk FHIR, HIE architecture, and patient matching.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Repository Structure](#repository-structure)
- [Week 1 — Healthcare Data Standards & C-CDA to FHIR Foundations](#week-1--healthcare-data-standards--c-cda-to-fhir-foundations)
  - [Topics Covered](#week-1-topics-covered)
  - [Implementations](#week-1-implementations)
  - [Key Learnings](#week-1-key-learnings)
- [Week 2 — TEFCA, SMART on FHIR, Bulk FHIR, HIE & Capstone Pipeline](#week-2--tefca-smart-on-fhir-bulk-fhir-hie--capstone-pipeline)
  - [Topics Covered](#week-2-topics-covered)
  - [Implementations](#week-2-implementations)
  - [Key Learnings](#week-2-key-learnings)
- [Tools & Technologies](#tools--technologies)

---

## Overview

This repository contains onboarding work focused on healthcare data interoperability. The training spans two weeks and progresses from foundational standards to real-world system design and implementation.

| Week | Focus |
|------|-------|
| **Week 1** | FHIR fundamentals, C-CDA document structure, Python-based parsing, and manual C-CDA → FHIR mapping |
| **Week 2** | TEFCA/QHIN architecture, SMART on FHIR (OAuth2), Bulk FHIR export, HIE models, patient matching, and a capstone pipeline |

---

## Repository Structure

```
.
├
│── C-CDA annotation and parsing files
│── FHIR resource examples
│── Mapping markdown files
│── Postman/HAPI FHIR related files
│── Python parser scripts
│
└── Week 2/
    ├── Screenshots/
    │   ├── 01_smart_launcher_configuration.png
    │   ├── 02_selected_test_patient.png
    │   ├── 03_authorization_launch_step.png
    │   ├── 04_app_displaying_patient_data.png
    │   └── 05_token_response.png
    ├── bulk_data_analysis.ipynb
    ├── bulk_export_client.py
    ├── ccda_to_fhir_pipeline.py
    ├── Patient.ndjson
    ├── Condition.ndjson
    ├── MedicationRequest.ndjson
    ├── epic_nexus_memo.md
    ├── exchange_purpose_decision_tree.md
    ├── hie_architecture_comparison.md
    ├── patient_matching_demo.py
    ├── smart_demo_steps.md
    ├── smart_launch_flow_diagrams.md
    ├── smart_scope_reference.md
    └── tefca_hierarchy_diagram.md
```

---

## Week 1 — Healthcare Data Standards & C-CDA to FHIR Foundations

Week 1 focused on understanding the evolution of healthcare interoperability standards, working with FHIR resources via a live server, parsing C-CDA XML documents in Python, and manually mapping C-CDA clinical data to FHIR.

### Week 1 Topics Covered

- Evolution from HL7v2 → CDA/C-CDA → FHIR
- FHIR resource modeling and REST API operations
- Core FHIR resources: `Patient`, `Organization`, `Encounter`, `Condition`, `Observation`, `MedicationRequest`
- US Core Patient profile requirements
- C-CDA document structure: header, sections, entries, and template OIDs
- Python XML parsing with `lxml` (namespace-aware XPath)
- Manual mapping from C-CDA Problems and Medications to FHIR resources

---

### Week 1 Implementations

#### 1. 🖥️ HAPI FHIR Server Setup

- Ran a [HAPI FHIR](https://hapifhir.io/) server locally using Docker
- Created test `Patient` and `Organization` resources
- Practiced full FHIR CRUD operations via the UI and Postman
- Tested FHIR search operations including `_include` queries

#### 2. 📦 FHIR Resource Creation

Created and validated sample FHIR resources:

| Resource | Description |
|----------|-------------|
| `Patient` | Demographics, identifiers, contact info |
| `Organization` | Healthcare organization details |
| `Condition` | Problem list entries |
| `MedicationRequest` | Medication orders |
| `Encounter` | Clinical visit records |

#### 3. 🐍 C-CDA Parsing (`ccda_parser.py`)

Implemented a Python parser using `lxml` to extract clinical data from C-CDA XML:

- Patient name and date of birth
- Section titles
- Problem list entries
- Medication list entries

The parser uses **namespace-aware XPath queries** and **section-level filtering** to avoid extracting unrelated clinical values from other sections.

```python
# Example: Namespace-aware XPath in lxml
ns = {'cda': 'urn:hl7-org:v3'}
problems = root.xpath('//cda:section[cda:templateId[@root="2.16.840.1.113883.10.20.22.2.5.1"]]', namespaces=ns)
```

#### 4. 📝 C-CDA Annotation

Annotated a sample C-CDA document by identifying:

- **Header elements** — patient demographics, author, custodian
- **Clinical sections** — structured sections with LOINC codes
- **Machine-readable entries** — coded clinical data (SNOMED, RxNorm, ICD-10)
- **Template OIDs** — conformance identifiers linking to C-CDA IG
- **Narrative ↔ Entry linkage** — relationship between human-readable text and structured entries

#### 5. 🔄 C-CDA to FHIR Mapping

Created detailed mapping documentation for:

| C-CDA Source | FHIR Target |
|--------------|-------------|
| Problem Concern Act / Problem Observation | `Condition` |
| Medication Activity | `MedicationRequest` |

Each mapping file documents:

- C-CDA XPath expression
- C-CDA sample value
- FHIR resource path
- FHIR target value
- Notes on transformation logic (code system conversion, date format, status mapping, etc.)

---

### Week 1 Key Learnings

| Standard | Paradigm | Key Characteristic |
|----------|----------|--------------------|
| **HL7v2** | Message-based | Event-driven, pipe-delimited, real-time triggers |
| **C-CDA** | Document-based | Human + machine readable, XML, template-constrained |
| **FHIR** | Resource/API-based | RESTful, modular, JSON/XML, granular querying |

- C-CDA contains **both** human-readable narrative (`<text>`) and machine-readable coded entries (`<entry>`)
- Clinical meaning in C-CDA depends heavily on **section context** and **template IDs** — the same XML structure can mean different things in different sections
- FHIR breaks clinical data into **modular resources** that can be independently queried and exchanged via REST APIs
- Mapping C-CDA → FHIR requires handling nested XML, multiple code systems, date format differences, missing data patterns, and status terminology mismatches

---

## Week 2 — TEFCA, SMART on FHIR, Bulk FHIR, HIE & Capstone Pipeline

Week 2 focused on real-world interoperability workflows — national exchange frameworks, secure API authorization, population-level data export, HIE architecture patterns, probabilistic patient matching, and building a complete end-to-end C-CDA to FHIR pipeline.

### Week 2 Topics Covered

- TEFCA framework and QHIN architecture
- Exchange purposes under TEFCA
- Epic Nexus QHIN research
- SMART on FHIR EHR launch and standalone launch flows
- OAuth2-based FHIR authorization and OpenID Connect
- SMART scopes and launch context parameters
- Bulk FHIR `$export` operation (async pattern)
- NDJSON format and population-level data analysis
- HIE architecture models: centralized, federated, hybrid
- Probabilistic patient matching logic
- C-CDA to FHIR transaction Bundle pipeline

---

### Week 2 Implementations

#### 1. 🏛️ TEFCA and QHIN Documentation

Created markdown documentation explaining the national health information exchange framework:

- **`tefca_hierarchy_diagram.md`** — ONC/ASTP → RCE → QHINs → Participants → Subparticipants
- **`exchange_purpose_decision_tree.md`** — Choosing the right TEFCA exchange purpose (Treatment, Payment, Operations, Individual Access, Public Health, Benefits Determination)
- **`epic_nexus_memo.md`** — Research memo on Epic's Nexus QHIN, connectivity, and participation model

#### 2. 🔐 SMART on FHIR Demo

Completed a full SMART on FHIR EHR launch flow using the [SMART Health IT Launcher](https://launch.smarthealthit.org/).

**Launch flow documented:**

```
EHR Launch Context
      │
      ▼
SMART App receives launch + iss parameters
      │
      ▼
App requests authorization (scope, state, PKCE)
      │
      ▼
Authorization Server issues code
      │
      ▼
App exchanges code for access_token + id_token
      │
      ▼
App calls FHIR API with Bearer token
```

**Screenshots captured:**

| Screenshot | Description |
|-----------|-------------|
| `01_smart_launcher_configuration.png` | SMART launcher setup with scopes and patient context |
| `02_selected_test_patient.png` | Test patient selected for the demo launch |
| `03_authorization_launch_step.png` | OAuth2 authorization consent screen |
| `04_app_displaying_patient_data.png` | App rendering Patient and Encounter FHIR resources |
| `05_token_response.png` | Raw access token response including scope and patient claim |

#### 3. 📖 SMART Scope Reference (`smart_scope_reference.md`)

Comprehensive reference covering SMART scope syntax and usage:

| Scope Type | Example | Purpose |
|------------|---------|---------|
| Patient-level read | `patient/Patient.read` | Read patient's own data |
| User-level read | `user/Observation.read` | Read data the user can access |
| System-level | `system/Patient.read` | Backend system access |
| Launch | `launch`, `launch/patient` | EHR launch context |
| OpenID Connect | `openid`, `profile`, `fhirUser` | Identity claims |

#### 4. 📊 Bulk FHIR NDJSON Analysis (`bulk_data_analysis.ipynb`)

Built a Jupyter notebook to analyze population-level FHIR data exported in NDJSON format.

**Data loaded:**

```
Patient.ndjson          → Demographics summary
Condition.ndjson        → Top diagnoses by frequency
MedicationRequest.ndjson → Medication frequency analysis
```

**Analysis performed:**
- Patient demographics summary (age distribution, gender breakdown)
- Top 10 conditions by ICD-10 code frequency
- Most prescribed medications by RxNorm code
- Bar chart visualizations with `matplotlib`

#### 5. ⚙️ Bulk Export Client (`bulk_export_client.py`)

Implemented a Bulk FHIR asynchronous export client demonstrating the full `$export` workflow:

```
POST [base]/$export
       │
       ▼ 202 Accepted + Content-Location header
       │
       ▼ Poll GET Content-Location
       │   ├── 202 → still running, wait and retry
       │   └── 200 → complete, manifest returned
       │
       ▼ Download each NDJSON file from manifest
       │
       ▼ Count and summarize records by resource type
```

#### 6. 🏗️ HIE Architecture Comparison (`hie_architecture_comparison.md`)

Compared three HIE architectural models:

| Attribute | Centralized | Federated | Hybrid |
|-----------|-------------|-----------|--------|
| **Storage Model** | Central repository | Data stays at source | Mix of both |
| **Query Pattern** | Direct lookup | Federated query broadcast | Varies by data type |
| **Privacy Implications** | Single point of risk | Data never leaves source | Balanced |
| **Scalability** | Limited by central store | Highly scalable | Flexible |
| **Real-world Examples** | Indiana HIE, CommonWell | eHealth Exchange | Carequality |

#### 7. 🔍 Patient Matching Demo (`patient_matching_demo.py`)

Implemented a probabilistic patient matching algorithm comparing two patient records:

**Matching attributes and weights:**

| Attribute | Algorithm | Weight |
|-----------|-----------|--------|
| First name | String similarity (Jaro-Winkler) | 25% |
| Last name | String similarity (Jaro-Winkler) | 30% |
| Date of birth | Exact match | 30% |
| Address | String similarity | 15% |

The script outputs a **weighted match score** and a **likely match / no match** decision threshold result.

#### 8. 🚀 C-CDA to FHIR Capstone Pipeline (`ccda_to_fhir_pipeline.py`)

Built a complete end-to-end pipeline that:

1. **Extracts** clinical data from a C-CDA XML document using `lxml`
2. **Transforms** and maps data to FHIR resource structures
3. **Creates** the following FHIR resources:
   - `Patient` — from C-CDA header demographics
   - `Condition` — from Problem Section entries
   - `MedicationRequest` — from Medications Section entries
   - `AllergyIntolerance` — from Allergies Section entries
4. **Packages** all resources into a FHIR **transaction Bundle**
5. **Submits** the Bundle to a FHIR server via HTTP POST

```python
# High-level pipeline flow
ccda_doc = parse_ccda("sample.xml")
patient   = map_patient(ccda_doc)
conditions = map_conditions(ccda_doc)
medications = map_medications(ccda_doc)
allergies  = map_allergies(ccda_doc)
bundle = build_transaction_bundle([patient, *conditions, *medications, *allergies])
response = post_to_fhir_server(bundle, base_url="http://localhost:8080/fhir")
```

---

### Week 2 Key Learnings

| Topic | Key Takeaway |
|-------|-------------|
| **TEFCA** | Provides a national trust framework enabling health information exchange under a single common agreement |
| **QHINs** | Enable network-to-network exchange — organizations connect once to a QHIN and gain access to all other QHINs |
| **SMART on FHIR** | Secures FHIR APIs using OAuth2 + OpenID Connect; scopes and launch context control what data an app can access |
| **Bulk FHIR** | Designed for population-level export using an asynchronous `$export` pattern; results delivered as NDJSON files |
| **HIE Architectures** | Centralized, federated, and hybrid models each have different tradeoffs in privacy, scalability, and query complexity |
| **Patient Matching** | Critical because the same patient may be represented differently across systems — no universal patient ID exists in the US |
| **C-CDA → FHIR Pipeline** | Must handle extraction, code system mapping, date transformation, resource validation, and Bundle packaging correctly |

---

## Tools & Technologies

| Category | Tools |
|----------|-------|
| **Language** | Python 3 |
| **XML Parsing** | `lxml` |
| **HTTP / FHIR Client** | `requests` |
| **Data Analysis** | `pandas`, `matplotlib` |
| **FHIR Server** | [HAPI FHIR](https://hapifhir.io/) (Docker) |
| **API Testing** | Postman |
| **SMART Demo** | [SMART Health IT Launcher](https://launch.smarthealthit.org/) |
| **Notebooks** | Jupyter Notebook |
| **Editor** | VS Code |
| **Version Control** | GitHub |

---

<div align="center">

**Built during a healthcare interoperability onboarding program**

`FHIR R4` · `C-CDA 2.1` · `TEFCA` · `SMART on FHIR` · `Bulk FHIR` · `HL7`

</div>
