from pathlib import Path

from django.http import Http404
from django.shortcuts import render
import markdown

BASE_DIR = Path(__file__).resolve().parent.parent
DOCS_DIR = BASE_DIR / "docs"   # create this folder

md = markdown.Markdown(extensions=["fenced_code", "tables"])

def doc_view(request, slug="index"):
    """
    Render docs/<slug>.md inside the main site layout.
    """
    md_file = DOCS_DIR / f"{slug}.md"
    if not md_file.exists():
        raise Http404("Document not found")

    text = md_file.read_text(encoding="utf-8")
    html = md.convert(text)

    return render(
        request,
        "docs/page.html",
        {
            "doc_html": html,
            "slug": slug,
        },
    )
