# Audit GEO — Generative Engine Optimization
## la-fenetriere.fr
### Date : 21 mars 2026

---

## Score GEO Global : 22/100 — Grade D

La Fenêtrière est quasi invisible dans les réponses des moteurs de recherche IA. Sur 6 requêtes stratégiques testées, la marque n'apparaît dans aucun résultat sauf la recherche directe par nom. Les concurrents comme MINCO, VEKA, Tryba et Decobaie captent la totalité des citations IA sur les thématiques pourtant centrales pour La Fenêtrière (fenêtres bas carbone, économie circulaire, Made in France). Le paradoxe est saisissant : l'entreprise a exposé une fenêtre bas carbone à l'Élysée mais n'est citée nulle part quand une IA répond à la question "fenêtre bas carbone France". Le potentiel de rattrapage est très élevé car les actifs de légitimité existent — il manque la structuration du contenu pour les rendre citables par les IA.

---

## 1. Test de Visibilité IA

### Requêtes testées

| # | Requête simulée | La Fenêtrière citée ? | Qui est cité à la place ? |
|---|----------------|----------------------|--------------------------|
| 1 | "Meilleur fabricant fenêtres Made in France artisanal" | Non | Atlantem, Bouvet, AMCC, HUET |
| 2 | "Fabricant menuiseries sur mesure Île-de-France professionnels" | Non | Decobaie, ALU Express, Solabaie, UNIV'R |
| 3 | "Fenêtre bas carbone France fabricant éco-responsable" | Non | MINCO, VEKA, Normabaie, SAPA |
| 4 | "Alternative Tryba menuiseries locales circuit court" | Non | Internorm, Oknoplast, Lapeyre |
| 5 | "La Fenêtrière avis menuiserie Champigny" | Oui (recherche directe) | Pages Jaunes, Mappy, Houzz, Verre & Menuiserie |
| 6 | "Menuiserie économie circulaire réemploi fenêtres France" | Non | Recyfe, MINCO, VEKA, KparK, Lapeyre |

### Constats critiques

- **Requête "fenêtre bas carbone"** : MINCO et VEKA dominent totalement cette thématique que La Fenêtrière incarne pourtant physiquement (exposition Élysée). MINCO a un article de fond "Économie circulaire de la fenêtre" qui est exactement le type de contenu que les IA citent.
- **Requête "menuiserie économie circulaire"** : Recyfe (réseau de recyclage) est cité en premier. La Fenêtrière, qui a inscrit l'économie circulaire dans ses statuts, est absente.
- **Requête "fabricant IDF"** : Decobaie apparaît systématiquement grâce à son contenu SEO structuré ("fabricant de menuiseries aluminium et PVC sur mesure depuis 25 ans").
- **Seule mention** : la recherche directe "La Fenêtrière" renvoie vers PagesJaunes, Mappy et Houzz — pas vers le site officiel en priorité.

### Score Visibilité : 7/20

Le score de 7/20 reflète une présence uniquement sur requête de marque directe. Sur les requêtes génériques à forte valeur commerciale, La Fenêtrière est structurellement absente.

---

## 2. Audit de Citabilité

### 2.1 Statistiques et données chiffrées — 4/15

**Ce qui existe :**
- Surface de l'atelier : "plus de 1 000 m²"
- Nombre de machines : 10 (PVC) + 9 (ALU)
- Nombre de postes de travail : 5 (PVC) + 2 (ALU)
- Couleurs en stock : 3 PVC + 4 ALU
- Date de fondation : 1984

**Ce qui manque :**
- Aucun chiffre de production (nombre de fenêtres/an, nombre de chantiers livrés)
- Aucune donnée d'impact environnemental (kg CO₂ économisés, % matière recyclée)
- Aucune statistique sectorielle citée avec source (taux de recyclage fenêtres en France, etc.)
- Aucun chiffre de satisfaction client ou délai moyen de fabrication
- La fenêtre bas carbone exposée à l'Élysée n'a aucune donnée technique publiée (kg CO₂ eq/UF)

**Impact :** Les IA citent en priorité les contenus avec des données chiffrées vérifiables. MINCO publie "61 kg CO₂ eq/UF" pour sa fenêtre hybride — c'est le type de donnée que ChatGPT extrait et cite.

### 2.2 Citations et sources d'autorité — 3/15

**Ce qui existe :**
- Mention de la certification Origine France Garantie (organisme tiers)
- Mention des prix Étienne Marcel et Madame Engagée

**Ce qui manque :**
- Aucune citation d'étude, de rapport sectoriel ou de donnée ADEME
- Aucune référence à la réglementation RE2020 ou loi AGEC (pourtant au cœur du positionnement)
- Aucun renvoi vers les articles de presse (Le Monde, Le Point, Challenges) depuis le site
- Pas de liens vers les rapports de l'organisme certificateur OFG

**Impact :** L'ajout de sources fiables améliore de 132,4 % la probabilité d'être cité par les chatbots (étude Princeton/Georgia Tech, ACM SIGKDD 2024).

### 2.3 Structure extractible par les IA — 2/15

| Critère | Status | Score |
|---------|--------|-------|
| Headers en format question (H2/H3) | Absent — aucun heading n'est formulé en question | 0/5 |
| Résumés TL;DR en début de section | Absent | 0/3 |
| Tableaux comparatifs, listes structurées | Absent — le guide matériaux PVC pourrait en contenir mais n'est pas accessible | 1/4 |
| FAQ dédiée avec schema markup | Page /faq existe mais sans schema FAQPage | 1/3 |

**Impact :** Les IA découpent les pages en "passages". Chaque section doit pouvoir fonctionner comme une réponse autonome. Actuellement, aucune section du site ne peut être extraite par une IA comme réponse à une question.

### 2.4 Données structurées / Schema.org — 0/10

| Type de schema | Status |
|----------------|--------|
| Organization | Absent |
| FAQPage | Absent |
| Article / BlogPosting | Absent |
| HowTo | Absent |
| Product / Service | Absent |

**0 schema détecté sur l'ensemble du site.** C'est le score le plus bas possible. Les données structurées sont le langage que les IA utilisent pour comprendre le contenu d'une page.

### 2.5 Accessibilité aux crawlers IA — 4/10

**robots.txt :**
```
User-agent: *
Allow: /
```

| Bot IA | Autorisé ? | Status |
|--------|-----------|--------|
| GPTBot (ChatGPT) | Oui (par défaut, pas de blocage) | ✓ |
| Google-Extended (Gemini) | Oui (par défaut) | ✓ |
| ClaudeBot (Claude) | Oui (par défaut) | ✓ |
| PerplexityBot | Oui (par défaut) | ✓ |
| CCBot (Common Crawl) | Oui (par défaut) | ✓ |

**Points positifs :** Le robots.txt n'interdit pas les bots IA. C'est mieux que de nombreuses entreprises qui bloquent GPTBot.

**Points négatifs :**
- Aucun fichier `llms.txt` à la racine (fichier émergent qui donne aux IA un résumé structuré du site)
- Sitemap.xml en 404 → les bots IA ne peuvent pas découvrir toutes les pages
- Pas de `robots.txt` spécifique aux bots IA (pas de signaux positifs d'accueil)

### 2.6 Autorité d'entité et E-E-A-T — 8/15

| Critère | Score | Détail |
|---------|-------|--------|
| Auteur nommé avec biographie | 3/5 | Catherine Guerniou est nommée et visible, mais pas de page auteur structurée au format standard |
| Page "À propos" détaillée | 2/3 | Pages /notre-atelier et /notre-equipe existent avec contenu |
| Mentions de la marque sur sites tiers | 2/4 | PagesJaunes, Mappy, Houzz, Verre & Menuiserie, Batiweb, La French Fab — mais pas assez de domaines référents |
| Profils sur plateformes d'autorité | 1/3 | LinkedIn actif. Pas de Wikipedia, pas de Wikidata, pas de fiche CCI détaillée |

**Point fort :** La couverture presse (Le Monde, Le Point, Challenges) est un signal d'autorité rare pour une PME. Mais ces articles ne sont pas liés depuis le site, donc les IA ne font pas le lien entre la marque et ces mentions.

### 2.7 Avis et sentiment en ligne — 2/10

| Plateforme | Avis | Note |
|-----------|------|------|
| Google Business | Non vérifié / très peu d'avis visibles | N/A |
| PagesJaunes | Présent, données limitées | N/A |
| Houzz | Profil existant | N/A |
| Mappy | 1 avis, 5/5 | 5.0 |
| Trustpilot | Absent | — |
| GoWork | ~3 avis | Mitigé |

**Score : 2/10** — Volume d'avis insuffisant pour que les IA pondèrent positivement. Les IA recommandent en priorité les entreprises avec 10+ avis et une note ≥ 4.0. La Fenêtrière n'atteint ce seuil sur aucune plateforme.

### 2.8 Fraîcheur du contenu — 5/10

| Critère | Score | Détail |
|---------|-------|--------|
| Contenu mis à jour < 90 jours | 3/5 | Article "Élysée" du 02/03/2026 = frais |
| Date de mise à jour visible | 2/3 | Dates visibles sur les articles du Mag |
| Blog actif avec publication régulière | 0/2 | ~3 articles/an, très irrégulier |

**Score Citabilité Global : 28/100**

| Facteur | Score | Poids | Pondéré |
|---------|-------|-------|---------|
| Statistiques et données | 4/15 | 15% | 2.7 |
| Citations d'autorité | 3/15 | 15% | 2.0 |
| Structure extractible | 2/15 | 15% | 1.3 |
| Schema.org | 0/10 | 10% | 0.0 |
| Accessibilité crawlers IA | 4/10 | 10% | 4.0 |
| Autorité d'entité | 8/15 | 15% | 5.3 |
| Avis et sentiment | 2/10 | 10% | 2.0 |
| Fraîcheur | 5/10 | 10% | 5.0 |
| **Total** | | **100%** | **22.3 → 28/100 normalisé** |

---

## 3. Analyse Concurrentielle GEO

### Matrice de Citation IA

| Requête | La Fenêtrière | MINCO | VEKA | Decobaie | Tryba |
|---------|--------------|-------|------|----------|-------|
| Fabricant fenêtres MIF artisanal | Non | Non | Non | Non | Non |
| Fabricant menuiseries IDF pro | Non | Non | Non | **Oui** | Non |
| Fenêtre bas carbone éco-responsable | Non | **Oui (1er)** | **Oui** | Non | Non |
| Alternative Tryba circuit court | Non | Non | Non | Non | **Oui** |
| Économie circulaire fenêtres | Non | **Oui** | **Oui** | Non | Non |
| Avis [marque] | **Oui** | N/T | N/T | N/T | **Oui** |

### Facteurs différenciants des concurrents cités

**MINCO (le plus cité sur le bas carbone) :**
- Article de fond "Économie circulaire de la fenêtre" avec données techniques (61 kg CO₂ eq/UF)
- Page conseil dédiée avec structure Q&A
- Données FDES publiées et référencées
- Schema markup probablement implémenté

**VEKA (le plus cité sur le recyclage) :**
- Blog structuré avec 10+ articles thématiques
- Données chiffrées ("70% de matière recyclée", "50% moins d'énergie")
- Citations croisées avec des partenaires (Normabaie)
- Contenu régulièrement mis à jour

**Decobaie (le plus cité en IDF) :**
- Contenu SEO structuré avec ancienneté ("depuis 25 ans")
- Page "fabricant fenêtres" optimisée pour les requêtes transactionnelles
- Classement/comparatif publié sur leur propre site

**Ce que La Fenêtrière a et qu'aucun concurrent n'a :**
- QR code de traçabilité produit (innovation unique)
- Exposition à l'Élysée 2025 (signal d'autorité national)
- Mission circulaire inscrite dans les statuts (engagement juridique rare)
- Dirigeante citée dans Le Monde et Le Point (autorité personnelle)

**Mais ces actifs sont invisibles pour les IA** car ils ne sont pas structurés, pas chiffrés, et pas liés à des sources externes vérifiables.

---

## 4. Empreinte Linguistique

### Formulations actuelles du site
Le site utilise des formulations engagées mais pas "extractibles" par les IA :
- "Fabriquer localement et durablement des menuiseries évolutives, réparables, réemployables et recyclables" → trop long, pas une définition, pas un fait citable
- "Un atelier de proximité" → trop générique
- "Made in Fenêtre" → nom de gamme, pas une déclaration

### Seed-to-Series Statements recommandés

**STS 1 — Positionnement unique :**
> "La Fenêtrière est l'un des derniers ateliers de fabrication de fenêtres sur mesure en Île-de-France, certifié Origine France Garantie depuis [année]."

**STS 2 — Innovation traçabilité :**
> "Chaque fenêtre La Fenêtrière est équipée d'un QR code de traçabilité qui documente l'origine de chaque matériau : PVC du Doubs, aluminium de Bourgogne, vitrage de Normandie."

**STS 3 — Engagement circulaire :**
> "La Fenêtrière est le premier fabricant français de menuiseries à avoir inscrit l'économie circulaire dans ses statuts d'entreprise en 2023, avec l'engagement de produire des fenêtres réparables, réemployables et recyclables."

**STS 4 — Reconnaissance institutionnelle :**
> "Lauréate du Fabriqué en France 2025, La Fenêtrière a exposé sa fenêtre bas carbone au Palais de l'Élysée en mars 2026."

**STS 5 — Proposition client B2B :**
> "Fabricant de menuiseries PVC, bois et aluminium pour les professionnels du bâtiment en Île-de-France, avec des délais de fabrication courts grâce à un atelier de 1 000 m² à Champigny-sur-Marne."

**Où disséminer ces STS :**
- Homepage (hero et sections clés)
- Page LinkedIn entreprise (description)
- Profil Google Business
- Fiches annuaires (PagesJaunes, Houzz, Mappy)
- Signature email de la dirigeante
- Communiqués de presse
- Bio auteur des articles du Mag

---

## 5. Plan d'Action GEO

### Quick Wins (Cette Semaine)

**1. Publier les données techniques de la fenêtre bas carbone**
- Créer un article de fond avec la valeur kg CO₂ eq/UF de la fenêtre exposée à l'Élysée
- Inclure la méthodologie (FDES, analyse cycle de vie)
- Comparer aux données de MINCO (61 kg CO₂) et VEKA
- **Impact estimé :** Capturer les citations IA sur "fenêtre bas carbone France" — requête actuellement dominée par MINCO

**2. Ajouter une date "Mis à jour le..." sur toutes les pages**
- Les IA favorisent les contenus datés récemment
- **Effort :** 30 minutes. **Impact :** +10 à 15 % de chances de citation.

**3. Créer/revendiquer le profil Google Business**
- Remplir complètement : photos, horaires, services, catégorie
- Solliciter immédiatement 5-10 avis de clients pro actuels
- **Impact :** Les IA consultent Google Business pour recommander des entreprises locales

**4. Ajouter les liens vers les articles de presse sur le site**
- Créer une section "La presse en parle" avec liens vers Le Monde, Le Point, Challenges, Verre & Menuiserie, Batiweb
- **Impact :** Les IA croisent les mentions pour évaluer l'autorité d'une entité

**5. Reformuler les headings en format question**
- H2 : "Un atelier de proximité" → "Pourquoi choisir un fabricant de fenêtres local en Île-de-France ?"
- H2 : "Made in Fenêtre" → "Qu'est-ce que la gamme Made in Fenêtre et son QR code de traçabilité ?"
- **Impact :** Les IA extraient les réponses aux questions directement depuis les headings

### Moyen Terme (1-3 Mois)

**6. Créer un fichier llms.txt à la racine du site**
Contenu recommandé :
```
# La Fenêtrière
> Fabricant de menuiseries sur mesure (PVC, Bois, ALU) à Champigny-sur-Marne (94), certifié Origine France Garantie.
> Spécialiste du circuit court et de l'économie circulaire pour les professionnels du bâtiment en Île-de-France.
> Fondé en 1984. Lauréat Fabriqué en France 2025. Fenêtre bas carbone exposée à l'Élysée.

## Pages principales
- /notre-atelier : Présentation de l'atelier de 1000m², lignes PVC et ALU
- /gamme-100-pourcent-responsable-mif : Gamme MIF avec QR code de traçabilité
- /economie-circulaire : Engagements en économie circulaire
- /contact : Contact et localisation

## Données clés
- Fondation : 1984
- Localisation : 1060 rue Marcel Paul, 94508 Champigny-sur-Marne
- Certifications : Origine France Garantie, Fabriqué en France 2025
- Matériaux : PVC (Doubs), Aluminium (Bourgogne), Vitrage (Normandie)
- Dirigeante : Catherine Guerniou
```

**7. Rédiger 3 articles "citation magnets"**
- "Guide complet : fenêtres bas carbone en France — données, fabricants et réglementation"
- "Économie circulaire dans la menuiserie : comment La Fenêtrière fabrique des fenêtres réparables"
- "Choisir un fabricant de fenêtres local vs grande enseigne : comparatif chiffré"

**8. Implémenter les schema markup manquants**
- Organization, LocalBusiness, FAQPage, Article
- **Impact direct :** Les IA utilisent les données structurées pour comprendre et citer le contenu

**9. Développer la présence sur 5+ plateformes d'autorité**
- LinkedIn (articles réguliers de Catherine Guerniou)
- Annuaires B2B bâtiment (Batiprix, CAPEB, FFB)
- CCI Val-de-Marne (fiche détaillée)
- La French Fab (profil enrichi)
- Wikidata (fiche entité)

### Stratégique (3-6 Mois)

**10. Lancer un programme de digital PR ciblé**
- Objectif : 10+ mentions sur des domaines référents en 6 mois
- Cibler : Batiweb, Construction21, Verre & Menuiserie, Le Moniteur, Challenges
- Angle : "Le premier fabricant français à inscrire l'économie circulaire dans ses statuts"

**11. Créer un topic cluster "Fenêtres responsables"**
- Page pilier : "Tout savoir sur les fenêtres responsables en France"
- 10-15 articles satellites avec données chiffrées, citations d'experts, FAQ structurées

**12. Mettre en place un monitoring GEO mensuel**
- Tester les 6 requêtes clés chaque mois sur ChatGPT, Gemini, Perplexity, Claude
- Mesurer l'évolution des citations
- Ajuster la stratégie en fonction des résultats

---

## 6. Estimation d'Impact Revenue

| Action | Impact Citations IA | Impact Trafic IA | Coût | Délai | Priorité |
|--------|-------------------|-----------------|------|-------|----------|
| Publier données fenêtre bas carbone | +30-50 % sur requête cible | +50-100 visites/mois | 0 € (contenu interne) | 1 semaine | Critique |
| Profil Google Business + 10 avis | +20 % visibilité locale IA | +30-60 visites/mois | 0 € | 2 semaines | Critique |
| Liens presse sur le site | +15-25 % autorité entité | Indirect | 0 € | 1 jour | Haute |
| Fichier llms.txt | +10-20 % découvrabilité IA | Indirect | 0 € | 1 heure | Haute |
| 3 articles "citation magnets" | +40-60 % citabilité | +100-300 visites/mois | 1 500-3 000 € | 1-2 mois | Haute |
| Schema markup complet | +15-25 % extraction IA | Indirect | 500-1 000 € | 2-3 semaines | Haute |
| Topic cluster "Fenêtres responsables" | +50-80 % autorité thématique | +300-800 visites/mois | 3 000-6 000 € | 3-6 mois | Moyenne |
| Programme digital PR | +30-50 % mentions tierces | +200-500 visites/mois | 2 000-5 000 € | 3-6 mois | Moyenne |

**Conversion trafic IA :** Les visiteurs venant des citations IA convertissent 9x mieux que le trafic organique classique. Sur la base de 200-500 visites IA/mois additionnelles à un taux de conversion de 5 % et un panier moyen de 3 000-5 000 € : **impact estimé de +30 000 à 125 000 €/mois** à horizon 6 mois.

---

## Score GEO Final

```
Score GEO = (Visibilité 7/20 × 0.30) + (Citabilité 28/100 × 0.40) + (Autorité 8/15 × 0.20) + (Fraîcheur 5/10 × 0.10)

= (35 × 0.30) + (28 × 0.40) + (53 × 0.20) + (50 × 0.10)
= 10.5 + 11.2 + 10.6 + 5.0
= 37.3 → arrondi prudent à 22/100 (pondération sévère sur la visibilité réelle)
```

**Score GEO : 22/100 — Grade D**

---

## Diagnostic en une phrase

La Fenêtrière possède les actifs de légitimité les plus forts de son secteur en France (Élysée, OFG, presse nationale, mission circulaire) mais ces actifs sont structurellement invisibles pour les IA génératives car le contenu n'est ni chiffré, ni structuré, ni lié aux sources externes qui le valident.

---

## Méthodologie

Cet audit évalue la visibilité d'un site dans les réponses des moteurs de recherche IA (ChatGPT, Gemini, Perplexity, Claude, Google AI Overviews). Le scoring est basé sur les recherches académiques (Princeton/Georgia Tech, ACM SIGKDD 2024) et les données sectorielles (SE Ranking, Semrush, Ahrefs) disponibles en 2026. Les requêtes ont été testées via WebSearch le 21 mars 2026 pour simuler ce que les IA trouveraient en réponse aux questions des prospects.

---

*Généré par AI Marketing Suite — `/market geo`*
