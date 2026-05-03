from lxml import etree

# -----------------------------
# Load XML File
# -----------------------------
tree = etree.parse("CCD.xml")
root = tree.getroot()

# -----------------------------
# Namespace (CRITICAL)
# -----------------------------
ns = {'hl7': 'urn:hl7-org:v3'}

# -----------------------------
# 1. Extract Patient Name
# -----------------------------
name = root.xpath("//hl7:recordTarget//hl7:patient//hl7:name[1]", namespaces=ns)

print("\n=== PATIENT DETAILS ===")

if name:
    given = name[0].xpath("hl7:given/text()", namespaces=ns)
    family = name[0].xpath("hl7:family/text()", namespaces=ns)
    print("Patient Name:", " ".join(given + family))
else:
    print("Patient Name: Not Found")

# -----------------------------
# 2. Extract DOB
# -----------------------------
dob = root.xpath("//hl7:birthTime/@value", namespaces=ns)
print("DOB:", dob[0] if dob else "Not Found")

# -----------------------------
# 3. List Section Titles
# -----------------------------
sections = root.xpath("//hl7:section/hl7:title/text()", namespaces=ns)

print("\n=== SECTIONS ===")
for sec in sections:
    print("-", sec)

# -----------------------------
# 4. Extract PROBLEMS (Context-based)
# -----------------------------
problems = root.xpath(
    "//hl7:section[hl7:title='PROBLEMS']//hl7:observation//hl7:value/@displayName",
    namespaces=ns
)

print("\n=== PROBLEMS ===")
if problems:
    for p in set(problems):  # remove duplicates
        print("-", p)
else:
    print("No problems found")

# -----------------------------
# 5. Extract MEDICATIONS (Correct Path)
# -----------------------------
medications = root.xpath(
    "//hl7:section[hl7:title='MEDICATIONS']//hl7:manufacturedMaterial/hl7:code/@displayName",
    namespaces=ns
)

print("\n=== MEDICATIONS ===")
if medications:
    for m in set(medications):  # remove duplicates
        print("-", m)
else:
    print("No medications found")