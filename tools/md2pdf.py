import re, sys, markdown
from weasyprint import HTML, CSS

CSS_TXT = """
@page { size: A4; margin: 20mm 18mm 18mm 18mm;
  @bottom-center { content: counter(page) " / " counter(pages); font-size: 8pt; color:#666; font-family: "DejaVu Sans", sans-serif; }
  @top-right { content: string(doctitle); font-size: 8pt; color:#888; font-family:"DejaVu Sans",sans-serif; } }
body { font-family: "DejaVu Serif", serif; font-size: 9.5pt; line-height: 1.45; color:#111; }
h1 { string-set: doctitle content(); font-family:"DejaVu Sans",sans-serif; font-size: 17pt; margin:0 0 2mm 0;
     border-bottom: 1.6pt solid #003366; padding-bottom: 2mm; color:#003366; }
h2 { font-family:"DejaVu Sans",sans-serif; font-size: 12pt; margin:6mm 0 2mm 0; color:#003366;
     border-bottom: 0.4pt solid #bbb; padding-bottom: 1mm; page-break-after: avoid; }
h3 { font-family:"DejaVu Sans",sans-serif; font-size: 10.5pt; margin:4mm 0 1.5mm 0; page-break-after: avoid; }
p { margin: 0 0 2.2mm 0; }
table { border-collapse: collapse; width: 100%; margin: 2mm 0 4mm 0; font-size: 8.5pt; }
thead { display: table-header-group; }
tr { page-break-inside: avoid; }
table.meta { margin-top: 3mm; margin-bottom: 5mm; font-size: 9pt; }
table.meta thead { display: none; }
table.meta td:first-child { width: 32mm; background:#eef2f7; font-family:"DejaVu Sans",sans-serif; font-size:8.2pt; }
table.sig td { height: 14mm; vertical-align: top; }
table.sig { page-break-inside: avoid; }
th { background: #eef2f7; border: 0.4pt solid #99a; padding: 1.4mm 1.8mm; text-align: left;
     font-family:"DejaVu Sans",sans-serif; font-size:8.2pt; }
td { border: 0.4pt solid #99a; padding: 1.4mm 1.8mm; vertical-align: top; }
tr:nth-child(even) td { background: #fafbfc; }
blockquote { border-left: 2.4pt solid #003366; background:#f4f7fa; margin: 2.5mm 0; padding: 2mm 3mm; font-size: 8.8pt; }
blockquote p { margin: 0 0 1.5mm 0; }
blockquote p:last-child { margin-bottom: 0; }
ul, ol { margin: 0 0 2.5mm 0; padding-left: 6mm; }
li { margin-bottom: 1mm; }
code { font-family:"DejaVu Sans Mono", monospace; font-size: 8.5pt; background:#f0f0f0; padding:0 1mm; }
strong { color:#000; }
hr { border:none; border-top:0.4pt solid #ccc; margin: 4mm 0; }
.sigrow td { height: 13mm; }
"""

def clean(md):
    md = re.sub(r'^---\n.*?\n---\n', '', md, flags=re.S)      # frontmatter raus
    md = re.sub(r'\[\[([^\]|]+)\|([^\]]+)\]\]', r'\2', md)     # [[a|b]] -> b
    md = re.sub(r'\[\[([^\]]+)\]\]', r'\1', md)                # [[a]] -> a
    md = md.replace('- [x] ', '- \u2714 ').replace('- [ ] ', '- \u25a1 ')
    md = re.sub(r'^\u2192 Sprintnotizen:.*$', '', md, flags=re.M)  # Repo-Navigation nicht ins PDF
    # Blockzitate, die mit "> [!vault]" beginnen, sind reine Vault-Notizen -> nicht ins PDF
    out, lines, i = [], md.split('\n'), 0
    while i < len(lines):
        if lines[i].lstrip().startswith('>') and '[!vault]' in lines[i]:
            while i < len(lines) and lines[i].lstrip().startswith('>'):
                i += 1
            while i < len(lines) and not lines[i].strip():
                i += 1
            continue
        out.append(lines[i]); i += 1
    md = '\n'.join(out)
    return md.strip()

src, out = sys.argv[1], sys.argv[2]
html_body = markdown.markdown(clean(open(src, encoding='utf-8').read()),
                              extensions=['tables', 'sane_lists', 'attr_list'])
# erste Tabelle = Kopfdaten
html_body = html_body.replace('<table>', '<table class="meta">', 1)
if '--sig' in sys.argv:
    i = html_body.rfind('<table>')
    if i != -1:
        html_body = html_body[:i] + '<table class="sig">' + html_body[i+len('<table>'):]
html = f'<html><head><meta charset="utf-8"></head><body>{html_body}</body></html>'
HTML(string=html).write_pdf(out, stylesheets=[CSS(string=CSS_TXT)])
print("geschrieben:", out)
