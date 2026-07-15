"""
Document Builder Demo (Builder Design Pattern)

- DocumentBuilder: abstract builder interface
- PlainTextBuilder, HTMLBuilder, PDFBuilderSimulated: concrete builders
- Director: re-usable construction sequences
- Demo: builds the same logical document in three formats

This example keeps the "PDF" builder simulated (text output that
illustrates how a real PDF generator would receive the content).
To produce real PDFs, replace the simulated builder with one that
uses a PDF library (e.g., reportlab).
"""

from abc import ABC, abstractmethod
from typing import List


class DocumentProduct:
    """Simple product wrapper. Builders produce this."""
    def __init__(self, content: str, metadata: dict = None):
        self.content = content
        self.metadata = metadata or {}

    def __str__(self):
        return self.content

    def save(self, filename: str):
        with open(filename, "w", encoding="utf-8") as f:
            f.write(self.content)


class DocumentBuilder(ABC):
    """Abstract builder: defines the steps to build a document."""
    @abstractmethod
    def start_document(self) -> None:
        pass

    @abstractmethod
    def set_title(self, title: str) -> None:
        pass

    @abstractmethod
    def add_header(self, header: str, level: int = 1) -> None:
        pass

    @abstractmethod
    def add_paragraph(self, text: str) -> None:
        pass

    @abstractmethod
    def add_list(self, items: List[str]) -> None:
        pass

    @abstractmethod
    def set_footer(self, footer: str) -> None:
        pass

    @abstractmethod
    def get_result(self) -> DocumentProduct:
        pass


class PlainTextBuilder(DocumentBuilder):
    """Concrete builder for plain text output."""
    def __init__(self):
        self.parts: List[str] = []
        self.metadata = {}

    def start_document(self) -> None:
        self.parts = []
        self.metadata = {}

    def set_title(self, title: str) -> None:
        self.metadata["title"] = title
        self.parts.append(title.upper())
        self.parts.append("=" * len(title))

    def add_header(self, header: str, level: int = 1) -> None:
        prefix = ("#" * level) + " "
        self.parts.append(f"\n{prefix}{header}")

    def add_paragraph(self, text: str) -> None:
        self.parts.append(f"\n{text}")

    def add_list(self, items: List[str]) -> None:
        for item in items:
            self.parts.append(f" - {item}")
        self.parts.append("")  # trailing newline

    def set_footer(self, footer: str) -> None:
        self.parts.append("\n" + ("-" * 20))
        self.parts.append(footer)

    def get_result(self) -> DocumentProduct:
        content = "\n".join(self.parts).strip() + "\n"
        return DocumentProduct(content, self.metadata)


class HTMLBuilder(DocumentBuilder):
    """Concrete builder for HTML output."""
    def __init__(self):
        self.parts: List[str] = []
        self.metadata = {}

    def start_document(self) -> None:
        self.parts = ['<!doctype html>', '<html>', '<head>', '<meta charset="utf-8">']
        self.metadata = {}

    def set_title(self, title: str) -> None:
        self.metadata["title"] = title
        self.parts.append(f"<title>{title}</title>")
        self.parts.append("</head>")
        self.parts.append("<body>")
        self.parts.append(f"<h1>{title}</h1>")

    def add_header(self, header: str, level: int = 1) -> None:
        level = max(1, min(6, level))
        self.parts.append(f"<h{level}>{header}</h{level}>")

    def add_paragraph(self, text: str) -> None:
        self.parts.append(f"<p>{text}</p>")

    def add_list(self, items: List[str]) -> None:
        self.parts.append("<ul>")
        for item in items:
            self.parts.append(f"  <li>{item}</li>")
        self.parts.append("</ul>")

    def set_footer(self, footer: str) -> None:
        self.parts.append(f"<footer>{footer}</footer>")
        self.parts.append("</body>")
        self.parts.append("</html>")

    def get_result(self) -> DocumentProduct:
        content = "\n".join(self.parts)
        return DocumentProduct(content, self.metadata)


class PDFBuilderSimulated(DocumentBuilder):
    """
    Simulated PDF builder. Instead of creating a binary PDF, this builder
    produces a string that demonstrates how content would be organized
    for a PDF generator. In a real implementation you'd call a PDF library
    (e.g., reportlab, wkhtmltopdf) here.
    """
    def __init__(self):
        self.commands: List[str] = []
        self.metadata = {}

    def start_document(self) -> None:
        self.commands = ["[PDF START]"]
        self.metadata = {}

    def set_title(self, title: str) -> None:
        self.metadata["title"] = title
        self.commands.append(f"TITLE: {title!r} (font=Bold, size=20, align=center)")
        self.commands.append("ADD_SPACING: 12")

    def add_header(self, header: str, level: int = 1) -> None:
        size = max(16 - (level - 1) * 2, 10)
        self.commands.append(f"HEADER: {header!r} (size={size})")

    def add_paragraph(self, text: str) -> None:
        self.commands.append(f"PARAGRAPH: {text!r}")

    def add_list(self, items: List[str]) -> None:
        for idx, item in enumerate(items, 1):
            self.commands.append(f"LIST_ITEM: {idx}. {item!r}")

    def set_footer(self, footer: str) -> None:
        self.commands.append("ADD_SPACING: 10")
        self.commands.append(f"FOOTER: {footer!r} (align=center)")
        self.commands.append("[PDF END]")

    def get_result(self) -> DocumentProduct:
        # The content is a textual representation of PDF commands.
        content = "\n".join(self.commands)
        return DocumentProduct(content, self.metadata)


class Director:
    """Director knows common sequences to build documents."""
    def __init__(self, builder: DocumentBuilder):
        self.builder = builder

    def construct_report(self, title: str, intro: str, bullets: List[str], conclusion: str):
        self.builder.start_document()
        self.builder.set_title(title)
        self.builder.add_header("Introduction", level=2)
        self.builder.add_paragraph(intro)
        self.builder.add_header("Key Points", level=2)
        self.builder.add_list(bullets)
        self.builder.add_header("Conclusion", level=2)
        self.builder.add_paragraph(conclusion)
        self.builder.set_footer("Generated by DocumentBuilder Demo")

    def construct_short_note(self, title: str, note: str):
        self.builder.start_document()
        self.builder.set_title(title)
        self.builder.add_paragraph(note)
        self.builder.set_footer("Short note generated")


def demo():
    title = "Builder Pattern Demo"
    intro = "This document illustrates the Builder Design Pattern by producing multiple formats."
    bullets = ["Decouple construction and representation", "Support multiple output formats", "Easy to extend new formats"]
    conclusion = "Builder lets you vary the internal representation without changing the construction logic."

    # Plain text
    pt_builder = PlainTextBuilder()
    director = Director(pt_builder)
    director.construct_report(title, intro, bullets, conclusion)
    pt_doc = pt_builder.get_result()
    print("=== Plain Text Output ===")
    print(pt_doc.content)

    # HTML
    html_builder = HTMLBuilder()
    director = Director(html_builder)
    director.construct_report(title, intro, bullets, conclusion)
    html_doc = html_builder.get_result()
    print("\n=== HTML Output ===")
    print(html_doc.content)

    # Simulated PDF
    pdf_builder = PDFBuilderSimulated()
    director = Director(pdf_builder)
    director.construct_report(title, intro, bullets, conclusion)
    pdf_doc = pdf_builder.get_result()
    print("\n=== Simulated PDF Output (commands) ===")
    print(pdf_doc.content)


if __name__ == "__main__":
    demo()
