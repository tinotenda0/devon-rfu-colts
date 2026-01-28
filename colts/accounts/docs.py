from pathlib import Path

from django.conf import settings
from django.http import Http404
from django.shortcuts import render
import markdown


DOCS_DIR = Path(settings.BASE_DIR) / "docs"
md_converter = markdown.Markdown(extensions=["fenced_code", "tables"])


def doc_view(request, slug="index"):
    print("DOC_VIEW CALLED, slug=", slug)
    md_file = DOCS_DIR / f"{slug}.md"
    print("MD FILE PATH:", md_file)

    if not md_file.exists():
        raise Http404(f"Document not found: {md_file}")

    text = md_file.read_text(encoding="utf-8")
    html = md_converter.reset().convert(text)

    return render(
        request,
        "docs/page.html",
        {
            "doc_html": html,
            "slug": slug,
        },
    )
