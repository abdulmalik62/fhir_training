## Exercise 12: Medication Mapping (C-CDA → FHIR MedicationRequest)

| C-CDA XPath | C-CDA Value | FHIR Path | FHIR Value | Notes |
|------------|------------|----------|------------|------|
| //section[title='MEDICATIONS']//manufacturedMaterial/code/@displayName | albuterol 0.09 MG/ACTUAT [Proventil] | MedicationRequest.medicationCodeableConcept.text | albuterol 0.09 MG/ACTUAT [Proventil] | Medication name |
| //section[title='MEDICATIONS']//manufacturedMaterial/code/@displayName | atenolol 25 MG Oral Tablet | MedicationRequest.medicationCodeableConcept.text | atenolol 25 MG Oral Tablet | Medication name |
| //substanceAdministration/@statusCode | active | MedicationRequest.status | active | Status mapping |
| //substanceAdministration | (exists) | MedicationRequest.intent | order | Default value |
| //patient | Eve Betterhalf | MedicationRequest.subject | Patient reference | Links to patient |