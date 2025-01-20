import xml.etree.ElementTree as ET
import pandas as pd

tree = ET.parse('input.xml')

root = tree.getroot()

# Extract data
rows = []
for level_list in root.findall("levelList"):
    level = level_list.find("level")
    name = level.find("name").text
    attributes = level.find("attributes")
    row = [name]
    for attribute in attributes.findall("attribute"):
        att_name = attribute.find("name").text
        att_value = attribute.find("value").text
        row.extend([att_name, att_value])
    rows.append(row)

# Convert to DataFrame
df = pd.DataFrame(rows)

# Save to CSV
csv_file = "output.csv"
df.to_csv(csv_file, index=False, header=False)

print(f"CSV file saved as {csv_file}")
