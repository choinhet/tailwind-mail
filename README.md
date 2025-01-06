# Tailwind Mail

A simple toolkit for building email templates using Tailwind CSS.

## Prerequisites

- Python 3.9+
- [uv](https://github.com/astral-sh/uv) - Fast Python package installer and resolver
- [Task](https://taskfile.dev/) - Task runner

## Getting Started

1. Clone the repository:

```sh
git clone https://github.com/choinhet/tailwind-mail.git
cd tailwind-mail
```

2. Install dependencies:

```sh
uv sync
```

## Usage

### Development Mode

To start the development server, run:

```sh
task dev
```

This will:
- Start the FastAPI development server at http://localhost:8000
- Watch for Tailwind CSS changes and rebuild automatically
- Live reload the preview when you make changes

### Creating Your Email

Edit the template at `tailwind_mail/templates/index.html.jinja`. This file supports:
- Full Tailwind CSS classes
- Jinja2 templating
- Regular HTML

### Building the Final Email

To generate the final HTML with inlined styles:

```sh
task build
```

Or you can specify the output path:

```sh
task build -- my_custom_output.html
```

Alternative syntax:

```sh
task build OUTPUT=my_custom_output.html
```

This will generate the final HTML and save it to `my_custom_output.html`.

## Tips

1. The development server provides a live preview that updates as you code
2. All Tailwind CSS features are supported
3. The final build will inline all styles, making it email-client friendly
4. Copy the generated HTML file to use in your email sending system