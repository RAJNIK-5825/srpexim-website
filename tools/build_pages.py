"""Generates the English pages (root) and Arabic pages (/ar/) from one source,
so both languages always have the same structure. Optional: you can also edit the HTML files directly.
Run:  python3 tools/build_pages.py"""
import json, os
from urllib.parse import quote

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
SITE = 'https://srpexim.in'
EMAIL = 'srpexim2025@gmail.com'
PH1, PH2 = '+91 96873 80132', '+91 92659 73224'
TEL1, TEL2 = '+919687380132', '+919265973224'
WA = 'https://wa.me/919265973224'
ADDR_EN = 'First Floor, 4, Survey No. 74/3, Padana Gam, Padana, Gandhidham, Kachchh, Gujarat 370240, India'
ADDR_AR = 'الطابق الأول، 4، رقم المسح 74/3، بادانا غام، بادانا، غاندهيدهام، كاتش، غوجارات 370240، الهند'
MAP = 'https://www.google.com/maps?q=' + quote(ADDR_EN) + '&output=embed'
MAPLINK = 'https://www.google.com/maps/search/?api=1&query=' + quote(ADDR_EN)
IEC, GST, FSSAI, UDYAM = 'JOWPS1256B', '24JOWPS1256B1ZL', '10726998000036', 'UDYAM-GJ-13-0103546'

PAGES = ['index', 'pomegranate', 'salt', 'about', 'certifications', 'contact']

def ltr(x): return f'<span class="ltr">{x}</span>'

ICON = {
 'port': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 2v13M8 6h8M3 14c0 4 4 7 9 7s9-3 9-7M5 14h14"/></svg>',
 'farm': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 22V10M12 10C12 6 9 4 5 4c0 4 3 6 7 6zM12 13c0-3 2-5 6-5 0 3-2 5-6 5z"/></svg>',
 'check': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="10"/><path d="M8 12l3 3 5-6"/></svg>',
 'doc': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8zM14 2v6h6M8 13h8M8 17h8"/></svg>',
 'user': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="8" r="4"/><path d="M4 21c0-4 4-6 8-6s8 2 8 6"/></svg>',
 'wa': '<svg viewBox="0 0 32 32" fill="currentColor" aria-hidden="true"><path d="M16 3C9 3 3.3 8.600 3.300 15.600c0 2.400.7 4.700 1.900 6.600L3 29l7-1.800c1.900 1 4 1.600 6 1.600 7 0 12.700-5.700 12.700-12.700S23 3 16 3zm0 23.200c-1.900 0-3.700-.5-5.300-1.500l-.4-.2-4.100 1.100 1.100-4-.3-.4a10.400 10.400 0 1 1 9 5zm5.700-7.800c-.3-.2-1.800-.9-2.100-1s-.5-.2-.7.200-.8 1-1 1.200-.4.200-.7.100a8.500 8.500 0 0 1-4.200-3.700c-.3-.6.300-.5.900-1.700.1-.2 0-.4 0-.5l-1-2.300c-.2-.6-.5-.5-.7-.5h-.6c-.2 0-.5.100-.8.400s-1 1-1 2.400 1 2.800 1.200 3c.2.200 2.100 3.200 5.100 4.500 1.900.8 2.600.9 3.600.7.600-.1 1.800-.7 2-1.400s.2-1.300.2-1.400-.3-.2-.6-.4z"/></svg>',
 'menu': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M3 6h18M3 12h18M3 18h18"/></svg>',
}

def build(lang):
    ar = lang == 'ar'
    pre = '../' if ar else ''
    base = SITE + ('/ar' if ar else '')
    def t(en, a): return a if ar else en
    def href(p): return ('index.html' if p == 'index' else p + '.html')
    ADDR = t(ADDR_EN, ADDR_AR)

    NAV = [('index', t('Home', 'الرئيسية')), ('pomegranate', t('Pomegranate', 'الرمان')),
           ('salt', t('Salt', 'الملح')), ('about', t('About Us', 'من نحن')),
           ('certifications', t('Certifications', 'التراخيص والتسجيلات')), ('contact', t('Contact', 'اتصل بنا'))]
    QUOTE = t('Get a Quotation', 'اطلب عرض سعر')
    arrow = '<span class="arrow" aria-hidden="true">&rarr;</span>'

    def org_schema():
        return {"@type": "Organization", "@id": SITE + "/#org", "name": "SRP EXIM",
                "alternateName": "SRP Exim", "url": SITE + "/", "logo": SITE + "/images/icon-512.png",
                "email": EMAIL, "telephone": [PH1, PH2],
                "founder": {"@type": "Person", "name": "Shambhubhai Sakhayabhai Humbal"},
                "address": {"@type": "PostalAddress",
                            "streetAddress": "First Floor, 4, Survey No. 74/3, Padana Gam, Padana",
                            "addressLocality": "Gandhidham", "addressRegion": "Gujarat",
                            "postalCode": "370240", "addressCountry": "IN"},
                "contactPoint": [{"@type": "ContactPoint", "telephone": PH1, "contactType": "sales", "email": EMAIL,
                                  "availableLanguage": ["English", "Arabic"]}]}

    def page(slug, title, desc, body, products=None, img='og-image.png'):
        url = base + '/' + ('' if slug == 'index' else href(slug))
        if slug == 'index': url = base + '/'
        en_url = SITE + '/' + ('' if slug == 'index' else href(slug))
        ar_url = SITE + '/ar/' + ('' if slug == 'index' else href(slug))
        other = ('../' if ar else 'ar/') + ('' if slug == 'index' else href(slug))
        if slug == 'index': other = '../' if ar else 'ar/'
        graph = [org_schema()] + (products or [])
        ld = json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False)
        navhtml = ''.join(f'<li><a href="{href(p)}"{" aria-current=\"page\"" if p == slug else ""}>{n}</a></li>' for p, n in NAV)
        return f'''<!DOCTYPE html>
<html lang="{lang}" dir="{'rtl' if ar else 'ltr'}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<link rel="alternate" hreflang="en" href="{en_url}">
<link rel="alternate" hreflang="ar" href="{ar_url}">
<link rel="alternate" hreflang="x-default" href="{en_url}">
<meta name="theme-color" content="#0f3d2e">
<meta property="og:type" content="website">
<meta property="og:site_name" content="SRP EXIM">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/images/{img}">
<meta property="og:locale" content="{'ar_AR' if ar else 'en_IN'}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{SITE}/images/{img}">
<link rel="icon" href="{pre}images/favicon.svg" type="image/svg+xml">
<link rel="icon" href="{pre}images/favicon-32.png" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="{pre}images/apple-touch-icon.png">
<link rel="stylesheet" href="{pre}css/styles.css">
<script>document.documentElement.classList.add('js')</script>
<script type="application/ld+json">{ld}</script>
</head>
<body>
<a class="skip" href="#main">{t('Skip to content', 'انتقل إلى المحتوى')}</a>
<header class="site-header">
<div class="container header-in">
<a class="logo" href="{href('index')}" aria-label="SRP EXIM {t('home', 'الرئيسية')}"><img src="{pre}images/logo.svg" width="250" height="64" alt="SRP EXIM"></a>
<a class="lang" href="{other}" hreflang="{'en' if ar else 'ar'}" lang="{'en' if ar else 'ar'}">{'English' if ar else 'العربية'}</a>
<button class="nav-toggle" type="button" aria-expanded="false" aria-controls="site-nav" aria-label="{t('Menu', 'القائمة')}">{ICON['menu']}</button>
<nav class="nav" id="site-nav" aria-label="{t('Main', 'القائمة الرئيسية')}"><ul>{navhtml}</ul></nav>
</div>
</header>
<main id="main">
{body}
</main>
<footer class="site-footer">
<div class="container">
<div class="foot-grid">
<div>
<a class="logo" href="{href('index')}"><img src="{pre}images/logo-white.svg" width="250" height="64" alt="SRP EXIM" loading="lazy"></a>
<p style="margin-top:14px">{t('Exporter of fresh Bhagwa pomegranates and salt from Gandhidham, Kachchh, Gujarat, India.', 'مُصدِّر الرمان الطازج (بهغوا) والملح من غاندهيدهام، كاتش، غوجارات، الهند.')}</p>
<p>{t('Proprietor', 'المالك')}: Shambhubhai Sakhayabhai Humbal</p>
</div>
<div><h3>{t('Pages', 'الصفحات')}</h3><ul>{''.join(f'<li><a href="{href(p)}">{n}</a></li>' for p, n in NAV)}</ul></div>
<div><h3>{t('Contact', 'تواصل معنا')}</h3>
<address>{ADDR}</address>
<ul style="margin-top:10px"><li><a href="tel:{TEL1}">{ltr(PH1)}</a></li><li><a href="tel:{TEL2}">{ltr(PH2)}</a></li><li><a href="mailto:{EMAIL}">{EMAIL}</a></li></ul></div>
<div><h3>{t('Registrations', 'التسجيلات')}</h3>
<ul class="regs">
<li><b>IEC (DGFT):</b> {ltr(IEC)}</li>
<li><b>GSTIN:</b> {ltr(GST)}</li>
<li><b>FSSAI:</b> {ltr(FSSAI)}</li>
<li><b>Udyam (MSME):</b> {ltr(UDYAM)}</li>
<li><b>RCMC (APEDA):</b> {ltr('[TBD]')}</li>
</ul></div>
</div>
<p class="copy">&copy; SRP EXIM. {t('All rights reserved.', 'جميع الحقوق محفوظة.')}</p>
</div>
</footer>
<a class="wa-float" href="{WA}" target="_blank" rel="noopener" aria-label="{t('Chat with SRP Exim on WhatsApp', 'تواصل مع SRP Exim عبر واتساب')}">{ICON['wa']}</a>
<script src="{pre}js/main.js" defer></script>
</body>
</html>
'''

    def head(title, lead, slug_name):
        return f'''<section class="page-head"><div class="container">
<p class="crumbs"><a href="index.html">{t('Home', 'الرئيسية')}</a> / {slug_name}</p>
<h1>{title}</h1>
<p>{lead}</p>
</div></section>'''

    def cta(h, p):
        return f'''<section class="cta"><div class="container">
<h2>{h}</h2><p>{p}</p>
<div class="btn-row"><a class="btn btn-red" href="contact.html">{QUOTE}</a><a class="btn btn-outline" href="{WA}" target="_blank" rel="noopener">{t('WhatsApp us', 'راسلنا على واتساب')}</a></div>
</div></section>'''

    def img(name, alt, w=800, h=600, cls='', lazy=True):
        return f'<img src="{pre}images/{name}" width="{w}" height="{h}" alt="{alt}"{" loading=\"lazy\"" if lazy else " fetchpriority=\"high\""}{f" class=\"{cls}\"" if cls else ""}>'

    ALT_HERO = t('Fresh Bhagwa pomegranates in front of white salt pans of Kutch', 'رمان بهغوا طازج أمام ملاحات كاتش البيضاء')
    ALT_POM = t('Fresh red Bhagwa pomegranates, whole and cut open', 'رمان بهغوا أحمر طازج، كامل ومقطوع')
    ALT_BOX = t('2 kg box packed with Bhagwa A grade pomegranates', 'علبة 2 كجم معبأة برمان بهغوا درجة A')
    ALT_PAN = t('White salt pans and salt heap in Kutch, Gujarat', 'ملاحات بيضاء وكومة ملح في كاتش، غوجارات')
    ALT_BAGS = t('25 kg and 50 kg PP salt bags and a 1 MT jumbo bag', 'أكياس ملح PP سعة 25 و50 كجم وكيس جامبو سعة طن متري')

    prod_pom = {"@type": "Product", "@id": SITE + "/pomegranate.html#product",
                "name": t("Fresh Bhagwa Pomegranate (A grade)", "رمان بهغوا طازج (درجة A)"),
                "description": t("Fresh Bhagwa pomegranate, A grade, packed in 2 kg boxes. Minimum order 1 reefer container. FOB and CIF.",
                                "رمان بهغوا طازج، درجة A، معبأ في علب 2 كجم. الحد الأدنى للطلب حاوية مبردة واحدة. FOB وCIF."),
                "image": SITE + "/images/pomegranate.svg", "category": "Fresh fruit",
                "brand": {"@id": SITE + "/#org"}, "manufacturer": {"@id": SITE + "/#org"},
                "additionalProperty": [{"@type": "PropertyValue", "name": "Variety", "value": "Bhagwa"},
                                       {"@type": "PropertyValue", "name": "Grade", "value": "A grade"},
                                       {"@type": "PropertyValue", "name": "Packing", "value": "2 kg boxes"},
                                       {"@type": "PropertyValue", "name": "Minimum order", "value": "1 container (reefer)"}]}
    prod_salt = [{"@type": "Product", "@id": SITE + "/salt.html#industrial",
                  "name": t("Industrial Salt", "الملح الصناعي"),
                  "description": t("Industrial salt from the salt pans of Kutch, Gujarat, for chemical industries, de-icing and water treatment. Packed in 25 kg and 50 kg PP bags, 1 MT jumbo bags or loose bulk.",
                                  "ملح صناعي من ملاحات كاتش في غوجارات، للصناعات الكيميائية وإذابة الجليد ومعالجة المياه. يُعبأ في أكياس PP سعة 25 و50 كجم أو أكياس جامبو سعة طن أو سائب."),
                  "image": SITE + "/images/salt-pan.svg", "category": "Salt",
                  "brand": {"@id": SITE + "/#org"}, "manufacturer": {"@id": SITE + "/#org"}},
                 {"@type": "Product", "@id": SITE + "/salt.html#edible",
                  "name": t("Edible Salt (iodized / non-iodized)", "الملح الغذائي (مُيودَّن / غير مُيودَّن)"),
                  "description": t("Refined edible salt, iodized or non-iodized, from the salt pans of Kutch, Gujarat. Purity as per buyer specification; test report available on request.",
                                  "ملح غذائي مكرر، مُيودَّن أو غير مُيودَّن، من ملاحات كاتش في غوجارات. النقاء حسب مواصفات المشتري، وتقرير الفحص متاح عند الطلب."),
                  "image": SITE + "/images/salt-bags.svg", "category": "Salt",
                  "brand": {"@id": SITE + "/#org"}, "manufacturer": {"@id": SITE + "/#org"}}]

    out = {}

    # ---------------- HOME
    why = [('port', t('Close to the ports', 'قريبون من الموانئ'), t('Based in Gandhidham, near Kandla (Deendayal) and Mundra ports.', 'مقرنا في غاندهيدهام، بالقرب من ميناءي كاندلا (ديندايال) ومندرا.')),
           ('farm', t('Direct sourcing', 'مصادر مباشرة'), t('We source directly from pomegranate farms and the salt pans of Kutch.', 'نشتري مباشرة من مزارع الرمان ومن ملاحات كاتش.')),
           ('check', t('Quality check before dispatch', 'فحص الجودة قبل الشحن'), t('Goods are quality-checked before they are dispatched.', 'تُفحص جودة البضاعة قبل إرسالها.')),
           ('doc', t('Complete export documentation', 'مستندات تصدير كاملة'), t('We prepare the export documents. FOB and CIF terms available.', 'نُعدّ مستندات التصدير كاملة. شروط FOB وCIF متاحة.'))]
    steps = [(t('Enquiry', 'الاستفسار'), t('Tell us the product, quantity and destination port.', 'أخبرنا بالمنتج والكمية وميناء الوجهة.')),
             (t('Quotation', 'عرض السعر'), t('We send you a quotation on FOB or CIF terms.', 'نرسل لك عرض سعر بشروط FOB أو CIF.')),
             (t('Sample / Approval', 'العينة / الموافقة'), t('You check the sample and approve the specification.', 'تفحص العينة وتوافق على المواصفات.')),
             (t('Packing & Quality Check', 'التعبئة وفحص الجودة'), t('Goods are packed as agreed and quality-checked before dispatch.', 'تُعبَّأ البضاعة كما اتفقنا وتُفحص جودتها قبل الشحن.')),
             (t('Shipment & Documents', 'الشحن والمستندات'), t('Container shipment with the complete export documents.', 'شحن بالحاويات مع مستندات التصدير كاملة.'))]
    body = f'''<section class="hero"><div class="container hero-grid">
<div>
<span class="eyebrow">{t('Exporter based in Gandhidham, Kachchh, Gujarat', 'مُصدِّر مقره في غاندهيدهام، كاتش، غوجارات')}</span>
<h1>{t('Bhagwa Pomegranate &amp; Salt Exporter from India', 'مُصدِّر رمان بهغوا وملح من الهند')}</h1>
<p class="lead">{t('SRP Exim supplies fresh Bhagwa pomegranates and industrial and edible salt, sourced directly from pomegranate farms and the salt pans of Kutch, Gujarat. Container loads on FOB and CIF terms.', 'تورّد SRP Exim الرمان الطازج من صنف بهغوا والملح الصناعي والملح الغذائي، من مصادر مباشرة: مزارع الرمان وملاحات كاتش في غوجارات. شحنات بالحاويات بشروط FOB وCIF.')}</p>
<div class="btn-row"><a class="btn btn-red" href="contact.html">{QUOTE}</a><a class="btn btn-outline" href="{WA}" target="_blank" rel="noopener">{t('WhatsApp us', 'راسلنا على واتساب')}</a></div>
<ul class="chips"><li>FOB &amp; CIF</li><li>{t('Minimum order: 1 container', 'الحد الأدنى: حاوية واحدة')}</li><li>{t('Near Kandla &amp; Mundra ports', 'قرب ميناءي كاندلا ومندرا')}</li></ul>
</div>
<div class="hero-img">{img('hero.svg', ALT_HERO, 800, 640, lazy=False)}</div>
</div></section>

<section class="reg-strip"><div class="container">
<ul aria-label="{t('Registrations', 'التسجيلات')}"><li>IEC</li><li>GSTIN</li><li>FSSAI</li><li>Udyam (MSME)</li><li>APEDA (RCMC)</li></ul>
<a href="certifications.html">{t('See registration details', 'عرض تفاصيل التسجيلات')} {arrow}</a>
</div></section>

<section class="section"><div class="container">
<div class="section-head"><h2>{t('Our Products', 'منتجاتنا')}</h2><p>{t('Two products from India, shipped by the container.', 'منتجان من الهند، يُشحنان بالحاويات.')}</p></div>
<div class="grid g2">
<article class="card">{img('pomegranate.svg', ALT_POM, cls='')}<div class="body">
<h3>{t('Fresh Bhagwa Pomegranate', 'رمان بهغوا الطازج')}</h3>
<ul class="ticks"><li>{t('Variety: Bhagwa &middot; Grade: A grade', 'الصنف: بهغوا · الدرجة: A')}</li><li>{t('Packing: 2 kg boxes', 'التعبئة: علب 2 كجم')}</li><li>{t('Minimum order: 1 container (reefer)', 'الحد الأدنى للطلب: حاوية واحدة (مبردة)')}</li></ul>
<a class="btn btn-green" href="pomegranate.html">{t('View details', 'عرض التفاصيل')} {arrow}</a></div></article>
<article class="card">{img('salt-pan.svg', ALT_PAN)}<div class="body">
<h3>{t('Salt &mdash; Industrial &amp; Edible', 'الملح — صناعي وغذائي')}</h3>
<ul class="ticks"><li>{t('From the salt pans of Kutch, Gujarat', 'من ملاحات كاتش في غوجارات')}</li><li>{t('25 kg &amp; 50 kg PP bags, 1 MT jumbo bags, loose bulk', 'أكياس PP سعة 25 و50 كجم، أكياس جامبو سعة طن، وسائب')}</li><li>{t('Minimum order: 1 container', 'الحد الأدنى للطلب: حاوية واحدة')}</li></ul>
<a class="btn btn-green" href="salt.html">{t('View details', 'عرض التفاصيل')} {arrow}</a></div></article>
</div></div></section>

<section class="section alt"><div class="container">
<div class="section-head"><h2>{t('Why SRP Exim', 'لماذا SRP Exim')}</h2></div>
<div class="grid g4">{''.join(f'<div class="card why"><div class="ico">{ICON[i]}</div><h3>{h}</h3><p>{p}</p></div>' for i, h, p in why)}</div>
</div></section>

<section class="section"><div class="container">
<div class="section-head"><h2>{t('How Export Works &mdash; 5 Steps', 'كيف يتم التصدير — 5 خطوات')}</h2><p>{t('A simple process from your first message to the shipment.', 'عملية بسيطة من رسالتك الأولى حتى الشحن.')}</p></div>
<ol class="steps">{''.join(f'<li><h3>{h}</h3><p>{p}</p></li>' for h, p in steps)}</ol>
</div></section>

{cta(t('Looking for Bhagwa pomegranates or salt from India?', 'تبحث عن رمان بهغوا أو ملح من الهند؟'), t('Send us your product, quantity and destination port. We will reply with a quotation.', 'أرسل لنا المنتج والكمية وميناء الوجهة، وسنرد عليك بعرض سعر.'))}'''
    out['index'] = page('index',
        t('SRP Exim | Bhagwa Pomegranate Exporter India &amp; Salt Exporter Gujarat', 'SRP Exim | مُصدِّر رمان بهغوا وملح من الهند - غوجارات'),
        t('SRP Exim, Gandhidham, Gujarat: Bhagwa pomegranate exporter India and salt exporter near Kandla and Mundra ports. Fresh pomegranate and industrial salt, FOB and CIF.',
          'SRP Exim في غاندهيدهام، غوجارات: مُصدِّر رمان بهغوا وملح من الهند قرب ميناءي كاندلا ومندرا. رمان طازج وملح صناعي وغذائي بشروط FOB وCIF.'), body)

    # ---------------- POMEGRANATE
    rows = [(t('Product', 'المنتج'), t('Fresh pomegranate', 'رمان طازج')), (t('Variety', 'الصنف'), t('Bhagwa', 'بهغوا')),
            (t('Grade', 'الدرجة'), t('A grade', 'A')), (t('Packing', 'التعبئة'), t('2 kg boxes', 'علب 2 كجم')),
            (t('Minimum order', 'الحد الأدنى للطلب'), t('1 container (reefer)', 'حاوية واحدة (مبردة)')),
            (t('Season / availability', 'الموسم / التوفر'), t('Contact us for current season and availability', 'تواصل معنا لمعرفة الموسم الحالي والتوفر')),
            (t('Sourcing', 'المصدر'), t('Directly from pomegranate farms', 'مباشرة من مزارع الرمان')),
            (t('Quality', 'الجودة'), t('Quality checking before dispatch', 'فحص الجودة قبل الشحن')),
            (t('Incoterms', 'شروط التسليم'), 'FOB, CIF'),
            (t('Documents', 'المستندات'), t('Complete export documentation', 'مستندات تصدير كاملة')),
            (t('Nearby ports', 'الموانئ القريبة'), t('Kandla (Deendayal), Mundra', 'كاندلا (ديندايال)، مندرا'))]
    body = head(t('Fresh Bhagwa Pomegranate Exporter from India', 'مُصدِّر رمان بهغوا الطازج من الهند'),
                t('A grade Bhagwa pomegranates, packed in 2 kg boxes and shipped by reefer container. SRP Exim is a fresh pomegranate supplier in Gujarat, sourcing directly from farms.',
                  'رمان بهغوا الطازج درجة A، معبأ في علب 2 كجم ويُشحن بحاويات مبردة. SRP Exim مورّد رمان طازج في غوجارات، نشتري مباشرة من المزارع.'),
                t('Pomegranate', 'الرمان')) + f'''
<section class="section"><div class="container split">
<div>
<h2>{t('Bhagwa pomegranate, direct from the farm', 'رمان بهغوا مباشرة من المزرعة')}</h2>
<p>{t('We export fresh Bhagwa pomegranate of A grade. As a Bhagwa pomegranate exporter in India, we source directly from pomegranate farms, check the quality before dispatch and prepare the complete export documentation.', 'نُصدّر رمان بهغوا الطازج من الدرجة A. وبصفتنا مُصدِّر رمان بهغوا في الهند، نشتري مباشرة من مزارع الرمان، ونفحص الجودة قبل الشحن، ونُعدّ مستندات التصدير كاملة.')}</p>
<ul class="ticks"><li>{t('Variety: Bhagwa &middot; Grade: A grade', 'الصنف: بهغوا · الدرجة: A')}</li><li>{t('Packing: 2 kg boxes', 'التعبئة: علب 2 كجم')}</li><li>{t('Minimum order: 1 container (reefer)', 'الحد الأدنى للطلب: حاوية واحدة (مبردة)')}</li><li>{t('Terms: FOB and CIF', 'الشروط: FOB وCIF')}</li></ul>
<div class="callout"><strong>{t('Season &amp; availability:', 'الموسم والتوفر:')}</strong> {t('Contact us for current season and availability.', 'تواصل معنا لمعرفة الموسم الحالي والتوفر.')}</div>
<div class="btn-row"><a class="btn btn-red" href="contact.html">{QUOTE}</a></div>
</div>
{img('pomegranate.svg', ALT_POM, lazy=False)}
</div></section>

<section class="section alt"><div class="container">
<div class="section-head"><h2>{t('Specification', 'المواصفات')}</h2></div>
<div class="table-wrap"><table><caption class="sr" style="display:none">{t('Pomegranate specification', 'مواصفات الرمان')}</caption><tbody>
{''.join(f'<tr><th scope="row">{k}</th><td>{v}</td></tr>' for k, v in rows)}
</tbody></table></div>
</div></section>

<section class="section"><div class="container split rev">
<div>
<h2>{t('Packing', 'التعبئة')}</h2>
<p>{t('Pomegranates are packed in 2 kg boxes and loaded into a reefer container. Ask us for the loading details together with your quotation.', 'يُعبأ الرمان في علب سعة 2 كجم ويُحمَّل في حاوية مبردة. اطلب منا تفاصيل التحميل مع عرض السعر.')}</p>
<div class="grid g2"><div class="card pack"><span class="big">2 kg</span><p>{t('Box packing', 'تعبئة في علب')}</p></div><div class="card pack"><span class="big">1</span><p>{t('Reefer container, minimum order', 'حاوية مبردة، الحد الأدنى للطلب')}</p></div></div>
</div>
{img('pomegranate-box.svg', ALT_BOX)}
</div></section>
{cta(t('Get a quotation for Bhagwa pomegranate', 'اطلب عرض سعر لرمان بهغوا'), t('Tell us your quantity and destination port. We will reply with FOB or CIF terms.', 'أخبرنا بالكمية وميناء الوجهة وسنرد عليك بشروط FOB أو CIF.'))}'''
    out['pomegranate'] = page('pomegranate',
        t('Fresh Bhagwa Pomegranate Exporter India | Pomegranate Supplier Gujarat - SRP Exim', 'مُصدِّر رمان بهغوا الطازج من الهند | مورّد رمان غوجارات - SRP Exim'),
        t('Bhagwa pomegranate exporter India: A grade fresh pomegranate in 2 kg boxes, reefer container, FOB and CIF. Fresh pomegranate supplier in Gujarat - SRP Exim.',
          'مُصدِّر رمان بهغوا من الهند: رمان طازج درجة A في علب 2 كجم، حاوية مبردة، FOB وCIF. مورّد رمان طازج في غوجارات - SRP Exim.'),
        body, [prod_pom], 'og-image.png')

    # ---------------- SALT
    srows = [(t('Source', 'المصدر'), t('Salt pans of Kutch, Gujarat', 'ملاحات كاتش، غوجارات'), t('Salt pans of Kutch, Gujarat', 'ملاحات كاتش، غوجارات')),
             (t('Used for', 'الاستخدام'), t('Chemical industries, de-icing, water treatment', 'الصناعات الكيميائية، إذابة الجليد، معالجة المياه'), t('Edible use (refined)', 'الاستخدام الغذائي (مكرر)')),
             (t('Type', 'النوع'), t('Industrial salt', 'ملح صناعي'), t('Refined &mdash; iodized / non-iodized', 'مكرر — مُيودَّن / غير مُيودَّن')),
             (t('Purity', 'النقاء'), t('As per buyer specification &mdash; test report available on request', 'حسب مواصفات المشتري — تقرير الفحص متاح عند الطلب'), t('As per buyer specification &mdash; test report available on request', 'حسب مواصفات المشتري — تقرير الفحص متاح عند الطلب')),
             (t('Packing', 'التعبئة'), t('25 kg &amp; 50 kg PP bags, 1 MT jumbo bags, loose bulk', 'أكياس PP سعة 25 و50 كجم، أكياس جامبو سعة طن، سائب'), t('25 kg &amp; 50 kg PP bags, 1 MT jumbo bags, loose bulk', 'أكياس PP سعة 25 و50 كجم، أكياس جامبو سعة طن، سائب')),
             (t('Minimum order', 'الحد الأدنى للطلب'), t('1 container', 'حاوية واحدة'), t('1 container', 'حاوية واحدة')),
             (t('Incoterms', 'شروط التسليم'), 'FOB, CIF', 'FOB, CIF')]
    packs = [('25 kg', t('PP bag', 'كيس PP')), ('50 kg', t('PP bag', 'كيس PP')), ('1 MT', t('Jumbo bag', 'كيس جامبو')), (t('Bulk', 'سائب'), t('Loose bulk', 'شحن سائب'))]
    body = head(t('Salt Exporter from Kandla, Gujarat &mdash; Industrial &amp; Edible Salt', 'مُصدِّر ملح من كاندلا، غوجارات — ملح صناعي وغذائي'),
                t('Industrial salt and edible salt from the salt pans of Kutch. SRP Exim is an industrial salt supplier in India, close to Kandla (Deendayal) and Mundra ports.',
                  'ملح صناعي وملح غذائي من ملاحات كاتش. SRP Exim مورّد ملح صناعي في الهند، قريبة من ميناءي كاندلا (ديندايال) ومندرا.'),
                t('Salt', 'الملح')) + f'''
<section class="section"><div class="container split">
<div>
<h2>{t('Two grades of salt from Kutch', 'نوعان من الملح من كاتش')}</h2>
<p>{t('We are a salt exporter near Kandla, Gujarat, sourcing directly from the salt pans of Kutch. Choose the grade that suits your use.', 'نحن مُصدِّر ملح قرب كاندلا في غوجارات، ونشتري مباشرة من ملاحات كاتش. اختر النوع المناسب لاستخدامك.')}</p>
<div class="grid g2">
<div class="card"><div class="body"><h3>{t('Industrial salt', 'الملح الصناعي')}</h3><p>{t('For chemical industries, de-icing and water treatment.', 'للصناعات الكيميائية وإذابة الجليد ومعالجة المياه.')}</p></div></div>
<div class="card"><div class="body"><h3>{t('Edible salt', 'الملح الغذائي')}</h3><p>{t('Refined, iodized or non-iodized.', 'مكرر، مُيودَّن أو غير مُيودَّن.')}</p></div></div>
</div>
<div class="btn-row"><a class="btn btn-red" href="contact.html">{QUOTE}</a></div>
</div>
{img('salt-pan.svg', ALT_PAN, lazy=False)}
</div></section>

<section class="section alt"><div class="container">
<div class="section-head"><h2>{t('Specification', 'المواصفات')}</h2><p>{t('Purity is as per buyer specification. A test report is available on request.', 'النقاء حسب مواصفات المشتري، وتقرير الفحص متاح عند الطلب.')}</p></div>
<div class="table-wrap"><table>
<thead><tr><th scope="col">{t('Detail', 'البند')}</th><th scope="col">{t('Industrial salt', 'الملح الصناعي')}</th><th scope="col">{t('Edible salt', 'الملح الغذائي')}</th></tr></thead><tbody>
{''.join(f'<tr><th scope="row">{k}</th><td>{a}</td><td>{b}</td></tr>' for k, a, b in srows)}
</tbody></table></div>
</div></section>

<section class="section"><div class="container split rev">
<div>
<h2>{t('Packing options', 'خيارات التعبئة')}</h2>
<p>{t('Choose the pack size that fits your handling and your container load.', 'اختر حجم التعبئة المناسب لطريقة التفريغ وحمولة الحاوية.')}</p>
<div class="grid g2">{''.join(f'<div class="card pack"><span class="big">{a}</span><p>{b}</p></div>' for a, b in packs)}</div>
</div>
{img('salt-bags.svg', ALT_BAGS)}
</div></section>
{cta(t('Get a quotation for salt', 'اطلب عرض سعر للملح'), t('Tell us the grade, packing, quantity and destination port. We will reply with FOB or CIF terms.', 'أخبرنا بالنوع والتعبئة والكمية وميناء الوجهة وسنرد عليك بشروط FOB أو CIF.'))}'''
    out['salt'] = page('salt',
        t('Salt Exporter Kandla Gujarat | Industrial Salt Supplier India - SRP Exim', 'مُصدِّر ملح كاندلا غوجارات | مورّد ملح صناعي من الهند - SRP Exim'),
        t('Salt exporter Kandla Gujarat: industrial salt supplier India and edible salt from the salt pans of Kutch. 25/50 kg PP bags, 1 MT jumbo bags, bulk. FOB and CIF.',
          'مُصدِّر ملح من كاندلا غوجارات: مورّد ملح صناعي من الهند وملح غذائي من ملاحات كاتش. أكياس 25/50 كجم، جامبو طن، سائب. FOB وCIF.'),
        body, prod_salt, 'og-image.png')

    # ---------------- ABOUT
    team = [('Shambhubhai Humbal', t('Proprietor', 'المالك')), ('Rajnik', t('Team member', 'عضو الفريق')), ('Pradip', t('Team member', 'عضو الفريق'))]
    body = head(t('About SRP Exim', 'عن SRP Exim'),
                t('A proprietorship exporter from Gandhidham, Kachchh, Gujarat, shipping fresh Bhagwa pomegranates and salt from Kutch.',
                  'شركة تصدير فردية من غاندهيدهام، كاتش، غوجارات، تشحن رمان بهغوا الطازج والملح من كاتش.'),
                t('About Us', 'من نحن')) + f'''
<section class="section"><div class="container split">
<div>
<h2>{t('Our story', 'قصتنا')}</h2>
<p>{t('SRP EXIM is a proprietorship firm based at Padana, Gandhidham, in Kachchh, Gujarat. The proprietor is Shambhubhai Sakhayabhai Humbal.', 'SRP EXIM شركة فردية مقرها بادانا، غاندهيدهام، في كاتش بولاية غوجارات. المالك هو شامبهوبهاي ساخايابهاي هومبال (Shambhubhai Sakhayabhai Humbal).')}</p>
<p>{t('We export fresh Bhagwa pomegranates and salt. We buy directly from pomegranate farms and from the salt pans of Kutch, check the quality before dispatch, and prepare the complete export documentation.', 'نُصدّر رمان بهغوا الطازج والملح. نشتري مباشرة من مزارع الرمان ومن ملاحات كاتش، ونفحص الجودة قبل الشحن، ونُعدّ مستندات التصدير كاملة.')}</p>
<p>{t('Our office is close to Kandla (Deendayal) and Mundra ports. We work on FOB and CIF terms and serve buyers who need full container loads.', 'مكتبنا قريب من ميناءي كاندلا (ديندايال) ومندرا. نعمل بشروط FOB وCIF ونخدم المشترين الذين يحتاجون حمولات حاويات كاملة.')}</p>
<div class="btn-row"><a class="btn btn-red" href="contact.html">{QUOTE}</a></div>
</div>
{img('hero.svg', ALT_HERO, 800, 640, lazy=False)}
</div></section>

<section class="section alt"><div class="container">
<div class="section-head"><h2>{t('Our team', 'فريقنا')}</h2></div>
<div class="grid g3">{''.join(f'<div class="card person"><div class="avatar">{ICON["user"]}</div><h3>{n}</h3><p>{r}</p></div>' for n, r in team)}</div>
</div></section>

<section class="section"><div class="container">
<div class="section-head"><h2>{t('Find us', 'موقعنا')}</h2><p><address style="font-style:normal">{ADDR}</address></p></div>
<iframe class="map" title="{t('Map of SRP Exim office in Padana, Gandhidham', 'خريطة مكتب SRP Exim في بادانا، غاندهيدهام')}" src="{MAP}" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe>
<p style="margin-top:14px"><a href="{MAPLINK}" target="_blank" rel="noopener">{t('Open in Google Maps', 'افتح في خرائط Google')} {arrow}</a></p>
</div></section>
{cta(t('Talk to our team', 'تحدث مع فريقنا'), t('Call, WhatsApp or send an enquiry. We will reply with a quotation.', 'اتصل أو راسلنا على واتساب أو أرسل استفسارك، وسنرد عليك بعرض سعر.'))}'''
    out['about'] = page('about',
        t('About SRP Exim | Pomegranate &amp; Salt Exporter, Gandhidham Gujarat', 'من نحن | SRP Exim - مُصدِّر رمان وملح، غاندهيدهام غوجارات'),
        t('SRP Exim is a proprietorship exporter in Gandhidham, Kachchh, Gujarat, near Kandla and Mundra ports. Meet the team and find our office on the map.',
          'SRP Exim شركة تصدير فردية في غاندهيدهام، كاتش، غوجارات، قرب ميناءي كاندلا ومندرا. تعرّف على الفريق وموقع مكتبنا على الخريطة.'),
        body)

    # ---------------- CERTIFICATIONS
    badges = [('IEC', t('Import Export Code (DGFT)', 'رمز الاستيراد والتصدير (DGFT)'), IEC, ''),
              ('GSTIN', t('GST Identification Number', 'رقم التسجيل الضريبي GST'), GST, ''),
              ('FSSAI', t('FSSAI Central License', 'ترخيص FSSAI المركزي'), FSSAI, ''),
              ('Udyam', t('Udyam Registration (MSME)', 'تسجيل أُديام (MSME)'), UDYAM, ''),
              ('RCMC', t('APEDA &mdash; registered member', 'APEDA — عضو مسجّل'), '[TBD]', ' tbd')]
    body = head(t('Registrations &amp; Certifications', 'التسجيلات والتراخيص'),
                t('SRP Exim is a registered exporter. These are our registration numbers.', 'SRP Exim مُصدِّر مسجّل. هذه أرقام تسجيلاتنا.'),
                t('Certifications', 'الشهادات')) + f'''
<section class="section"><div class="container">
<div class="grid g3">{''.join(f'<div class="card badge"><span class="tag">{a}</span><h3>{b}</h3><span class="num{c}" dir="ltr">{n}</span></div>' for a, b, n, c in badges)}</div>
<p class="form-note" style="margin-top:22px">{t('Firm: SRP EXIM (Proprietorship) &middot; Proprietor: Shambhubhai Sakhayabhai Humbal', 'المنشأة: SRP EXIM (شركة فردية) · المالك: Shambhubhai Sakhayabhai Humbal')}</p>
</div></section>
{cta(t('Need more details?', 'هل تحتاج إلى مزيد من التفاصيل؟'), t('Contact us and we will answer your questions.', 'تواصل معنا وسنجيب عن أسئلتك.'))}'''
    out['certifications'] = page('certifications',
        t('Registrations &amp; Certifications | IEC, GSTIN, FSSAI, Udyam - SRP Exim', 'التسجيلات والتراخيص | IEC وGSTIN وFSSAI وأُديام - SRP Exim'),
        t('SRP Exim registrations: IEC (DGFT), GSTIN, FSSAI Central License, Udyam (MSME) and APEDA RCMC. Registered exporter from Gandhidham, Gujarat.',
          'تسجيلات SRP Exim: IEC (DGFT)، GSTIN، ترخيص FSSAI المركزي، أُديام (MSME) وAPEDA RCMC. مُصدِّر مسجّل من غاندهيدهام، غوجارات.'),
        body)

    # ---------------- CONTACT
    products = [t('Fresh Bhagwa Pomegranate', 'رمان بهغوا الطازج'), t('Industrial Salt', 'ملح صناعي'), t('Edible Salt', 'ملح غذائي'), t('More than one product', 'أكثر من منتج')]
    F = lambda en, a: t(en, a)
    body = head(t('Request a Quotation', 'اطلب عرض سعر'),
                t('Send us your enquiry for Bhagwa pomegranate or salt. We will reply with a quotation on FOB or CIF terms.', 'أرسل استفسارك عن رمان بهغوا أو الملح، وسنرد عليك بعرض سعر بشروط FOB أو CIF.'),
                t('Contact', 'اتصل بنا')) + f'''
<section class="section"><div class="container contact-grid">
<!-- FORMSPREE_ID: replace FORMSPREE_ID in the action below with your Formspree form id (see README.md) -->
<form class="quote" id="quote-form" action="https://formspree.io/f/FORMSPREE_ID" method="POST"
 data-ok="{t('Thank you! Your enquiry has been sent. We will reply soon.', 'شكراً لك! تم إرسال استفسارك وسنرد قريباً.')}"
 data-err="{t('Sorry, the form could not be sent. Your email app will open so you can send it by email instead.', 'عذراً، تعذّر إرسال النموذج. سيُفتح تطبيق البريد لإرساله عبر البريد الإلكتروني.')}"
 data-mailto="{t('Your email app has been opened. Please press Send there.', 'تم فتح تطبيق البريد. يرجى الضغط على إرسال هناك.')}">
<div class="fields">
<div><label for="f-name">{t('Name', 'الاسم')} <span class="req">*</span></label><input id="f-name" name="name" type="text" autocomplete="name" required></div>
<div><label for="f-company">{t('Company', 'الشركة')}</label><input id="f-company" name="company" type="text" autocomplete="organization"></div>
<div><label for="f-country">{t('Country', 'الدولة')} <span class="req">*</span></label><input id="f-country" name="country" type="text" autocomplete="country-name" required></div>
<div><label for="f-email">{t('Email', 'البريد الإلكتروني')} <span class="req">*</span></label><input id="f-email" name="email" type="email" autocomplete="email" required dir="ltr"></div>
<div><label for="f-wa">{t('WhatsApp (with country code)', 'واتساب (مع رمز الدولة)')}</label><input id="f-wa" name="whatsapp" type="tel" autocomplete="tel" placeholder="+" dir="ltr"></div>
<div><label for="f-product">{t('Product', 'المنتج')} <span class="req">*</span></label><select id="f-product" name="product" required><option value="">{t('Select a product', 'اختر المنتج')}</option>{''.join(f'<option>{p}</option>' for p in products)}</select></div>
<div><label for="f-qty">{t('Quantity', 'الكمية')}</label><input id="f-qty" name="quantity" type="text" placeholder="{t('e.g. 1 container', 'مثال: حاوية واحدة')}"></div>
<div><label for="f-port">{t('Destination port', 'ميناء الوجهة')}</label><input id="f-port" name="destination_port" type="text"></div>
<div class="full"><label for="f-msg">{t('Message', 'الرسالة')}</label><textarea id="f-msg" name="message"></textarea></div>
<div class="hp" aria-hidden="true"><label>Leave empty <input name="_gotcha" type="text" tabindex="-1" autocomplete="off"></label></div>
<input type="hidden" name="_subject" value="New quotation request - SRP Exim website">
</div>
<div class="btn-row"><button class="btn btn-red" type="submit">{t('Send enquiry', 'إرسال الاستفسار')}</button><button class="btn btn-line" type="button" id="mailto-btn">{t('Send by email instead', 'أرسل عبر البريد بدلاً من ذلك')}</button></div>
<p class="status" id="form-status" role="status" aria-live="polite"></p>
<p class="form-note">{t('Fields marked * are required. You can also message us directly on WhatsApp.', 'الحقول المعلّمة * مطلوبة. يمكنك أيضاً مراسلتنا مباشرة على واتساب.')}</p>
</form>
<aside class="card info"><h3>{t('Contact details', 'بيانات التواصل')}</h3>
<ul>
<li><span class="lbl">{t('Phone / WhatsApp 1', 'الهاتف / واتساب 1')}</span><a href="tel:{TEL1}">{ltr(PH1)}</a></li>
<li><span class="lbl">{t('Phone / WhatsApp 2', 'الهاتف / واتساب 2')}</span><a href="tel:{TEL2}">{ltr(PH2)}</a></li>
<li><span class="lbl">{t('Email', 'البريد الإلكتروني')}</span><a href="mailto:{EMAIL}">{EMAIL}</a></li>
<li><span class="lbl">{t('Address', 'العنوان')}</span>{ADDR}</li>
</ul>
<div class="btn-row"><a class="btn btn-wa" href="{WA}" target="_blank" rel="noopener">{t('Chat on WhatsApp', 'تحدث عبر واتساب')}</a></div>
</aside>
</div></section>'''
    out['contact'] = page('contact',
        t('Request a Quotation | Contact SRP Exim - Pomegranate &amp; Salt Exporter', 'اطلب عرض سعر | اتصل بـ SRP Exim - مُصدِّر رمان وملح'),
        t('Request a quotation from SRP Exim, Gandhidham, Gujarat. Call or WhatsApp +91 96873 80132 / +91 92659 73224, or email srpexim2025@gmail.com.',
          'اطلب عرض سعر من SRP Exim في غاندهيدهام، غوجارات. اتصل أو راسل على واتساب +91 96873 80132 / +91 92659 73224 أو عبر البريد srpexim2025@gmail.com.'),
        body)

    d = os.path.join(ROOT, 'ar') if ar else ROOT
    os.makedirs(d, exist_ok=True)
    for slug, html in out.items():
        with open(os.path.join(d, href(slug)), 'w', encoding='utf-8') as f:
            f.write(html)

build('en'); build('ar')

# sitemap, robots
urls = ''
for p in PAGES:
    e = SITE + '/' + ('' if p == 'index' else p + '.html'); a = SITE + '/ar/' + ('' if p == 'index' else p + '.html')
    for u in (e, a):
        urls += (f'<url><loc>{u}</loc><xhtml:link rel="alternate" hreflang="en" href="{e}"/>'
                 f'<xhtml:link rel="alternate" hreflang="ar" href="{a}"/></url>\n')
open(os.path.join(ROOT, 'sitemap.xml'), 'w').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' + urls + '</urlset>\n')
open(os.path.join(ROOT, 'robots.txt'), 'w').write(f'User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n')
open(os.path.join(ROOT, 'CNAME'), 'w').write('srpexim.in\n')
open(os.path.join(ROOT, '.nojekyll'), 'w').write('')
print('built')
