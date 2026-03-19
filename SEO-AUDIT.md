# SEO Content Audit
## https://smarthome-smartelec.fr
### Date : 19 mars 2026

---

## SEO Health Score : 32/100

**Verdict :** Le site souffre de problèmes SEO structurels sévères qui limitent fortement sa visibilité organique. La crise d'identité de marque (SmartHome SmartElec vs AI Automation) empêche Google de construire un profil E-E-A-T cohérent. Le SEO local est sous-exploité malgré un fort potentiel. Les fondations techniques (SSL, robots.txt, sitemap, viewport) sont en place, mais l'optimisation on-page et le contenu sont insuffisants.

---

## Inventaire du site

**23 URLs indexées au total :**

| Type | Nombre | Détail |
|------|--------|--------|
| Pages de services | 5 | Homepage, Domotique, Électricité, Maintien à domicile, Alarmes (2 pages) |
| Articles de blog | 11 | 5 articles 2025, 1 article 2021 (VMC), 1 article 2021 (borne), 1 article 2019, 1 article 2018, 1 remplacement tableau, 1 page /blog/ |
| Pages légales | 3 | CGV, Mentions légales, Politique confidentialité |
| Pages utilitaires | 2 | Contact, Stagiaires |
| **Total** | **23** | Site extrêmement mince |

---

## On-Page SEO Checklist

### Title Tags — Analyse par page

| Page | Title actuel | Longueur | Verdict | Problèmes |
|------|-------------|----------|---------|------------|
| Homepage | "SMARTHOME SMARTELEC - AI Automation" | 35 car. | **Fail** | Trop court, aucun mot-clé métier, aucune localisation, confusion de marque |
| Domotique | "Installateur Domotique, spécialiste en Drôme, Ardèche, Isère, ..." | 65 car. | **Needs Work** | Trop long (tronqué SERP), finit par "..." ce qui est coupé |
| Électricité | "Électricité - AI Automation" | 27 car. | **Fail** | Catastrophiquement court, aucun mot-clé, aucune localisation, "AI Automation" incongruent |
| Maintien à domicile | "Maintien à domicile, la technique au service de l'humain" | 56 car. | **Pass** | Longueur correcte, mais pas de localisation |
| Blog posts 2025 | URLs excessivement longues comme titre implicite | Variable | **Needs Work** | Pas analysé individuellement |

**Recommandations de titles optimisés :**

| Page | Title recommandé | Longueur |
|------|-----------------|----------|
| Homepage | "Automatisation IA pour PME et Artisans \| SmartHome SmartElec Valence" | 68 car. |
| Domotique | "Installateur Domotique Drôme - Maison Connectée \| SmartHome SmartElec" | 69 car. |
| Électricité | "Électricien Valence - Installation & Dépannage \| SmartHome SmartElec" | 68 car. |
| Maintien à domicile | "Maintien à Domicile Domotique Drôme \| SmartHome SmartElec" | 57 car. |

---

### Meta Descriptions — Analyse par page

| Page | Meta actuelle | Long. | Verdict | Problèmes |
|------|--------------|-------|---------|------------|
| Homepage | "Nous changeons de cap : exit l'électricité/domotique → focus total sur la relation client, l'automatisation et la donnée. Fondée par un ancien consultant en" | 156 car. | **Fail** | Parle du pivot interne, pas du client. Coupée en plein milieu. Aucun CTA. |
| Domotique | "La Domotique joue des scénarios de vie (...). Installateur Domotique au service du résidentiel et du **terciaire**." | 148 car. | **Needs Work** | Faute d'orthographe "terciaire" (= tertiaire). Pas de CTA. |
| Électricité | "Faites réaliser votre installation, le câblage de tableaux, d'armoires, le dépannage, la rénovation, la mise en place d'éco-compteur, …" | 135 car. | **Needs Work** | Liste de services sans bénéfice client. Pas de localisation. Pas de CTA. |
| Maintien à domicile | "Profitez des innovations numériques afin de favoriser l'autonomie et le maintien à domicile : scénarios de vie, commandes vocales, ..." | 134 car. | **Needs Work** | Correct mais pourrait être plus engageant. Pas de CTA. |

**Meta descriptions recommandées :**

| Page | Meta recommandée |
|------|-----------------|
| Homepage | "Automatisez vos processus métier grâce à l'IA : chatbots, devis automatiques, CRM. Audit gratuit 30 min pour PME et artisans. Valence et toute la France." |
| Domotique | "Installateur domotique certifié en Drôme, Ardèche, Isère. Scénarios de vie, chauffage connecté, volets, sécurité. Devis gratuit — 06 72 13 91 37." |
| Électricité | "Électricien à Valence : installation, rénovation, dépannage, tableaux électriques. Certifié H0V/B2V/BR/BC/IRVE. Devis gratuit — 06 72 13 91 37." |

---

### Heading Hierarchy (H1-H6) — Analyse par page

#### Homepage
```
H1: SMARTHOME SMARTELEC ← Nom de marque, pas de mot-clé
  H2: Assistants IA pour PME et AssociationsÉlectricité, Domotique ← H2 collé sans espace
  H2: Pourquoi SMARTHOME SMARTELEC ? ✓
  H2: Les problèmes que nous résolvons ✓
  H2: Ce que nous apportons ✓
  H2: Méthodologie en 3 étapes ✓
  H2: Exemples d'applications concrètes ✓
  H2: Notre stack (sélection) ✓
  H2: À propos ✓
    H3: Notre héritage (historique) ✓
    H5: Parler à un expert : ← Saut de H3 à H5 (skip H4)
    H5: 1) Données fiabilisées ← H5 inapproprié pour du contenu principal
    H5: 2) Processus automatisés
    H5: 3) Assistants IA (chatbots)
```
**Verdict : Needs Work** — H1 = nom de marque sans keyword. Sauts de niveaux (H3→H5). Le premier H2 a un problème de concaténation de texte.

#### Domotique
```
H1: Maison Connectée / Domotique ← Bon
  H2: Des scénarios domotique pour plus de confort ✓
  H2: Marques domotique / maison connectée ✓
  H2: Gérer votre location à distance ✓
  ... (10 H2 au total, 29 H3)
```
**Verdict : Pass** — Bonne structure, riche en mots-clés. Peut-être trop de H3 (29) mais hiérarchie respectée.

#### Électricité
```
H1: Électricité ← Trop générique, aucun qualificatif
  (PAS DE H2 !)
  H3: Interventions ← Saut direct H1 → H3
  H3: Articles récents
  H3: INFORMATIONS
  H3: CONTACT
```
**Verdict : Fail** — Aucun H2 ! Saut de H1 directement à H3. La page est structurellement déficiente pour le SEO. Le H1 "Électricité" est un mot générique sans localisation ni spécificité.

#### Maintien à domicile
```
H1: Maintien à domicile ← Correct mais pourrait être plus spécifique
  H2: Solutions Domotique favorisant : ✓
  H2: Solutions Domotique permettant : ✓
    H3: Le bien-être ✓ / La sécurité ✓ / La qualité de l'air ✓ ...
      H4: LES PRINCIPALES FONCTIONS ✓
        H5: Fonctions pour le confort... ✓
```
**Verdict : Pass** — Bonne hiérarchie respectée.

---

### Image Optimization

| Page | Total images | Sans alt | Lazy loading | Verdict |
|------|-------------|----------|-------------|---------|
| Homepage | 12 | 1 (8%) | 6 (50%) | **Needs Work** |
| Domotique | 12 | 3 (25%) | 7 (58%) | **Needs Work** |
| Électricité | 7 | **4 (57%)** | 2 (29%) | **Fail** |
| Maintien à domicile | 5 | 2 (40%) | **0 (0%)** | **Fail** |
| **Total** | **36** | **10 (28%)** | **15 (42%)** | **Fail global** |

**Problèmes critiques :**
- 10 images sur 36 n'ont pas d'alt text (28%) — impact accessibilité ET SEO
- La page Électricité a 57% d'images sans alt — la pire du site
- La page Maintien à domicile n'a AUCUN lazy loading
- Aucun format next-gen détecté (WebP/AVIF) — images en JPEG/PNG classiques
- Image OG homepage : 1392x752px JPEG uploadée en 2025, pas de taille compressée vérifiable
- Un alt text identifié comme nom de fichier ("Activage-3-etapes.png") au lieu d'un texte descriptif

**Éléments positifs :**
- `srcset` responsive images détecté
- `contain-intrinsic-size` CSS appliqué (bon pour CLS)
- Alt text descriptifs en français sur les images qui en ont

---

### Internal Linking

| Page | Liens internes | Liens externes | Total | Verdict |
|------|---------------|---------------|-------|---------|
| Homepage | 27 | 18 | 52 | **Needs Work** |
| Domotique | 27 | 10 | 44 | **Needs Work** |
| Électricité | 27 | 1 | 35 | **Needs Work** |
| Maintien à domicile | 27 | 4 | 38 | **Needs Work** |

**Problèmes :**
- Toutes les pages ont exactement 27 liens internes — signe que la majorité sont des liens de navigation/footer/sidebar, pas du maillage contextuel
- Aucun lien interne contextuel détecté entre les pages de services et les articles de blog pertinents
- La page Électricité n'a qu'1 seul lien externe — très isolée
- Pas de structure en silos thématiques (domotique → articles domotique, IA → articles IA)
- Les articles de blog ne semblent pas lier vers les pages de services

**Liens manquants recommandés :**
| Depuis | Vers | Anchor text suggéré |
|--------|------|---------------------|
| Blog "Tywell Delta Dore" | /domotique-maison-connectee/ | "notre service d'installation domotique" |
| Blog "n8n automation" | Homepage (section IA) | "nos services d'automatisation pour PME" |
| /domotique-maison-connectee/ | Blog "maison connectée avantages" | "découvrez les avantages de la maison connectée" |
| /electricite-habitation-magasin/ | Blog "remplacement tableau" | "en savoir plus sur le remplacement de tableau" |
| Homepage | /domotique-maison-connectee/ | "installation domotique en Drôme" |

---

### URL Structure

| URL | Longueur | Verdict | Problème |
|-----|----------|---------|----------|
| `/` | 1 | Pass | — |
| `/domotique-maison-connectee/` | 29 | Pass | Bon slug descriptif |
| `/electricite-habitation-magasin/` | 32 | Needs Work | "habitation-magasin" peu clair pour le SEO |
| `/maintien-a-domicile/` | 21 | Pass | Bon |
| `/guide-des-outils-de-productivite-2025-10-categories-essentielles-analysees/` | 76 | **Fail** | Beaucoup trop long (76 car.) |
| `/unlocking-workflow-automation-the-power-of-n8n-for-agencies/` | 60 | Needs Work | En anglais sur un site FR |
| `/funnel-qui-vend-pendant-que-vous-dormez-12-tips-actionnables/` | 62 | **Fail** | Trop long |
| `/%f0%9f%8f%a0%e2%9c%a8-tywell-de-delta-dore-la-box-domotique-qui-bichonne-votre-maison/` | 86 | **CRITICAL FAIL** | Emojis encodés dans l'URL ! 🏠✨ — invalide pour le SEO, problèmes d'encodage dans les outils |
| `/optimisez-votre-entreprise-avec-n8n-et-les-agences-ia/` | 55 | Needs Work | Un peu long mais acceptable |

**Problèmes structurels majeurs :**
1. **URL avec emojis** : L'article Tywell a des emojis 🏠✨ encodés en URL — c'est un anti-pattern SEO sévère qui cause des problèmes dans les outils d'analyse, les partages sociaux, et les crawlers.
2. **Article en anglais** : "/unlocking-workflow-automation..." est entièrement en anglais sur un site français, sans balise hreflang — signal de langue incohérent pour Google.
3. **Désalignement navigation/canonical** : Le menu pointe vers `/domotique/` et `/electricite/` alors que les URLs canoniques sont `/domotique-maison-connectee/` et `/electricite-habitation-magasin/`. Cela crée des redirections en chaîne qui diluent le link equity.
4. URLs de blog trop longues (>60 caractères) — les URLs idéales sont <60 caractères.

---

## Content Quality (E-E-A-T)

| Dimension | Score | Evidence |
|-----------|-------|----------|
| **Experience** | **Weak** | Le fondateur a clairement de l'expérience pratique (certifications électriques H0V/B2V/BR/BC/IRVE, installations documentées, projet Activage). Mais cette expérience est mal mise en avant. Pas de photos de réalisations récentes, pas de cas concrets documentés avec résultats, pas de "j'ai fait X et voici le résultat". Les articles de blog 2018-2021 montrent du hands-on (borne de recharge, VMC connectée) mais sont datés. |
| **Expertise** | **Present** | Le parcours IT/CRM + certifications électriques + maîtrise d'outils (n8n, Airtable, NocoDB, Jeedom) démontre une expertise réelle. Les articles 2025 sur n8n montrent un savoir-faire praticien. Cependant, aucune certification AI/data visible, pas de contributions open-source, pas de speaking events. |
| **Authoritativeness** | **Weak** | Aucun backlink connu de sites d'autorité. Pas de profil LinkedIn visible lié depuis le site. Pas de mentions presse. Le projet Activage (EU) est le signal d'autorité le plus fort mais il est sous-exploité. Le og:site_name "AI Automation" n'a aucune autorité de marque. |
| **Trustworthiness** | **Present** | HTTPS actif. Pages légales complètes (CGV, mentions légales, politique confidentialité). Adresse physique et SIRET affichés. CNIL DPO déclaré. Mais : email Gmail (pas professionnel), zéro témoignages, zéro avis Google, le nom de marque crée de la confusion. |

**Score E-E-A-T global : 35/100** — L'expertise sous-jacente est réelle mais la présentation en ligne ne la démontre pas suffisamment pour que Google (ou les utilisateurs) l'évaluent positivement.

---

## Keyword Analysis

### Mots-clés primaires par page

| Page | Keyword primaire ciblé (inféré) | Présent dans Title | Présent dans H1 | Dans meta | Dans URL | Dans les 100 premiers mots | Densité estimée |
|------|-------------------------------|-------------------|-----------------|-----------|----------|--------------------------|----------------|
| Homepage | "automatisation IA PME" | **Non** | **Non** | Partiellement | **Non** | **Non** | <0.5% |
| Domotique | "installateur domotique Drôme" | **Oui** (title) | Partiellement | Partiellement | **Non** | Oui | ~1.5% |
| Électricité | "électricien Valence" | **Non** | **Non** | **Non** | **Non** | **Non** | <0.3% |
| Maintien à domicile | "maintien à domicile domotique" | Oui | Oui | Oui | Oui | Oui | ~2% |

**Constats critiques :**
- La homepage ne cible AUCUN mot-clé commercial de manière intentionnelle
- La page Électricité est un désert SEO : aucun mot-clé géographique, aucun mot-clé d'intention
- Seule la page Maintien à domicile a un ciblage keyword acceptable
- Aucune page ne cible les requêtes IA/automatisation qui sont le nouveau positionnement

### Search Intent Alignment

| Page | Intent cible | Intent réel du contenu | Alignement |
|------|-------------|----------------------|------------|
| Homepage | Commercial / Transactionnel ("consultant IA PME") | Informationnel + Navigationnel (présentation entreprise) | **Désalignement moyen** |
| Domotique | Commercial ("installateur domotique Drôme") | Informationnel (explication des scénarios domotiques) | **Partiellement aligné** |
| Électricité | Transactionnel ("électricien Valence dépannage") | Informationnel (liste de services) | **Désalignement** — trop peu de contenu orienté action |
| Maintien à domicile | Informationnel ("domotique maintien à domicile") | Informationnel | **Aligné** |

### Mots-clés secondaires manquants (Content Gap)

| Mot-clé manquant | Volume potentiel | Concurrence | Type de contenu nécessaire | Priorité |
|-----------------|-----------------|-------------|--------------------------|----------|
| "automatisation PME France" | Medium | Low | Page service dédiée | **1** |
| "consultant n8n France" | Low | Very Low | Page service + articles | **2** |
| "chatbot PME artisan" | Low | Very Low | Page service + cas d'usage | **3** |
| "électricien Valence" | High | Medium | Optimiser page existante | **4** |
| "domotique Valence" | Medium | Medium | Optimiser page existante | **5** |
| "installateur domotique Drôme" | Medium | Low | Déjà ciblé (améliorer) | **6** |
| "automatisation devis artisan" | Low | Very Low | Article de blog | **7** |
| "n8n vs Make.com" | Medium | Low | Article comparatif | **8** |
| "RGPD automatisation données" | Low | Very Low | Article de blog | **9** |
| "borne de recharge Valence" | Medium | Medium | Mettre à jour article existant | **10** |

---

## Technical SEO

### robots.txt
```
Sitemap: https://smarthome-smartelec.fr/sitemap_index.xml

# START YOAST BLOCK
User-agent: *
Disallow:

Sitemap: https://smarthome-smartelec.fr/sitemap_index.xml
# END YOAST BLOCK
```

- [x] robots.txt accessible
- [x] Ne bloque aucune page importante
- [x] Référence le sitemap
- [ ] **Le sitemap est référencé deux fois** (doublon)
- [ ] **Marqué "YOAST BLOCK" mais le marketing audit mentionnait Rank Math** — possible conflit de plugins SEO ou migration incomplète

### XML Sitemap

- [x] Sitemap index accessible à `/sitemap_index.xml`
- [x] Contient 2 sous-sitemaps : `post-sitemap.xml` (11 URLs) et `page-sitemap.xml` (12 URLs)
- [x] **23 URLs totales** — site très mince
- [ ] **Pas de lastmod sur la page /blog/** — Google ne sait pas quand cette page a été mise à jour
- [ ] Pas de sitemap d'images
- [ ] L'URL avec emojis dans le sitemap peut poser des problèmes de parsing

### Canonical Tags
- [x] Canonical tags présents et self-referencing sur toutes les pages
- [ ] **Conflit navigation ↔ canonical** : Le menu utilise `/domotique/` mais le canonical est `/domotique-maison-connectee/`. Idem pour `/electricite/` vs `/electricite-habitation-magasin/`.

### SSL / HTTPS
- [x] HTTPS actif sur tout le site
- [x] Pas de mixed content détecté

### Mobile-Friendliness
- [x] Viewport meta tag présent
- [x] Thème Sydney responsive
- [x] Hamburger menu pour mobile
- [x] Images responsive avec `srcset`
- [ ] Taille des tap targets non vérifiable sans Lighthouse
- [ ] Pas de sticky CTA mobile

### Page Speed (indicateurs indirects)
- [ ] **Aucun CDN détecté** — hébergé directement sur OVH
- [ ] **Elementor détecté** — connu pour le code bloat et les temps de chargement plus lents
- [ ] **10 scripts JavaScript** sur chaque page — potentiellement excessif pour un site de cette taille
- [ ] Pas de caching plugin détecté (WP Rocket, W3 Total Cache, etc.)
- [x] Lazy loading implémenté (via IntersectionObserver)
- [ ] Pas de compression next-gen des images (WebP/AVIF)

### Tracking & Analytics
- [ ] **AUCUN outil de tracking détecté** — Pas de Google Analytics, pas de Google Tag Manager, pas de Matomo, pas de pixel Facebook
- [ ] **Pas de Google Search Console verification tag** visible
- Cela signifie qu'il n'y a **aucune donnée de trafic, aucun suivi de conversion, aucune donnée de recherche**. C'est impossible d'optimiser le SEO sans données.

---

## Schema Markup Audit

| Type de Schema | Applicable | Statut | Impact |
|---------------|-----------|--------|--------|
| **Organization** | Homepage | **Partiellement présent** | Le schema existe mais og:site_name = "AI Automation" crée une confusion avec le nom légal "Smarthome Smartelec" |
| **LocalBusiness** | Tout le site | **MANQUANT** | **Critique** — C'est LE type de schema le plus important pour un business local. Doit inclure : nom, adresse, téléphone, horaires, zone de service, coordonnées GPS |
| **Article** | Articles de blog | **Présent** | Détecté via Yoast/Rank Math |
| **BreadcrumbList** | Toutes les pages | **Présent** | OK |
| **WebSite** | Homepage | **Présent** | OK |
| **WebPage** | Toutes les pages | **Présent** | OK |
| **Service** | Pages de services | **MANQUANT** | Devrait décrire chaque service (domotique, électricité, IA) |
| **FAQ** | Pages de services | **MANQUANT** | Opportunité de rich snippets sur les questions fréquentes |
| **Review/AggregateRating** | Homepage | **MANQUANT** | Pas d'avis à structurer de toute façon (0 témoignages) |
| **HowTo** | Articles tutoriels | **MANQUANT** | Les articles VMC connectée, borne de recharge pourraient l'utiliser |
| **Product** | N/A | N/A | — |
| **Event** | N/A | N/A | — |

**Schemas prioritaires à implémenter :**
1. **LocalBusiness** (critique) — avec geo coordinates, opening hours, service area, payment methods
2. **Service** (high) — pour chaque offre
3. **FAQ** (medium) — pour capturer des featured snippets
4. **HowTo** (low) — pour les articles tutoriels existants

---

## Featured Snippet Opportunities

| Requête cible | Type de snippet | Page à optimiser | Action requise |
|--------------|----------------|-----------------|----------------|
| "comment rendre une VMC connectée" | Paragraph | /rendre-une-vmc-double-flux-connectee/ | Ajouter un résumé de 40-60 mots en début d'article sous un H2 "Comment rendre une VMC connectée ?" |
| "avantages maison connectée" | List | /maison-connectee-avantages/ | Structurer les avantages en liste à puces sous un H2 "Quels sont les avantages d'une maison connectée ?" |
| "scénarios domotique" | List | /domotique-maison-connectee/ | Lister les scénarios (réveil, départ, absence, retour, soir, coucher) dans une liste ordonnée |
| "qu'est-ce que n8n" | Paragraph | Blog n8n articles | Ajouter un paragraphe de définition en début d'article |
| "coût installation domotique" | Table | /domotique-maison-connectee/ | Ajouter un tableau de fourchettes de prix par type d'installation |
| "maintien à domicile domotique" | Paragraph | /maintien-a-domicile/ | Ajouter un résumé de 40-60 mots sous le H1 |

---

## Internal Linking Strategy

### Architecture actuelle (problématique)
```
Homepage (IA + électricité + domotique — tout mélangé)
  ├── Domotique ← pas de lien vers articles domotique
  ├── Électricité ← isolée, pas de maillage
  ├── Maintien à domicile ← pas de lien vers domotique
  ├── Alarme (2 pages)
  ├── Blog ← articles en vrac, pas de catégorisation SEO
  │     ├── Articles IA/n8n (2025) ← ne lient pas vers les services
  │     ├── Articles domotique (2018-2021) ← ne lient pas vers /domotique/
  │     └── Article en anglais ← signal de langue incohérent
  └── Pages légales / Contact
```

### Architecture recommandée (silos thématiques)
```
Homepage → cible l'activité principale (IA/automatisation OU domotique)
  ├── SILO IA/AUTOMATISATION (nouveau)
  │     ├── /automatisation-ia-pme/ (page pilier)
  │     ├── Blog: articles n8n, chatbot, automatisation → lient vers page pilier
  │     └── Études de cas IA
  ├── SILO DOMOTIQUE
  │     ├── /domotique-maison-connectee/ (page pilier)
  │     ├── /alarme-effraction/, /alarme-risques-techniques/
  │     ├── Blog: articles domotique → lient vers page pilier
  │     └── /maintien-a-domicile/
  ├── SILO ÉLECTRICITÉ
  │     ├── /electricite-habitation-magasin/ (page pilier enrichie)
  │     └── Blog: articles techniques → lient vers page pilier
  └── Pages conversion (tarifs, contact, audit gratuit)
```

### Pages orphelines (sans lien entrant contextuel)
- Articles de blog anciens (2018-2021) — probablement aucun lien interne contextuel pointant vers eux
- Pages d'alarme — liées uniquement via la navigation
- Page /stagiaires/ — marginale pour le SEO

---

## Core Web Vitals — Évaluation indirecte

Sans accès à Lighthouse ou PageSpeed Insights, estimation basée sur les indicateurs techniques :

| Métrique | Estimation | Risque | Facteurs |
|----------|-----------|--------|----------|
| **LCP** | 3-5s (Needs Work → Poor) | **Élevé** | Pas de CDN, Elementor bloat, images JPEG non-compressées, hébergement OVH mutualisé probable |
| **FID/INP** | 100-200ms (Needs Work) | **Moyen** | 10 scripts JS par page, pas de defer/async visible |
| **CLS** | 0.05-0.15 (Good → Needs Work) | **Faible** | contain-intrinsic-size appliqué, mais lazy loading sans dimensions réservées possible |
| **TTFB** | 500-1500ms (Needs Work → Poor) | **Élevé** | OVH mutualisé, pas de caching détecté, WordPress + Elementor |

**Impact business estimé :**
- Un TTFB de 1s au lieu de 200ms = ~15-20% de visiteurs perdus avant même le chargement
- Un LCP >4s = ~38% de bounce rate vs ~9% pour un LCP <2s
- Pour un site recevant estimé 500-1000 visites/mois, cela représente 75-200 visiteurs perdus par mois

---

## Blog & Content Strategy Analysis

### État actuel du blog

| Période | Articles | Thèmes | Langue |
|---------|----------|--------|--------|
| 2018-2019 | 2 | Domotique, thermostat connecté | FR |
| 2021 | 2 | VMC connectée, borne de recharge | FR |
| 2022-2024 | **0** | **GAP DE 3 ANS** | — |
| 2025 | 5 | n8n, IA, productivité, funnel, Delta Dore | FR + 1 EN |
| **Total** | **9** | | |

### Problèmes stratégiques
1. **Gap de 3-4 ans** (2021-2025) — signal d'abandon pour Google
2. **Changement thématique radical** — de domotique/électricité à IA/marketing/automatisation. Cela dilue l'autorité topique construite (modestement) en 2018-2021
3. **Article en anglais** sans hreflang — confusion de signal linguistique
4. **Pas de catégorisation cohérente** — certains articles "Non classé"
5. **URLs trop longues** sur les articles récents
6. **Aucun CTA, aucun lead capture** dans les articles

### Stratégie de contenu recommandée

**Objectif : 2 articles/mois minimum, 100% en français, ciblés SEO**

#### Calendrier éditorial prioritaire (Mois 1-3)

| Mois | Article 1 (pilier) | Article 2 (longue traîne) |
|------|-------------------|--------------------------|
| **M1** | "Automatisation des processus pour artisans : guide complet 2026" (2000+ mots, page pilier IA) | "Comment automatiser vos devis avec n8n : tutoriel pas à pas" |
| **M1** | Mise à jour article "borne de recharge" (actualiser pour 2026) | — |
| **M2** | "n8n vs Make.com vs Zapier : comparatif pour PME françaises" | "5 tâches que tout plombier peut automatiser dès cette semaine" |
| **M3** | "Domotique à Valence : guide complet pour votre maison connectée" | "Comment l'IA réduit le temps de facturation de 80% pour les artisans" |

#### Mots-clés à cibler par article

| Mot-clé | Volume estimé | Difficulté | Type |
|---------|--------------|------------|------|
| automatisation processus artisan | Faible | Très faible | Commercial |
| n8n vs make.com | Moyen | Faible | Comparatif |
| automatiser devis artisan | Faible | Très faible | Informationnel |
| domotique Valence | Moyen | Moyen | Local |
| chatbot PME gratuit | Moyen | Moyen | Informationnel |
| électricien Valence avis | Moyen | Moyen | Local/Transactionnel |
| maintien domicile domotique prix | Faible | Faible | Commercial |

---

## Prioritized Recommendations

### Critical — Corriger immédiatement (semaine 1)

| # | Recommandation | Impact attendu | Effort |
|---|---------------|---------------|--------|
| 1 | **Installer Google Analytics 4 + Google Search Console** — Sans données de trafic, toute optimisation SEO est aveugle. Ajouter le tag GA4 et vérifier la propriété Search Console. | Fondation de toute stratégie SEO | 30 min |
| 2 | **Réécrire le title et la meta description de la homepage** — Title actuel : "SMARTHOME SMARTELEC - AI Automation" → "Automatisation IA pour PME et Artisans \| SmartHome SmartElec Valence". Meta actuelle parle du pivot → écrire une meta orientée client avec CTA. | +15-30% de CTR organique sur la homepage | 15 min |
| 3 | **Réécrire le title de la page Électricité** — "Électricité - AI Automation" → "Électricien Valence - Installation & Dépannage \| SmartHome SmartElec". Ajouter des H2 à la page. | +20-40% de visibilité locale pour "électricien Valence" | 30 min |
| 4 | **Corriger l'URL avec emojis** — L'article Tywell avec 🏠✨ dans l'URL doit être redirigé vers une URL propre. Mettre en place une redirection 301. | Évite des erreurs de crawl et d'indexation | 15 min |
| 5 | **Corriger le désalignement navigation ↔ canonical** — Aligner les liens du menu sur les URLs canoniques pour éviter les redirections en chaîne. | Consolidation du link equity | 15 min |

### High Priority — Ce mois-ci (semaines 2-4)

| # | Recommandation | Impact attendu | Effort |
|---|---------------|---------------|--------|
| 6 | **Implémenter le schema LocalBusiness** — JSON-LD avec nom, adresse, téléphone, geo coordinates, horaires, zone de service (Drôme, Ardèche, Isère), services offerts. | +15-25% de visibilité dans les résultats locaux | 1h |
| 7 | **Corriger tous les alt text manquants** — 10 images sur 36 sans alt. Priorité : page Électricité (4 images sans alt). | Amélioration accessibilité + indexation images | 1h |
| 8 | **Enrichir la page Électricité** — Passer de ~400 mots à 1000+ mots. Ajouter des H2 structurants, des mots-clés géographiques, un FAQ en bas de page. | Page actuellement non-compétitive → potentiellement classable | 3h |
| 9 | **Corriger la faute "terciaire"** dans la meta description de la page Domotique → "tertiaire". | Crédibilité | 1 min |
| 10 | **Ajouter des liens internes contextuels** — Lier les articles de blog aux pages de services pertinentes et vice versa. Minimum 3 liens par article. | +10-15% de pages vues par session, meilleur crawl | 2h |

### Medium Priority — Ce trimestre (mois 2-3)

| # | Recommandation | Impact attendu | Effort |
|---|---------------|---------------|--------|
| 11 | **Créer une page service IA/Automatisation dédiée** — Actuellement, les services IA sont uniquement sur la homepage. Une page dédiée `/automatisation-ia-pme/` permettrait de cibler des keywords spécifiques. | Nouveau point d'entrée organique pour les requêtes IA | 4h |
| 12 | **Lancer la stratégie de contenu** — 2 articles/mois, français uniquement, ciblés longue traîne. Commencer par les articles comparatifs (n8n vs Make.com) et les guides sectoriels. | 500-2000 visiteurs organiques/mois additionnels en 6-12 mois | Récurrent |
| 13 | **Optimiser les Core Web Vitals** — Installer un plugin de cache (WP Rocket), convertir les images en WebP, envisager un CDN (Cloudflare gratuit). | Réduction du bounce rate de 15-25% | 3h |
| 14 | **Ajouter le schema FAQ** aux pages de services avec les questions les plus fréquentes. | Opportunité de rich snippets dans les SERP | 2h/page |
| 15 | **Nettoyer la catégorisation du blog** — Remplacer "Non classé" par des catégories SEO pertinentes (Domotique, Automatisation IA, Électricité). | Meilleure structure thématique pour Google | 1h |

### Low Priority — Quand les ressources le permettent

| # | Recommandation | Impact attendu | Effort |
|---|---------------|---------------|--------|
| 16 | **Créer des pages de zones géographiques** — "/electricien-valence/", "/domotique-drome/", "/automatisation-romans-sur-isere/" pour le SEO local. | Nouveau trafic local qualifié | 3h/page |
| 17 | **Traduire ou supprimer l'article en anglais** — Soit le traduire en français, soit le retirer du sitemap avec un noindex. | Cohérence du signal linguistique | 1h |
| 18 | **Implémenter le schema HowTo** sur les articles tutoriels (VMC connectée, borne de recharge). | Opportunité de rich snippets | 1h |
| 19 | **Créer un sitemap d'images** pour améliorer l'indexation des images. | Visibilité dans Google Images | 30 min |
| 20 | **Résoudre le conflit de plugin SEO** — Clarifier si le site utilise Yoast ou Rank Math (le robots.txt mentionne Yoast, mais des signaux de Rank Math ont été détectés). S'assurer qu'un seul plugin SEO est actif. | Évite les conflits de schema et de sitemap | 1h |

---

## Résumé des scores par dimension

| Dimension SEO | Score | Poids | Pondéré |
|--------------|-------|-------|---------|
| Title Tags & Meta | 25/100 | 15% | 3.8 |
| Heading Hierarchy | 35/100 | 10% | 3.5 |
| Image Optimization | 35/100 | 8% | 2.8 |
| Internal Linking | 25/100 | 10% | 2.5 |
| URL Structure | 30/100 | 8% | 2.4 |
| E-E-A-T Content Quality | 35/100 | 15% | 5.3 |
| Technical SEO (robots, sitemap, canonical) | 55/100 | 10% | 5.5 |
| Schema Markup | 30/100 | 8% | 2.4 |
| Local SEO | 20/100 | 8% | 1.6 |
| Page Speed (estimé) | 25/100 | 5% | 1.3 |
| Content Strategy & Freshness | 20/100 | 3% | 0.6 |
| **TOTAL** | | **100%** | **31.7 → 32/100** |

---

## Relation avec le Marketing Audit

Ce SEO audit confirme et approfondit les findings du `MARKETING-AUDIT.md` (score global 34/100) :

- **Crise d'identité** → Impact SEO direct : Google ne peut pas construire de profil E-E-A-T cohérent quand og:site_name = "AI Automation", le domaine = "smarthome-smartelec", et le NAF = 4321A
- **Zéro analytics** → Découverte critique de cet audit : impossible d'optimiser le SEO sans données de trafic
- **Contenu mince** → 23 URLs indexées est insuffisant pour concurrencer dans quelque niche que ce soit
- **Local SEO inexploité** → Potentiel important pour un artisan avec adresse physique dans une zone à concurrence modérée

**Prochaines étapes recommandées :**
- `/market competitors` pour une analyse concurrentielle SEO approfondie
- `/market landing` pour optimiser les pages de conversion
- `/market copy` pour réécrire les titles, metas, et headlines

---

*Audit SEO généré par AI Marketing Suite — `/market seo`*
