<p align="center">
  <img src="https://raw.githubusercontent.com/remarkablegames/renpy-template/master/game/gui/window_icon.png" alt="Ren'Py Template">
</p>

# renpy-template

![release](https://img.shields.io/github/v/release/remarkablegames/renpy-template)
[![build](https://github.com/remarkablegames/renpy-template/actions/workflows/build.yml/badge.svg)](https://github.com/remarkablegames/renpy-template/actions/workflows/build.yml)
[![lint](https://github.com/remarkablegames/renpy-template/actions/workflows/lint.yml/badge.svg)](https://github.com/remarkablegames/renpy-template/actions/workflows/lint.yml)

📖 Write visual novels with Ren'Py Template.

Play the game on:

- [remarkablegames](https://remarkablegames.org/renpy-template)

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
git clone https://github.com/remarkablegames/renpy-template.git
cd renpy-template
```

Rename the project:

```sh
git grep -l 'Renpy Template' | xargs sed -i '' -e 's/Renpy Template/My Novel/g'
```

```sh
git grep -l 'renpy-template' | xargs sed -i '' -e 's/renpy-template/my-novel/g'
```

Replace the assets:

- `web-presplash.jpg`
- `game/gui/main_menu.png`
- `game/gui/window_icon.png`

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
