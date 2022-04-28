# Chunker
CLI tool to chunk up things!

## Examples

```bash
# Default total 1, index 0.
λ chunker a.txt b.txt c.txt d.txt e.txt f.txt
a.txt b.txt c.txt d.txt e.txt f.txt

$ chunker --total 2 --index 0 a.txt b.txt c.txt d.txt e.txt f.txt
a.txt c.txt e.txt

λ chunker --total 2 --index 1 a.txt b.txt c.txt d.txt e.txt f.txt
b.txt d.txt f.txt

# Use env vars.
λ PARALELLISM_TOTAL=2 PARALELLISM_INDEX=1 chunker a.txt b.txt c.txt d.txt e.txt f.txt
b.txt d.txt f.txt

# Pipe input
λ echo "a.txt b.txt c.txt d.txt e.txt f.txt" | chunker --total 2 --index 1
b.txt d.txt f.txt

# Get help
λ chunker --help
Usage: chunker [OPTIONS] [ITEMS]...

Arguments:
  [ITEMS]...  The thing to split up. Typically a list of file names.

Options:
  --total INTEGER                 [env var: PARALLELISM_TOTAL; default: 1]
  --index INTEGER                 [env var: PARALLELISM_INDEX; default: 0]
  --install-completion [bash|zsh|fish|powershell|pwsh]
                                  Install completion for the specified shell.
  --show-completion [bash|zsh|fish|powershell|pwsh]
                                  Show completion for the specified shell, to
                                  copy it or customize the installation.
  --help                          Show this message and exit.
```