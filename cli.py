import os
import typer
from scanner.repo_scanner import scan_repo
from agent.readme_agent import generate_readme

import difflib


def show_readme_diff(old_content: str, new_content: str):
    """Show a colorized diff between old and new README content."""
    old_lines = old_content.splitlines()
    new_lines = new_content.splitlines()
    diff = difflib.unified_diff(
        old_lines, new_lines,
        fromfile='README.md (old)',
        tofile='README.md (new)',
        lineterm=''
    )
    for line in diff:
        if line.startswith('+') and not line.startswith('+++'):
            typer.secho(line, fg=typer.colors.GREEN)
        elif line.startswith('-') and not line.startswith('---'):
            typer.secho(line, fg=typer.colors.RED)
        elif line.startswith('@'):
            typer.secho(line, fg=typer.colors.YELLOW)
        else:
            typer.echo(line)


app = typer.Typer(
    help="Auto-generate high-quality README.md files for your code repositories using LLMs."
)

@app.command()
def generate(
    repo: str = typer.Option(
        ..., "--repo", "-r", help="Path to the target repository (folder) you want to document."
    ),
    openai_key: str = typer.Option(
        None, "--openai-key", "-k", help="OpenAI API key (set here or via OPENAI_API_KEY env var)."
    ),
):
    """
    Generates a comprehensive README.md for the given repo using code analysis and LLMs.

    Example:
        python cli.py generate --repo ./myproject --openai-key sk-...
    
    - Scans the provided repo for modules, classes, functions, and docstrings.
    - Uses an LLM to generate a rich README file (previewed before saving).
    - Prompts for confirmation before overwriting any existing README.md.
    """
    typer.echo(f"Scanning repository at {repo}")

    # scanner call
    summary = scan_repo(repo)
    typer.echo(f"Found {len(summary['modules'])} Python modules.")
    typer.echo(f"Classes: {summary['classes']}")
    typer.echo(f"Functions: {summary['functions']}")
    typer.echo(f"Requirements: {summary['requirements']}")
    typer.echo(f"README exists: {summary['readme_exists']}")
    typer.echo(f"License exists: {summary['license_exists']}")

    # send the summary to LLM
    typer.echo("Generating README using LLM...")
    readme_content = generate_readme(summary)

    # preview the first N lines (configurable)
    preview_lines = 20
    preview = "\n".join(readme_content.splitlines()[:preview_lines])
    typer.echo("\n" + "="*20)
    typer.secho("README PREVIEW:", fg=typer.colors.BRIGHT_GREEN, bold=True)
    typer.echo(preview)
    typer.echo("="*20 + "\n")

    readme_path = os.path.join(repo, "README.md")
    if os.path.exists(readme_path):
        with open(readme_path, "r", encoding="utf-8") as f:
            old_content = f.read()
        typer.secho("\nDiff between existing and new README.md:", fg=typer.colors.BRIGHT_BLUE, bold=True)
        show_readme_diff(old_content, readme_content)
        typer.echo("")  # spacing
        typer.secho(f"Warning: README.md already exists at {readme_path}.", fg=typer.colors.YELLOW, bold=True)
        if not typer.confirm("Overwrite the existing README.md with the new version?"):
            typer.secho("Aborted. No changes made.", fg=typer.colors.RED)
            raise typer.Exit()
    else:
        if not typer.confirm("Write new README.md to this repo?"):
            typer.secho("Aborted. No changes made.", fg=typer.colors.RED)
            raise typer.Exit()


    # Write the README
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(readme_content)
    typer.secho(f"README.md written to {readme_path}.", fg=typer.colors.GREEN, bold=True)

if __name__=="__main__":
    app()
