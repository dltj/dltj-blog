# DLTJ Blog with Pelican

Using PDM as a Python manager. Use `pdm run zsh` to activate a shell.

## Basic setup

1. `pdm install` — install prereq
1. `pdm run pelican-themes -s ../pelican-papyrus-theme`

## View site

1. `invoke serve` or `invoke liveupdate`

## Editable modules

This isn't clean, but it is a [work-around suggested on GitHub](https://github.com/pdm-project/pdm/issues/2256#issuecomment-1717984339):

```bash
pdm run python -m ensurepip --upgrade
pdm run python -m pip install -e ../pelican-personal
pdm run python -m pip install -e ../pelican-dltj-plugin
```

`pdm sync --no-editable` will restore the virtual environment to what's in pyproject.toml.

## Historic Notes

- Files with `.markdown` extensions were converted from the Wordpress site (and still may need some manual editing)

## Macros

### Image

```
{{ image(
    div_float: str = None,
    width: str = None,
    localsrc: str = None,
    abssrc: str = None,
    caption: str = None,
    alt: str = None,
    ahref: str = None,
    localhref: str = None) }}
```

### Captioned section

Used for things other than an image to get the same rendered output

```
{{ captioned(
    div_float: str = None,
    width: str = None,
    caption: str = None,
    contents: str = None) }}
```
