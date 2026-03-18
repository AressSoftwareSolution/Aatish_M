import json
import yaml
import xml.etree.ElementTree as ET


# -------- Load JSON --------
with open("json_example.json") as f:
    data = json.load(f)

print("Original JSON:", data)


# -------- Convert to YAML --------
with open("converted.yaml", "w") as f:
    yaml.dump(data, f)

print("Converted to YAML ✔")


# -------- Convert to XML --------
root = ET.Element("person")

for key, value in data.items():
    child = ET.SubElement(root, key)
    child.text = str(value)

tree = ET.ElementTree(root)
tree.write("converted.xml")

print("Converted to XML ✔")
