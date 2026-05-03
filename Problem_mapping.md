## Exercise 11: Problem Mapping (C-CDA → FHIR Condition)

| C-CDA XPath | C-CDA Value | FHIR Path | FHIR Value | Notes |
|------------|------------|----------|------------|------|
| //section[title='PROBLEMS']//observation/value/@displayName | Pneumonia | Condition.code.text | Pneumonia | Clinical diagnosis |
| //section[title='PROBLEMS']//observation/value/@displayName | Angina | Condition.code.text | Angina | Clinical diagnosis |
| //section[title='PROBLEMS']//observation/value/@displayName | Chest pain | Condition.code.text | Chest pain | Symptom |
| //section[title='PROBLEMS']//observation/value/@displayName | Left lower lobe of lung | Condition.bodySite.text | Left lower lobe of lung | Anatomical location |
| //section[title='PROBLEMS']//observation | (exists) | Condition.clinicalStatus | active | Default mapping |
| //section[title='PROBLEMS']//observation | (exists) | Condition.subject | Patient reference | Links to patient |