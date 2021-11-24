#!/usr/bin/env python

import os
from string import Template
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: format_template <input-file>")
        sys.exit(1)
    with open(sys.argv[1], 'r') as file:
        template = Template(file.read())
        try:
            print(template.substitute(os.environ))
        except KeyError as key:
            print("\nError formatting template: undefined environment variable", key, file=sys.stderr)
            sys.exit(1)




