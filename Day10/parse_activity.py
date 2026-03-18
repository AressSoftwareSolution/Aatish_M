import json
import yaml
import xml.etree.ElementTree as ET

# ---------------- JSON ----------------
with open("json_example.json") as f:
    json_data = json.load(f)
print("JSON:", json_data)

# ---------------- YAML ----------------
with open("yaml_example.yaml") as f:
    yaml_data = yaml.safe_load(f)
print("YAML:", yaml_data)

# ---------------- XML ----------------
tree = ET.parse("xml_example.xml")
root = tree.getroot()

xml_data = {
    "name": root.find("name").text,
    "age": root.find("age").text
}
print("XML:", xml_data)

# ---------------- CONFIG ----------------
with open("config.json") as f:
    config = json.load(f)

print("Config App Name:", config["app_name"])
print("Debug Mode:", config["debug"])
