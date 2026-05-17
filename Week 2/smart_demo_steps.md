
---

## Exercise 17: Working SMART Demo Steps

Create `smart_demo_steps.md`:

# Exercise 17: SMART App Launcher Demo

## Goal
Use the SMART App Launcher to simulate launching a healthcare app with SMART authorization.

## Steps

1. Open SMART App Launcher:
   - https://launch.smarthealthit.org

2. Select a sample FHIR server.

3. Select a test patient from the launcher.

4. Choose a sample SMART app.

5. Start the launch.

6. Observe the authorization redirect:
   - The app redirects to the authorization server.
   - The authorization request includes client_id, redirect_uri, scope, state, and audience.

7. Complete authorization.

8. Observe token exchange:
   - The app receives an authorization code.
   - The app exchanges the code for an access token.

9. Observe FHIR API access:
   - The app uses the access token to call the FHIR server.
   - Example: GET /Patient/{id}

## Screenshots to Capture

| Screenshot | What to Capture |
|---|---|
| 1 | SMART launcher configuration |
| 2 | Selected test patient |
| 3 | Authorization/launch step |
| 4 | App displaying patient data |
| 5 | Browser/network evidence of token/FHIR request if available |

## Explanation

SMART on FHIR protects FHIR APIs using OAuth2. The app does not directly access patient data until it receives an access token. The scopes in the authorization request define what data the app is allowed to access.