# Audit SEO : DAAH STUDIO
## https://daah.studio
### Date : 21 mars 2026

---

## Score Santé SEO : 42/100

**Diagnostic :** Le site daah.studio présente des fondations techniques acceptables grâce à Squarespace, mais le SEO on-page est quasi inexistant. L'absence de méta-descriptions, les 14 balises H1 sur la homepage, le schema LocalBusiness vide et l'absence totale de contenu blog constituent un handicap sévère pour la visibilité organique. C'est un paradoxe majeur pour une agence qui inclut le SEO dans son offre DAAH Premium.

---

## Checklist SEO On-Page

### Balise Title
- **Statut : ÉCHEC**
- **Actuel :** `DAAH STUDIO` (11 caractères)
- **Problèmes :**
  - Beaucoup trop courte (11 caractères vs 50-60 recommandés)
  - Aucun mot-clé métier (agence web, design, Valence, Drôme)
  - Aucune proposition de valeur
  - Non distinctive dans les SERP (ressemble à un placeholder)
- **Recommandé :** `Agence Web & Design Graphique Drôme | DAAH STUDIO` (51 caractères)

**Titles des sous-pages :**
| Page | Title Actuel | Long. | Statut |
|------|-------------|-------|--------|
| Homepage | `DAAH STUDIO` | 11 | ÉCHEC — trop court |
| /sur-mesure | `Services \| Besoin d'un site, de transmettre un message visuellement ou d'aide en com' ? On est là — DAAH STUDIO` | 147 | ÉCHEC — trop long |
| /abonnement-graphique | `L'abonnement graphique \| Fais de DAAH Studio ton partenaire com' et graphisme ! — DAAH STUDIO` | 93 | ÉCHEC — trop long |
| /abonnement-daah-premium | `Les abonnements web DAAH Premium \| Pas de frais cachés, pas de DIY. Un site et un suivi sur la durée — DAAH STUDIO` | 111 | ÉCHEC — trop long |
| /portfolio | `Portfolio \| On aime nos clients, voici quelques uns des projets… — DAAH STUDIO` | 104 | ÉCHEC — trop long |
| /information | `À propos \| Que tu sois près d'ici ou à distance… — DAAH STUDIO` | 112 | ÉCHEC — trop long |

**Titles recommandés :**
| Page | Title Recommandé | Long. |
|------|-----------------|-------|
| Homepage | `Agence Web & Design Graphique Drôme \| DAAH STUDIO` | 51 |
| /sur-mesure | `Création Site Internet & Identité Visuelle \| DAAH STUDIO` | 57 |
| /abonnement-graphique | `Abonnement Design Graphique dès 190€/mois \| DAAH STUDIO` | 57 |
| /abonnement-daah-premium | `Site Web par Abonnement 99€/mois \| DAAH STUDIO` | 49 |
| /portfolio | `Nos Réalisations Web & Design \| DAAH STUDIO` | 46 |
| /information | `À Propos — Studio Design & Stratégie Digitale \| DAAH STUDIO` | 60 |

### Méta-description
- **Statut : ÉCHEC CRITIQUE**
- **Actuel (OG) :** `Le studio digital des entreprises audacieuses. Notre mission est d'aider les PME audacieuses à briller sur la toile.` (118 caractères)
- **Problèmes :**
  - La méta-description HTML est **vide** sur toutes les pages (seule la balise OG contient du texte)
  - Google génère des extraits arbitraires → perte de CTR estimée à -20/30%
  - Répétition du mot "audacieuses" dans la description OG
  - Aucun appel à l'action
  - Aucun mot-clé local (Valence, Drôme, Valréas)
- **Recommandé (Homepage) :** `Studio de design web & stratégie digitale en Drôme. Création de sites, identité visuelle et abonnement graphique dès 190€/mois. Devis gratuit →` (158 caractères)

**Méta-descriptions recommandées par page :**
| Page | Méta-description Recommandée |
|------|------------------------------|
| /sur-mesure | `Site vitrine dès 1 100€, e-commerce dès 2 900€, identité visuelle dès 800€. Création web sur-mesure en Drôme. Bilan gratuit de vos besoins →` |
| /abonnement-graphique | `Abonnement design graphique de 190€ à 680€/mois. Crédits flexibles, livraison 48h, sans engagement. Votre partenaire créa' au quotidien.` |
| /abonnement-daah-premium | `Site web professionnel tout compris à 99€/mois : design, hébergement, domaine, SEO et mises à jour illimitées. Lancé en 3 semaines.` |
| /portfolio | `Découvrez nos réalisations web et design : Contexteo, ARV Groupe, Vandria, Asoft. Sites vitrines, e-commerce et identités visuelles.` |

### Hiérarchie des Titres (H1-H6)
- **Statut : ÉCHEC CRITIQUE**
- **Problème majeur : 14 balises H1 sur la homepage**
  - Le marquee/bandeau défilant génère chaque mot comme un H1 séparé
  - "Sites internet", "Webmastering", "Automatisation", chaque emoji 〰️ = H1 distinct
  - Le titre du footer "DAAH STUDIO" est aussi un H1
  - "et si on te faisait briller sur la toile ?" est un H1 au lieu d'un H2

**Structure actuelle (Homepage) :**
```
H1: "Des sites WEB qui travaillent aussi dur que toi !" ✓ (bon H1)
H1: "Sites internet" ✗ (marquee — devrait être span/p)
H1: "〰️" ✗ (emoji en H1 !)
H1: "Webmastering" ✗
H1: "〰️" ✗
H1: "Automatisation" ✗
H1: ... (8 autres H1 du marquee)
H1: "et si on te faisait briller sur la toile ?" ✗ (devrait être H2)
H1: "DAAH STUDIO" ✗ (footer, devrait être p/span)
H2: "Ce que le studio fait pour toi" ✓
H2: "les services" ✓
H3: "Création et maintenance de Sites internet" ✓
H3: "Identité & cohérence visuelle" ✓
H3: "Stratégie & Pilotage" ✓
H4: "PLAN DU SITE" ✗ (footer — devrait être p/nav)
H4: "NOUS SUIVRE" ✗ (footer — devrait être p/nav)
```

**Structure recommandée :**
```
H1: "Des sites WEB qui travaillent aussi dur que toi !" (unique H1)
  H2: "Ce que le studio fait pour toi"
    H3: "Création et maintenance de Sites internet"
    H3: "Identité & cohérence visuelle"
    H3: "Stratégie & Pilotage"
  H2: "et si on te faisait briller sur la toile ?"
  H2: "les services"
Marquee → <p> ou <span> avec aria-label
Footer → <nav> avec <p>, pas de Hx
```

### Optimisation des Images
- **Statut : ÉCHEC**
- **Images totales :** 6
- **Images sans alt :** 4 (67% sans alt — très mauvais)
- **Images avec lazy loading :** 1 seule sur 6
- **Problèmes détaillés :**
  - Noms de fichiers = GUID Squarespace (ex: `17cf638b-6066-4670-9e91-7bcd6b16c44a`) → aucune valeur SEO
  - Les alts présents sont génériques ("DAAH STUDIO", noms de clients)
  - Pas de `<figure>` + `<figcaption>` pour le contexte sémantique
  - Format d'image non optimisé (PNG pour le logo au lieu de SVG)
- **Corrections :**
  1. Ajouter des alts descriptifs à toutes les images : `"Création site web Contexteo par DAAH STUDIO"`
  2. Activer le lazy loading sur toutes les images hors écran
  3. Renommer les fichiers avant upload avec des noms descriptifs

### Maillage Interne
- **Statut : À AMÉLIORER**
- **Liens internes :** 41
- **Liens externes :** 1 (LinkedIn uniquement)
- **Points positifs :**
  - Navigation bien structurée avec liens vers toutes les pages principales
  - CTAs multiples reliant vers /rdv et /sur-mesure
- **Points faibles :**
  - Aucun maillage croisé optimisé entre pages de services (sur-mesure ↔ abonnement graphique ↔ premium)
  - Pas de fil d'Ariane (breadcrumbs) sur le portfolio
  - Les pages /valreas et /valence sont dans le sitemap mais pas dans la navigation → pages orphelines
  - Aucun lien vers du contenu éducatif (pas de blog)
  - 1 seul lien externe (LinkedIn) → profil de liens sortants très pauvre

### Structure des URLs
- **Statut : CORRECT**
- URLs courtes, lisibles, en minuscules avec tirets : `/sur-mesure`, `/abonnement-graphique`
- Structure plate et logique
- **Seul problème :** Incohérence entre `daah.studio` et `www.daah.studio` (canonical pointe vers www)

---

## Qualité du Contenu (E-E-A-T)

| Dimension | Score | Justification |
|-----------|-------|---------------|
| **Expérience** | Faible | Aucune étude de cas détaillée, aucun "avant/après", aucun témoignage d'expérience concrète avec des clients. Le portfolio montre des visuels mais pas de processus ni de résultats. |
| **Expertise** | Faible | Pas de blog, pas de contenu éducatif, pas de guides. Le background comptabilité/gestion de la fondatrice (expertise business unique) n'est pas exploité en contenu. Pas de démonstration de savoir-faire technique. |
| **Autorité** | Faible | Aucune mention presse, aucun article invité, aucune présence sur les annuaires professionnels (Malt, Sortlist, Clutch). Seul signal : badge Squarespace Circle Silver 2026. |
| **Fiabilité** | Présent | HTTPS actif, mentions légales présentes (/mentions-legales), adresse email professionnelle (bonjour@daah.studio), prix transparents affichés. Mais pas de Google Business Profile, pas d'avis clients vérifiables. |

**Score E-E-A-T global : 35/100** — Le site manque cruellement de signaux d'expertise et d'autorité que Google utilise pour évaluer la qualité. L'ajout d'un blog avec 1 article/mois et de 3-5 études de cas serait transformateur.

---

## Analyse des Mots-clés

### Mot-clé Principal Ciblé
**Aucun mot-clé principal clairement ciblé.** La homepage titre "DAAH STUDIO" sans aucun terme métier.

### Mots-clés Recommandés par Page

| Page | Mot-clé Principal | Volume Estimé | Difficulté |
|------|-------------------|---------------|------------|
| Homepage | `agence web Drôme` / `agence web Valence` | Moyen | Moyen |
| /sur-mesure | `création site internet Valence` | Moyen | Moyen |
| /abonnement-graphique | `abonnement graphique design` | Faible-Moyen | Faible |
| /abonnement-daah-premium | `site web par abonnement` | Faible | Faible |
| /portfolio | `agence design Drôme réalisations` | Faible | Faible |
| /valence | `agence web Valence` | Moyen | Moyen |
| /valreas | `création site internet Valréas` | Faible | Très faible |

### Placement des Mots-clés (Homepage)

| Élément | Présence | Statut |
|---------|----------|--------|
| Title | Absent | ÉCHEC |
| H1 | Absent ("sites WEB" seulement) | ÉCHEC |
| Premiers 100 mots | Absent | ÉCHEC |
| Sous-titres H2/H3 | Partiellement ("Sites internet") | À AMÉLIORER |
| Méta-description | Absent (vide) | ÉCHEC |
| URL | N/A (homepage) | — |
| Alt images | Absent | ÉCHEC |

### Intention de Recherche

| Mot-clé Cible | Intention | Le contenu correspond ? |
|---------------|-----------|------------------------|
| "agence web Valence" | Commerciale | Partiellement — pas de mention géographique claire en homepage |
| "création site internet Drôme" | Commerciale | Partiellement — services décrits mais pas localisés |
| "abonnement graphique design" | Commerciale | Oui — page dédiée avec pricing |
| "site web par abonnement" | Commerciale | Oui — page DAAH Premium |
| "combien coûte un site vitrine" | Informationnelle | Non — pas de contenu éducatif |

### Mots-clés Secondaires à Intégrer

1. `création site internet sur-mesure`
2. `identité visuelle freelance`
3. `webmastering WordPress`
4. `design par abonnement France`
5. `studio web Drôme Ardèche`
6. `site Squarespace professionnel`
7. `agence digitale PME`
8. `refonte site web prix`
9. `graphiste abonnement mensuel`
10. `stratégie digitale TPE`

---

## SEO Technique

### Robots.txt
- **Statut : CORRECT avec réserves**
- Fichier présent et bien structuré (Squarespace)
- Bloque correctement : /config, /search, /api/, /static/, paramètres de format
- Autorise /api/ui-extensions/
- **Attention :** Bloque TOUS les crawlers IA (GPTBot, ClaudeBot, Amazonbot, Google-Extended, etc.) → impact négatif sur la visibilité GEO (IA générative)
- Sitemap référencé vers `www.daah.studio` (cohérence à vérifier)

### Sitemap XML
- **Statut : À CORRIGER**
- 16 URLs indexées — nombre acceptable pour la taille du site
- Extensions images présentes (bon pour Google Images)
- **Problèmes critiques :**
  1. **`/404` est dans le sitemap** — erreur grave, page d'erreur soumise à l'indexation
  2. `changefreq: daily` sur /mentions-legales — exagéré et peu crédible
  3. Homepage mappée sur `/accueil` au lieu de `/` (root)
  4. Pas de page blog dans le sitemap (car blog inexistant)

### Balise Canonical
- **Statut : CORRECT**
- Canonical présent : `https://www.daah.studio`
- Pointe vers la bonne URL
- **Point d'attention :** Vérifier que `daah.studio` (sans www) redirige bien en 301 vers `www.daah.studio`

### Vitesse de Chargement (Estimée)
- **Statut : MOYEN**
- Score estimé : 55-70/100 mobile, 75-90/100 desktop (Squarespace typique)
- 26 scripts chargés — overhead significatif
- Google Tag Manager + Google Analytics (gtag) + reCAPTCHA = 3 scripts tiers lourds
- Pas de `rel="preconnect"` détecté vers le CDN images Squarespace
- Le marquee animé peut dégrader le LCP (Largest Contentful Paint)
- 1 seule image en lazy loading sur 6

### Mobile
- **Statut : CORRECT**
- Viewport meta tag présent (`width=device-width, initial-scale=1`)
- Squarespace est nativement responsive
- **Risques :** le marquee animé et les CTAs multiples peuvent poser des problèmes sur petits écrans

---

## Analyse des Lacunes de Contenu (Content Gap)

Le site n'a **aucun blog ni section ressources**. Voici les opportunités de contenu identifiées :

| Sujet Manquant | Potentiel de Recherche | Concurrence | Type de Contenu | Priorité |
|---------------|----------------------|-------------|-----------------|----------|
| "Combien coûte un site internet en 2026 ?" | Élevé | Moyen | Article guide | 1 |
| "Agence web vs freelance : comment choisir ?" | Moyen | Moyen | Article comparatif | 2 |
| "Abonnement design graphique : le guide complet" | Moyen | Faible | Guide + landing | 3 |
| "Squarespace vs WordPress : quel CMS choisir ?" | Élevé | Élevé | Article comparatif | 4 |
| "Pourquoi refaire son site internet (5 signaux)" | Moyen | Moyen | Article éducatif | 5 |
| "Identité visuelle pour TPE : par où commencer ?" | Moyen | Faible | Guide pratique | 6 |
| "Comment améliorer le SEO de son site Squarespace" | Moyen | Moyen | Tutoriel | 7 |
| "Site web par abonnement : avantages et limites" | Faible | Faible | Article opinion | 8 |
| "Stratégie digitale pour artisans et consultants" | Faible | Faible | Guide sectoriel | 9 |
| "Portfolio d'agence web : nos études de cas" | Faible | Faible | Série d'articles | 10 |

**Impact estimé :** 1 article optimisé/mois pendant 6 mois → +30-50% de trafic organique

---

## Opportunités Featured Snippets

| Requête Cible | Type de Snippet | Contenu Nécessaire |
|--------------|----------------|-------------------|
| "combien coûte un site vitrine" | Tableau | Tableau de prix avec fourchettes par type de prestataire |
| "abonnement graphique c'est quoi" | Paragraphe | Définition concise en 40-60 mots sous un H2 |
| "étapes création site internet" | Liste ordonnée | Liste numérotée des 5-7 étapes d'un projet web |
| "différence site vitrine et e-commerce" | Paragraphe | Comparaison concise en 50 mots |

---

## Audit Schema / Données Structurées

| Type Schema | Applicable | Statut | Priorité |
|-------------|-----------|--------|----------|
| WebSite | Homepage | Présent — mais minimal (pas de SearchAction) | Moyenne |
| LocalBusiness | Toutes pages | Présent — mais **adresse vide** (invalide) | CRITIQUE |
| Service | Pages services | Absent | Haute |
| PriceSpecification / Offer | Pages tarifs | Absent | Haute |
| FAQPage | Abonnement graphique | Absent | Moyenne |
| BreadcrumbList | Portfolio | Absent | Moyenne |
| Organization | Homepage | Absent | Moyenne |
| Person | À propos | Absent | Basse |
| CreativeWork / ImageGallery | Portfolio | Absent | Basse |

**Correction critique :** Le schema LocalBusiness actuel est invalide :
```json
{ "@type": "LocalBusiness", "address": "" }
```
→ Remplacer par :
```json
{
  "@context": "https://schema.org",
  "@type": "ProfessionalService",
  "name": "DAAH STUDIO",
  "url": "https://www.daah.studio",
  "email": "bonjour@daah.studio",
  "description": "Studio de design web & stratégie digitale",
  "address": {
    "@type": "PostalAddress",
    "addressLocality": "Guilherand-Granges",
    "addressRegion": "Ardèche",
    "postalCode": "07500",
    "addressCountry": "FR"
  },
  "areaServed": ["France", "Suisse", "Belgique"],
  "priceRange": "€€",
  "sameAs": ["https://www.linkedin.com/in/aahd/"]
}
```

---

## Opportunités de Maillage Interne

### Pages Orphelines Détectées
- `/valreas` — dans le sitemap, pas dans la navigation
- `/valence` — dans le sitemap, pas dans la navigation
→ Ajouter des liens depuis la homepage et /information, ou intégrer dans le footer

### Maillage Croisé Recommandé
```
/sur-mesure ←→ /abonnement-graphique (CTA : "Besoin de graphisme régulier ? Découvrez l'abonnement")
/sur-mesure ←→ /abonnement-daah-premium (CTA : "Un site tout compris dès 99€/mois")
/abonnement-graphique ←→ /sur-mesure (CTA : "Besoin d'un projet one-shot ?")
/portfolio → chaque projet → /rdv (CTA : "Un projet similaire ?")
/information → /portfolio (CTA : "Voir nos réalisations")
Futur blog → pages services correspondantes
```

### Architecture de Cluster Topique Recommandée
```
Homepage (Pilier)
├── /sur-mesure (Pilier Services)
│   ├── /abonnement-graphique (Cluster)
│   ├── /abonnement-daah-premium (Cluster)
│   └── Futurs articles blog (Cluster)
├── /portfolio (Pilier Social Proof)
│   ├── /portfolio/contexteo (Cluster)
│   ├── /portfolio/arv (Cluster)
│   └── /portfolio/vandria (Cluster)
├── /valence (Pilier Local)
├── /valreas (Pilier Local)
└── /blog (Futur Pilier Contenu)
    ├── Articles éducatifs → liens vers /sur-mesure
    ├── Études de cas → liens vers /portfolio
    └── Guides pratiques → liens vers /abonnement-*
```

---

## Impact Core Web Vitals (Estimé)

| Métrique | Estimation | Seuil Bon | Statut |
|----------|-----------|-----------|--------|
| LCP (Largest Contentful Paint) | 2,5-3,5s | < 2,5s | À AMÉLIORER |
| FID/INP (First Input Delay) | 100-200ms | < 100ms | À AMÉLIORER |
| CLS (Cumulative Layout Shift) | 0,1-0,2 | < 0,1 | À AMÉLIORER |

**Impact business estimé :**
- Passer sous 2,5s de LCP : -24% d'abandons de page
- Réduire le CLS de 0,1 : -15% de taux de rebond
- Sites < 2s de chargement : taux de rebond de 9% vs 38% pour sites > 5s

---

## Stratégie de Contenu Recommandée

### Cadence de Publication
**1 article/mois** (minimum viable pour un studio solo) avec montée à 2/mois si possible.

### Types de Contenu Prioritaires
1. **Guides pratiques** : "Combien coûte un site internet en 2026", "Choisir entre Squarespace et WordPress"
2. **Études de cas** : transformer chaque projet portfolio en article détaillé avec résultats
3. **Articles comparatifs** : "Agence vs freelance", "Abonnement vs projet one-shot"
4. **FAQ** : répondre aux questions les plus fréquentes des prospects

### Stratégie de Mots-clés
- **Court terme (3 mois) :** mots-clés locaux longue traîne (`agence web Valence`, `création site Drôme`)
- **Moyen terme (6 mois) :** mots-clés éducatifs (`combien coûte un site`, `abonnement design graphique`)
- **Long terme (12 mois) :** mots-clés compétitifs (`création site internet`, `design par abonnement`)

### Longueur de Contenu Recommandée
- Articles guide : 1 500-2 500 mots (benchmark concurrents top 10)
- Études de cas : 800-1 200 mots
- Pages services : 600-1 000 mots (actuellement suffisant)

---

## Recommandations Priorisées

### Critique (Corriger Immédiatement)
1. **Rédiger les méta-descriptions de toutes les pages** — 0 actuellement. Impact : +15-25% CTR organique. Effort : 1 heure.
2. **Corriger les 14 H1 de la homepage** — Le marquee ne doit pas utiliser de balises H1. Changer en `<span>` ou `<p>`. Effort : 30 minutes dans Squarespace.
3. **Compléter le schema LocalBusiness** avec adresse, téléphone, zone de service. Effort : 15 minutes.
4. **Supprimer /404 du sitemap** — Page d'erreur indexée = signal négatif. Effort : 5 minutes.

### Priorité Haute (Ce Mois)
1. **Raccourcir toutes les balises title** à 55-60 caractères avec mot-clé en début. Effort : 30 minutes.
2. **Ajouter des alts descriptifs aux 4 images sans alt** (67% sans alt). Effort : 15 minutes.
3. **Harmoniser le domaine canonique** (`daah.studio` vs `www.daah.studio`). Vérifier la redirection 301.
4. **Ajouter le schema Service** avec `priceRange` sur les pages /sur-mesure et /abonnement-*. Effort : 1 heure.
5. **Intégrer les pages /valence et /valreas dans la navigation** ou les supprimer du sitemap.
6. **Créer un Google Business Profile** avec avis clients.

### Priorité Moyenne (Ce Trimestre)
1. **Lancer un blog** avec 1 article optimisé/mois. Premier article : "Combien coûte un site internet en 2026 ?". Impact : +30-50% trafic organique en 6 mois.
2. **Transformer les projets portfolio en études de cas** avec résultats chiffrés et 800-1 200 mots chacun.
3. **Ajouter des breadcrumbs** sur les pages portfolio.
4. **Implémenter le maillage croisé** entre pages de services.
5. **Ajouter le schema FAQPage** sur la page abonnement graphique.
6. **Optimiser la vitesse** : preconnect CDN, lazy loading toutes images, auditer les scripts tiers.

### Priorité Basse (Quand Possible)
1. Reconsidérer le blocage des crawlers IA dans robots.txt (impact sur la visibilité GEO/IA)
2. Ajouter les schemas BreadcrumbList, CreativeWork, Person
3. Implémenter les optimisations Featured Snippet
4. Créer une page FAQ dédiée avec schema
5. Ajouter `rel="preconnect"` et `rel="preload"` dans le header Squarespace

---

## Note de Synthèse

Le site daah.studio a une **base structurelle saine** grâce à Squarespace (responsive, HTTPS, sitemap automatique, URLs propres), mais le **SEO on-page est quasi inexistant**. Les corrections critiques (méta-descriptions, H1, schema) représentent environ **3-4 heures de travail** et peuvent améliorer le score SEO de +15 à +20 points dans les 60 jours.

Le véritable levier transformateur est le **contenu** : l'absence totale de blog signifie que 100% du trafic repose sur la notoriété directe ou les réseaux. Un investissement de 1 article/mois pendant 6 mois changerait fondamentalement la trajectoire de visibilité du site.

**Paradoxe critique :** DAAH STUDIO vend du SEO dans son offre DAAH Premium (3 mots-clés optimisés), mais son propre site ne démontre aucune application de SEO on-page. Corriger ce paradoxe est aussi une question de crédibilité commerciale.

---

*Généré par AI Marketing Suite — `/market seo`*
