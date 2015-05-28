# sublime-query-completions-silencer

Silence query completions in Sublime Text

This was built as a companion to [sublime-snippet-destroyer][] to silence any callback based completions (i.e. `EventListener.on_query_completions`)

[sublime-snippet-destroyer]: https://github.com/twolfson/sublime-snippet-destroyer

## Getting Started
### Installation
This package is available under `query-completions-silencer` inside of [Package Control][], a [Sublime Text][] plugin that allows for easy management of other plugins.

[Sublime Text]: http://www.sublimetext.com/
[Package Control]: http://wbond.net/sublime_packages/package_control

If you prefer the manual route, you can install the script via the following command in the Sublime Text terminal (``ctrl+` ``) which utilizes `git clone`.

```python
import os; path=sublime.packages_path(); (os.makedirs(path) if not os.path.exists(path) else None); window.run_command('exec', {'cmd': ['git', 'clone', 'https://github.com/twolfson/sublime-query-completions-silencer', 'query-completions-silencer'], 'working_dir': path})
```

Packages can be uninstalled via "Package Control: Remove Package" via the command pallete, `ctrl+shift+p` on Windows/Linux, `command+shift+p` on Mac.

## Documentation
_(Coming soon)_

## Examples
_(Coming soon)_

## Contributing
In lieu of a formal styleguide, take care to maintain the existing coding style. Add unit tests for any new or changed functionality.

## Donating
Support this project and [others by twolfson][gratipay] via [gratipay][].

[![Support via Gratipay][gratipay-badge]][gratipay]

[gratipay-badge]: https://cdn.rawgit.com/gratipay/gratipay-badge/2.x.x/dist/gratipay.png
[gratipay]: https://www.gratipay.com/twolfson/

## Unlicense
As of May 28 2015, Todd Wolfson has released this repository and its contents to the public domain.

It has been released under the [UNLICENSE][].

[UNLICENSE]: UNLICENSE
