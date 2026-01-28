from pathlib import Path

from django.conf import settings
from django.http import Http404
from django.shortcuts import render
import markdown
from bs4 import BeautifulSoup

DOCS_DIR = Path(settings.BASE_DIR) / "docs"

# Initialize markdown with more extensions
md_converter = markdown.Markdown(
    extensions=[
        "fenced_code",
        "tables",
        "nl2br",  # Convert newlines to <br>
        "sane_lists",  # Better list handling
    ]
)


def add_bootstrap_classes(html_content):
    """Add Bootstrap classes to HTML elements for better styling."""
    soup = BeautifulSoup(html_content, 'html.parser')

    # Add Bootstrap table classes
    for table in soup.find_all('table'):
        table['class'] = table.get('class', []) + ['table', 'table-striped', 'table-bordered', 'table-hover', 'mb-4']

    # Add styling to code blocks (inline code)
    for code in soup.find_all('code'):
        if code.parent.name != 'pre':
            code['class'] = code.get('class', []) + ['bg-light', 'text-danger', 'px-2', 'py-1', 'rounded']

    # Add styling to pre blocks (code blocks)
    for pre in soup.find_all('pre'):
        pre['class'] = pre.get('class', []) + ['bg-light', 'p-3', 'rounded', 'border']

    # Add Bootstrap alert classes to blockquotes
    for blockquote in soup.find_all('blockquote'):
        blockquote['class'] = blockquote.get('class', []) + ['alert', 'alert-info', 'border-start', 'border-primary',
                                                             'border-4']

    return str(soup)


def doc_view(request, slug="index"):
    print("DOC_VIEW CALLED, slug=", slug)
    md_file = DOCS_DIR / f"{slug}.md"
    print("MD FILE PATH:", md_file)

    if not md_file.exists():
        raise Http404(f"Document not found: {md_file}")

    text = md_file.read_text(encoding="utf-8")
    html = md_converter.reset().convert(text)

    # Add Bootstrap classes to HTML elements
    html = add_bootstrap_classes(html)

    return render(
        request,
        "docs/page.html",
        {
            "doc_html": html,
            "slug": slug,
        },
    )
