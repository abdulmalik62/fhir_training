# Exercise 16: SMART on FHIR Launch Flow Diagrams

## 1. Standalone Launch Flow


sequenceDiagram
    participant User
    participant App
    participant Auth as Authorization Server
    participant FHIR as FHIR Server

    User->>App: Open patient app
    App->>Auth: Redirect to authorize endpoint with client_id, redirect_uri, scope, state, aud
    Auth->>User: Login and consent
    User->>Auth: Approves access
    Auth-->>App: Redirect back with authorization code
    App->>Auth: Exchange code for access token
    Auth-->>App: Access token + patient context
    App->>FHIR: GET /Patient/{id} with Bearer token
    FHIR-->>App: Patient resource