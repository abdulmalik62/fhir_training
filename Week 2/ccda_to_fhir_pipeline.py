from lxml import etree
import requests
import json
from datetime import datetime

FHIR_BASE_URL = "http://localhost:8080/fhir"
CCD_FILE = "CCD.xml"

ns = {"hl7": "urn:hl7-org:v3"}

def format_ccda_date(value):
    if not value:
        return None
    try:
        return datetime.strptime(value[:8], "%Y%m%d").strftime("%Y-%m-%d")
    except Exception:
        return value

def parse_ccda(path):
    tree = etree.parse(path)
    root = tree.getroot()

    name = root.xpath("//hl7:recordTarget//hl7:patient//hl7:name[1]", namespaces=ns)
    given = name[0].xpath("hl7:given/text()", namespaces=ns) if name else []
    family = name[0].xpath("hl7:family/text()", namespaces=ns) if name else []

    dob = root.xpath("//hl7:birthTime/@value", namespaces=ns)
    gender = root.xpath("//hl7:administrativeGenderCode/@code", namespaces=ns)

    problems = root.xpath(
        "//hl7:section[hl7:title='PROBLEMS']//hl7:observation//hl7:value/@displayName",
        namespaces=ns
    )

    medications = root.xpath(
        "//hl7:section[hl7:title='MEDICATIONS']//hl7:manufacturedMaterial/hl7:code/@displayName",
        namespaces=ns
    )

    allergies = root.xpath(
        "//hl7:section[hl7:title='ALLERGIES AND ADVERSE REACTIONS']//hl7:observation//hl7:value/@displayName",
        namespaces=ns
    )

    return {
        "given": given,
        "family": family,
        "birthDate": format_ccda_date(dob[0]) if dob else None,
        "gender": "female" if gender and gender[0] == "F" else "male" if gender and gender[0] == "M" else "unknown",
        "problems": sorted(set(problems)),
        "medications": sorted(set(medications)),
        "allergies": sorted(set(allergies))
    }

def build_transaction_bundle(data):
    bundle = {
        "resourceType": "Bundle",
        "type": "transaction",
        "entry": []
    }

    patient_resource = {
        "resourceType": "Patient",
        "name": [
            {
                "family": data["family"][0] if data["family"] else "Unknown",
                "given": data["given"] if data["given"] else ["Unknown"]
            }
        ],
        "gender": data["gender"],
        "birthDate": data["birthDate"]
    }

    bundle["entry"].append({
        "fullUrl": "urn:uuid:patient-1",
        "resource": patient_resource,
        "request": {
            "method": "POST",
            "url": "Patient"
        }
    })

    for index, problem in enumerate(data["problems"], start=1):
        condition = {
            "resourceType": "Condition",
            "clinicalStatus": {
                "text": "active"
            },
            "code": {
                "text": problem
            },
            "subject": {
                "reference": "urn:uuid:patient-1"
            }
        }

        bundle["entry"].append({
            "fullUrl": f"urn:uuid:condition-{index}",
            "resource": condition,
            "request": {
                "method": "POST",
                "url": "Condition"
            }
        })

    for index, medication in enumerate(data["medications"], start=1):
        med_request = {
            "resourceType": "MedicationRequest",
            "status": "active",
            "intent": "order",
            "medicationCodeableConcept": {
                "text": medication
            },
            "subject": {
                "reference": "urn:uuid:patient-1"
            }
        }

        bundle["entry"].append({
            "fullUrl": f"urn:uuid:medication-{index}",
            "resource": med_request,
            "request": {
                "method": "POST",
                "url": "MedicationRequest"
            }
        })

    for index, allergy in enumerate(data["allergies"], start=1):
        allergy_resource = {
            "resourceType": "AllergyIntolerance",
            "clinicalStatus": {
                "text": "active"
            },
            "code": {
                "text": allergy
            },
            "patient": {
                "reference": "urn:uuid:patient-1"
            }
        }

        bundle["entry"].append({
            "fullUrl": f"urn:uuid:allergy-{index}",
            "resource": allergy_resource,
            "request": {
                "method": "POST",
                "url": "AllergyIntolerance"
            }
        })

    return bundle

def post_bundle(bundle):
    response = requests.post(
        FHIR_BASE_URL,
        headers={"Content-Type": "application/fhir+json"},
        data=json.dumps(bundle, indent=2)
    )

    print("Status:", response.status_code)
    print(response.text)

if __name__ == "__main__":
    data = parse_ccda(CCD_FILE)

    print("Extracted C-CDA Data:")
    print(json.dumps(data, indent=2))

    bundle = build_transaction_bundle(data)

    with open("transaction_bundle.json", "w", encoding="utf-8") as f:
        json.dump(bundle, f, indent=2)

    print("\nFHIR transaction bundle saved as transaction_bundle.json")

    post_bundle(bundle)