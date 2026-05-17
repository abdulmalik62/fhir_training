
# Exercise 14: TEFCA Exchange Purpose Decision Tree


flowchart TD
    A[Why is data being requested?]

    A --> B{Is the request for direct patient care?}
    B -->|Yes| T[Treatment]
    B -->|No| C{Is the patient requesting their own records?}

    C -->|Yes| I[Individual Access Services]
    C -->|No| D{Is the request for billing or claims?}

    D -->|Yes| P[Payment]
    D -->|No| E{Is the request for quality improvement or operations?}

    E -->|Yes| O[Health Care Operations]
    E -->|No| F{Is the request for disease reporting or public health monitoring?}

    F -->|Yes| PH[Public Health]
    F -->|No| G{Is it for eligibility or government benefits?}

    G -->|Yes| GB[Government Benefits Determination]
    G -->|No| X[Do not exchange until purpose and authorization are clarified]