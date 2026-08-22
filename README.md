# Structor — landing page

The page at [structor.systematum.net](https://structor.systematum.net),
describing the Warhammer 40,000 11th edition companion app of the same name.
The app itself lives in a separate repository.

Two static files and a folder of images. No build step, no dependencies, no
JavaScript.

```
index.html      the page
style.css       its stylesheet
assets/         logo and favicons, generated from the app icon
deploy/         container image and origin configuration
DESIGN.md       why the page says and looks like what it does
```

## Preview

```bash
python3 -m http.server 8124 --directory .
```

Opening `index.html` from the filesystem also works; nothing on the page needs
an origin.

## Editing the copy

[DESIGN.md](DESIGN.md) records the register the page is written in and the
before/after pairs that make it checkable. Read that section before changing a
sentence — the plainness is a decision, not an omission.

The **Where the data comes from** section is not decoration. Two of the six
sources ask for a specific phrase ("Powered by 40kdc-data", "Powered by
Wahapedia") and one is CC BY, which obliges attribution and a statement that
changes were made. Do not shorten those entries without checking the terms they
satisfy.

## Deployment

`deploy/` holds the container image and origin configuration. The host, its
addresses and the tunnel are described in `DEPLOYMENT.md` and `deploy/deploy.sh`,
which are deliberately untracked — this repository is public.

## Licence

MIT, see [LICENSE](LICENSE). The Structor helmet mark is the app's own icon and
belongs with the app.
