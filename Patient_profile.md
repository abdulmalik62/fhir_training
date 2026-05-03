## US Core Patient Profile – Must Support Checklist

| Element Path                  | Data Type                                   | Example Value                                   |
|-------------------------------|---------------------------------------------|-------------------------------------------------|
| Patient.identifier            | Identifier                                  | MRN12345                                        |
| Patient.active                | boolean                                     | true                                            |
| Patient.name                  | HumanName                                   | Abdul Malik                                     |
| Patient.name.family           | string                                      | Malik                                           |
| Patient.name.given            | string[]                                    | ["Abdul"]                                       |
| Patient.gender                | code                                        | male                                            |
| Patient.birthDate             | date                                        | 2000-01-01                                      |
| Patient.address               | Address                                     | Chennai, Tamil Nadu, India                      |
| Patient.address.city          | string                                      | Chennai                                         |
| Patient.address.state         | string                                      | Tamil Nadu                                      |
| Patient.address.postalCode    | string                                      | 600001                                          |
| Patient.telecom               | ContactPoint                                | +91-9876543210                                  |
| Patient.communication         | BackboneElement                             | English                                         |
| Patient.communication.language| CodeableConcept                             | en                                              |
| Patient.generalPractitioner   | Reference(Practitioner \| Organization)      | Practitioner/200                                |
| Patient.managingOrganization  | Reference(Organization)                     | Organization/1001                               |
| Patient.link                  | BackboneElement                             | Link to another patient record                  |
| Patient.extension (race)      | Extension                                   | Asian                                           |
| Patient.extension (ethnicity) | Extension                                   | Not Hispanic or Latino                          |
| Patient.extension (birthsex)  | Extension                                   | male                                            |