# cli.py

import typer

def main(repo: str = typer.Option(..., help="Path to target repo")):
    typer.echo(f"Scanning repository at {repo}")

    # scanner call

if __name__=="__main__":
    typer.run(main)

