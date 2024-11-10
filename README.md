# DLTJ Blog with Pelican

Using PDM as a Python manager. Use `pdm run zsh` to activate a shell.

## Basic setup 

1. `pdm python install` — install Python venv
1. `pdm install` — install prereq

## View site

1. `invoke serve` or `invoke liveupdate`

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
