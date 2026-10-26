# Govt. Model Boys (Evening) College Mirpurkhas — Website

A six-page static website (HTML5, CSS3, JavaScript, Bootstrap 5, Bootstrap Icons). **All college details are sample placeholders** and are marked "SAMPLE" — replace them with verified information.

## Run
Unzip and double-click `index.html`. No build step or server is needed. An internet connection is needed to load Bootstrap, icons and fonts from CDNs (the site still works without them, but unstyled). Optional local server: `python3 -m http.server 8000`, then open http://localhost:8000.

## Structure
- `index.html`, `about.html`, `departments.html`, `faculty.html`, `notices.html`, `contact.html`
- `css/style.css` — shared styles; colours are variables at the top (`--navy`, `--gold`).
- `js/script.js` — notices data, search/filter, contact form.
- `img/` — SVG placeholders (logo, campus, person). Replace with real images using the same file names, or edit the `<img>` tags.
- `build.py` — optional generator for the shared header/footer.

## Customize
- **Notices:** edit the `NOTICES` array at the top of `js/script.js`. The home page shows the first 3.
- **Contact email:** set `CONTACT_EMAIL` in `js/script.js`. The form has no backend: it validates input, then opens the visitor's email app with a draft. For real submissions use a service such as Formspree or your own server.
- **Address, phone, map:** edit `contact.html`; paste a Google Maps embed in the map placeholder box.
- **Departments / faculty / history / mission:** edit the sample text in the matching HTML file.
- **Editing the shared header/footer:** either edit `build.py` and run `python3 build.py` (this overwrites the HTML files), or edit each HTML file directly.
- Search the project for `SAMPLE` and `[` to find placeholders; remove the top banner in `build.py`/HTML when done.

## Publishing
Upload the folder to any static host (GitHub Pages, Netlify, or a web host).
