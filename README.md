<p align="center">
  <img src="https://raw.githubusercontent.com/remarkablegames/renpy-examples/master/game/gui/window_icon.png" alt="Ren'Py Logo">
</p>

# Ren'Py Examples

[![build](https://github.com/remarkablegames/renpy-examples/actions/workflows/build.yml/badge.svg)](https://github.com/remarkablegames/renpy-examples/actions/workflows/build.yml)
[![lint](https://github.com/remarkablegames/renpy-examples/actions/workflows/lint.yml/badge.svg)](https://github.com/remarkablegames/renpy-examples/actions/workflows/lint.yml)

📖 Learn how to write visual novels with Ren'Py examples.

Play the game on:

- [remarkablegames](https://remarkablegames.org/renpy-examples)

## Prerequisites

Download [Ren'Py SDK](https://www.renpy.org/latest.html):

```sh
git clone https://github.com/remarkablegames/renpy-sdk.git
```

Symlink `renpy`:

```sh
sudo ln -sf "$(realpath renpy-sdk/renpy.sh)" /usr/local/bin/renpy
```

## Install

Clone the repository to the `Projects Directory`:

```sh
git clone https://github.com/remarkablegames/renpy-examples.git
cd renpy-examples
```

## Run

Launch the project:

```sh
renpy .
```

Or open the `Ren'Py Launcher`:

```sh
renpy
```

Press `Shift`+`R` to reload the game.

Press `Shift`+`D` to display the developer menu.

Clean the cache:

```sh
find game -name "*.rpyc" -delete
```

## Lint

Lint the game:

```sh
renpy game lint
```

## License

[MIT](LICENSE)
