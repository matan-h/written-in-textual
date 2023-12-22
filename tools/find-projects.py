import json
from urllib.parse import urlparse
from posixpath import basename
import re
YAML_INT_RE = re.compile( # from so:65574890::65575113
    r"""
    ^(?:[-+]?0b[0-1_]+
    |[-+]?0[0-7_]+
    |[-+]?(?:0|[1-9][0-9_]*)
    |[-+]?0x[0-9a-fA-F_]+
    |[-+]?[1-9][0-9_]*(?::[0-5]?[0-9])+)$""",
    re.X,
)

fmt = """
  - name: {name}
    github_id: {github_id}"""
with open("table2.json") as io:
    data = json.load(io) # {url:<>,stars:<>,url:<>}

for element in data:
    url = element["url"] 
    path = urlparse(url).path[1:] # github_id
    name = basename(path) # name
    if YAML_INT_RE.match(name): # for example 17 or 0x0
      name = f'"{name}"'
    print(fmt.format(name=name,github_id=path))
