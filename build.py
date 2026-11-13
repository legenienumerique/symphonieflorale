"""Générateur de la maquette Symphonie Florale. Usage : python build.py <dossier-du-projet>
Contenus relevés le 13/11/2026 sur symphonieflorale.eu : textes, prestations, galerie photos, logo (fleur au trait
vert-jaune #bfc75f), police Poppins ; fiche Google (4,6/5, 78 avis, horaires, avis cités)."""
import os
import sys
OUT = sys.argv[1] if len(sys.argv) > 1 else "."
A = 'assets/'
PH = A + 'ph/'
V = 2  # cache : incrémenter à chaque changement de CSS ou JS
TEL, TELH = '04 74 55 03 32', 'tel:0474550332'
MAIL = 'symphonie.florale370@orange.fr'
ADR = ('3 rue Gambetta', '01400 Châtillon-sur-Chalaronne')
SHOP = 'https://fleuristes-et-fleurs.com/fleuriste/symphonie-florale-chatillon-sur-chalaronne-01400'

NAV = [('fleuriste.html', 'Le fleuriste'), ('mariages.html', 'Mariages'), ('galerie.html', 'Galerie')]
PHONE_SVG = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2c.3-.3.7-.4 1-.2 1.1.4 2.3.6 3.6.6.6 0 1 .4 1 1V20c0 .6-.4 1-1 1A17 17 0 0 1 3 4c0-.6.4-1 1-1h3.5c.6 0 1 .4 1 1 0 1.3.2 2.5.6 3.6.1.3 0 .7-.2 1z" fill="currentColor"/></svg>'


def pill(t, href, cls='', arrow='↗'):
    ext = ' target="_blank" rel="noopener"' if href.startswith('http') else ''
    return f'<a class="pill {cls}" href="{href}"{ext}><span class="r"><span>{t}</span><span>{t}</span></span><b>{arrow}</b></a>'


def tile(src, cls='', style='', alt='', par=None, lazy=True):
    p = f' data-par="{par}" style="height:118%;width:100%"' if par else ''
    return f'<figure class="tile {cls}" style="{style}"><img src="{src}" alt="{alt}"{p}{" loading=lazy" if lazy else ""}></figure>'


def logo(cls=''):
    return f'<span class="lgo sf {cls}" aria-hidden="true"><i><img src="{A}fleur.png" alt=""></i><span><span class="wm">Symphonie <b>florale</b></span><small>Fleuriste · Châtillon</small></span></span>'


def head(title, desc, cur):
    def a(h, t, cls=''):
        return f'<a href="{h}"{" class="+cls if cls else ""}{" aria-current=page" if h == cur else ""}>{t}</a>'
    items = a('index.html', 'Accueil') + ''.join(a(h, t) for h, t in NAV) + a('contact.html', 'Nous trouver', 'hl')
    return f'''<!doctype html>
<html lang="fr"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><meta name="description" content="{desc}">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:type" content="website">
<meta name="theme-color" content="#141112">
<meta name="robots" content="noindex, nofollow">
<link rel="icon" href="{A}favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{A}style.css?v={V}">
</head><body>
<div class="pipe" aria-hidden="true"><div class="pp"><i class="drop"></i></div></div>
<header class="top">
<a class="logo" href="index.html" aria-label="Symphonie Florale, accueil">{logo()}</a>
<nav class="nav" aria-label="Navigation principale">{items}</nav>
<span class="side"><a class="tel" href="{TELH}" aria-label="Appeler le {TEL}">{PHONE_SVG}<span>{TEL}</span></a></span>
<button class="burger" aria-label="Menu" aria-expanded="false"><i></i><i></i></button>
</header>
<main>'''


def foot():
    return f'''</main>
<footer><div class="wrap"><div class="fg">
<div>{logo('big')}<p>Le fleuriste au cœur de l’histoire : dans le centre historique de Châtillon-sur-Chalaronne, entre les Halles et les Portes de Villars.</p></div>
<div><h4 class="micro">Fleurs</h4><ul><li><a href="fleuriste.html">Bouquets et compositions</a></li><li><a href="mariages.html">Mariages</a></li><li><a href="fleuriste.html#deuil">Deuils</a></li><li><a href="fleuriste.html#deco">Décoration</a></li><li><a href="galerie.html">Galerie</a></li></ul></div>
<div><h4 class="micro">Contact</h4><ul><li><a href="{TELH}">{TEL}</a></li><li><a href="mailto:{MAIL}">{MAIL}</a></li><li><a href="{SHOP}" target="_blank" rel="noopener">Boutique en ligne</a></li></ul></div>
<div><h4 class="micro">Boutique</h4><ul><li>{ADR[0]}</li><li>{ADR[1]}</li><li><a href="contact.html">Horaires</a></li></ul></div>
</div></div>
<div class="fw" aria-hidden="true">SYMPHONIE</div>
<div class="fb micro"><span class="pad">© Symphonie Florale</span><span class="pad">Maquette de site · Le Génie Numérique</span></div></footer>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"></script>
<script src="https://unpkg.com/lenis@1.1.13/dist/lenis.min.js"></script>
<script src="{A}main.js?v={V}"></script></body></html>'''


def cta(t='Une envie <em>de fleurs ?</em>'):
    return f'''<section class="sec cta"><div class="wrap"><span class="micro mute" style="display:block;margin-bottom:1.6rem">Commande par téléphone · en boutique · en ligne</span><h2 class="sp">{t}</h2>
<div class="row rv">{pill('Appeler la boutique', TELH, 'blue')}{pill('Commander en ligne', SHOP, 'ghost')}</div></div></section>'''


def pagehead(crumb, h1, lead, img, img2=None, extra=''):
    t2 = tile(img2, 'small', lazy=False) if img2 else ''
    return f'''<section class="ph"><div class="wrap"><div class="crumb micro"><a href="index.html">Accueil</a> / {crumb}</div><h1 class="sp">{h1}</h1><p class="lead rv">{lead}</p>{extra}</div>{tile(img, lazy=False)}{t2}</section>'''


def faq(its):
    return '<div class="faq">' + ''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in its) + '</div>'


# avis Google publiés (prénom affiché par l'auteur), relevés le 13/11/2026
AVIS = [('Alyson C.', '2026', 'J’ai commandé par téléphone un bouquet de fleurs pour l’anniversaire d’un proche. Je suis extrêmement heureuse du rendu du bouquet, solaire, garni et magnifique. Je la recommande très fortement !'),
        ('Martine', '2026', 'J’ai commandé par téléphone un coussin de fleurs coupées pour des obsèques. La composition florale était vraiment superbe. Le choix des fleurs, des couleurs, tout était parfait.'),
        ('Mélissa P.', '2026', 'Une fleuriste passionnée, à l’écoute. Cette année, je lui ai confié mon bouquet de mariage : il était magnifique, elle a compris ce que je souhaitais.'),
        ('Blandine S.', '2026', 'Quel plaisir de se rendre dans ce beau magasin décoré avec goût ! Cliente depuis des années, j’ai toujours été très bien conseillée, avec gentillesse.')]


def avis_cards(items):
    return '<div class="rcs">' + ''.join(f'<blockquote class="rc rv"><span class="micro mute">Google · {d}</span><p>« {t} »</p><footer><b>{n}</b><span>Avis Google</span><i>5/5</i></footer></blockquote>' for n, d, t in items) + '</div>'


GAL = [('tournesol2', 'Bouquets', 'Bouquet tournesols et fleurs d’été'), ('arche-lac', 'Mariages', 'Arche fleurie au bord de l’eau'),
       ('peche', 'Bouquets', 'Bouquet tendre, roses et gerberas'), ('reception', 'Mariages', 'Décor de salle de réception'),
       ('hortensia', 'Bouquets', 'Hortensias et roses'), ('coeur', 'Deuils', 'Cœur de roses blanches et bleues'),
       ('pampa', 'Bouquets', 'Bouquet blanc et herbes de la pampa'), ('allee', 'Mariages', 'Allée de cérémonie fleurie'),
       ('vif', 'Bouquets', 'Bouquet coloré'), ('cage', 'Compositions', 'Cage fleurie'),
       ('automne', 'Bouquets', 'Bouquet d’automne'), ('table', 'Mariages', 'Centre de table'),
       ('renoncules', 'Bouquets', 'Renoncules et roses'), ('deuil', 'Deuils', 'Composition ronde de fleurs blanches'),
       ('orange', 'Bouquets', 'Bouquet orangé'), ('chemin-table', 'Mariages', 'Chemin de table fleuri'),
       ('tournesol3', 'Bouquets', 'Tournesols et dahlias'), ('table-blanche', 'Mariages', 'Table blanche et fleurs')]


def gal(items):
    return '<div class="gal">' + ''.join(f'<figure class="rv" data-c="{c}" style="--d:{(i % 3) * .07}s"><img src="{PH}{k}.webp" alt="{t}" loading="lazy"><figcaption><span class="micro">{c}</span>{t}</figcaption></figure>' for i, (k, c, t) in enumerate(items)) + '</div>'


def sec(id_, kicker, h, p, img, alt):
    return f'''
<section class="sec" id="{id_}" style="padding-top:0"><div class="wrap fin"><div><span class="micro mute" style="display:block;margin-bottom:1.2rem">{kicker}</span><h2 class="sp">{h}</h2>
<p class="lead rv" style="margin-top:1.4rem">{p}</p></div>{tile(PH + img, '', par=8, alt=alt)}</div></section>'''


def service(file, title, desc, crumb, h1, lead, img, img2, intro_h, intro_p, checks, faqs, more=''):
    extra = f'<div class="row rv" style="display:flex;gap:10px;flex-wrap:wrap;margin-top:2.2rem">{pill("Appeler", TELH, "blue")}{pill("Commander en ligne", SHOP, "ghost")}</div>'
    cl = ''.join(f'<li><span><b>{a}</b> {b}</span></li>' for a, b in checks)
    return head(title, desc, file) + pagehead(crumb, h1, lead, img, img2, extra) + f'''
<section class="sec"><div class="wrap split"><div><span class="micro mute" style="display:block;margin-bottom:1.2rem">La boutique</span><h2 class="sp">{intro_h}</h2><p class="lead rv" style="margin-top:1.4rem">{intro_p}</p></div><ul class="checks rv">{cl}</ul></div></section>{more}
<section class="sec" style="padding-top:0"><div class="wrap split"><div><span class="micro mute" style="display:block;margin-bottom:1.2rem">Questions fréquentes</span><h2 class="sp">On vous <em>répond</em></h2></div><div class="rv">{faq(faqs)}</div></div></section>''' + cta() + foot()


FAQ_TEL = ('Puis-je commander par téléphone ?', f'Oui. Appelez le {TEL} : donnez votre idée et votre budget, la fleuriste compose le bouquet.')
FAQ_LIV = ('Livrez-vous ?', 'La boutique propose la livraison à Châtillon-sur-Chalaronne et aux alentours (Villars-les-Dombes, Neuville-les-Dames, Saint-Trivier-sur-Moignans…). Conditions à confirmer avec la boutique.')
FAQ_RES = ('Faites-vous partie d’un réseau ?', 'Oui : Symphonie Florale est membre des réseaux Florajet et Agitateur Floral.')


def pages():
    P = {}
    hero_tiles = [('t1', 'logo'), ('t4', 'tournesol2'), ('t5', 'arche-lac')]
    ht = ''.join(f'<figure class="tile {c}{" lg" if f == "logo" else ""}"><div class="fl"><div class="in"><img src="{A + "logo.png" if f == "logo" else PH + f + ".webp"}" alt=""></div></div></figure>' for c, f in hero_tiles)
    items = [('fleuriste.html', '01', 'Bouquets', 'Classiques ou contemporains, pour le plaisir d’offrir.', 'peche'),
             ('mariages.html', '02', 'Mariages', 'Bouquet de la mariée, arches, tables, voitures.', 'arche-lac'),
             ('fleuriste.html#deuil', '03', 'Deuils', 'Coussins, cœurs et compositions, avec délicatesse.', 'coeur'),
             ('fleuriste.html#plantes', '04', 'Plantes', 'Plantes vertes et fleuries, orchidées.', 'vitrine'),
             ('fleuriste.html#deco', '05', 'Décoration', 'Bougies, vases, chandeliers.', 'decoration')]
    pl = ''.join(f'<a href="{h}"><span class="micro mute">{n}</span><span class="nm">{t}</span><span class="d">{d}</span></a>' for h, n, t, d, _ in items)
    prev = ''.join(tile(f'{PH}{it[4]}.webp', 'on' if i == 0 else '') for i, it in enumerate(items))
    steps = [('Vous écouter', 'Votre idée, votre budget, votre occasion.'),
             ('Conseiller', 'Classique ou contemporain : le style qui vous ressemble.'),
             ('Composer', 'Des fleurs fraîches, choisies une à une.'),
             ('Offrir', 'En boutique, par téléphone ou en ligne.')]
    st = ''.join(f'<div class="stp"><div class="n">{i + 1}</div><h3>{t}</h3><p>{d}</p></div>' for i, (t, d) in enumerate(steps))
    mq = ''.join(f'<span>{x}</span>' for x in ['Bouquets', 'Compositions', 'Mariages', 'Deuils', 'Anniversaires', 'Baptêmes', 'Plantes', 'Décoration'] * 2)
    hor = [('Lundi', 'Fermé'), ('Mardi – vendredi', '9 h – 12 h 30 · 14 h – 19 h'), ('Samedi', '9 h – 13 h · 13 h 30 – 19 h'), ('Dimanche', '9 h – 12 h 30')]
    horh = ''.join(f'<span><b>{j}</b> · {h}</span>' for j, h in hor)

    P['index.html'] = head('Symphonie Florale — Fleuriste à Châtillon-sur-Chalaronne (Ain)', 'Symphonie Florale, fleuriste au cœur de Châtillon-sur-Chalaronne : bouquets, compositions, mariages, deuils, plantes et décoration. 4,6/5 sur Google, 78 avis.', 'index.html') + f'''
<section class="hero">
<div class="cap micro c1"><b>Fleuriste</b>au cœur de Châtillon</div>
<div class="cap micro c2"><b>4,6 / 5</b>78 avis Google</div>
<div class="cap micro c3"><b>Florajet</b>et Agitateur Floral</div>
<div class="go">{pill('Commander', TELH)}</div>
{ht}
<p class="para">Bouquets et compositions pour tous les événements de la vie.</p>
<h1 class="word">SYMPHONIE</h1>
<div class="scrollhint micro"><i></i>Défiler</div>
</section>

<div class="mq" aria-hidden="true"><div>{mq}</div></div>

<section class="sec"><div class="wrap fin"><div><span class="micro mute" style="display:block;margin-bottom:1.4rem">Entre les Halles et les Portes de Villars</span><h2 class="sp">Le fleuriste <em>au cœur de l’histoire</em></h2>
<p class="lead rv" style="margin:1.4rem 0 2rem">Dans le centre historique de Châtillon-sur-Chalaronne, Symphonie Florale réalise vos compositions et vos bouquets, pour tous les événements de la vie.</p>
<ul class="checks rv" style="margin-bottom:2rem"><li><span><b>Fleurs fraîches</b>, à la tige ou coupées.</span></li><li><span><b>Plantes vertes et fleuries</b>, pour la maison.</span></li><li><span><b>Des conseils</b> sur tous les styles de bouquets.</span></li></ul>{pill('Nos fleurs', '#services', 'blue')}</div>{tile(PH + 'roses.webp', '', par=8, alt='Bouquet de roses rouges et blanches')}</div></section>

<section class="story"><span class="micro mute m3">Une occasion</span>
<h2><span class="w">Ou</span> <span class="w">juste</span> <span class="w">le</span> <span class="w"><em>plaisir</em></span> <span class="w"><em>d’offrir</em></span></h2>
<div class="stack">{tile(PH + 'gerberas.webp')}{tile(PH + 'hortensia.webp')}{tile(PH + 'tournesol.webp')}</div>
<p class="micro mute m1">Anniversaires, baptêmes, mariages, deuils : venez nous rendre visite.</p><span class="micro mute m2">3 rue Gambetta</span></section>

<section class="sec" id="services"><div class="wrap"><span class="micro mute" style="display:block;margin-bottom:1.4rem">Fleurs, plantes, décoration</span><h2 class="sp" style="margin-bottom:clamp(2rem,5vw,4rem)">Qu’est-ce qu’on <em>compose ?</em></h2>
<div class="plist">{pl}</div></div><div class="prev">{prev}</div></section>

<section class="sec"><div class="wrap"><span class="micro mute" style="display:block;margin-bottom:1.4rem">La galerie</span><h2 class="sp" style="margin-bottom:clamp(2rem,4vw,3rem)">Fraîchement <em>composé</em></h2>
{gal(GAL[:6])}<div class="row rv" style="margin-top:2rem">{pill('Toute la galerie', 'galerie.html', 'blue')}</div></div></section>

<section class="sec"><div class="wrap"><span class="micro mute" style="display:block;margin-bottom:1.4rem">Avis Google</span><h2 class="sp">Elles en <em>parlent</em></h2>
<div class="cnt rv"><div><b data-to="4.6">0</b><span>sur 5, note moyenne sur Google</span></div><div><b data-to="78">0</b><span>avis publiés sur Google</span></div><div><b data-to="2">0</b><span>réseaux de livraison : Florajet, Agitateur Floral</span></div></div>
<div style="margin-top:clamp(2rem,4vw,3rem)">{avis_cards(AVIS[:2])}</div><div style="margin-top:16px">{avis_cards(AVIS[2:])}</div></div></section>

<section class="sec" style="padding-top:0"><div class="wrap"><span class="micro mute" style="display:block;margin-bottom:1.4rem">Votre bouquet</span><h2 class="sp">De l’idée <em>aux fleurs</em></h2><div class="steps">{st}</div></div></section>
{cta()}''' + foot()

    more = sec('deuil', 'Deuils', 'Dire adieu <em>avec des fleurs</em>', 'Coussins, cœurs, compositions et gerbes : la fleuriste respecte vos souhaits, le choix des fleurs et des couleurs. Commande possible par téléphone.', 'deuil.webp', 'Composition de fleurs blanches') + \
        sec('plantes', 'Plantes', 'Vertes <em>et fleuries</em>', 'Plantes vertes, plantes fleuries, orchidées, compositions de plantes grasses, et aussi des fleurs artificielles.', 'vitrine.webp', 'Vitrine de la boutique') + \
        sec('deco', 'Décoration d’intérieur', 'Bougies, vases, <em>chandeliers</em>', 'La boutique présente aussi des objets de décoration d’intérieur, pour accompagner vos fleurs ou faire plaisir.', 'decoration.webp', 'Objets de décoration en boutique')
    P['fleuriste.html'] = service('fleuriste.html', 'Fleuriste à Châtillon-sur-Chalaronne — Symphonie Florale', 'Fleurs fraîches, bouquets, compositions, deuils, plantes vertes et fleuries, décoration d’intérieur. Symphonie Florale, 3 rue Gambetta, Châtillon-sur-Chalaronne.',
        'Le fleuriste', 'Votre <em>fleuriste</em>', 'Fleurs fraîches, à la tige, coupées, plantes vertes et fleuries : nous sommes à votre écoute et vous conseillons.', PH + 'roses.webp', PH + 'peche.webp',
        'Classique ou <em>contemporain</em>', 'Une occasion particulière ou tout simplement le plaisir d’offrir : la fleuriste vous conseille sur tous les styles de bouquets.',
        [('Bouquets', 'et compositions florales.'), ('Anniversaires', ', baptêmes, cadeaux.'), ('Mariages', 'et deuils.'), ('Fleurs naturelles', 'ou artificielles.')],
        [FAQ_TEL, FAQ_LIV, FAQ_RES, ('Où se trouve la boutique ?', f'{ADR[0]}, dans le centre historique de Châtillon-sur-Chalaronne, entre les Halles et les Portes de Villars.')], more)

    mmore = sec('voiture', 'Le grand jour', 'Arches, tables <em>et voitures</em>', 'Arches fleuries, allées de cérémonie, centres et chemins de table, décoration de la voiture des mariés : un seul interlocuteur pour toutes les fleurs du mariage.', 'reception.webp', 'Décor floral de réception')
    P['mariages.html'] = service('mariages.html', 'Fleurs de mariage à Châtillon-sur-Chalaronne — Symphonie Florale', 'Bouquet de mariée, arches, décoration de salle, de table et de voiture. Symphonie Florale, fleuriste à Châtillon-sur-Chalaronne (Ain).',
        'Mariages', 'Flowers for the <em>wedding day</em>', 'Le bouquet de la mariée, la cérémonie, la salle, la voiture : vos fleurs de mariage, pensées avec vous.', PH + 'arche-lac.webp', PH + 'allee.webp',
        'Le bouquet <em>qui vous ressemble</em>', 'Racontez vos envies, vos couleurs, votre lieu. La fleuriste comprend ce que vous souhaitez et le compose.',
        [('Bouquet', 'de la mariée.'), ('Cérémonie', ': arches, allées.'), ('Réception', ': tables et chemins de table.'), ('Voiture', 'des mariés décorée.')],
        [('Quand réserver les fleurs du mariage ?', 'Le plus tôt possible : appelez la boutique pour fixer un rendez-vous. Délais à confirmer avec Symphonie Florale.'), FAQ_LIV, FAQ_TEL], mmore)

    P['galerie.html'] = head('Galerie — Symphonie Florale, Châtillon-sur-Chalaronne', 'Bouquets, mariages, deuils et compositions de Symphonie Florale, fleuriste à Châtillon-sur-Chalaronne.', 'galerie.html') + pagehead('Galerie', 'Galerie <em>photos</em>', 'Bouquets, compositions, mariages : un aperçu de ce qui sort de la boutique.', PH + 'tournesol2.webp') + f'''
<section class="sec"><div class="wrap">{gal(GAL)}</div></section>''' + cta() + foot()

    P['contact.html'] = head('Nous trouver — Symphonie Florale, Châtillon-sur-Chalaronne', f'Symphonie Florale, {ADR[0]}, {ADR[1]}. {TEL}. Horaires, téléphone, e-mail.', 'contact.html') + pagehead('Nous trouver', 'Venez <em>nous voir</em>', 'Une occasion particulière, ou juste le plaisir d’offrir : la boutique vous attend.', PH + 'boutique.webp') + f'''
<section class="sec" id="devis"><div class="wrap split"><div><span class="micro mute" style="display:block;margin-bottom:1.2rem">Coordonnées</span><h2 class="sp">Un appel, <em>un bouquet</em></h2>
<div class="contactline rv" style="margin-top:2rem"><a href="{TELH}">{TEL}</a><a href="mailto:{MAIL}">{MAIL}</a></div>
<p class="lead rv" style="margin-top:1.6rem">{ADR[0]}<br>{ADR[1]}</p>
<div class="hor rv">{horh}<span class="micro">Horaires de la fiche Google, à confirmer</span></div></div>
<form class="f calc rv" id="resa"><div class="fld"><label for="pr">Occasion</label><select id="pr"><option>Anniversaire</option><option>Mariage</option><option>Deuil</option><option>Baptême</option><option>Pour le plaisir</option><option>Autre</option></select></div>
<div class="fld"><label for="pc">Votre idée</label><textarea id="pc" rows="4" placeholder="Couleurs, fleurs, budget, date"></textarea></div>
<div class="r2"><div class="fld"><label for="rn">Nom</label><input id="rn" required></div><div class="fld"><label for="rt">Téléphone</label><input id="rt" type="tel" required></div></div>
<button class="pill blue" type="submit" style="justify-self:start"><span class="r"><span>Envoyer</span><span>Envoyer</span></span><b>↗</b></button><div class="ok">Merci ! (Maquette : aucune demande n’est envoyée.)</div></form></div></section>''' + foot()
    return P


for k, v in pages().items():
    open(os.path.join(OUT, k), 'w', encoding='utf-8').write(v)
print('ok')
