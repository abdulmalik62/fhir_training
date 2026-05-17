# Exercise 18: SMART Scope Reference Sheet

## Patient vs User Scopes

| Scope Type | Meaning | Example |
|---|---|---|
| patient scope | Access limited to a specific patient context | patient/Patient.read |
| user scope | Access based on logged-in user privileges | user/Patient.read |
| system scope | Backend service access without interactive user | system/Patient.read |

## Read vs Write Permissions

| Permission | Meaning | Example |
|---|---|---|
| .read | Read/search resources | patient/Observation.read |
| .write | Create/update/delete resources | user/MedicationRequest.write |
| .* | Read and write | patient/*.read |

## Resource-Level vs Wildcard

| Type | Example | Meaning |
|---|---|---|
| Resource-level | patient/Condition.read | Read Condition resources for current patient |
| Wildcard resource | patient/*.read | Read all allowed resource types for current patient |
| User wildcard | user/*.read | Read all allowed resources based on user access |

## Common Use Cases

| Use Case | Example Scope |
|---|---|
| Patient app reading own demographics | patient/Patient.read |
| Patient app reading labs/vitals | patient/Observation.read |
| Patient app reading problems | patient/Condition.read |
| Patient app reading medications | patient/MedicationRequest.read |
| Clinician app reading chart data | user/Patient.read user/Observation.read user/Condition.read |
| App needing patient context | launch/patient |
| App launched from EHR | launch |
| App requesting identity information | openid profile |
| App requesting refresh token | offline_access |