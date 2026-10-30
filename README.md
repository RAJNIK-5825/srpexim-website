# SRP Exim website (srpexim.in)

A fast, simple website in plain HTML, CSS and JavaScript. No framework, no build step.
English pages are in the main folder. Arabic pages (right-to-left) are in the `ar/` folder.

```
index.html  pomegranate.html  salt.html  about.html  certifications.html  contact.html
ar/         (same 6 pages in Arabic)
css/styles.css   js/main.js   images/   sitemap.xml   robots.txt   CNAME
```

## 1. Turn on GitHub Pages
1. Open the repository on GitHub, then **Settings → Pages**.
2. Under **Build and deployment**, set **Source** = *Deploy from a branch*.
3. Choose the branch that holds these files (usually `main`) and folder `/ (root)`. Click **Save**.
4. After 1–2 minutes the site is live at `https://<your-username>.github.io/<repo-name>/`.

(These files are first pushed on branch `claude/blissful-mayer-5rwfg3`. Merge it into `main` first, or choose that branch in step 3.)

## 2. Connect the domain srpexim.in
The file `CNAME` already contains `srpexim.in`.
1. In **Settings → Pages → Custom domain**, type `srpexim.in` and Save.
2. At your domain registrar (DNS settings) add these records:
   - 4 **A** records for `@`: `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`
   - 1 **CNAME** record: `www` → `<your-username>.github.io`
3. Wait (can take up to a few hours), then tick **Enforce HTTPS** in Pages settings.

## 3. Change text, numbers and photos later
- **Text / phone numbers / registration numbers:** open the `.html` file in GitHub (pencil icon) and edit. Do the same in the `ar/` file for Arabic. Phone and registration numbers also appear in the footer of every page.
- **Photos:** put your photo in `images/` (JPG/WebP, under ~200 KB). In the HTML, change the file name in the `<img src="...">` and write a short `alt="..."` text. Add it to `CREDITS.md`. Right now the site uses SVG illustrations (see `CREDITS.md`).
- **Colours:** top of `css/styles.css` (`:root`).
- **Optional:** `tools/build_pages.py` can regenerate all 12 pages from one source (`python3 tools/build_pages.py`). Note: it overwrites hand edits to the HTML files, so use either one method or the other.

## 4. Checklist: things still to fill
- [ ] **FORMSPREE_ID** – create a free form at formspree.io, then replace `FORMSPREE_ID` in `contact.html` and `ar/contact.html` (search for `formspree.io/f/FORMSPREE_ID`). Until then the form opens the visitor's email app (mailto fallback to srpexim2025@gmail.com).
- [ ] **RCMC (APEDA) number [TBD]** – shown on `certifications.html`, `ar/certifications.html` and in the footer of all 12 pages.
- [ ] Season / availability for pomegranate – currently "Contact us for current season and availability".
- [ ] Real photos (optional) – replace the SVG illustrations and update `CREDITS.md`.
- [ ] After the domain is live, submit `https://srpexim.in/sitemap.xml` in Google Search Console.
