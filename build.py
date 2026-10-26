# Generates the six HTML pages from shared header/footer. Run: python3 build.py (optional; HTML files are already included)
NAME="GOVT. MODEL BOYS (EVENING) COLLEGE MIRPURKHAS"
PAGES=[("index.html","Home"),("about.html","About"),("departments.html","Departments"),("faculty.html","Faculty"),("notices.html","Notices"),("contact.html","Contact")]
def page(fn,title,desc,body):
    nav="".join(f'<li class="nav-item"><a class="nav-link{" active" if f==fn else ""}" href="{f}"{" aria-current=\"page\"" if f==fn else ""}>{t}</a></li>' for f,t in PAGES)
    return f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} | {NAME}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title} | {NAME}"><meta property="og:description" content="{desc}"><meta property="og:type" content="website">
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
<link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Merriweather:wght@700&family=Source+Sans+3:wght@400;600&display=swap" rel="stylesheet">
<link href="css/style.css" rel="stylesheet">
</head><body>
<a class="skip-link" href="#main">Skip to main content</a>
<div class="topbar py-1"><div class="container small">Sample site &mdash; details marked <span class="badge badge-sample">SAMPLE</span> are placeholders to be replaced with official information.</div></div>
<nav class="navbar navbar-expand-lg site-nav" aria-label="Main navigation"><div class="container">
<a class="navbar-brand d-flex align-items-center gap-2" href="index.html"><img src="img/logo-placeholder.svg" alt="College logo placeholder" width="52" height="52"><span class="brand-name">{NAME}</span></a>
<button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#menu" aria-controls="menu" aria-expanded="false" aria-label="Toggle navigation"><span class="navbar-toggler-icon"></span></button>
<div class="collapse navbar-collapse" id="menu"><ul class="navbar-nav ms-auto">{nav}</ul></div></div></nav>
<main id="main">
{body}
</main>
<footer class="site-footer"><div class="container"><div class="row g-4 py-4">
<div class="col-md-5"><h2 class="h6 text-gold">{NAME}</h2><p class="small mb-0">Evening college, Mirpurkhas, Sindh, Pakistan.<br>Address, phone and email: see the <a href="contact.html">Contact</a> page (placeholders until verified).</p></div>
<div class="col-6 col-md-3"><h2 class="h6 text-gold">Pages</h2><ul class="list-unstyled small mb-0">{"".join(f'<li><a href="{f}">{t}</a></li>' for f,t in PAGES)}</ul></div>
<div class="col-6 col-md-4"><h2 class="h6 text-gold">Note</h2><p class="small mb-0">This is an unofficial sample website. Names, dates, programs and contact details marked as sample are not verified.</p></div></div>
<div class="border-top border-secondary py-3 small">&copy; <span id="year">2026</span> {NAME}. All rights reserved.</div></div></footer>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
<script src="js/script.js"></script>
</body></html>'''
S='<span class="badge badge-sample">SAMPLE</span>'
def hero(t,sub): return f'<section class="page-hero"><div class="container"><h1>{t}</h1><p class="mb-0">{sub}</p></div></section>'
pages={}
pages["index.html"]=("Home","Official-style website of Govt. Model Boys (Evening) College Mirpurkhas: about, departments, faculty, notices and contact.",f'''
<section class="hero"><div class="container"><div class="row align-items-center g-4">
<div class="col-lg-7"><p class="hero-kicker">Evening college &bull; Mirpurkhas</p><h1>{NAME}</h1>
<p class="lead">Education for working students and those who study after the day's work is done.</p>
<a class="btn btn-gold btn-lg me-2 mb-2" href="about.html">About the college</a><a class="btn btn-outline-light btn-lg mb-2" href="notices.html">Read notices</a></div>
<div class="col-lg-5"><img class="img-fluid rounded shadow" src="img/campus-placeholder.svg" alt="Campus image placeholder" width="640" height="420"></div></div></div></section>
<section class="section"><div class="container"><div class="row g-4">
<div class="col-lg-7"><h2>Welcome message {S}</h2><p>Welcome to the website of {NAME}. This paragraph is sample text: replace it with the Principal's official welcome message.</p>
<p>The college is an evening institution for boys. Admission details, programs and timings are not published here until verified &mdash; please contact the college office.</p></div>
<div class="col-lg-5"><div class="card h-100 border-0 shadow-sm"><div class="card-body"><h2 class="h5">Quick links</h2><div class="list-group list-group-flush">
<a class="list-group-item list-group-item-action" href="departments.html"><i class="bi bi-building me-2"></i>Academic departments</a>
<a class="list-group-item list-group-item-action" href="faculty.html"><i class="bi bi-people me-2"></i>Faculty &amp; administration</a>
<a class="list-group-item list-group-item-action" href="notices.html"><i class="bi bi-megaphone me-2"></i>Notices &amp; announcements</a>
<a class="list-group-item list-group-item-action" href="contact.html"><i class="bi bi-geo-alt me-2"></i>Contact &amp; location</a></div></div></div></div></div></div></section>
<section class="section alt"><div class="container"><h2>Key highlights {S}</h2><div class="row g-4">
<div class="col-md-4"><div class="card feature h-100"><div class="card-body"><i class="bi bi-moon-stars"></i><h3 class="h5">Evening classes</h3><p class="mb-0">Placeholder: describe class timings once confirmed.</p></div></div></div>
<div class="col-md-4"><div class="card feature h-100"><div class="card-body"><i class="bi bi-book"></i><h3 class="h5">Academic programs</h3><p class="mb-0">Placeholder: list officially offered programs.</p></div></div></div>
<div class="col-md-4"><div class="card feature h-100"><div class="card-body"><i class="bi bi-person-check"></i><h3 class="h5">Dedicated staff</h3><p class="mb-0">Placeholder: add verified faculty information.</p></div></div></div></div></div></section>
<section class="section"><div class="container"><div class="d-flex justify-content-between align-items-end mb-3"><h2 class="mb-0">Latest notices</h2><a href="notices.html">All notices</a></div><div id="latest-notices" class="row g-3"></div></div></section>''')
pages["about.html"]=("About the College","About Govt. Model Boys (Evening) College Mirpurkhas: overview, mission, vision and history (placeholders).",hero("About the College",NAME)+f'''
<section class="section"><div class="container"><div class="row g-4"><div class="col-lg-8">
<h2>Overview</h2><p>{NAME} is an evening college in Mirpurkhas, Sindh. {S} Replace this text with an official description approved by the college administration.</p>
<h2 class="mt-4">Mission {S}</h2><p>Sample mission statement: to provide accessible, quality education to students who study in the evening. Replace with the official mission.</p>
<h2 class="mt-4">Vision {S}</h2><p>Sample vision statement: to be a respected institution that prepares students for higher study and work. Replace with the official vision.</p>
<h2 class="mt-4">History {S}</h2><p>No verified history is included. Add the establishment year, milestones and notable events here once confirmed by the college.</p></div>
<div class="col-lg-4"><img class="img-fluid rounded shadow-sm mb-3" src="img/campus-placeholder.svg" alt="Campus placeholder" width="640" height="420"><div class="card border-0 bg-light"><div class="card-body"><h3 class="h6">Key facts {S}</h3><ul class="small mb-0"><li>Established: [year]</li><li>Affiliation: [board/university]</li><li>Classes: [timings]</li></ul></div></div></div></div></div></section>''')
depts=["Department of Sciences","Department of Arts &amp; Humanities","Department of Commerce","Department of Computer Studies","Department of Languages","Department of Islamic Studies"]
pages["departments.html"]=("Academic Departments","Academic departments at Govt. Model Boys (Evening) College Mirpurkhas (sample listing, to be confirmed).",hero("Academic Departments","Sample listing &mdash; confirm official departments and programs with the college.")+'<section class="section"><div class="container"><div class="alert alert-warning">The departments below are <strong>sample entries</strong>, not an official list. Edit or delete them before publishing.</div><div class="row g-4">'+"".join(f'<div class="col-md-6 col-lg-4"><div class="card h-100 border-0 shadow-sm"><div class="card-body"><i class="bi bi-journal-bookmark fs-2 text-gold-d"></i><h2 class="h5 mt-2">{d} {S}</h2><p>Sample description. Add the real subjects, programs and head of department.</p><p class="small text-muted mb-0">Head: [name] &bull; Programs: [list]</p></div></div></div>' for d in depts)+'</div></div></section>')
fac=[("Principal","Sample Name 1"),("Vice Principal","Sample Name 2"),("Head of Department","Sample Name 3"),("Lecturer","Sample Name 4"),("Lecturer","Sample Name 5"),("Office Superintendent","Sample Name 6")]
pages["faculty.html"]=("Faculty and Administration","Faculty and administration of Govt. Model Boys (Evening) College Mirpurkhas (placeholder profiles).",hero("Faculty &amp; Administration","Placeholder profiles")+'<section class="section"><div class="container"><div class="alert alert-warning">All names, roles and images are <strong>sample content</strong>. Replace with verified staff details.</div><div class="row g-4">'+"".join(f'<div class="col-sm-6 col-lg-4"><div class="card text-center h-100 border-0 shadow-sm"><div class="card-body"><img class="rounded-circle mb-3" src="img/person-placeholder.svg" alt="Photo placeholder for {n}" width="120" height="120"><h2 class="h5 mb-1">{n}</h2><p class="mb-1 fw-semibold">{r} {S}</p><p class="small text-muted mb-0">Qualification: [add] &bull; Subject: [add]</p></div></div></div>' for r,n in fac)+'</div></div></section>')
pages["notices.html"]=("Notices and Announcements","Searchable notices and announcements from Govt. Model Boys (Evening) College Mirpurkhas (sample notices).",hero("Notices &amp; Announcements","Search by keyword or filter by category")+'''<section class="section"><div class="container">
<div class="alert alert-warning">These are <strong>sample notices</strong>. To add real ones, edit the <code>NOTICES</code> list at the top of <code>js/script.js</code>.</div>
<div class="row g-2 mb-4"><div class="col-md-8"><label class="visually-hidden" for="notice-search">Search notices</label><input id="notice-search" type="search" class="form-control" placeholder="Search notices..."></div>
<div class="col-md-4"><label class="visually-hidden" for="notice-category">Category</label><select id="notice-category" class="form-select"><option value="">All categories</option></select></div></div>
<p id="notice-count" class="small text-muted" aria-live="polite"></p><div id="notice-list" class="row g-3"></div></div></section>''')
pages["contact.html"]=("Contact","Contact Govt. Model Boys (Evening) College Mirpurkhas: address, phone, email and contact form (placeholders).",hero("Contact","Placeholder details &mdash; replace with verified information")+f'''<section class="section"><div class="container"><div class="row g-4">
<div class="col-lg-5"><h2>College details {S}</h2><ul class="list-unstyled contact-list">
<li><i class="bi bi-geo-alt"></i> {NAME}, Mirpurkhas, Sindh, Pakistan. [Street address to be added]</li>
<li><i class="bi bi-telephone"></i> [Phone number to be added]</li>
<li><i class="bi bi-envelope"></i> [Official email to be added]</li>
<li><i class="bi bi-clock"></i> [Office hours to be added]</li></ul>
<div class="map-box" role="img" aria-label="Map placeholder"><i class="bi bi-map"></i><p class="mb-0">Map placeholder. Paste a Google Maps embed &lt;iframe&gt; here.</p></div></div>
<div class="col-lg-7"><h2>Send a message</h2>
<div class="alert alert-info small"><strong>How this form works:</strong> it is not connected to a server. Clicking Send opens your email app with a draft addressed to the college email set in <code>js/script.js</code> (currently a placeholder). Nothing is stored or sent automatically.</div>
<form id="contact-form" novalidate><div class="row g-3">
<div class="col-md-6"><label class="form-label" for="c-name">Your name</label><input class="form-control" id="c-name" required minlength="2"><div class="invalid-feedback">Enter your name (at least 2 characters).</div></div>
<div class="col-md-6"><label class="form-label" for="c-email">Your email</label><input type="email" class="form-control" id="c-email" required><div class="invalid-feedback">Enter a valid email address.</div></div>
<div class="col-12"><label class="form-label" for="c-subject">Subject</label><input class="form-control" id="c-subject" required><div class="invalid-feedback">Enter a subject.</div></div>
<div class="col-12"><label class="form-label" for="c-message">Message</label><textarea class="form-control" id="c-message" rows="5" required minlength="10"></textarea><div class="invalid-feedback">Enter a message (at least 10 characters).</div></div>
<div class="col-12"><button class="btn btn-navy" type="submit">Open email draft</button> <span id="form-status" class="ms-2 small" role="status"></span></div></div></form></div></div></div></section>''')
for fn,(t,d,b) in pages.items(): open(fn,"w",encoding="utf-8").write(page(fn,t,d,b))
