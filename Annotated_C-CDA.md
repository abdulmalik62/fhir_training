## Exercise 9: Annotated C-CDA

### 1. Header Elements

- Patient Name: Eve Betterhalf  
- Date of Birth: 1975-05-01  
- Gender: Female  
- Address: Beaverton, Oregon, USA  
- Organization: The DoctorsTogether Physician Group  
- Author: Dr. Patricia Primary  

---

### 2. Sections Identified

- Advance Directives  
- Allergies and Adverse Reactions  
- Encounters  
- Family History  
- Functional Status  
- Immunizations  

---

### 3. Entries with OIDs

| Entry Type       | OID                                      | Description                  |
|----------------|------------------------------------------|------------------------------|
| Allergy         | 2.16.840.1.113883.10.20.22.4.7          | Allergy Observation          |
| Encounter       | 2.16.840.1.113883.10.20.22.4.49         | Encounter Activity           |
| Immunization    | 2.16.840.1.113883.10.20.22.4.52         | Immunization Activity        |

---

### 4. Human vs Machine Data Relationship

C-CDA documents contain both human-readable narrative text and machine-readable structured data. The text sections (tables and descriptions) are intended for clinicians, while coded entries (using OIDs and standardized codes like SNOMED, LOINC, RxNorm) are used by systems for interoperability and automated processing.