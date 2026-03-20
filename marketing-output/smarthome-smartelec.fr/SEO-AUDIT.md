# Audit SEO Content — SMARTHOME SMARTELEC
## https://smarthome-smartelec.fr
### Date : 20 mars 2026

**Plateforme :** WordPress + Elementor + thème Sydney | **Plugin SEO :** Rank Math (anciennement Yoast)
**Hébergement :** OVH (mutualisé) | **Langue :** fr-FR

---

## SEO Health Score : 38/100

| Catégorie | Score | Statut |
|-----------|-------|--------|
| On-Page SEO | 35/100 | Critique |
| Content Quality (E-E-A-T) | 42/100 | Insuffisant |
| Keyword Strategy | 25/100 | Critique |
| Technical SEO | 45/100 | Insuffisant |
| Content Strategy | 35/100 | Critique |
| Schema & Structured Data | 55/100 | Moyen |

---

## On-Page SEO Checklist

### Title Tag
- **Statut : Needs Work**
- **Actuel :** "SMARTHOME SMARTELEC - AI Automation" (35 caractères)
- **Recommandé :** "Automatisation IA pour PME & Artisans | SMARTHOME SMARTELEC - Valence" (70 car.)
- **Problèmes :**
  - Trop court (35 car. vs 50-60 recommandés) — espace gaspillé dans les SERPs
  - Suffixe "AI Automation" en anglais sur un site fr-FR — incohérence linguistique
  - Pas de mot-clé métier (automatisation, PME, artisan)
  - Pas de géolocalisation (Valence, Drôme)
  - Le nom de marque seul ne communique pas la proposition de valeur

#### Comparaison par page

| Page | Title | Long. | Verdict |
|------|-------|-------|---------|
| Homepage | "SMARTHOME SMARTELEC - AI Automation" | 35 | **Fail** — trop court, anglais, pas de keyword |
| Domotique | "Installateur Domotique, spécialiste en Drôme, Ardèche, Isère, ..." | 65 | **Pass** — keyword + géo, bon modèle |
| Électricité | "Électricité - AI Automation" | 28 | **Fail** — générique, trop court |
| Blog | "Blog - AI Automation" | 21 | **Fail** — aucune valeur SEO |
| Alarme effraction | "Alarme effraction radio, avec transmetteur..." | 68 | **Needs Work** — descriptif mais long |

### Meta Description
- **Statut : Needs Work**
- **Actuel :** "Nous changeons de cap : exit l'électricité/domotique → focus total sur la relation client, l'automatisation et la donnée. Fondée par un ancien consultant en" (156 car.)
- **Recommandé :** "Automatisez vos devis, relances et service client grâce à l'IA. Audit gratuit 30 min. Expert n8n à Portes-lès-Valence, Drôme-Ardèche." (135 car.)
- **Problèmes :**
  - Tronquée à 156 car. (phrase incomplète "Fondée par un ancien consultant en...")
  - Ton interne ("nous changeons de cap") au lieu d'un message client
  - Pas de CTA ("audit gratuit", "devis", "contactez-nous")
  - Ne répond pas à la question du visiteur "qu'est-ce que je gagne ?"

| Page | Meta Description | Long. | Verdict |
|------|-----------------|-------|---------|
| Homepage | "Nous changeons de cap..." (tronquée) | 156 | **Needs Work** |
| Domotique | "La Domotique joue des scénarios de vie..." | 148 | **Pass** |
| Électricité | "Faites réaliser votre installation..." | ~138 | **Pass** |
| Blog | *(absente)* | 0 | **Fail** |

### Heading Hierarchy

**Homepage :**
```
H1: "SMARTHOME SMARTELEC" ← Nom seul, pas de keyword
  H2: "Assistants IA pour PME et Associations / Électricité, Domotique"
  H2: "Pourquoi SMARTHOME SMARTELEC ?"
  H2: "Les problèmes que nous résolvons"
  H2: "Ce que nous apportons"
  H2: "Méthodologie en 3 étapes"
  H2: "Exemples d'applications concrètes"
  H2: "Notre stack (sélection)"
  H2: "À propos"
    H3: "Notre héritage (historique)"
    H3: "Interventions"
    H3: "Articles récents"
    H3: "INFORMATIONS" ← Footer en H3
    H3: "CONTACT" ← Footer en H3
      H5: "Parler à un expert :" ← Saut H3→H5, pas de H4
      H5: "1) Données fiabilisées"
      H5: "2) Processus automatisés"
      H5: "3) Assistants IA (chatbots)"
```

- **Statut : Needs Work**
- **Problèmes :**
  - H1 = nom de marque sans valeur sémantique. Recommandé : "Automatisation IA et Assistants Intelligents pour PME"
  - Saut de niveau H3 → H5 (H4 absent) — hiérarchie cassée
  - Footer encodé en H3 (INFORMATIONS, CONTACT) — pollution sémantique
  - Méthodologie en H5 au lieu de H3 sous la section parent

**Page Domotique :**
```
H1: "Maison Connectée / Domotique" ← BON : descriptif et unique
  H2: "Des scénarios domotique pour plus de confort"
  H2: "Marques domotique / maison connectée"
  H2: "Gérer votre location à distance"
  ...10 H2 au total
```
- **Statut : Pass** — Structure exemplaire, modèle à reproduire

### Image Optimization
- **Statut : Fail**

| Page | Images | Sans alt | Verdict |
|------|--------|----------|---------|
| Homepage | 12 | 1 | Needs Work |
| Domotique | 12 | 3 | Fail |
| Électricité | 7 | 4 | **Fail** — 57% sans alt |

**Problèmes détaillés :**
- Aucune image en format WebP — toutes en JPEG/PNG
- Pas de `srcset` détecté pour le responsive
- Image hero sans `preload` (impacte le LCP)
- Logos partenaires (n8n, Softr, Airtable) hébergés sur CDN tiers sans contrôle cache
- Alt de l'OG image : "SMARTHOME SMARTELEC" — non descriptif
- 6/12 images en lazy loading sur la homepage (positif)

### Internal Linking
- **Statut : Needs Work**
- Homepage : 27 liens internes, 18 liens externes
- Domotique : 27 liens internes, 10 liens externes
- **Problèmes :**
  - Articles de blog sans liens croisés vers les pages services
  - Pas de page pilier ("automatisation IA pour PME") avec maillage hub
  - Liens externes vers n8n.io, softr.io, airtable.com sans `rel="nofollow"` — fuite de link juice
  - Page `/alarme-risques-techniques/` dans le sitemap mais orpheline (absente de la navigation)
  - 3 pages légales dans le sitemap — gaspillage du budget de crawl

### URL Structure
- **Statut : Needs Work**

| URL | Verdict | Problème |
|-----|---------|----------|
| `/domotique-maison-connectee/` | Pass | Clean et descriptif |
| `/electricite-habitation-magasin/` | Pass | Descriptif |
| `/alarme-effraction-intrusion/` | Pass | |
| `/%f0%9f%8f%a0%e2%9c%a8-tywell-de-delta-dore...` | **Fail** | Emojis encodés — illisible |
| `/unlocking-workflow-automation-the-power-of-n8n-for-agencies/` | Needs Work | Anglais sur site FR |
| `/conditions-generales-de-prestations-ventes-c-g-p-v/` | Needs Work | Trop long |

---

## Content Quality (E-E-A-T)

| Dimension | Score | Preuve |
|-----------|-------|--------|
| **Experience** | Présent | Fondateur avec expérience terrain (électricien certifié, installations réelles). Blog documente le pivot métier. Cas d'usage concrets mentionnés (chauffagiste, menuisier). Mais aucune étude de cas structurée. |
| **Expertise** | Présent | Stack technique maîtrisée (n8n, Airtable, Supabase). Background consultant SI/CRM chez opérateur télécom. Certifications électriques (H0V, B2V, BR, BC, IRVE). Articles blog démontrent une connaissance réelle. |
| **Authoritativeness** | Faible | Aucun avis sur Google Business ou plateformes tierces. Absent de Malt, Impli, La Fabrique du Net. Pas de mentions presse. Pas de certifications IA formelles. Projet européen Activage mentionné mais non mis en avant. |
| **Trustworthiness** | Faible | HTTPS actif (positif). Mentions légales présentes. DPO déclaré CNIL. Mais : email Gmail, aucun témoignage, aucune garantie formelle, thème WordPress générique. |

**Score E-E-A-T global : 42/100** — L'expertise est réelle mais les signaux d'autorité et de confiance sont quasi absents. Google a besoin de signaux externes (avis, backlinks, mentions) pour valider l'expertise affirmée.

---

## Keyword Analysis

### Mot-clé Principal : "automatisation IA PME"
| Élément | Évaluation |
|---------|------------|
| Intent de recherche | Commercial investigation — le prospect compare les options |
| Keyword dans le title | **Absent** — "AI Automation" en anglais ne compte pas |
| Keyword dans le H1 | **Absent** — H1 = nom de marque |
| Keyword dans les 100 premiers mots | **Absent** |
| Keyword dans les H2 | Partiellement ("Assistants IA pour PME") |
| Keyword dans la meta description | Partiellement ("automatisation") |
| Keyword dans l'URL | **Absent** |
| Densité estimée | < 0.5% — sous-optimisé |

### Mots-clés Secondaires Recommandés

| Mot-clé | Volume estimé | Concurrence | Priorité |
|---------|--------------|-------------|----------|
| automatisation entreprise PME | Moyen | Moyenne | 1 |
| assistant IA artisan | Faible | Faible | 1 |
| chatbot PME | Moyen | Haute | 2 |
| n8n consultant France | Faible | Faible | 1 |
| automatiser devis artisan | Faible | Très faible | 1 |
| CRM automatisé PME | Moyen | Haute | 3 |
| consultant automatisation Valence | Très faible | Très faible | 1 |
| agent IA pour entreprise | Moyen | Moyenne | 2 |
| automatisation facturation | Moyen | Moyenne | 2 |
| domotique Drôme installateur | Faible | Faible | 3 |

### Analyse de l'Intent de Recherche

Le site tente de servir **deux intentions incompatibles** :
1. **Résidentiel/B2C** : "installateur domotique Drôme" → pages Domotique, Alarme, Électricité
2. **B2B PME** : "automatisation IA pour PME artisan" → homepage, blog récent

Google ne peut pas classer un même domaine comme expert des deux sujets. Le résultat : **aucune autorité thématique sur aucun des deux sujets.**

---

## Technical SEO

### Robots.txt
- **Statut : Needs Work**
```
Sitemap: https://smarthome-smartelec.fr/sitemap_index.xml
User-agent: *
Disallow:
Sitemap: https://smarthome-smartelec.fr/sitemap_index.xml  ← DOUBLON
```
- Directive Sitemap en doublon (résidu Yoast → Rank Math)
- Aucun `Disallow: /wp-admin/`
- Pages légales et `/stagiaires/` librement crawlables

### XML Sitemap
- **Statut : Needs Work**
- 2 sous-sitemaps : page-sitemap.xml (12 URLs) + post-sitemap.xml (11 URLs) = **23 URLs total**

**Pages obsolètes dans le sitemap :**
| URL | Dernière modification | Action |
|-----|----------------------|--------|
| `/alarme-risques-techniques/` | Nov 2023 | Redirect 301 ou noindex |
| `/alarme-intrusion-technique/` | Nov 2023 | Redirect 301 ou noindex |
| `/alarme-effraction-intrusion/` | Nov 2023 | Évaluer la pertinence |
| `/stagiaires/` | Oct 2024 | noindex — pas de valeur SEO |
| `/contactez-nous/` | Nov 2023 | Garder mais vérifier contenu |
| Pages légales (x3) | Nov 2023 | noindex — gaspillage crawl |

### Canonical Tags
- ✅ Canonical présent et self-referencing sur la homepage
- ✅ Cohérent avec l'URL canonique

### Core Web Vitals (Estimation)

| Métrique | Estimation | Seuil "Bon" | Verdict |
|----------|-----------|-------------|---------|
| **LCP** | 3.5-5.0s mobile | < 2.5s | **Mauvais** |
| **INP** | 150-250ms | < 200ms | **À risque** |
| **CLS** | 0.1-0.2 | < 0.1 | **À risque** |
| **TTFB** | > 400ms | < 200ms | **Mauvais** |
| **FCP** | 2.5-4.0s | < 1.8s | **Mauvais** |

**Facteurs aggravants :**
- Aucun plugin de cache détecté
- Aucun CDN
- Images JPEG non compressées (pas de WebP)
- Image hero sans `preload` — impacte directement le LCP
- 10 scripts JS chargés
- OVH mutualisé = TTFB élevé
- Elementor génère du CSS/JS surdimensionné

**Impact estimé :** Un LCP de 4s+ provoque 38% de taux de rebond (vs 9% pour un LCP < 2s). Perte potentielle de 25-35% du trafic organique.

### Mobile-Friendliness
- ✅ Viewport meta tag présent
- ✅ Theme Sydney responsive par défaut
- ✅ Elementor avec breakpoints responsives
- ⚠️ Pas de srcset sur les images
- ⚠️ Menu avec sous-menus complexes
- ❌ Pas de CTA sticky mobile
- ❌ Pas de click-to-call sur le numéro de téléphone

### Tracking & Analytics
- **Statut : Fail**
- **Aucun outil de tracking détecté** — Pas de Google Analytics, pas de Google Tag Manager, pas de Search Console visible
- **Impact :** Impossible de mesurer le trafic, les conversions, les sources. Vol à l'aveugle.

---

## Content Gap Analysis

| Sujet Manquant | Volume Potentiel | Concurrence | Type de Contenu | Priorité |
|---------------|-----------------|-------------|-----------------|----------|
| "Comment automatiser ses devis d'artisan" | Moyen | Faible | Guide pratique (TOFU) | 1 |
| "n8n vs Make pour PME" | Moyen | Moyenne | Comparatif (MOFU) | 1 |
| "Chatbot IA pour artisan : guide complet" | Moyen | Faible | Guide (TOFU) | 1 |
| "Automatisation CRM artisan BTP" | Faible | Très faible | Étude de cas (BOFU) | 1 |
| "Consultant automatisation IA Valence Drôme" | Très faible | Très faible | Page locale SEO | 1 |
| "Aides France Num digitalisation PME 2026" | Moyen | Moyenne | Guide (TOFU) | 2 |
| "Prix automatisation IA PME" | Moyen | Faible | Page pricing/FAQ | 2 |
| "Automatiser facturation plombier" | Faible | Très faible | Cas d'usage (BOFU) | 2 |
| "ROI automatisation petite entreprise" | Moyen | Moyenne | Calculateur/article | 2 |
| "Domotique Drôme installateur" | Faible | Faible | Page locale (si maintenu) | 3 |

---

## Featured Snippet Opportunities

### Opportunités immédiates :

1. **"Qu'est-ce que l'automatisation IA pour PME ?"** — Créer un H2 + réponse en 40-60 mots sur une page pilier
2. **"Comment automatiser ses devis artisan ?"** — Guide étape par étape avec liste ordonnée
3. **"n8n c'est quoi ?"** — Paragraphe définition en 50 mots (le site a déjà des articles n8n)
4. **"Combien coûte un chatbot IA pour PME ?"** — Tableau de prix avec 3 niveaux

### Optimisations de contenu existant :
- L'article "Optimisez votre entreprise avec n8n" pourrait capturer le snippet "n8n PME" avec un paragraphe résumé en introduction
- L'article "Le funnel qui vend pendant que vous dormez" pourrait capturer "funnel automatique PME" avec une liste numérotée

---

## Schema Markup

| Type de Schema | Applicable | Statut | Priorité |
|---------------|-----------|--------|----------|
| Organization | Oui | ✅ Présent (adresse, tel, réseaux) | — |
| WebSite | Oui | ✅ Présent (mais name="AI Automation" en anglais) | Corriger |
| WebPage | Oui | ✅ Présent | — |
| BreadcrumbList | Oui | ✅ Présent | — |
| Article | Oui | ✅ Présent sur les posts | — |
| **LocalBusiness** | Oui | ❌ **Absent** | **Critique** |
| **Service** | Oui | ❌ **Absent** | **Haute** |
| **FAQPage** | Oui | ❌ **Absent** | **Haute** |
| **AggregateRating** | Oui | ❌ **Absent** (aucun avis) | Moyenne |
| HowTo | Potentiel | ❌ Absent | Basse |
| **ProfessionalService** | Oui | ❌ **Absent** | **Haute** |

**Actions critiques :**
1. Ajouter `LocalBusiness` avec adresse, téléphone, horaires, zone de service
2. Ajouter `Service` pour chaque offre (automatisation, chatbot, infrastructure données)
3. Créer une section FAQ et implémenter `FAQPage` schema
4. Corriger `WebSite.name` : "AI Automation" → "SMARTHOME SMARTELEC"

---

## Internal Linking Opportunities

### Architecture recommandée :
```
Homepage (pilier principal)
├── /automatisation-ia-pme/ (page pilier - À CRÉER)
│   ├── /automatiser-devis-artisan/ (cluster)
│   ├── /chatbot-ia-pme/ (cluster)
│   ├── /crm-automatise-artisan/ (cluster)
│   └── Blog articles IA → liens vers pilier
├── /consultant-ia-valence/ (page locale SEO - À CRÉER)
├── /consultant-ia-grenoble/ (page locale SEO - À CRÉER)
├── /tarifs/ (page pricing - À CRÉER)
├── /a-propos/ (E-E-A-T - À CRÉER)
└── /domotique/ (archive - si maintenu)
    ├── Articles domotique existants
    └── Banner "Nos services ont évolué → IA"
```

### Liens manquants critiques :
- Blog articles → pages services (0 lien actuellement)
- Homepage → page pricing (inexistante)
- Articles n8n → CTA audit gratuit contextuel
- Page Domotique → redirection douce vers offre IA

---

## Content Strategy Recommendations

### Cadence de publication
- **Recommandé :** 2 articles/mois minimum (actuellement : 4 en 2025, gap de 4 ans avant)
- **Benchmark concurrence :** Synapze et Volteyr publient 1-2x/semaine

### Priorités de contenu (90 jours)

| # | Contenu | Type | Keywords cibles | Priorité |
|---|---------|------|----------------|----------|
| 1 | Page pilier "Automatisation IA pour PME" | Pilier (3000+ mots) | automatisation IA PME, assistant IA entreprise | **Critique** |
| 2 | Page "Nos tarifs" avec FAQ | Conversion | prix automatisation IA, combien coûte chatbot PME | **Critique** |
| 3 | Page locale "Consultant IA Valence Drôme" | SEO local | consultant IA Valence, automatisation Drôme | **Haute** |
| 4 | Étude de cas "Artisan X gagne 15h/semaine" | BOFU | automatiser devis artisan, ROI automatisation | **Haute** |
| 5 | Guide "Automatiser ses devis en 7 jours" | TOFU / Lead magnet | automatiser devis, devis automatique artisan | **Haute** |
| 6 | Comparatif "n8n vs Make pour PME en 2026" | MOFU | n8n vs Make, meilleur outil automatisation PME | Moyenne |
| 7 | Guide "Aides France Num pour la digitalisation PME" | TOFU | France Num, aide digitalisation PME | Moyenne |
| 8 | FAQ "Tout savoir sur les chatbots IA pour PME" | TOFU + Schema | chatbot IA PME, assistant virtuel entreprise | Moyenne |

### Contenu à mettre à jour :
- Article Tywell : corriger l'URL avec emojis → redirect 301
- Article n8n en anglais : traduire en français ou ajouter hreflang
- Articles domotique anciens : ajouter un bandeau "Nos services ont évolué"

---

## Recommandations Priorisées

### Critique (Corriger Immédiatement)

1. **Installer Google Analytics 4 + Search Console** — Actuellement aucun tracking. Impossible de mesurer quoi que ce soit. Impact : base de toute stratégie SEO. (15 min)

2. **Réécrire le title tag homepage** — "Automatisation IA pour PME & Artisans | SMARTHOME SMARTELEC - Valence" — Impact : +20-35% de CTR sur les impressions existantes. (5 min)

3. **Réécrire la meta description homepage** — Message orienté bénéfice client + CTA. (5 min)

4. **Corriger tous les alt text manquants** — 8+ images sans alt sur 3 pages. Impact : accessibilité + visibilité image Google. (30 min)

5. **Installer un plugin de cache** — WP Rocket ou LiteSpeed Cache. Impact : LCP divisé par 2, -30% de taux de rebond. (30 min)

### Haute Priorité (Ce Mois)

6. **Ajouter le schema LocalBusiness** — Indispensable pour le SEO local. (15 min avec Rank Math)

7. **Convertir les images en WebP** — Plugin Imagify ou ShortPixel. Impact : -40-60% de poids page. (1h)

8. **Créer la page pilier "/automatisation-ia-pme/"** — Hub de contenu avec maillage interne. Impact : autorité thématique sur le keyword principal. (1-2 jours)

9. **Corriger l'URL emoji de l'article Tywell** — Redirect 301 vers une URL propre. (10 min)

10. **Restructurer le H1 homepage** — Remplacer le nom de marque par un H1 orienté keyword. (5 min)

### Moyenne Priorité (Ce Trimestre)

11. **Créer 5 pages locales SEO** — Valence, Montélimar, Grenoble, Lyon, Privas. (1 semaine)

12. **Noindex les pages sans valeur SEO** — Pages légales, /stagiaires/, pages alarme obsolètes. (15 min)

13. **Publier 2 articles/mois** ciblés sur les keywords identifiés. (En continu)

14. **Ajouter les schemas Service et FAQPage.** (1h)

15. **Traduire l'article anglais** ou ajouter hreflang. (1h)

### Basse Priorité (Quand Possible)

16. **Migrer vers un hébergement plus rapide** (TTFB > 400ms sur OVH mutualisé). Ou ajouter un CDN (Cloudflare gratuit).

17. **Mettre en place un blog bilingue** si la cible internationale est confirmée.

18. **Créer un template n8n open-source** pour générer des backlinks naturels.

---

## Inventaire Complet du Sitemap

### Pages (12 URLs)
| URL | Dernière MAJ | Statut |
|-----|-------------|--------|
| `/` (homepage) | Sept 2025 | ✅ Active |
| `/domotique-maison-connectee/` | Nov 2023 | ⚠️ Ancien métier |
| `/electricite-habitation-magasin/` | Nov 2023 | ⚠️ Ancien métier |
| `/alarme-effraction-intrusion/` | Nov 2023 | ⚠️ Ancien métier |
| `/alarme-intrusion-technique/` | Nov 2023 | ⚠️ Ancien métier |
| `/alarme-risques-techniques/` | Nov 2023 | ⚠️ Orpheline |
| `/maintien-a-domicile/` | Nov 2023 | ⚠️ Ancien métier |
| `/stagiaires/` | Oct 2024 | ❌ noindex recommandé |
| `/contactez-nous/` | Nov 2023 | ✅ Garder |
| `/conditions-generales-...c-g-p-v/` | Nov 2023 | ❌ noindex |
| `/mentions-legales-...domotique/` | Nov 2023 | ❌ noindex |
| `/politique-confidentialite-...domotique/` | Nov 2023 | ❌ noindex |

### Articles (11 URLs)
| URL | Dernière MAJ | Thématique |
|-----|-------------|------------|
| `/blog/` | — | Index |
| `/guide-des-outils-de-productivite-2025...` | Sept 2025 | IA/Productivité ✅ |
| `/unlocking-workflow-automation...` | Août 2025 | n8n (EN) ⚠️ |
| `/optimisez-votre-entreprise-avec-n8n...` | Août 2025 | n8n ✅ |
| `/funnel-qui-vend-pendant-que-vous-dormez...` | Août 2025 | Marketing ✅ |
| `/%f0%9f%8f%a0...tywell-de-delta-dore...` | Juin 2025 | Domotique ⚠️ URL cassée |
| `/remplacement-dun-tableau-electrique/` | Nov 2023 | Électricité ⚠️ |
| `/un-thermostat-connecte...` | Nov 2023 | Domotique ⚠️ |
| `/maison-connectee-avantages/` | Nov 2023 | Domotique ⚠️ |
| `/rendre-une-vmc-double-flux-connectee/` | Nov 2023 | Domotique ⚠️ |
| `/borne-de-recharge/` | Nov 2023 | IRVE ⚠️ |

**Bilan :** 23 URLs indexées dont **12 obsolètes ou à faible valeur SEO** (52%). Le budget de crawl est gaspillé sur du contenu qui ne sert plus le positionnement cible.

---

*Généré par AI Marketing Suite — `/market seo`*
*Données : script analyze_page.py + crawl WebFetch + analyse experte*
