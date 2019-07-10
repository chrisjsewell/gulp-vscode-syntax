import json
import yaml

with open("help_file.txt") as handle:
    lines = handle.readlines()

snippets = {}

len_lines = len(lines)

for i, line in enumerate(lines):
    if line.startswith("Type"):
        name = lines[i - 1].strip()
        vtype = line.split()[1].lower()
        ident = "{}-{}".format(vtype, name)
        j = i + 1
        description = []
        while j < len_lines and not lines[j].startswith("Type"):
            dline = lines[j].rstrip()
            for subhead in ["Use", "See also", "Format", "Default"]:
                if dline.startswith(subhead):
                    dline = "- " + subhead + ":" + dline[len(subhead):]
            description.append(dline)
            j += 1
        snippets[ident] = {
            "prefix": ident,
            "body": name,
            "description": "\n".join(description)
        }

with open("help_file_output_types.yaml") as handle:
    output_data = yaml.load(handle)

for name, descript in output_data.items():
    ident = "output-" + name
    snippets[ident] = {
        "prefix": ident,
        "body": "output {} ${{0:filename}}".format(name),
        "description": descript
    }

with open("snippets/gulp-snippets.code-snippets", "w") as handle:
    json.dump(snippets, handle, indent=2)
