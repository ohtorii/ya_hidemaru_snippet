# intoc

TOC generator for Markdown.

<!-- toc -->
- [intoc](#intoc)
  - [Feature](#feature)
  - [Install](#install)
  - [Requirement](#requirement)
  - [CLI](#cli)
  - [Samples](#samples)
    - [Basic](#basic)
    - [Depth control](#depth-control)
    - [Use not hyphen but aasterisk](#use-not-hyphen-but-aasterisk)
    - [Direct update](#direct-update)
    - [Plain enumeration](#plain-enumeration)
  - [License](#license)
  - [Author](#author)

## Feature

- Python based.
- No WebAPI use.
- Multiple output ways.
  - Output to the stdout
  - Direct Update(Insert TOC to the next of `<!-- toc -->` line directly).
- Support sections written in Japanese.

## Install

```
$ git clone https://github.com/stakiran/intoc
$ cd intoc
$ python intoc.py -i (Target-Markdown-File)
```

Create an alias if needed.

## Requirement

- Python 3 (Tested on Python 3.6 and Windows 7+)

## CLI

```
$ python intoc.py -h
usage: intoc.py [-h] -i INPUT [--indent-depth INDENT_DEPTH]
                [--parse-depth PARSE_DEPTH] [--use-asterisk]
                [--use-plain-enum] [--edit] [--edit-target EDIT_TARGET]

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        A input filename. (default: None)
  --indent-depth INDENT_DEPTH
                        The number of spaces per a nest in TOC. (default: 2)
  --parse-depth PARSE_DEPTH
                        The depth of the TOC list nesting. If minus then no
                        limit depth. (default: -1)
  --use-asterisk        Use an asterisk `*` as a list grammer. (default:
                        False)
  --use-plain-enum      Not use Markdown grammer, but use simple plain section
                        name listing. (default: False)
  --edit                If given then insert TOC to the file from "--input".
                        (default: False)
  --edit-target EDIT_TARGET
                        A insertion destination label when --edit given. NOT
                        CASE-SENSITIVE. (default: <!-- TOC)
```

## Samples

The sample file `intoc.md` in this section is like this:

```
$ type intoc.md
# intoc
TOC generator for Markdown.

<!-- toc -->

## Install
...

## CLI
..

## Info
...

### License
...

### Author
...
```

### Basic

An option `-i` is required for your input.

```
$ python intoc.py -i README.md
- [intoc](#intoc)
  - [Install](#install)
  - [CLI](#cli)
  - [Info](#info)
    - [License](#license)
    - [Author](#author)
```

### Depth control

`--indent-depth` and `--parse-depth`.

```
$ python intoc.py -i README.md --indent-depth 4 --parse-depth 2
- [intoc](#intoc)
    - [Install](#install)
    - [CLI](#cli)
    - [Info](#info)
```

### Use not hyphen but aasterisk

`--use-asterisk`.

```
$ python intoc.py -i README.md --use-asterisk
* [intoc](#intoc)
  * [Install](#install)
  * [CLI](#cli)
  * [Info](#info)
    * [License](#license)
    * [Author](#author)
```

### Direct update

Write `<!-- toc -->` to your input file and use `--edit`.

```
$ python intoc.py -i README.md --edit

$ type README.md
# intoc
TOC generator for Markdown.

<!-- toc -->
- [intoc](#intoc)
  - [Install](#install)
  - [CLI](#cli)
  - [Info](#info)
    - [License](#license)
    - [Author](#author)

## Install
...
```

### Plain enumeration

`--use-plain-enum`.

```
$ python intoc.py -i README.md --use-plain-enum
intoc
Feature
Install
Requirement
CLI
Samples
Basic
Depth control
Use not hyphen but aasterisk
Direct update
Plain Enumeration
License
Author
```

## License

[MIT License](LICENSE)

## Author

[stakiran](https://github.com/stakiran)
