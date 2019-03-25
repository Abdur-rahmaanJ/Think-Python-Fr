import argparse
import sys

import jinja2
import markdown

TEMPLATE = """<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="utf-8">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
    <link rel="stylesheet"
      href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/9.15.6/styles/atelier-forest-light.min.css">
    <style>

    </style>
</head>
<body>
<div class="container">

{{content}}

<script src="http://cdnjs.cloudflare.com/ajax/libs/highlight.js/9.15.6/highlight.min.js"></script>
<script>hljs.initHighlightingOnLoad();</script>
</div>
</body>
</html>
"""

'''
def parse_args(args=None):
    d = 'Make a complete, styled HTML document from a Markdown file.'
    parser = argparse.ArgumentParser(description=d)
    parser.add_argument('mdfile', type=argparse.FileType('r'), nargs='?',
                        default=sys.stdin,
                        help='File to convert. Defaults to stdin.')
    parser.add_argument('-o', '--out', type=argparse.FileType('w'),
                        default=sys.stdout,
                        help='Output file name. Defaults to stdout.')
    return parser.parse_args(args)


def main(args=None):
    print('[x] capturing args ...')
    args = parse_args(args)
    
    md = args.mdfile.read()
    print('[x] fetching extentions ...')
    extensions = ['extra', 'smarty']
    print('[x] converting to html ...')
    html = markdown.markdown(md, extensions=extensions, output_format='html5')
    print('[x] rendering with jinja ...')
    doc = jinja2.Template(TEMPLATE).render(content=html)
    print('[x] writing ...')
    args.out.write(doc)
    print('Terminated')
'''

def main(args=None):
    print('[x] reading md file ...')
    with open('completed_upto_now.md', 'r', encoding='utf8') as f:
        md = f.read()
    print('[x] fetching extentions ...')
    extensions = ['extra', 'smarty']
    print('[x] converting to html ...')
    html = markdown.markdown(md, extensions=extensions, output_format='html5')
    print('[x] rendering template ...')
    doc = jinja2.Template(TEMPLATE).render(content=html)
    print('[x] writing ...')
    with open('completed_upto_now.html', 'w+', encoding='utf8') as f:
        f.write(doc)
    print('Terminated')


if __name__ == '__main__':
    sys.exit(main())