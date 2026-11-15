#!/usr/bin/env python3
"""Regenerate the public CV and publication list from the website sources.

Install requirements-dev.txt, then run python3 scripts/build_downloads.py.
Pass --font-dir /path/to/DejaVu to use a local DejaVu Sans installation.
"""
from pathlib import Path
from html import escape
import argparse
import datetime
import re
import yaml
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, KeepTogether

ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--font-dir', type=Path, default=Path('/usr/share/fonts/truetype/dejavu'))
args = parser.parse_args()
for suffix, face in [('', 'Regular'), ('-Bold', 'Bold'), ('-Oblique', 'Italic'), ('-BoldOblique', 'BoldItalic')]:
    pdfmetrics.registerFont(TTFont(face, str(args.font_dir / f'DejaVuSans{suffix}.ttf')))
pdfmetrics.registerFontFamily('Regular', normal='Regular', bold='Bold', italic='Italic', boldItalic='BoldItalic')
BLUE = colors.HexColor('#285a72')
GRAY = colors.HexColor('#52616b')
styles = getSampleStyleSheet()
styles.add(ParagraphStyle('Body', fontName='Regular', fontSize=9.5, leading=14, spaceAfter=7, textColor=colors.HexColor('#25313a')))
styles.add(ParagraphStyle('TitlePublic', parent=styles['Body'], fontName='Bold', fontSize=24, leading=29, spaceAfter=7, textColor=BLUE))
styles.add(ParagraphStyle('SectionPublic', parent=styles['Body'], fontName='Bold', fontSize=13, leading=18, spaceBefore=14, spaceAfter=8, textColor=BLUE, keepWithNext=True))
styles.add(ParagraphStyle('SubsectionPublic', parent=styles['Body'], fontName='Bold', fontSize=10.5, leading=15, spaceBefore=8, spaceAfter=6, keepWithNext=True))
styles.add(ParagraphStyle('SmallPublic', parent=styles['Body'], fontSize=8.5, leading=12, textColor=GRAY))
styles.add(ParagraphStyle('Bibliography', parent=styles['Body'], fontSize=9, leading=13, spaceAfter=7))

def markdown_inline(s):
    s = escape(s)
    s = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', lambda m: '<a href="'+ ('https://alexkaltenbach.github.io'+m[2] if m[2].startswith('/') else m[2]) +'" color="#285a72">'+m[1]+'</a>', s)
    s = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', s)
    return re.sub(r'\*([^*]+)\*', r'<i>\1</i>', s)

def footer(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(colors.HexColor('#dce3e7'))
    canvas.line(46, 42, A4[0]-46, 42)
    canvas.setFont('Regular', 8)
    canvas.setFillColor(GRAY)
    canvas.drawString(46, 29, 'Alex Kaltenbach · Updated 15 November 2026')
    canvas.drawRightString(A4[0]-46, 29, str(doc.page))
    canvas.restoreState()

def build(filename, title, story):
    doc = SimpleDocTemplate(str(ROOT/'files'/filename), pagesize=A4, topMargin=43, bottomMargin=55, leftMargin=46, rightMargin=46, title=title, author='Alex Kaltenbach', pageCompression=1)
    doc.build(story, onFirstPage=footer, onLaterPages=footer)

cv = [Paragraph('Alex Kaltenbach', styles['TitlePublic']),
      Paragraph('Curriculum vitae', styles['SubsectionPublic']),
      Paragraph('Numerical analysis · Nonlinear PDEs · Scientific computing', styles['Body']),
      Paragraph('<a href="mailto:kaltenbach@math.tu-berlin.de" color="#285a72">kaltenbach@math.tu-berlin.de</a> · <a href="https://alexkaltenbach.github.io" color="#285a72">alexkaltenbach.github.io</a>', styles['SmallPublic'])]
source=(ROOT/'_pages/cv.md').read_text().split('## Work Experience',1)[1]
source='## Work Experience'+source
for block in re.split(r'(?=^## )', source, flags=re.M):
    if not block.strip(): continue
    lines=block.strip().splitlines()
    heading=lines[0][3:].strip()
    if heading=='Editorial Activity':
        cv += [PageBreak(), Paragraph('Research and academic service',styles['TitlePublic']),
               Paragraph('Research focus',styles['SectionPublic']),
               Paragraph('Numerical analysis of nonlinear PDEs and nonsmooth variational problems; convex duality and error control; finite element and discontinuous Galerkin methods; non-Newtonian and smart fluids.', styles['Body']),
               Paragraph('Funded research projects',styles['SectionPublic']),
               Paragraph('<b>LenhTVHM · DFG–NSFC, 2027–2029.</b> Learning-enhanced robust iterative methods for non-smooth and constrained variational problems. Scientific co-lead with Sören Bartels, Yi Zhu and Shuo Yang. DFG share: €201,800 plus 22% programme allowance.',styles['Body']),
               Paragraph('<b>DOC-TWIN · MATH+, 2027–2028.</b> Duality-based error control for optimal control problems in digital-twin-based structural health monitoring. Scientific co-lead with Michael Hintermüller and Harbir Antil (associated). Funding for one full-time research position for two years.',styles['Body'])]
    cv.append(Paragraph(heading,styles['SectionPublic']))
    entries = re.split(r'^\* ', '\n'.join(lines[1:]).strip(), flags=re.M)
    entries = [e.strip() for e in entries if e.strip()]
    if heading=='Reviewer Activity':
        cv.append(Paragraph('; '.join(markdown_inline(e.strip()) for e in entries)+'.',styles['Body']))
    else:
        for entry in entries:
            text='<br/>'.join(markdown_inline(line.strip()) for line in entry.splitlines() if line.strip())
            cv.append(Paragraph(text,styles['Body']))
build('Alex_Kaltenbach_CV.pdf','Alex Kaltenbach — Curriculum vitae',cv)

pubs=[]
for path in (ROOT/'_publications').glob('*.md'):
    pubs.append(yaml.safe_load(path.read_text().split('---',2)[1]))
pubs.sort(key=lambda p:p['sort_key'],reverse=True)
story=[Paragraph('Publications',styles['TitlePublic']),Paragraph('Alex Kaltenbach',styles['SubsectionPublic']),Paragraph('<a href="https://alexkaltenbach.github.io/publications/" color="#285a72">alexkaltenbach.github.io/publications/</a>',styles['SmallPublic'])]
groups=[('unpublished','Preprints'),('accepted','Accepted / forthcoming'),('published','Peer-reviewed publications'),('monograph_book','Books'),('monograph_book_contribution','Book chapters and proceedings'),('monograph_thesis','Theses')]
for status,heading in groups:
    story.append(Paragraph(heading,styles['SectionPublic']))
    previous_year=None
    for pub in [p for p in pubs if p['status']==status]:
        if status=='published' and previous_year!=pub['publication_year']:
            previous_year=pub['publication_year']
            story.append(Paragraph(str(previous_year),styles['SubsectionPublic']))
        links=[]
        if pub.get('doi'): links.append(('https://doi.org/'+pub['doi'],'DOI'))
        if pub.get('arxiv_url'): links.append((pub['arxiv_url'],'arXiv'))
        elif pub.get('paperurl') and not pub.get('doi'): links.append((pub['paperurl'],'Read paper'))
        if pub.get('code_url'): links.append((pub['code_url'],'Code'))
        suffix=' '.join('<a href="'+escape(url,quote=True)+'" color="#285a72">['+label+']</a>' for url,label in links)
        story.append(Paragraph(pub['citation']+' '+suffix,styles['Bibliography']))
    if status=='monograph_thesis':
        for title,year,filename in [('Verallgemeinerte nichtlineare Evolutionsgleichungen','2019','Kaltenbach_Masterarbeit_2019.pdf'),('Nichtlineare Evolutionsgleichungen','2017','Kaltenbach_Bachelorarbeit_2017.pdf')]:
            kind="Master’s" if year=='2019' else "Bachelor’s"
            story.append(Paragraph(f'Kaltenbach, A. <i>{title}.</i> {kind} thesis, University of Freiburg ({year}). <a href="https://alexkaltenbach.github.io/files/{filename}" color="#285a72">[PDF, corrected version]</a>',styles['Bibliography']))
build('PubList.pdf','Alex Kaltenbach — Publications',story)
print('Updated files/Alex_Kaltenbach_CV.pdf and files/PubList.pdf')
