# Audit SEO : La Fenêtrière
## https://www.la-fenetriere.fr/
### Date : 20 mars 2026

---

## Score SEO Global : 22/100

---

## Checklist SEO On-Page

### Balise Title
- **Statut : Needs Work**
- **Actuel :** "La Fenêtière : Atelier de proximité de menuiseries extérieures" (62 caractères)
- **Problèmes :**
  - Contient une coquille : "Fenêtière" au lieu de "Fenêtrière" (faute dans le HTML source)
  - Longueur à 62 caractères — légèrement au-dessus de la limite optimale de 60
  - Aucun mot-clé principal géolocalisé (manque "Champigny-sur-Marne" ou "Île-de-France")
  - Aucun mot-clé produit (fenêtres, PVC, aluminium, bois)
- **Recommandé :** "Fenêtres PVC, Bois & ALU sur mesure | La Fenêtrière - Champigny (94)" (68 car.)
- **Impact :** Une correction du title peut augmenter le CTR de 20-35% sur les requêtes positionnées.

### Meta Description
- **Statut : Fail**
- **Actuelle :** "La Fenêtrière se fournit en France ; son PVC vient du Doubs, son aluminium de Bourgogne et son vitrage de Normandie. Depuis sa création en 1984, La Fenêtrière développe toujours plus ses engagements, comme le circuit court, l'économie circulaire et la production française." (274 caractères)
- **Problèmes :**
  - **274 caractères** — presque le double de la limite recommandée de 150-160 caractères
  - Google tronquera cette description à ~155 caractères, coupant le message en plein milieu
  - Aucun appel à l'action (CTA)
  - Orientée fournisseur, pas orientée bénéfice client
  - Pas de mention de la cible (professionnels, particuliers)
- **Recommandée :** "Fabricant artisanal de fenêtres PVC, bois et ALU à Champigny-sur-Marne. Certifié Origine France Garantie. Devis gratuit pour professionnels du bâtiment." (157 car.)
- **Impact :** Un meta description optimisé peut augmenter le CTR de 5-10%.

### Hiérarchie des Titres (H1-H6)
- **Statut : Needs Work**
- **Structure actuelle :**
  ```
  H1: "La Fenêtrière" (1 seul — OK structurellement)
  H2: "En 2023, nous avons inscrit dans nos statuts notre raison d'être..." (460+ caractères !)
  H2: "Un atelier de proximité :"
  H2: "Made in Fenêtre"
  H2: "Les dernières"
  H2: "Nos partenaires"
  H3: "Service rapide et personnalisé pour les professionnels du bâtiment"
  H3: "L'intérêt pour nos clients ?"
  H3: "La Fenêtrière expose sa fenêtre bas carbone à l'Élysée"
  H3: "La Fenêtrière, lauréate du Fabriqué en France 2025"
  H3: "Fenêtre ouverte : Décembre 2025 - Janvier 2026"
  H3: "Origine France Garantie - Certification"
  ```
- **Problèmes :**
  - Le H1 "La Fenêtrière" est générique — ne contient aucun mot-clé produit ou géographique
  - Le premier H2 contient **toute la raison d'être** de l'entreprise (~460 caractères) — c'est un paragraphe, pas un titre
  - "Les dernières" est un H2 tronqué et non descriptif
  - Aucun H2 ne cible un mot-clé SEO stratégique (fenêtres, menuiseries, PVC, sur mesure, Champigny)
- **Recommandations :**
  - H1 : "Fabricant de menuiseries extérieures à Champigny-sur-Marne"
  - H2 : "Nos fenêtres PVC, bois et aluminium sur mesure"
  - H2 : "Un atelier de proximité en Île-de-France"
  - H2 : "La gamme Made in Fenêtre — 100% française"
  - H2 : "Nos dernières actualités"
  - Déplacer la raison d'être dans un paragraphe sous un H2, pas dans le H2 lui-même

### Optimisation des Images
- **Statut : Fail (critique)**
- **Données du script :**
  - **21 images au total**
  - **20 images sans attribut alt** (95% !)
  - **0 image avec lazy loading**
- **Problèmes :**
  - Quasi-totalité des images sans attribut alt — pénalité SEO et accessibilité majeure
  - Noms de fichiers non descriptifs (ex: `1654630435_1.jpg`, `1755685707_certification-gris.png`)
  - Aucun lazy loading implémenté — toutes les images chargent immédiatement, ralentissant la page
  - Pas de format WebP détecté — images probablement en JPG/PNG non optimisées
  - Image Open Graph avec chemin relatif (`/img/banner/6.jpg`) — devrait être une URL absolue
- **Recommandations :**
  1. Ajouter un alt descriptif sur chaque image : `alt="Atelier de fabrication La Fenêtrière à Champigny-sur-Marne"`
  2. Renommer les fichiers : `fenetre-pvc-sur-mesure-champigny.jpg`
  3. Implémenter `loading="lazy"` sur toutes les images sous le fold
  4. Convertir en WebP avec fallback JPG
  5. Corriger l'og:image en URL absolue : `https://www.la-fenetriere.fr/img/banner/6.jpg`

### Maillage Interne
- **Statut : Needs Work**
- **Données :** 23 liens internes, 9 liens externes, 36 liens au total
- **Problèmes :**
  - 23 liens internes pour 756 mots (3 liens / 100 mots) — quantité acceptable mais qualité insuffisante
  - La plupart des liens sont des éléments de navigation, pas du maillage contextuel
  - Pas de liens entre contenu éditorial (blog) et pages produits (blog en 404 de toute façon)
  - Pas de liens vers une page devis ou conversion depuis le contenu principal
- **Recommandations :**
  1. Ajouter des liens contextuels dans le corps du texte vers les pages produits
  2. Lier les articles du Mag (une fois réparé) vers les pages produits correspondantes
  3. Ajouter un lien CTA vers la page devis/contact dans chaque section de contenu

### Structure des URLs
- **Statut : Pass**
- URLs propres, lisibles, en minuscules avec tirets : `/notre-atelier`, `/economie-circulaire`, `/guide-de-choix-des-materiaux/pvc`
- Hiérarchie logique et cohérente
- Pas de paramètres inutiles
- Pas de majuscules ni underscores

---

## Qualité du Contenu (E-E-A-T)

| Dimension | Score | Preuves |
|-----------|-------|---------|
| **Experience** | Présent | Entreprise existant depuis 1984 (42 ans), atelier visitable, équipe nommée avec ancienneté. Mais aucune étude de cas chantier, aucune photo avant/après, aucun témoignage terrain. |
| **Expertise** | Faible | Contenu peu profond (756 mots sur la homepage). Pas de guides techniques, pas de contenu éducatif sur les matériaux, les normes ou les process. Le blog qui pourrait démontrer l'expertise est en 404. |
| **Authoritativeness** | Présent | Prix Madame Engagée 2021, Lauréate Fabriqué en France 2025, Prix Étienne Marcel, certification OFG. Articles dans Batiweb, Verre & Menuiserie, Entrepreneurs d'Avenir. Mais pas d'auteur identifié sur le contenu. |
| **Trustworthiness** | Présent | HTTPS actif, adresse physique complète, téléphone, email, mentions légales, politique de cookies (Axeptio). Mais aucun avis client, aucun témoignage, aucune garantie explicitée. |

**Score E-E-A-T global : 45/100** — Les signaux d'autorité institutionnelle sont solides mais le contenu web ne les met pas en valeur.

---

## Analyse des Mots-Clés

### Mot-clé Principal Identifié
- **Mot-clé cible probable :** "menuiseries extérieures" / "fabricant fenêtres"
- **Intention de recherche :** Commercial (recherche de fournisseur)
- **Alignement contenu :** Faible — le contenu parle davantage de valeurs RSE que de produits

### Présence du Mot-clé Principal

| Élément | Présent ? | Commentaire |
|---------|-----------|-------------|
| Title | ✅ Partiel | "menuiseries extérieures" est présent |
| H1 | ❌ | H1 = "La Fenêtrière" (nom de marque uniquement) |
| 100 premiers mots | ❌ | Les premiers mots parlent de la raison d'être, pas des produits |
| Sous-titres (H2/H3) | ❌ | Aucun H2/H3 ne contient "fenêtres", "menuiseries" ou un mot-clé produit |
| Meta description | ❌ | Parle du circuit court, pas des produits |
| URL | ❌ | "/" — URL racine, neutre |

### Mots-Clés Secondaires Recommandés

| Mot-clé | Volume estimé (FR) | Priorité |
|---------|-------------------|----------|
| fenêtres PVC sur mesure | Élevé | 1 |
| fabricant fenêtres Made in France | Moyen | 2 |
| menuiseries Champigny-sur-Marne | Faible (local) | 3 |
| fenêtres aluminium Île-de-France | Moyen | 4 |
| remplacement fenêtres MaPrimeRénov | Élevé | 5 |
| volets roulants sur mesure | Moyen | 6 |
| porte d'entrée PVC | Moyen | 7 |
| menuiseries économie circulaire | Faible (niche) | 8 |
| fenêtres Origine France Garantie | Faible (niche) | 9 |
| devis fenêtres professionnel bâtiment | Moyen | 10 |

---

## SEO Technique

### Robots.txt
- **Statut : Needs Work**
- Le fichier existe et est accessible
- Contenu : `User-agent: * / Allow: /`
- ❌ **Pas de référence au sitemap** (directive `Sitemap:` absente)
- Le fichier est minimal mais fonctionnel — ne bloque pas le crawl

### Sitemap XML
- **Statut : Fail (critique)**
- ❌ **Sitemap introuvable** — ni `/sitemap.xml` ni `/sitemap_index.xml` ne sont accessibles
- Impact : Google découvre les pages uniquement par exploration de liens, sans priorisation
- **Action immédiate :** Générer un sitemap.xml, le soumettre dans Google Search Console, et ajouter `Sitemap: https://www.la-fenetriere.fr/sitemap.xml` dans robots.txt

### Balise Canonical
- **Statut : Fail**
- ❌ **Aucune balise canonical** détectée sur la page d'accueil
- Risque de contenu dupliqué non géré (HTTP/HTTPS, avec/sans trailing slash, avec/sans www)

### Vitesse de Chargement
- **Statut : Non mesuré directement**
- **Signaux préoccupants :**
  - 0/21 images avec lazy loading
  - 8 scripts JavaScript chargés
  - Noms d'images suggérant l'absence de pipeline d'optimisation
  - Pas de CDN détecté
  - Google Tag Manager + Google Analytics (scripts tiers)
- **Recommandation :** Lancer un test PageSpeed Insights et viser LCP < 2,5s

### Mobile-Friendliness
- **Statut : Pass (partiel)**
- ✅ Balise viewport présente (`<meta name="viewport">` confirmée par le script)
- ⚠️ Test mobile complet non réalisé (taille des zones de clic, scroll horizontal, etc.)

### Schema Markup
- **Statut : Fail (critique)**
- ❌ **Zéro schema markup** détecté (0 types de schema)
- C'est la lacune la plus dommageable pour un artisan local
- **Schémas manquants critiques :**

| Schema | Applicable | Statut | Priorité |
|--------|-----------|--------|----------|
| LocalBusiness / HomeAndConstructionBusiness | ✅ | ❌ Absent | CRITIQUE |
| Organization | ✅ | ❌ Absent | HAUTE |
| BreadcrumbList | ✅ | ❌ Absent | HAUTE |
| FAQPage | ✅ (page /faq existe) | ❌ Absent | HAUTE |
| Article | ✅ (articles du Mag) | ❌ Absent | MOYENNE |
| Product | ✅ (gammes produits) | ❌ Absent | MOYENNE |
| WebSite + SearchAction | ✅ (recherche interne existe) | ❌ Absent | BASSE |

### Tracking et Analytics
- **Statut : Pass**
- ✅ Google Tag Manager détecté
- ✅ Google Analytics (gtag) détecté
- L'infrastructure de mesure est en place

---

## Analyse des Lacunes de Contenu

| Sujet Manquant | Volume de Recherche | Concurrence | Type de Contenu | Priorité |
|---------------|-------------------|-------------|-----------------|----------|
| Guide MaPrimeRénov' fenêtres 2026 | Élevé | Moyenne | Landing page + guide | 1 |
| Comparatif PVC vs ALU vs Bois | Élevé | Haute | Guide comparatif | 2 |
| Fenêtres conformes RE2020 | Moyen | Faible | Article expert | 3 |
| Prix fenêtres sur mesure (fourchette) | Élevé | Haute | Page informative | 4 |
| Remplacement fenêtres copropriété | Moyen | Faible | Guide pratique | 5 |
| Comment choisir son vitrage | Moyen | Moyenne | Guide technique | 6 |
| Fabrication artisanale menuiseries | Faible | Faible | Visite virtuelle / article | 7 |
| Économie circulaire bâtiment | Faible | Faible | Article thought leadership | 8 |
| Entretien fenêtres bois | Moyen | Moyenne | Guide pratique | 9 |
| Rénovation fenêtres patrimoine ancien | Faible | Faible | Étude de cas | 10 |

---

## Opportunités Featured Snippets

1. **"Comment bénéficier de MaPrimeRénov' pour ses fenêtres ?"** — Paragraphe de 40-60 mots en réponse directe sous un H2 question
2. **"Quelle différence entre fenêtre PVC et aluminium ?"** — Tableau comparatif HTML avec colonnes PVC/ALU/Bois
3. **"Qu'est-ce que la certification Origine France Garantie ?"** — Paragraphe explicatif ciblant le snippet définition
4. **"Combien coûte une fenêtre sur mesure en France ?"** — Liste avec fourchettes de prix par matériau

---

## Opportunités de Maillage Interne

1. **Pages orphelines potentielles :** Les sous-pages produits (si elles existent) ne semblent pas liées depuis la homepage
2. **Page hub manquante :** Créer une page pilier "/nos-menuiseries" liant vers chaque catégorie produit
3. **Liens blog → produits :** Chaque article du Mag devrait lier vers la page produit correspondante
4. **Liens produits → contact :** Chaque page produit devrait avoir un CTA "Demander un devis" liant vers /contact
5. **Architecture recommandée :**
   ```
   Accueil
   ├── Nos Menuiseries (pilier)
   │   ├── Fenêtres PVC
   │   ├── Fenêtres Aluminium
   │   ├── Fenêtres Bois
   │   ├── Portes d'entrée
   │   ├── Volets roulants
   │   └── Portails
   ├── Le Mag (blog)
   │   ├── Guide MaPrimeRénov'
   │   ├── Comparatif matériaux
   │   └── → Liens vers pages produits
   ├── Notre Atelier
   ├── Nos Valeurs
   └── Contact / Devis
   ```

---

## Core Web Vitals — Évaluation d'Impact

| Métrique | Estimation | Statut | Correctifs |
|----------|-----------|--------|------------|
| LCP (Largest Contentful Paint) | > 3s probable | ⚠️ Needs Work | Optimiser hero image, implémenter lazy loading, ajouter CDN |
| FID/INP (Interaction to Next Paint) | Inconnu | ⚠️ | Différer scripts non-critiques (GTM, Axeptio) |
| CLS (Cumulative Layout Shift) | Inconnu | ⚠️ | Définir dimensions sur toutes les images |

**Impact financier estimé :**
- Sites passant tous les Core Web Vitals : 24% moins d'abandons de page
- Réduction du LCP de 100ms : +1,1% de taux de conversion
- Réduction du CLS de 0,1 : -15% de taux de rebond

---

## Stratégie de Contenu Recommandée

### Cadence de Publication
- **Court terme (3 mois) :** 2 articles/mois pour construire le socle SEO
- **Moyen terme (6 mois) :** 4 articles/mois avec mix guides + actualités + études de cas
- **Long terme :** 4 articles/mois + mise à jour trimestrielle des articles existants

### Priorités de Contenu

| Contenu | Volume Recherche | Concurrence | Valeur Business | Score Priorité |
|---------|-----------------|-------------|-----------------|----------------|
| Guide MaPrimeRénov' fenêtres 2026 | Élevé | Moyenne | Élevée | 10/10 |
| Comparatif PVC vs ALU vs Bois | Élevé | Haute | Élevée | 9/10 |
| Pages produits enrichies (6 pages) | Élevé | Moyenne | Très élevée | 9/10 |
| Fenêtres RE2020 pour professionnels | Moyen | Faible | Élevée | 8/10 |
| Études de cas chantiers (3-5) | Faible | Faible | Très élevée | 8/10 |
| Guide entretien menuiseries | Moyen | Moyenne | Moyenne | 6/10 |
| Économie circulaire dans le bâtiment | Faible | Faible | Moyenne | 5/10 |

---

## Recommandations Priorisées

### Critique (À corriger immédiatement)

1. **Corriger la coquille dans le title** — "Fenêtière" → "Fenêtrière". Chaque impression Google affiche cette faute. *Effort : 1 minute. Impact : crédibilité.*

2. **Générer et soumettre un sitemap.xml** — Le site n'a aucun sitemap. Google découvre les pages par hasard. Ajouter la référence dans robots.txt. *Effort : 30 minutes. Impact : indexation complète.*

3. **Ajouter les attributs alt sur les 20 images** — 95% des images n'ont pas d'alt. C'est la plus grosse faille technique du site. *Effort : 2 heures. Impact : SEO images + accessibilité.*

4. **Raccourcir la meta description à 155 caractères** — La description actuelle de 274 caractères est tronquée par Google. *Effort : 15 minutes. Impact : CTR +5-10%.*

5. **Implémenter le schema LocalBusiness** — En JSON-LD sur la page d'accueil et contact. Nom, adresse, téléphone, horaires, coordonnées GPS. *Effort : 1 heure. Impact : pack local Google Maps.*

### Haute Priorité (Ce Mois)

6. **Réécrire le H1 avec un mot-clé produit** — "La Fenêtrière" → "Fabricant de menuiseries extérieures à Champigny-sur-Marne". *Impact : signal SEO on-page principal.*

7. **Ajouter la balise canonical sur toutes les pages** — Prévenir les problèmes de contenu dupliqué. *Effort : 30 minutes.*

8. **Réparer la raison d'être en H2** — Déplacer le texte de 460 caractères du H2 vers un paragraphe. Le H2 devrait être un titre court et descriptif. *Impact : structure sémantique.*

9. **Corriger l'og:image** — Passer de chemin relatif `/img/banner/6.jpg` à URL absolue. *Impact : partages réseaux sociaux.*

10. **Créer les pages produits individuelles** — 6 pages : Fenêtres PVC, ALU, Bois, Portes, Volets, Portails. Chacune avec 500+ mots, images alt-taggées, schema Product. *Impact : multiplication des pages indexables et des requêtes ciblées.*

### Moyenne Priorité (Ce Trimestre)

11. **Lancer le blog avec 3 articles SEO prioritaires** — MaPrimeRénov', comparatif matériaux, RE2020. *Impact : +30-50% trafic organique à 6 mois.*

12. **Implémenter le lazy loading** — `loading="lazy"` sur toutes les images sous le fold. *Impact : vitesse de chargement.*

13. **Implémenter les schemas FAQPage et Article** — Sur la page FAQ et les articles du blog. *Impact : rich snippets.*

14. **Inscrire le site dans Google Search Console et Bing Webmaster Tools** — Si ce n'est pas déjà fait. *Impact : visibilité sur les problèmes d'indexation.*

### Basse Priorité (Quand les Ressources le Permettent)

15. **Convertir les images en WebP** — Format moderne, taille réduite de 25-35%. *Impact : vitesse.*

16. **Mettre en place un CDN** — Cloudflare gratuit suffirait. *Impact : temps de réponse serveur.*

17. **Implémenter les breadcrumbs** — Fil d'Ariane balisé en BreadcrumbList. *Impact : navigation + SEO.*

---

*Généré par AI Marketing Suite — `/market seo`*
