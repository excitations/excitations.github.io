# Exitations Organization


## Site development

The static website uses the [**Chirpy**][chirpy] Jekyll theme
[![Gem Version](https://img.shields.io/gem/v/jekyll-theme-chirpy)][gem]&nbsp;
[![GitHub license](https://img.shields.io/github/license/excitations/excitations.github.io.svg?color=blue)][mit]

Check out the [Chirpy theme's docs](https://github.com/cotes2020/jekyll-theme-chirpy/wiki).

### Local development
Install [**Jekyll**][jekyll], clone this repository and run

```cmd
~/excitations.github.io $ bundle exec jekyll serve --livereload
```

### Author new content
Optionally make use of the [**Jekyll-Compose**](https://github.com/jekyll/jekyll-compose)
to fill in the required [front matter](https://cirpy.cotes.pages/posts/write-a-new-post)
which allows

```cmd
~/excitations.github.io $ bundle exec jekyll post "A New Post"
```

to create a new Markdown page under `_posts/`.

Compare [raw Markdown](https://raw.githubusercontent.com/cotes2020/jekyll-theme-chirpy/refs/heads/master/_posts/2019-08-08-text-and-typography.md) to its [rendered result](https://chirpy.cotes.page/posts/text-and-typography) for an idea on what is possible to typeset.

### Add new pages to the sidebar
Add new markdown to the `_tabs/` folder, see the existing files' front matter for an example of how to specify order and icon for the new entry.


## License

This work is published under [MIT][mit] License.

[gem]: https://rubygems.org/gems/jekyll-theme-chirpy
[chirpy]: https://github.com/cotes2020/jekyll-theme-chirpy/
[CD]: https://en.wikipedia.org/wiki/Continuous_deployment
[mit]: https://github.com/excitations/excitations.github.io/blob/main/LICENSE
[jekyll]: https://jekyllrb.com
