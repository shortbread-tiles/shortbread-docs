# Shortbread website

The website is created using [Hugo](https://gohugo.io/).

## Theme

The theme is based on [Hextra](https://imfing.github.io/hextra/docs/).

## Development

```
hugo serve
```

Update theme:

```
git remote add hextra git@github.com:pka/hextra.git
git subtree pull --prefix=shortbread-website/themes/hextra hextra backport-debian --squash
```
