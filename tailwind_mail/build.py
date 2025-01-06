from pathlib import Path
import sys

def build(output_path: str = "output.html"):
    origin = Path(__file__).parent

    loaded_template = origin / "templates" / "index.html.jinja"
    styles = origin / "static" / "output.css"

    rendered_html = loaded_template.read_text().replace(
        "<link href=\"{{ url_for('static', path='output.css') }}\" rel=\"stylesheet\">",
        f"<style>{styles.read_text()}</style>",
    )

    Path(output_path).write_text(rendered_html)

if __name__ == "__main__":
    # Get the output path from command line args or use default
    output_path = sys.argv[1] if len(sys.argv) > 1 else "output.html"
    build(output_path) 