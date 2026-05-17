
# Exercise 15: Epic Nexus QHIN Research Memo

## Subject
Epic Nexus as a QHIN and implications for CCDForge during FHIR transition.

## Summary
Epic Nexus is Epic’s health information network entity participating in TEFCA as a Qualified Health Information Network (QHIN). Its purpose is to support nationwide exchange of electronic health information under the TEFCA Common Agreement. As a QHIN, Epic Nexus can connect Epic customers and other approved participants into a national exchange framework.

## What Epic Nexus Offers
Epic Nexus offers a TEFCA-aligned exchange pathway for healthcare organizations that use Epic and related interoperability services. It supports exchange across organizations through a national trust framework rather than relying only on local point-to-point interfaces. For providers, this can reduce the need to join many separate networks because QHIN-to-QHIN exchange allows data to move across participating networks.

## Difference from Carequality and CommonWell
Carequality and CommonWell are existing interoperability networks/frameworks that helped healthcare organizations exchange clinical documents and patient data before TEFCA. TEFCA differs because it creates a national common agreement, common governance, and a recognized QHIN structure. Epic Nexus as a QHIN operates within this TEFCA framework, while Carequality/CommonWell historically served as industry-led exchange networks. In practice, TEFCA is intended to create a more standardized national floor for exchange.

## Implications for CCDForge
CCDForge should be designed to handle both legacy document-based exchange and modern FHIR-based exchange. Many TEFCA-related workflows may still involve C-CDA documents, but the industry is moving toward FHIR APIs and structured resources. CCDForge should therefore support:
- C-CDA parsing and conversion to FHIR resources
- Accurate mapping of Problems, Medications, Allergies, Encounters, Results, and Vitals
- Preservation of source document metadata
- FHIR transaction Bundle generation
- Validation against US Core profiles
- Future support for TEFCA/FHIR transition workflows

## Conclusion
Epic Nexus as a QHIN represents the movement from isolated exchange networks toward nationwide trusted exchange. For CCDForge, the key implication is that conversion logic must be reliable, standards-based, and ready for both C-CDA legacy workflows and FHIR-first interoperability.