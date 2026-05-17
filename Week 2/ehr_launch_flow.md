sequenceDiagram
    participant Clinician
    participant EHR
    participant App
    participant Auth as Authorization Server
    participant FHIR as FHIR Server

    Clinician->>EHR: Opens app inside patient chart
    EHR->>App: Launch URL with launch parameter
    App->>Auth: Redirect to authorize endpoint with launch, scope, aud
    Auth->>Clinician: Authenticate/authorize
    Auth-->>App: Authorization code
    App->>Auth: Exchange code for token
    Auth-->>App: Access token + patient + encounter context
    App->>FHIR: Request patient/clinical data with Bearer token
    FHIR-->>App: FHIR resources