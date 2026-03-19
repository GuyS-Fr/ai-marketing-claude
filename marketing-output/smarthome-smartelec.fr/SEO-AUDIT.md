# Audit SEO Technique — SMARTHOME SMARTELEC
**URL :** https://smarthome-smartelec.fr
**Date :** 19 mars 2026
**Plateforme :** WordPress + thème Sydney | **Hébergement :** OVH
**Score Global : 42/100**

---

## Synthèse

Le site dispose d'une base technique correcte (Schema.org, Rank Math, robots.txt, HTTPS) mais souffre de lacunes critiques : meta descriptions absentes, images sans alt, pages obsolètes indexées, contenu bilingue sans hreflang, et un positionnement technique qui contredit le pivot stratégique vers l'IA/automatisation.

---

## Scores Détaillés

| Critère | Score | Priorité |
|---|---|---|
| Title tags & meta descriptions | 4/10 | CRITIQUE |
| Structure URL & maillage interne | 5/10 | HAUTE |
| Optimisation des images | 2/10 | CRITIQUE |
| Responsivité mobile | 6/10 | MOYENNE |
| Performance & chargement | 5/10 | HAUTE |
| Schema markup | 7/10 | BASSE |
| Sitemap & robots.txt | 6/10 | MOYENNE |
| Contenu multilingue (impact SEO) | 2/10 | CRITIQUE |
| Pages anciennes vs positionnement | 3/10 | CRITIQUE |
| Accessibilité de base | 3/10 | HAUTE |

---

## Forces

- **Schema.org JSON-LD bien implémenté** : WebPage, Organization, WebSite, Article, BreadcrumbList, ImageObject
- **Plugin Rank Math SEO actif** : sitemap index structuré (post-sitemap / page-sitemap)
- **robots.txt valide** : syntaxe correcte, sitemap référencé, aucune restriction abusive
- **Attribut `lang="fr-FR"`** présent sur `<html>`
- **Canonical URLs** correctement définies
- **HTTPS actif** sans redirection HTTP détectée
- **Pas de `noindex`** sur les pages principales
- **Adresse physique et téléphone** intégrés dans le schéma Organization

---

## Faiblesses

- **Meta descriptions absentes** sur homepage et /blog/ — champ critique vide dans Rank Math
- **Images quasi sans alt text** : logo, hero, articles, logos partenaires — lacune SEO et accessibilité majeure
- **URL avec emojis encodés** : `/%f0%9f%8f%a0%e2%9c%a8-tywell...` — non lisible, problème d'indexation
- **Article entièrement en anglais** sans hreflang ni version FR alternative
- **8 pages de l'ancien métier** toujours indexables sans redirection ni mise à jour (alarme, domotique, électricité, maintien à domicile)
- **Images JPEG uniquement** — pas de WebP détecté
- **Logo PNG de 2018** : format non optimisé
- **Aucun hreflang** sur l'article anglais — signal confus pour Google
- **Titre meta anglais** "AI Automation" sur un site fr-FR
- **Double H1 potentiel** sur la homepage
- **Pas de plugin de cache** détecté (WP Rocket, LiteSpeed, W3TC absents)
- **Pas de CDN** configuré
- **Sitemap sans `priority` ni `changefreq`**
- **Schéma LocalBusiness manquant**
- **Auteur "GuyS"** — nom incomplet pour E-E-A-T

---

## Analyse Détaillée

### 1. Balises Title et Meta Descriptions (4/10)

| Page | Title | Meta Description |
|---|---|---|
| Homepage | "SMARTHOME SMARTELEC - AI Automation" (37 car.) | **ABSENTE** |
| Blog | ? | **ABSENTE** |
| Articles | "Titre - AI Automation" | Variable |
| Alarme intrusion | Présent | Présente (117 car.) |

**Problèmes :**
- Le suffixe "AI Automation" en anglais sur un site fr-FR est incohérent
- La meta description manquante sur la homepage force Google à générer un extrait automatique
- Format uniforme recommandé : "Titre | SMARTHOME SMARTELEC - Automatisation IA Valence"

### 2. Structure URL et Maillage Interne (5/10)

- URLs globalement propres : `/slug-lisible/` sans paramètres excessifs
- URL avec emojis : `/🏠✨-tywell...` → encodage non lisible
- Navigation principale présente + liens en footer + "Articles récents"
- Page orpheline potentielle : `/alarme-risques-techniques/` dans le sitemap mais pas dans la navigation
- Toutes les pages à 1 clic de la homepage (profondeur correcte)
- Liens sortants vers partenaires sans `nofollow` (à évaluer)

### 3. Optimisation des Images (2/10)

**C'est le point le plus faible de l'audit.**

| Élément | Constat |
|---|---|
| Format | JPEG uniquement — pas de WebP |
| Logo | PNG 2018, alt="AI Automation" (non descriptif, en anglais) |
| Hero image | JPEG, alt absent |
| Images articles | Alt absent |
| Logos partenaires | Alt absent |
| Lazy loading | Non confirmé |
| Taille hero | Estimée > 100 Ko — WebP diviserait par 2-3 |

### 4. Responsivité Mobile (6/10)

- Viewport meta présent (standard WordPress/Elementor)
- Thème Sydney responsive par nature
- Elementor utilisé — responsive par défaut mais peut générer du CSS lourd
- À vérifier avec Google Search Console (rapport Utilisabilité mobile)

### 5. Performance et Chargement (5/10)

| Élément | Constat |
|---|---|
| Hébergement OVH | Mutualisé probable — TTFB souvent > 400ms |
| WordPress + Elementor | Stack connue pour JS/CSS non minifié |
| Images JPEG | Impact direct sur LCP |
| Plugin de cache | Non détecté |
| CDN | Non détecté |
| Preload LCP | Absent sur image hero |

Score Lighthouse estimé : 45-60/100 en Performance mobile.

### 6. Schema Markup / Données Structurées (7/10)

**Point le plus positif de l'audit.**

| Schéma | Présent | Qualité |
|---|---|---|
| WebSite | Oui | Correct |
| WebPage | Oui | Correct |
| Organization | Oui | Complet (adresse, téléphone) |
| Article/BlogPosting | Oui | Présent |
| BreadcrumbList | Oui | Correct |
| ImageObject | Oui | Présent |
| LocalBusiness | Non | **Manquant** — pertinent pour local |
| FAQPage | Non | Opportunité |
| Person (auteur) | Oui | "GuyS" — incomplet pour E-E-A-T |

### 7. Sitemap et robots.txt (6/10)

- robots.txt valide avec sitemap référencé
- Sitemap index Rank Math : 10 posts + 12 pages = 22 URLs
- 8 pages de services anciens (2023) dans page-sitemap sans signal de dépréciation
- `lastmod` présent (positif)
- `priority` et `changefreq` absents
- Page `/stagiaires/` indexée — pertinence SEO discutable

### 8. Contenu en Langues Mixtes (2/10)

- `lang="fr-FR"` déclaré sur tout le site
- 1 article entièrement en anglais ("Unlocking Workflow Automation...") sans hreflang
- Google traite cet article comme fr-FR avec contenu anglais → signal contradictoire
- URL en anglais sur domaine .fr
- Risque de déclassement sur les deux marchés linguistiques

### 9. Pages Anciennes vs Positionnement (3/10)

| Constat | Impact |
|---|---|
| 5 pages services anciens (alarme ×2, domotique, électricité, maintien) | Google perçoit un site hybride |
| Dernière modification : novembre 2023 | Aucune mise à jour depuis 2+ ans |
| 5 articles blog 2018-2021 sur domotique résidentielle | Hors-sujet total vs positionnement actuel |
| Navigation affiche toujours l'ancien métier | Signal de positionnement contradictoire |
| Risque E-E-A-T | Mix électricien + IA nuit à la crédibilité thématique |

### 10. Accessibilité de Base (3/10)

- Alt text images : quasi absent
- Structure titres : H1 multiple potentiel
- Langue `html lang` : présent (positif)
- Contraste, navigation clavier, ARIA labels : non vérifiables sans rendu

---

## Plan d'Action

### Phase 1 — Quick Wins (1-2 semaines)
1. Rédiger meta descriptions manquantes (homepage, blog, pages services)
2. Ajouter attributs `alt` sur toutes les images
3. Corriger URL avec emojis + redirection 301
4. Ajouter `hreflang="en"` sur l'article anglais
5. Compléter le nom d'auteur "GuyS" → "Guy SALVATORE"

### Phase 2 — Restructuration (1-2 mois)
6. Décider du sort des pages obsolètes (301 redirect ou mise à jour)
7. Mettre à jour la navigation pour refléter le nouveau positionnement
8. Convertir images en WebP (plugin Imagify ou ShortPixel)
9. Activer un plugin de cache (WP Rocket recommandé)
10. Recycler ou désindexer les articles 2018-2021 hors-sujet
11. Changer le suffixe meta "AI Automation" → "Automatisation IA | Valence"

### Phase 3 — Consolidation (2-4 mois)
12. Créer contenu pilier "Automatisation IA pour PME" avec maillage interne
13. Ajouter schémas `LocalBusiness` et `FAQPage`
14. Auditer Core Web Vitals via Google Search Console
15. Publier stratégie de contenu 100% française sur thématiques IA ciblées
16. Créer pages locales SEO : `/automatisation-valence/`, `/assistant-ia-drome/`
17. Implémenter `preload` pour l'image LCP hero

---

*Audit SEO Technique — AI Marketing Suite `/market seo`*
*Date : 19 mars 2026*
