# Router Topology Map Generator

## Usage:

- Compile dnslookup.c using the Makefile provided.
- Run `./generate <url_1> ... <url_n>` where <url_i> is a DNS name (e.g. www.example.com).
- Include the flag `-m` in the command line arguments to skip the step for removing any intermmediate files created in the process.
  - Example: `./generate www.example.com -m` or `./generate -m www.example.com`.

## Requirements
- Python 3.*
- [Graphviz](https://graphviz.org/)
