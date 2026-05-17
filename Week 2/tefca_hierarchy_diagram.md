# Exercise 13: TEFCA Hierarchy Diagram


flowchart TD
    ONC[ONC / ASTP<br/>Federal Health IT Policy]
    RCE[RCE: The Sequoia Project<br/>Maintains Common Agreement and QHIN process]

    Q1[Epic Nexus<br/>QHIN]
    Q2[CommonWell Health Alliance<br/>QHIN]
    Q3[Health Gorilla<br/>QHIN]

    IOWA[Iowa HIN<br/>Participant]
    
    H1[Hospital A<br/>Subparticipant]
    H2[Clinic B<br/>Subparticipant]
    H3[Public Health Agency<br/>Subparticipant]

    ONC --> RCE
    RCE --> Q1
    RCE --> Q2
    RCE --> Q3

    Q1 <--> Q2
    Q2 <--> Q3
    Q1 <--> Q3

    Q1 --> IOWA
    IOWA --> H1
    IOWA --> H2
    IOWA --> H3

    H1 --> IOWA
    H2 --> IOWA
    H3 --> IOWA