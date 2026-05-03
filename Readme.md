# Healthcare Interoperability Training – Week 1

This repository contains my Week 1 onboarding work focused on healthcare data interoperability, specifically C-CDA to FHIR transformation.

## 📌 Topics Covered

- HL7v2 to FHIR evolution
- FHIR resource modeling (Patient, Encounter, Condition, MedicationRequest)
- US Core Patient profile
- C-CDA document structure (Header, Sections, Entries)
- XML parsing using Python (lxml)
- C-CDA to FHIR mapping

---

## 🧪 Implementations

### 1. C-CDA Parsing
- Extracted patient demographics, sections, problems, and medications
- Implemented using Python (lxml with namespace handling)

### 2. FHIR Resource Creation
- Condition (for Problems)
- MedicationRequest (for Medications)
- Patient resource

### 3. Mapping Work
- Problem → Condition mapping
- Medication → MedicationRequest mapping
- Documented XPath to FHIR field transformations

---

## ⚙️ Tools Used

- Python (lxml)
- HAPI FHIR Server (Docker)
- Postman
- VS Code

---

## 🧠 Key Learnings

- Handling deeply nested C-CDA XML structures
- Context-based data extraction (section-level parsing)
- Mapping between document-based (C-CDA) and resource-based (FHIR) models
- Managing interoperability challenges like code systems and missing data

---

## 🚀 Next Steps

- Automate full C-CDA → FHIR conversion
- Handle advanced mappings (Encounter, Observation, Allergies)
- Implement validation using US Core profiles