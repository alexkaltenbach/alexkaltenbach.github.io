# Homepage update — 15 November 2026

The existing Jekyll/AcademicPages site and restrained academic layout are retained.

- Shorter homepage; a Research page with the existing research profile, four selected publications, three companion code repositories and an original research figure.
- Publications include complete author lists, consistent citations and years, separate DOI/arXiv/code links, and distinct article URLs. The Signorini and optimal-insulation algorithm records no longer overwrite the variable-exponent Dirichlet record.
- Corrected the Signorini citation, the unsteady variable-exponent Navier–Stokes DOI, the pressure-paper DOI, the LDG volume number, the 2021 quasi-nonconforming paper's journal and a malformed book date. Final issue years are used when available; online-only articles are labelled accordingly.
- Added a two-page public CV. The three-page publication PDF is generated from the publication collection. Both PDF files contain clickable links.
- Clarified teaching roles and semesters; made existing lecture notes and the four Freiburg slide sets easier to find.
- Excluded unused template pages, examples and maintenance files from the generated website. Added page descriptions, an Open Graph fallback image, social-profile metadata, a simple SVG favicon and GitHub profile links.
- Darker link colours, keyboard focus indicators, a skip link, accessible menu names and expanded states, and earlier stacking of funding logos on smaller screens.

## Sources and editorial decisions

Source repository: `alexkaltenbach/alexkaltenbach.github.io`, base commit `fc33264cb86815e8a6a780b434f2ce79ee6a0a36`.
Bibliographic corrections were checked against DOI/Crossref records and the repository's existing publication PDF.
The Ferdinand-von-Lindemann Prize is dated 2022, consistent with the [University of Freiburg prize list](https://uni-freiburg.de/mathphys/fakultaet/preise-und-auszeichnungen/).
The editorial activity remains described as in the original CV; no unverified role title or appointment dates have been added.
The DOC-TWIN funding entry specifies the funded position without repeating a pay-scale label that conflicted with the job advertisement.
Only existing public lecture notes are linked; the older modelling script from the chat is not added.
The research figure is copied unchanged from the linked companion repository; its source and licence are in `images/research/`.

## Maintenance

Edit the main pages in `_pages/`, research links in `_pages/research.md`, and publication metadata in `_publications/`.
For a new publication, copy a recent record and use a unique `key` and `permalink`. Set `publication_year`, `publication_details`, `citation`, and `sort_key` consistently. Use `doi`, `arxiv_url`, and `code_url` for links. Preserve existing URLs when updating a publication's status.

Regenerate the downloads with `python3 scripts/build_downloads.py` after installing `requirements-dev.txt`. The script uses DejaVu Sans fonts; on macOS supply their directory with `--font-dir`. Update the displayed revision date in the CV page and the script when updating the PDFs.

Build using the existing GitHub Pages dependencies:

```sh
bundle install
bundle exec jekyll build
python3 scripts/check_site.py _site
bundle exec jekyll serve
```

For validation, the site was built with Jekyll 3.10.0 / GitHub Pages 232 and Ruby 3.3.6. A Linux-specific dependency lock was used outside the repository; the original Gemfile and Gemfile.lock are unchanged.
The PDFs were rendered and visually reviewed. The generated HTML, internal links, anchors, asset paths and source permalinks were checked.
Interactive desktop/mobile browser inspection remains to be done locally: the available remote browser could not access the local development preview. Open the local preview at desktop and phone widths before publishing.

Nothing has been pushed to GitHub or published to the live site.
