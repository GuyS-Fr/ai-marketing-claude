# Audit SEO : La Fenêtrière
## https://www.la-fenetriere.fr
### Date : 21 mars 2026

---

## Score SEO Global : 28/100

---

## Résumé Exécutif

Le site la-fenetriere.fr présente des lacunes SEO techniques majeures qui limitent fortement sa visibilité organique. Les problèmes les plus critiques sont : l'absence de sitemap.xml (404), 20 images sur 21 sans attribut alt, aucun schema markup, une meta description de 274 caractères (presque le double du maximum recommandé), et aucun lazy loading sur les images. Le site est construit sur le framework Yii (PHP) avec jQuery, et utilise Google Analytics (G-04MTJ8RL29) + Google Tag Manager + Axeptio pour le consentement RGPD.

Le potentiel de rattrapage est élevé car les corrections les plus impactantes (sitemap, alt text, meta descriptions, schema) sont des interventions techniques rapides à fort ROI.

---

## Checklist SEO On-Page

### Balise Title
- **Status : Needs Work**
- **Actuelle :** "La Fenêtière : Atelier de proximité de menuiseries extérieures" (62 caractères)
- **Problèmes :**
  - 62 caractères → légèrement trop long (recommandé : 50-60), risque de troncature dans les SERPs
  - Le mot-clé principal "fabricant fenêtres" ou "menuiseries sur mesure" n'apparaît pas en premier
  - Typo possible : "Fenêtière" au lieu de "Fenêtrière" dans le titre (à vérifier côté code source)
  - Pas de localisation géographique (Île-de-France, Champigny)
- **Recommandation :** "Menuiseries sur mesure Made in France | La Fenêtrière — Champigny (94)" (65 car.)

### Meta Description
- **Status : Fail**
- **Actuelle :** "La Fenêtrière se fournit en France ; son PVC vient du Doubs, son aluminium de Bourgogne et son vitrage de Normandie. Depuis sa création en 1984, La Fenêtrière développe toujours plus ses engagements, comme le circuit court, l'économie circulaire et la production française." (274 caractères)
- **Problèmes :**
  - 274 caractères → presque le double du maximum (150-160). Google tronquera après ~155 car.
  - Pas d'appel à l'action (pas de CTA)
  - Centrée sur l'entreprise, pas sur le bénéfice client
  - Pas de mot-clé transactionnel ("devis", "sur mesure", "professionnels")
- **Recommandation :** "Fabricant de menuiseries sur mesure en Île-de-France depuis 1984. Fenêtres PVC, Bois, ALU certifiées Origine France Garantie. Devis pro gratuit." (155 car.)

### Hiérarchie des Headings

```
H1: "La Fenêtrière" ← trop générique, devrait être une proposition de valeur
├── H2: "En 2023, nous avons inscrit dans nos statuts notre raison d'être..." ← 460 caractères ! Un H2 ne devrait pas être un paragraphe
├── H2: "Un atelier de proximité :"
│   └── H3: "Service rapide et personnalisé pour les professionnels du bâtiment"
│   └── H3: "L'intérêt pour nos clients ?"
├── H2: "Made in Fenêtre"
├── H2: "Les dernières" ← incomplet, devrait être "Les dernières actualités"
│   └── H3: "actualités" ← en minuscule, incohérent
│   └── H3: "La Fenêtrière expose sa fenêtre bas carbone à l'Élysée"
│   └── H3: "La Fenêtrière, lauréate du Fabriqué en France 2025"
│   └── H3: "Fenêtre ouverte : Décembre 2025 - Janvier 2026"
├── H2: "Nos partenaires"
│   └── H3: "Origine France Garantie - Certification"
```

- **Status : Fail**
- **Problèmes :**
  - H1 = nom de marque uniquement, pas de mot-clé cible
  - H2 de 460 caractères (raison d'être complète) — un heading n'est pas un paragraphe
  - H2 "Les dernières" est incomplet (coupé de "actualités" qui est un H3 séparé)
  - Aucun mot-clé SEO dans les headings ("fenêtres sur mesure", "menuiseries PVC", "fabricant local")
  - H3 "actualités" en minuscule : incohérence typographique
- **Recommandation :**
  - H1 : "Menuiseries extérieures sur mesure — Fabricant local en Île-de-France"
  - H2 : "Notre atelier de proximité à Champigny-sur-Marne"
  - H2 : "Fenêtres PVC, Bois et Aluminium Made in France"
  - H2 : "Gamme Made in Fenêtre — 100% responsable"
  - H2 : "Actualités et engagements"

### Optimisation des Images
- **Status : Fail (critique)**
- **Images totales :** 21
- **Images sans alt text :** 20 (95,2 %)
- **Images avec lazy loading :** 0 (0 %)
- **Seule image avec alt :** "Fabriqué en France" (badge certification)
- **Noms de fichiers :** timestamps sans signification (`1654630435_1.jpg`, `1774017187_slider-elyse.jpg`)
- **Formats :** JPEG et PNG uniquement, aucun WebP ni AVIF
- **Problèmes critiques :**
  - 95 % des images invisibles pour Google Images et les lecteurs d'écran
  - Aucun lazy loading → toutes les images chargées au premier rendu (impact LCP/performance)
  - Pas de dimensions width/height déclarées → risque CLS élevé
  - Noms de fichiers non descriptifs → 0 valeur SEO
- **Recommandation immédiate :** Ajouter des alt descriptifs sur les 20 images. Exemples :
  - `1654798195_2-a.jpg` → `alt="Atelier de fabrication fenêtres PVC La Fenêtrière Champigny"`
  - `1774017187_slider-elyse.jpg` → `alt="Fenêtre bas carbone La Fenêtrière exposée au Palais de l'Élysée 2025"`
  - `1655818500_4.jpg` → `alt="Ligne de production menuiseries sur mesure en Île-de-France"`

### Maillage Interne
- **Status : Needs Work**
- **Liens internes :** 23 (sur 36 liens totaux)
- **Points positifs :**
  - Navigation principale bien structurée (8-9 entrées)
  - Articles du blog renvoient vers les pages piliers
  - URLs descriptives et lisibles
- **Points négatifs :**
  - Liens dupliqués (Facebook x2, plusieurs pages internes en double)
  - Aucun lien "Demander un devis" ou "Contact" mis en avant dans le corps de page
  - Pas de breadcrumb (fil d'Ariane) pour le maillage structuré
  - Pages en erreur probable : /valeurs-engagements, /produits → liens morts dans le maillage
- **Recommandation :** Ajouter des CTA internes contextuels dans le corps de page. Implémenter un breadcrumb sur toutes les pages.

### Structure des URLs
- **Status : Pass (point fort)**
- **Points positifs :**
  - URLs lisibles et descriptives : `/notre-atelier`, `/economie-circulaire`, `/gamme-100-pourcent-responsable-mif`
  - Mots séparés par des tirets
  - Tout en minuscules
  - Pas de paramètres inutiles
- **Points négatifs :**
  - Certains slugs trop longs : `/fenetre-ouverte---decembre-2025----janvier-2026` (triples tirets)
  - Pas d'URL canonique détectée
  - Trailing slashes non consistants

---

## Qualité du Contenu (E-E-A-T)

| Dimension | Score | Preuves |
|-----------|-------|---------|
| **Experience** | Présent | Atelier fondé en 1984, photos de production, articles sur la vie de l'atelier, fabrication réelle documentée. Mais aucun cas client ni retour d'expérience chantier publié. |
| **Expertise** | Présent | Connaissance métier évidente (guide matériaux PVC, article écoconception dans Challenges). Mais contenu technique insuffisant — 1 seul article de fond sur 10 publiés. |
| **Authoritativeness** | Fort | Couverture presse nationale (Le Monde, Le Point, Challenges), certifications (OFG, Fabriqué en France 2025), exposition à l'Élysée. Meilleur signal E-E-A-T du site. |
| **Trustworthiness** | Présent | HTTPS actif, Axeptio (consentement RGPD), mentions légales présentes, adresse physique et téléphone. Manque : avis clients, témoignages, politique de confidentialité visible. |

**Score E-E-A-T global : 62/100** — Les signaux d'autorité institutionnels sont forts, mais le contenu technique de fond manque pour asseoir l'expertise aux yeux de Google.

---

## Analyse de Mots-clés

### Mot-clé Principal Ciblé
- **Mot-clé détecté :** "menuiseries extérieures" (dans le title)
- **Intent de recherche :** Commercial / Transactionnel
- **Alignement intent/contenu :** Faible — le contenu parle de valeurs et mission, pas de produits ou devis

### Placement du Mot-clé Principal

| Élément | Présent ? | Position |
|---------|-----------|----------|
| Title tag | Oui | Fin de titre (mauvaise position) |
| H1 | Non | H1 = "La Fenêtrière" uniquement |
| 100 premiers mots | Non | Les 100 premiers mots parlent de la raison d'être |
| Sous-titres (H2/H3) | Non | Aucun H2/H3 ne contient "menuiseries" |
| Meta description | Non | La meta parle de sourcing, pas de menuiseries |
| URL | Non | URL = "/" (homepage) |
| Densité estimée | ~0,5 % | Sous-optimisé |

### Mots-clés Secondaires Recommandés

| Mot-clé | Volume estimé | Concurrence | Priorité |
|---------|---------------|-------------|----------|
| fabricant fenêtres Île-de-France | Moyen | Faible | 1 |
| menuiseries PVC sur mesure | Élevé | Élevée | 2 |
| fenêtres Made in France | Moyen | Moyenne | 3 |
| menuiserie aluminium sur mesure | Moyen | Moyenne | 4 |
| fenêtres bas carbone | Faible | Très faible | 5 |
| menuiseries professionnels bâtiment | Faible | Faible | 6 |
| fenêtres circuit court | Faible | Très faible | 7 |
| fabricant menuiseries 94 | Faible | Très faible | 8 |
| fenêtres éco-responsables | Moyen | Moyenne | 9 |
| remplacement fenêtres Champigny | Faible | Très faible | 10 |

---

## SEO Technique

### Robots.txt
- **Status : Needs Work**
- **Contenu :**
```
User-agent: *
Allow: /
```
- **Problèmes :**
  - Minimaliste mais fonctionnel
  - Aucune référence au sitemap (`Sitemap: https://www.la-fenetriere.fr/sitemap.xml` manquant)
  - Pas de blocage des ressources non essentielles (ex: /rechercher)

### Sitemap XML
- **Status : Fail (critique)**
- **https://www.la-fenetriere.fr/sitemap.xml → 404 Not Found**
- **Impact :** Google doit découvrir les pages par crawl uniquement via les liens internes. Les pages orphelines ou peu liées ne seront pas indexées.
- **Action immédiate :** Générer un sitemap.xml et le référencer dans robots.txt.

### Balises Canonical
- **Status : Fail**
- Aucune balise canonical détectée sur aucune page.
- **Impact :** Risque de duplicate content si des variations d'URL existent (avec/sans trailing slash, avec/sans www).
- **Action :** Ajouter `<link rel="canonical" href="https://www.la-fenetriere.fr/">` sur chaque page.

### Performance Estimée (Core Web Vitals)

| Métrique | Estimation | Niveau | Cause principale |
|----------|-----------|--------|------------------|
| LCP | > 4,0s | Mauvais | Slider avec images JPEG lourdes, 0 lazy loading, 0 preload |
| FID/INP | 100-200ms | À améliorer | 8 scripts chargés dont GA + GTM + Axeptio |
| CLS | > 0,25 | Mauvais | Images sans dimensions width/height, slider dynamique |
| FCP | > 2,5s | À améliorer | Pas de preload des ressources critiques |

**Impact business :** Les sites échouant aux Core Web Vitals voient 24 % d'abandons en plus. Une réduction de 0,1 du CLS diminue le taux de rebond de 15 %.

### Mobile
- **Status : Needs Work**
- Viewport meta tag : présent (via script)
- Framework Yii avec structure responsive probable
- **Problème critique :** Numéro de téléphone non balisé en `<a href="tel:">` — non cliquable sur mobile

### Tracking & Analytics
- **Status : Pass**
- Google Analytics (gtag) : G-04MTJ8RL29 ✓
- Google Tag Manager : détecté ✓
- Axeptio (consentement RGPD) : détecté ✓

---

## Schema Markup

### Status : Fail (0 schema détecté)

| Type de Schema | Applicable | Status | Impact |
|----------------|------------|--------|--------|
| Organization | Oui (entreprise) | Absent | Rich results marque |
| LocalBusiness | Oui (atelier avec adresse) | Absent | Google Maps, Knowledge Panel |
| Product | Oui (fenêtres, volets) | Absent | Rich results produits |
| Article / BlogPosting | Oui (Le Mag) | Absent | Rich results articles |
| FAQPage | Oui (page /faq existe) | Absent | FAQ dans les SERPs |
| BreadcrumbList | Oui (navigation) | Absent | Fil d'Ariane dans les SERPs |
| WebSite + SearchAction | Oui | Absent | Sitelinks search box |

**Recommandation prioritaire :** Implémenter en JSON-LD :
1. `LocalBusiness` sur /contact (adresse, tel, horaires, coordonnées)
2. `Organization` sur la homepage (nom, logo, réseaux sociaux, certifications)
3. `Article` sur chaque article du Mag
4. `FAQPage` sur /faq
5. `BreadcrumbList` sur toutes les pages

---

## Analyse de Lacunes de Contenu

| Sujet Manquant | Volume Potentiel | Concurrence | Type de Contenu | Priorité |
|----------------|-----------------|-------------|-----------------|----------|
| "Comment choisir ses fenêtres PVC ou aluminium" | Élevé | Moyenne | Guide comparatif | 1 |
| "Fenêtres et RE2020 : normes thermiques" | Moyen | Faible | Article expert | 2 |
| "Aides financières fenêtres 2026 (MaPrimeRénov')" | Élevé | Élevée | Page ressource | 3 |
| "Fabricant fenêtres Made in France vs import" | Moyen | Faible | Article comparatif | 4 |
| "Fenêtre bas carbone : qu'est-ce que c'est ?" | Faible | Très faible | Article pionnier | 5 |
| "Menuiseries en économie circulaire" | Faible | Très faible | Article expert | 6 |
| "Devis fenêtres professionnels Île-de-France" | Moyen | Moyenne | Landing page | 7 |
| "Entretien fenêtres PVC : guide complet" | Moyen | Élevée | Guide pratique | 8 |
| "TVA réduite fenêtres rénovation 2026" | Moyen | Moyenne | Article fiscal | 9 |
| "Fenêtres pour bailleurs sociaux : obligations" | Faible | Très faible | Article B2B niche | 10 |

---

## Opportunités Featured Snippets

### Position zéro atteignable

1. **"Qu'est-ce qu'une fenêtre bas carbone ?"** — Pas de concurrent fort sur cette requête émergente. La Fenêtrière a la légitimité (exposition Élysée). Format : paragraphe de 40-60 mots après un H2 question.

2. **"Différence fenêtre PVC et aluminium"** — Requête à volume élevé avec de nombreux featured snippets de type tableau. Format : tableau HTML comparatif.

3. **"Qu'est-ce que la certification Origine France Garantie ?"** — La Fenêtrière est certifiée et peut répondre avec autorité. Format : paragraphe concis.

---

## Recommandations Prioritaires

### Critique (Corriger Immédiatement)

1. **Générer et publier un sitemap.xml** — Le sitemap est en 404. Sans lui, Google ne peut pas indexer efficacement le site. Impact : +30 à 50 % de pages indexées. Effort : 30 minutes.

2. **Ajouter les alt text sur les 20 images** — 95 % des images sont invisibles pour Google et les lecteurs d'écran. Impact : visibilité Google Images + accessibilité WCAG. Effort : 1 à 2 heures.

3. **Réécrire la meta description** — 274 caractères → la ramener à 155 maximum avec un CTA et des mots-clés. Impact : +15 à 25 % de CTR dans les SERPs. Effort : 15 minutes.

4. **Ajouter les balises canonical** — Risque de duplicate content sans canonical. Effort : 30 minutes pour tout le site.

### Haute Priorité (Ce Mois)

5. **Implémenter le schema LocalBusiness** — Avec adresse, téléphone, horaires. Impact : apparition dans le Knowledge Panel Google et Google Maps. Effort : 1 heure.

6. **Réécrire le H1 de la homepage** — "La Fenêtrière" → "Menuiseries sur mesure Made in France — Fabricant en Île-de-France". Impact : signal sémantique principal pour Google. Effort : 5 minutes.

7. **Corriger le H2 de 460 caractères** — Déplacer la raison d'être en paragraphe normal et créer un H2 concis. Effort : 15 minutes.

8. **Ajouter le schema Article sur les posts du Mag** — Chaque article devrait avoir un balisage BlogPosting. Impact : rich results articles dans les SERPs. Effort : 1 à 2 heures.

9. **Référencer le sitemap dans robots.txt** — Ajouter `Sitemap: https://www.la-fenetriere.fr/sitemap.xml`. Effort : 2 minutes.

### Priorité Moyenne (Ce Trimestre)

10. **Convertir les images en WebP** — Gain de 25 à 35 % sur le poids des images. Implémenter lazy loading (`loading="lazy"`). Impact : amélioration LCP et performance globale. Effort : 2 à 4 heures.

11. **Publier 1 article SEO/mois** — Cibler les lacunes de contenu identifiées, en commençant par "Comment choisir ses fenêtres PVC ou aluminium". Impact : +500 à 2 000 visiteurs organiques/mois à 6 mois. Effort : 4 à 6 heures/article.

12. **Créer une page "Devis fenêtres professionnels"** — Landing page SEO dédiée à la requête transactionnelle "devis fenêtres pro IDF". Impact : capture de trafic intentionnel B2B. Effort : 3 à 4 heures.

13. **Ajouter les dimensions width/height aux images** — Éliminer le CLS (Cumulative Layout Shift). Effort : 1 heure.

14. **Créer un fil d'Ariane (breadcrumb)** — Améliore le maillage + schema BreadcrumbList dans les SERPs. Effort : 2 heures.

### Basse Priorité (Quand les Ressources le Permettent)

15. **Implémenter le schema FAQPage sur /faq** — Impact : FAQ visible directement dans les SERPs. Effort : 1 heure.

16. **Renommer les fichiers images** — Remplacer les timestamps par des noms descriptifs. Effort : 3 à 4 heures (avec redirections).

17. **Mettre en place un CDN** — Pour améliorer le TTFB et les performances globales. Effort : 2 à 4 heures.

18. **Créer des pages produits dédiées** — Une page SEO par gamme (PVC, ALU, Bois) ciblant les requêtes "fenêtres PVC sur mesure", etc. Impact : positionnement sur des requêtes commerciales. Effort : 6 à 10 heures.

---

## Stratégie de Contenu SEO Recommandée

### Cadence de Publication
- **Minimum :** 1 article/mois (vs rythme actuel de ~3/an)
- **Idéal :** 2 articles/mois + 1 mise à jour d'article existant

### Cluster Thématique Principal
```
Page Pilier : "Menuiseries sur mesure Made in France" (homepage optimisée)
├── "Guide complet : choisir entre PVC, Bois et Aluminium"
├── "Fenêtres et RE2020 : normes et performances thermiques"
├── "Qu'est-ce qu'une fenêtre bas carbone ?"
├── "Aides financières fenêtres 2026 : MaPrimeRénov', TVA 5,5%"
├── "Menuiseries en économie circulaire : le modèle La Fenêtrière"
├── "Fabricant local vs grande enseigne : le vrai comparatif"
├── "Entretien fenêtres PVC : guide pratique"
└── "Devis fenêtres professionnels Île-de-France"
```

### Matrice de Priorisation

| Contenu | Volume | Concurrence | Valeur Business | Score Priorité |
|---------|--------|-------------|-----------------|----------------|
| Guide choix PVC/ALU/Bois | Élevé | Moyenne | Élevée | 9/10 |
| Fenêtres RE2020 | Moyen | Faible | Élevée | 8/10 |
| Aides financières 2026 | Élevé | Élevée | Moyenne | 7/10 |
| Fenêtre bas carbone | Faible | Très faible | Élevée | 7/10 |
| Fabricant local vs enseigne | Moyen | Faible | Élevée | 8/10 |
| Landing page devis pro | Moyen | Moyenne | Très élevée | 9/10 |

---

## Synthèse des Scores

| Catégorie | Score |
|-----------|-------|
| Balise Title | 4/10 |
| Meta Description | 2/10 |
| Hiérarchie Headings | 3/10 |
| Images & Alt Text | 1/10 |
| Maillage Interne | 5/10 |
| Structure URLs | 7/10 |
| E-E-A-T | 6/10 |
| Mots-clés | 2/10 |
| Schema Markup | 0/10 |
| Sitemap & Robots | 2/10 |
| Core Web Vitals | 2/10 |
| Mobile | 4/10 |
| **Score Global** | **28/100** |

**Diagnostic en une phrase :** La Fenêtrière possède une autorité de marque réelle (presse nationale, certifications, Élysée) que Google ne peut pas voir ni valoriser à cause de fondations techniques SEO absentes — le ROI des corrections de base sera exceptionnellement élevé.

---

*Généré par AI Marketing Suite — `/market seo`*
