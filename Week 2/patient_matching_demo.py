import jellyfish

def normalize(value):
    if value is None:
        return ""
    return str(value).strip().lower()

def name_score(name1, name2):
    return jellyfish.jaro_winkler_similarity(
        normalize(name1),
        normalize(name2)
    )

def exact_score(value1, value2):
    return 1.0 if normalize(value1) == normalize(value2) else 0.0

def patient_match_score(patient1, patient2):
    first_name_score = name_score(patient1.get("first_name"), patient2.get("first_name"))
    last_name_score = name_score(patient1.get("last_name"), patient2.get("last_name"))
    dob_score = exact_score(patient1.get("dob"), patient2.get("dob"))
    address_score = name_score(patient1.get("address"), patient2.get("address"))

    final_score = (
        first_name_score * 0.25 +
        last_name_score * 0.30 +
        dob_score * 0.30 +
        address_score * 0.15
    )

    return {
        "first_name_score": round(first_name_score, 3),
        "last_name_score": round(last_name_score, 3),
        "dob_score": round(dob_score, 3),
        "address_score": round(address_score, 3),
        "final_match_score": round(final_score, 3),
        "match_decision": "Likely Match" if final_score >= 0.85 else "Possible/No Match"
    }

if __name__ == "__main__":
    patient_a = {
        "first_name": "Eve",
        "last_name": "Betterhalf",
        "dob": "1975-05-01",
        "address": "Beaverton OR"
    }

    patient_b = {
        "first_name": "Eva",
        "last_name": "Betterhalf",
        "dob": "1975-05-01",
        "address": "Beaverton Oregon"
    }

    result = patient_match_score(patient_a, patient_b)

    print("Patient Matching Result")
    for key, value in result.items():
        print(f"{key}: {value}")