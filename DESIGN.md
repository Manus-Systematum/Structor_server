# Structor — landing page

Authoritative record of decisions for this page. Reversed decisions are marked
superseded with the reason rather than deleted.

Status: first build, 2026-08-22, live the same day at
structor.systematum.net. Open items at the end.

The page describes **Structor**, the Warhammer 40,000 11th edition companion
app in `Wh40k_Companion/`, published under the **manus systematum** name.
`manus systematum` is a distribution name, not a legal entity: the page carries
no copyright line of its own, no "Ltd/Inc", no registered address.

---

## Voice

The page sounds like **the person who wrote the app telling you what it does
and where its data came from, with no interest in whether you download it.**
It states facts, names limits, and stops. It refuses **performed cheerfulness**
("The ultimate 40k companion!", "Build your army in seconds 🚀") and **performed
reassurance** ("don't worry, your lists are always safe", "everything you need,
nothing you don't").

Two things make the plain register load-bearing here rather than a preference.

**The product's claim is that it is free and unfunded.** Enthusiasm in the copy
reads as a pitch, and a pitch undermines the claim it is attached to. This is
inherited from systematum.net and holds for the same reason.

**The subject is a rules reference, and its value is entirely that it is
believed.** A page that oversells a tool for checking whether a list is legal
has already damaged the tool. This is why "What it does not do" is a section of
its own rather than a footnote — the limits are as much of the description as
the features, and a reader deciding whether to trust the app in a tournament
needs them at the same size.

### Before / after, from this page's own strings

| Rejected | Shipped | Why |
|---|---|---|
| "Everything you need to build the perfect list — fast, accurate, and beautiful." | "Structor builds army lists under the 11th edition detachment rules, and runs beside a game…" | The second names what it does. The first names how it wants to be regarded, and "accurate" is precisely the claim a reader should not simply take. |
| "Coming soon to the App Store! 🎉" | "In testing on iOS. Not released yet — there is no download on this page." | A reader arriving to download something needs to be told there is nothing to download, in the sentence where they look for the button. |
| "Don't worry — your data never leaves your device." | "Nothing is collected. There are no accounts, no analytics and no tracking, and no part of the app needs a network connection." | The first soothes a worry it just raised. The second is checkable. |
| "Powered by an amazing open-source community!" | Six named projects, each with what it supplies and the terms it is used under. | The gratitude is the part that costs nothing. The attribution is the part two of these licences actually require. |
| "35+ armies and counting!" | "Thirty-five armies and the core rules are bundled with the app." | "and counting" is a promise about work not done. The number is a fact about the build. |
| "Play smarter with instant stratagem lookup." | "Each phase lists the stratagems usable in it, with the full printed text and the cost." | The first sells an outcome the app cannot deliver on its own. The second describes the screen. |
| "Some data may be slightly out of date." | "Some of the data is still on a pre-launch provisional dataslate carried over from 10th edition." | A hedge replaced by the actual condition, in the words the app itself uses. |

### Patterns the voice rules out

Checked, because the register arrives as a package:

- No counters, no star ratings, no download badges, no "trusted by" line, no
  testimonials, no screenshots-as-glamour.
- No newsletter capture, no cookie banner — nothing is tracked, so there is
  nothing to consent to and no list to join.
- No call-to-action button of any kind. The page has no action to offer:
  the app is not released. A "Notify me" button would exist to collect
  addresses, not to help the reader.
- The two links that could be pitched — the source repository and the support
  form — are ordinary sentences in a list, not buttons.

The one sentence set apart visually is the "not released yet" line, because it
is the single thing on the page a reader could act on wrongly. It gets a
left rule and a lighter ground, not an alert colour: it is information, not a
warning.

---

## What the page claims, and where each claim was checked

The point of listing this is that a landing page is the easiest place in a
project to state something that used to be true. Every factual sentence was
read out of the code or the data rather than recalled:

| Claim | Checked against |
|---|---|
| Thirty-five armies plus core | `packages/wh40k_app/assets/bundles/` — 36 bundles, one of them `core` |
| Bundled, no download step | the bundles are shipped assets; the app has no fetch path yet |
| Detachment points, enhancement slots, unit caps, wargear limits | `wh40k_core/lib/src/rules/validator.dart` |
| A price that cannot be resolved is a reported problem | `PricingProblem` in `roster/points.dart` |
| Plain-text import, unmatched names listed | `wh40k_core/lib/src/import/` — text parser and resolver; no other format is implemented |
| A saved list keeps a copy of its data | roster snapshots, DESIGN.md §2.2 |
| Stratagem full text and cost, per phase | §3.12; 2,130 of 2,246 carry text |
| Using one deducts CP and records the unit | turn screen and battle state |
| Abilities attributed to their datasheet | §3.8, the Coldstar shield-generator finding |
| Nothing collected, works offline | About screen, Privacy |
| Lists cannot be sent between devices | QR (§6.4) is not built |

**Deliberately not claimed:** that the data is complete or current, that the
app is on any store, that it is on Android (Flutter targets it; only iOS has
been built and tested), and any coverage percentage — a number like "95% of
stratagems have text" invites the reader to compute what is missing without
telling them which 5%.

**One thing the app says that this page does not repeat.** The About screen's
trademark paragraph ends "No Games Workshop rules text is distributed with it."
That was true when it was written and is not true now: §3.12 added the printed
stratagem wording, by way of Wahapedia's export, to the shipped bundles. The
page describes the sources instead and makes no such claim. **The About screen
is what should change** — flagged as open item 3.

---

## Licence and attribution — the section with obligations behind it

Six sources, each named with what it supplies and its terms. Three of the six
impose something concrete, and the wording on the page satisfies it:

- **40kdc-data** is **CC BY 4.0**, which requires attribution, a link, and an
  indication that changes were made. All three are in the entry, including a
  specific statement of the changes (repackaged, corrected, rendered). Its
  schemas are **CC0**. The phrase "Powered by 40kdc-data" is what the project
  asks for and is the entry's heading — the app has a test pinning the same
  phrase verbatim, and this page should be treated as under the same rule.
- **Wahapedia**'s data export asks to be credited as "Powered by Wahapedia".
  Same treatment.
- **pguetschow/warhammer-40k-stratagem-card-generator** is **MIT**, which
  requires the notice to travel with the software; naming it here is the
  attribution half, and it is credited in the app as well.
- **BSData/wh40k-11e** has **no licence file**. The maintainers said in
  [issue 918](https://github.com/BSData/wh40k-11e/issues/918) that the
  repository is intended to be open source and may be cloned and altered
  freely. The page says so **and says that this is permission rather than a
  licence** — the weaker fact is the honest one, and stating it publicly is
  also the version most likely to prompt someone to add a `LICENSE`.
- **BSData/wh40k-11e-mfm** is **MIT**.
- **gdmissions.app** publishes no licence, terms or attribution notice at all.
  The page says that too. Softening it to "with thanks to gdmissions.app" would
  have implied a permission nobody granted.

Games Workshop's trademark notice sits at the end of that section, once. It is
not repeated in the footer: two notices read as a legal department, and there
isn't one.

---

## Visual decisions

**The same page as systematum.net, with different content.** Tokens, spacing
grid, elevation, type stack, the pinned gold dot field and the navy bars are
carried over unchanged. A subdomain of a distribution that looks like a
different company's site is a worse outcome than a slightly repetitive one.

| Token | Value | Use |
|---|---|---|
| `--navy` | `#0b1c36` | header, footer, the logo tile |
| `--page` | `#f1e7d3` | pale gold — the pinned background |
| `--panel` | `#dbe7f5` | the sections |
| `--surface` | `#f9fbfd` | source cards, the status line |
| `--gold` | `#ca994b` | accent: heading rules, list marks, the bars' edge |

**The mark is the app's own icon, and it needed no recolouring.** The Structor
icon is a gold helmet on navy, drawn in the same two colours as the group logo
— `#f8d8a3` on `#082447` against the palette's `#ca994b` on `#0b1c36`. What was
done to it: the navy ground was projected out to transparency along the
navy→gold axis, so the mark composites onto the page's navy rather than
carrying its own slightly different one, and the result was trimmed to its
bounding box so it fills the tile it is given.

**A rounded tile, not the circle systematum.net uses.** The apex page's logo is
drawn inside a circle; this one is an app icon, and an app icon is a squircle
everywhere else a reader has seen it.

**Lists carry a drawn gold dot** rather than the browser's bullet. Nearly all
the content is lists, the default marker sits too tight to the text at 16px,
and the gold ties them to the heading rules.

**No JavaScript at all.** The apex page has a form and needs a script; this
page has neither. The consequence is recorded in the origin config: `script-src`
and `connect-src` are `'none'` rather than `'self'`, so adding any script means
changing that line — intended friction.

**No screenshots, for now.** They belong on a page like this, and the app is
photogenic enough. They are absent because the only list on the simulator is a
one-unit stub, and a screenshot of an empty app describes the app worse than a
sentence does. Open item 2.

---

## Technical decisions

- **Two static files** plus images: [index.html](index.html),
  [style.css](style.css). No build step, no dependencies, no fonts fetched from
  anywhere. Drop them on any static host.
- **Semantic sections with `aria-labelledby`**, headings in order, one `h1`.
  The page is legible as a document with the stylesheet switched off, which is
  also what a search engine reads.
- **`assets/` is generated, not hand-drawn** —
  [tools/make-assets.py](tools/make-assets.py) produces the mark and the
  favicons from the app's icon source, so a new icon is one command away
  from being the page's too.
- **Favicons carry their own navy ground.** The mark is gold line art; on a
  light browser tab strip a transparent version would disappear.
- **MIT licensed**, matching the other systematum repositories. The copyright
  line names *manus systematum*, which is a distribution name rather than a
  legal person — fine for attribution, and the line to change if the licence
  ever has to be enforced by someone.
- **`DEPLOYMENT.md` and `deploy/deploy.sh` are untracked** — they name the
  host, its addresses and the tunnel, and this repository is public.

### On `design-against-real-data`

The group's rules call for that skill on layout questions, and it does not
apply here: it works by measuring two contrasting real datasets and scoring
arrangements against both, and this page has no dataset — its content is a
fixed set of paragraphs that will not vary by user. The nearest real risk is
the source list growing, so the layout is a `flex` column of cards that takes a
seventh entry without any change. Recorded rather than silently skipped.

---

## Open items

1. ~~**The app repository has no `LICENSE`.**~~ Resolved 2026-08-23: the app is
   **MIT**, and the page now says so in the Source bullet — with the qualifier
   that MIT covers the code and the rules data keeps the terms listed above it,
   since none of those sources are the project's to relicense. This page is MIT
   too, and GitHub detects both.

2. **No screenshots.** Needs a representative list built in the simulator first
   — the 2,000 pt T'au reference roster is the obvious candidate — then a
   handful of captures: the builder with a real detachment, the turn page with
   stratagems open, and the setup map.
3. **The About screen's "No Games Workshop rules text is distributed with it"
   is stale**, since stratagem text was added. This page does not repeat it; the
   screen should be corrected in the app repository.
4. ~~**Not deployed.**~~ Done 2026-08-22: the host's `structor` service was
   changed from the stock `nginx:alpine` placeholder to a build of this repo,
   in the same shape as `apex` — read-only root, all capabilities dropped,
   published on loopback only. See `DEPLOYMENT.md`.
5. **No Android statement.** Flutter targets both, only iOS has been built and
   tested, so the page says "In testing on iOS" and nothing about Android. When
   an Android build exists this line needs revisiting rather than extending.
