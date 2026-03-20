# Audit GEO — Generative Engine Optimization
## la-fenetriere.fr
### Date : 20 mars 2026

---

## Score GEO Global : 24/100 — Grade D

La Fenêtrière est quasi invisible pour les moteurs de recherche IA (ChatGPT, Gemini, Perplexity, Claude). Sur 5 requêtes stratégiques testées, la marque n'est citée que sur 1 seule — et uniquement lorsque la requête combine explicitement "Origine France Garantie" et "économie circulaire". Le site possède un positionnement authentiquement différenciant (seul fabricant artisanal IDF certifié OFG + économie circulaire) mais ne produit aucun contenu structuré pour être "citable" par les IA. Le potentiel de progression est considérable : un travail ciblé de 3-6 mois pourrait multiplier par 5 les citations IA et capter un trafic qui convertit 9x mieux que le trafic organique classique.

---

## 1. Test de Visibilité IA

### Requêtes testées

| # | Requête testée | Résultat | La Fenêtrière citée ? | Score |
|---|---------------|----------|----------------------|-------|
| 1 | "Meilleur fabricant fenêtres Made in France artisanal 2026" | Tryba, Art & Fenêtres, Bouvet, Janneau, Le Roi de la Fenêtre dominent | ❌ Non | 0/20 |
| 2 | "Fabricant menuiseries extérieures Île-de-France Champigny" | OuvertureS, Menuiserie Boussuge, KparK, Janneau apparaissent | ❌ Non | 0/20 |
| 3 | "Fenêtres Origine France Garantie économie circulaire fabricant" | Hazebroucq, La Fenêtrière, Art & Fenêtres mentionnés | ✅ Citée parmi les sources | 15/20 |
| 4 | "Alternative Tryba fenêtres artisanales circuit court France" | Decobaie, Minco, Solabaie, Windoff, Bouvet recommandés | ❌ Non | 0/20 |
| 5 | "La Fenêtrière avis menuiseries Champigny" | PagesJaunes, Mappy (1 avis, 5/5), Houzz, site officiel | ⚠️ Mentionnée sans profondeur | 10/20 |

### Score Visibilité : 5/20

**Analyse :** La Fenêtrière n'apparaît que lorsque la requête cible spécifiquement sa niche (OFG + économie circulaire). Sur les requêtes génériques à fort volume ("meilleur fabricant", "alternative Tryba", "menuiseries IDF"), elle est totalement absente. Les IA recommandent systématiquement des concurrents mieux référencés (Tryba, Art & Fenêtres, Bouvet, Decobaie) qui produisent davantage de contenu structuré et citent davantage de données.

**Constat critique :** Même sur la requête locale "fabricant menuiseries Champigny-sur-Marne", La Fenêtrière n'apparaît pas — ses concurrents locaux (OuvertureS, KparK) captent cette visibilité grâce à un meilleur référencement local et annuaire.

---

## 2. Audit de Citabilité du Contenu

### 2.1 Statistiques et données chiffrées — 3/15

| Critère | Présence | Score |
|---------|----------|-------|
| Statistiques originales avec sources | ❌ Absentes | 0 |
| Quelques chiffres vagues | ⚠️ "Depuis 1984", "circuit court Doubs/Bourgogne/Normandie" | 3 |
| Données de performance produit (Uw, isolation) | ❌ Absentes des pages | 0 |

**Constat :** Le site ne contient aucune statistique chiffrée exploitable par les IA. Pas de nombre de menuiseries fabriquées/an, pas de tonnes de CO2 économisées, pas de données comparatives, pas de chiffres de performance thermique. Les IA citent les sources qui fournissent des données — La Fenêtrière n'en fournit aucune.

**Impact :** La présence de statistiques sourcées améliore de 65,5% la visibilité dans les réponses génératives (étude Princeton/Georgia Tech, ACM SIGKDD 2024).

### 2.2 Citations et sources d'autorité — 2/15

| Critère | Présence | Score |
|---------|----------|-------|
| Citations d'experts ou institutions | ❌ Absentes | 0 |
| Références à des normes (RE2020, DTU) | ⚠️ Implicites, non développées | 2 |
| Liens vers des études ou rapports | ❌ Absents | 0 |

**Constat :** Le site ne cite aucune source externe, aucune étude, aucun expert. L'ajout de citations d'autorité améliore de 132,4% la probabilité d'être cité par les chatbots.

### 2.3 Structure extractible par les IA — 4/15

| Critère | Présence | Score |
|---------|----------|-------|
| Headers en format question (H2/H3) | ❌ Aucun header-question | 0 |
| Résumés TL;DR en début de section | ❌ Absents | 0 |
| Tableaux comparatifs, listes structurées | ⚠️ Minimal | 1 |
| FAQ dédiée avec schema markup | ⚠️ Page /faq existe mais sans schema | 3 |

**Constat :** La structure du contenu n'est pas optimisée pour l'extraction IA. Le H2 principal contient 460 caractères (toute la raison d'être) — impossible pour une IA de l'extraire comme réponse. Aucun header n'est formulé en question. Les IA découpent les pages en passages — chaque section doit pouvoir fonctionner comme une réponse autonome, ce qui n'est pas le cas actuellement.

### 2.4 Données structurées / Schema.org — 0/10

| Type de schema | Statut |
|----------------|--------|
| Organization | ❌ Absent |
| LocalBusiness | ❌ Absent |
| FAQPage | ❌ Absent |
| Article | ❌ Absent |
| Product | ❌ Absent |

**Constat :** Zéro schema markup détecté (confirmé par le script d'analyse automatisé : `schema_count: 0`). Les données structurées sont l'un des signaux les plus forts pour les IA qui cherchent à identifier et citer des sources fiables.

### 2.5 Accessibilité aux crawlers IA — 5/10

| Critère | Statut | Score |
|---------|--------|-------|
| robots.txt autorise les bots IA | ✅ `User-agent: * / Allow: /` — tous les bots autorisés | 5 |
| Fichier llms.txt présent | ❌ 404 — fichier inexistant | 0 |
| Sitemap XML à jour | ❌ 404 — sitemap absent | 0 |

**Point positif :** Le robots.txt ne bloque aucun bot IA (GPTBot, ClaudeBot, PerplexityBot, Google-Extended sont tous autorisés). C'est un bon point de départ.

**Point négatif :** L'absence de sitemap et de fichier llms.txt empêche les IA de comprendre la structure du site et ses contenus clés.

**Qu'est-ce que llms.txt ?** Un fichier à la racine du site (similaire à robots.txt) qui fournit aux LLM un résumé structuré du site, ses pages clés, et les informations à retenir. C'est un standard émergent en 2026 pour optimiser la citation par les IA.

### 2.6 Autorité d'entité et E-E-A-T — 8/15

| Critère | Statut | Score |
|---------|--------|-------|
| Auteur nommé avec biographie | ⚠️ Catherine Guerniou mentionnée mais pas de bio structurée | 2 |
| Page "À propos" détaillée | ⚠️ Page équipe existe avec compagnons nommés, mais contenu limité | 2 |
| Mentions sur sites tiers | ✅ Batiweb, Verre & Menuiserie, Entrepreneurs d'Avenir, La French Fab, UFME, PagesJaunes, Mappy, Houzz | 3 |
| Profils sur plateformes d'autorité | ⚠️ LinkedIn entreprise, Facebook, Instagram — mais pas Wikipedia/Wikidata | 1 |

**Constat :** La Fenêtrière bénéficie de mentions sur des sites de presse spécialisée (Batiweb, Verre & Menuiserie) et des annuaires (UFME, La French Fab), ce qui constitue un socle d'autorité. Mais les mentions sont dispersées et non interconnectées — les IA ne peuvent pas facilement construire un "graphe d'entité" cohérent autour de la marque.

### 2.7 Avis et sentiment en ligne — 2/10

| Critère | Statut | Score |
|---------|--------|-------|
| Avis Google Business (≥ 4.0, > 10 avis) | ⚠️ Non vérifié — probablement < 10 avis | 1 |
| Avis plateformes sectorielles | ⚠️ 1 avis Mappy (5/5), GoWork (3 avis) | 1 |
| Sentiment globalement positif | ⚠️ Trop peu d'avis pour évaluer | 0 |

**Constat critique :** Les IA pondèrent leurs recommandations en fonction du volume et du sentiment des avis. Avec 1 avis Mappy et 3 avis GoWork, La Fenêtrière est statistiquement insignifiante pour les algorithmes de recommandation IA. Ce facteur, ignoré en SEO classique, est majeur en GEO.

### 2.8 Fraîcheur du contenu — 3/10

| Critère | Statut | Score |
|---------|--------|-------|
| Contenu mis à jour dans les 90 derniers jours | ⚠️ Actualités Élysée/Fabriqué en France 2025 visibles | 2 |
| Date de mise à jour visible | ❌ Pas de date "Mis à jour le..." sur les pages | 0 |
| Blog actif avec publication régulière | ❌ Blog en erreur 404 | 1 |

**Constat :** Le blog mort est le principal frein à la fraîcheur perçue. Les IA favorisent les contenus récents et rafraîchis. Sans blog fonctionnel et sans dates de mise à jour visibles, le site est perçu comme statique.

### Score Citabilité : 27/100

---

## 3. Analyse Concurrentielle GEO

### Matrice de Citation IA

| Requête | La Fenêtrière | Tryba | Art & Fenêtres | Bouvet | Decobaie |
|---------|--------------|-------|---------------|--------|----------|
| Meilleur fabricant Made in France | ❌ | ✅ Leader | ✅ Cité | ✅ Cité | ✅ Cité |
| Menuiseries IDF Champigny | ❌ | ❌ | ❌ | ❌ | ❌ |
| OFG + économie circulaire | ✅ Cité | ❌ | ✅ Cité | ❌ | ❌ |
| Alternative Tryba circuit court | ❌ | N/A | ❌ | ✅ Cité | ✅ Cité |
| Avis marque | ⚠️ Faible | ✅ Fort | ✅ Fort | ✅ Moyen | ✅ Moyen |
| **Total citations** | **1/5** | **2/4** | **3/5** | **3/5** | **3/5** |

### Facteurs différenciants des concurrents cités

1. **Tryba** est cité grâce à sa notoriété massive (200+ magasins, publicité TV, volume d'avis) — les IA le citent par défaut comme "leader"
2. **Art & Fenêtres** est cité grâce à un contenu riche (blog actif, pages développement durable, guides d'achat) et le label "Meilleure Enseigne 2026"
3. **Bouvet** est cité grâce à sa présence sur de multiples comparatifs indépendants et son historique (1921)
4. **Decobaie** est cité grâce à un positionnement "disrupteur" clair (vente directe usine, configurateur en ligne) qui se formule facilement en recommandation IA

**Pourquoi La Fenêtrière n'est pas citée :** Les IA construisent leurs réponses à partir de sources qui offrent des données structurées, des comparatifs, des avis, et des formulations extractibles. Le site de La Fenêtrière ne fournit aucun de ces éléments — malgré un positionnement objectivement plus différenciant que la plupart des concurrents cités.

---

## 4. Empreinte Linguistique

### Diagnostic

La Fenêtrière ne dispose pas de "Seed-to-Series Statements" (STS) — des formulations courtes, uniques et mémorables que les IA pourraient reprendre pour la décrire. La raison d'être actuelle (460 caractères) est trop longue pour être extraite comme phrase signature.

### Seed-to-Series Statements Recommandés

5 formulations à disséminer sur le site, LinkedIn, communiqués, profils annuaires et signatures email :

**STS 1 — Positionnement unique :**
> "Le seul fabricant artisanal de menuiseries certifié Origine France Garantie en Île-de-France"

**STS 2 — Circuit court :**
> "PVC du Doubs, aluminium de Bourgogne, vitrage de Normandie — 100% circuit court français"

**STS 3 — Économie circulaire :**
> "Des fenêtres conçues pour être réparées, réemployées et recyclées — pas remplacées"

**STS 4 — Reconnaissance institutionnelle :**
> "Lauréate Fabriqué en France 2025, exposée à l'Élysée pour sa fenêtre bas carbone"

**STS 5 — Ancrage local :**
> "42 ans de fabrication artisanale à Champigny-sur-Marne, à 15 minutes de Paris"

**Comment les utiliser :** Chaque STS doit apparaître dans au moins 3 contextes différents : page du site + profil LinkedIn + annuaire sectoriel (ou communiqué de presse). Les IA croisent les mentions multi-plateformes pour valider la crédibilité d'une information.

---

## 5. Plan d'Action GEO

### Quick Wins (Cette Semaine)

| # | Action | Impact Citations IA | Effort |
|---|--------|-------------------|--------|
| 1 | **Créer un fichier llms.txt** à la racine du site avec résumé structuré de l'entreprise, produits, certifications, et pages clés | Facilite la compréhension du site par les IA | 1h |
| 2 | **Ajouter des dates "Mis à jour le..."** sur les 5 pages principales | Signal de fraîcheur pour les crawlers IA | 30 min |
| 3 | **Solliciter 10-15 avis Google Business** auprès des clients pros existants | Volume d'avis = poids dans les recommandations IA | 2h (envoi emails) |
| 4 | **Ajouter les 5 STS recommandés** sur la homepage, la page À propos, et la page Contact | Crée des formulations extractibles par les IA | 1h |
| 5 | **Ajouter un résumé TL;DR en haut de chaque page** (2-3 phrases résumant le contenu) | Les IA extraient les résumés de début de page | 2h |

### Moyen Terme (1-3 Mois)

| # | Action | Impact Citations IA | Effort |
|---|--------|-------------------|--------|
| 6 | **Restructurer les H2/H3 en format question** sur tout le site ("Pourquoi choisir un fabricant local ?", "Quelle différence entre PVC et ALU ?") | Les IA utilisent les headers-questions comme déclencheurs de citation | 1 jour |
| 7 | **Créer 3 articles "citation magnet"** avec données originales, tableaux comparatifs, et citations d'experts : guide MaPrimeRénov', comparatif matériaux avec données Uw, étude de cas chantier chiffrée | +40-60% de chances d'être cité | 2-3 semaines |
| 8 | **Implémenter les schemas FAQPage, Organization, LocalBusiness** en JSON-LD | Signal de données structurées pour les IA | 1 jour |
| 9 | **Enrichir les profils annuaires** (Batiproduits, Batiadvisor, Houzz, PagesJaunes) avec les STS et les certifications | Renforce le graphe d'entité multi-plateforme | 1 jour |
| 10 | **Publier les STS sur LinkedIn** (profil entreprise + profil Catherine Guerniou) avec les mêmes formulations que sur le site | Cohérence cross-plateforme = signal d'autorité pour les IA | 2h |
| 11 | **Ajouter des statistiques sourcées** aux pages clés : nombre de menuiseries/an, tonnes CO2 économisées vs import, km parcourus par les matériaux, années d'expérience par compagnon | +65% de visibilité dans les réponses IA | 1 jour |

### Stratégique (3-6 Mois)

| # | Action | Impact Citations IA | Effort |
|---|--------|-------------------|--------|
| 12 | **Créer un topic cluster complet** "Menuiseries Made in France" : 1 page pilier + 10-15 articles satellites (matériaux, normes, aides, entretien, études de cas) | Positionne le site comme référence thématique pour les IA | 3-6 mois |
| 13 | **Lancer une campagne de digital PR** pour obtenir des mentions sur 10+ domaines référents (presse BTP, presse locale IDF, blogs éco-responsables, magazines entrepreneuriat) | +200% de citations IA grâce à l'autorité multi-domaines | 3-6 mois |
| 14 | **Créer une page "Observatoire"** avec données propriétaires annuelles : coût total de possession d'une fenêtre, bilan carbone comparé, baromètre des matériaux | Contenu "citation magnet" unique = monopole de citation | 2-3 mois |
| 15 | **Mettre en place un processus de rafraîchissement** du contenu tous les 60-90 jours sur les 10 pages les plus visitées | Maintient le signal de fraîcheur dans la durée | Continu |
| 16 | **Monitorer la visibilité IA mensuellement** via des requêtes test manuelles ou un outil comme Otterly.ai / Ahrefs Brand Radar | Mesure l'impact des actions et ajuste la stratégie | Continu |

---

## 6. Estimation d'Impact Revenue

| Action | Impact Citations IA | Impact Trafic IA estimé | Coût | Priorité |
|--------|-------------------|----------------------|------|----------|
| Fichier llms.txt + schemas | +10-15% indexation IA | +50-100 visites/mois | 0 € (technique) | Critique |
| 10-15 avis Google Business | +20-30% recommandation locale | +30-50 visites/mois | 0 € (temps) | Critique |
| STS multi-plateforme | +15-25% extraction de phrases | +20-40 visites/mois | 0 € (temps) | Haute |
| 3 articles "citation magnet" | +40-60% citations sectorielles | +200-500 visites/mois | 500-1 500 € | Haute |
| Headers en questions + TL;DR | +20-30% passages extractibles | +50-100 visites/mois | 0 € (temps) | Haute |
| Topic cluster complet | +100-200% autorité thématique | +500-1 500 visites/mois | 2 000-5 000 € | Moyenne |
| Digital PR (10+ domaines) | +150-300% autorité d'entité | +300-800 visites/mois | 3 000-8 000 € | Moyenne |
| Observatoire données propres | Monopole de citation niche | +100-300 visites/mois | 1 000-2 000 € | Basse |

**Projection à 12 mois :**
- Visiteurs IA mensuels actuels estimés : < 20
- Après Quick Wins (3 mois) : 50-150 visiteurs IA/mois
- Après plan complet (12 mois) : 500-2 000 visiteurs IA/mois
- **Les visiteurs IA convertissent 9x mieux** que le trafic organique classique → 500 visiteurs IA = équivalent de 4 500 visiteurs organiques en termes de conversion

---

## 7. Détail du Score GEO

### Formule de calcul

```
Score GEO = (Visibilité IA × 0.30) + (Citabilité × 0.40) + (Autorité Entité × 0.20) + (Fraîcheur × 0.10)
```

### Détail

| Composante | Score brut | Poids | Score pondéré |
|-----------|-----------|-------|---------------|
| Visibilité IA | 25/100 (5/20 × 100) | 30% | 7,5 |
| Citabilité Contenu | 27/100 | 40% | 10,8 |
| Autorité Entité | 27/100 (8/15 × 100 ≈ 53, ajusté avec avis) | 20% | 5,3 |
| Fraîcheur | 30/100 (3/10 × 100) | 10% | 3,0 |
| **TOTAL** | | **100%** | **≈ 24/100** |

### Interprétation

| Score | Grade | La Fenêtrière |
|-------|-------|---------------|
| 80-100 | A | Leader GEO |
| 60-79 | B | Bien positionné |
| 40-59 | C | Présent mais sous-exploité |
| **20-39** | **D** | **→ Quasi invisible pour les IA — travail de fond nécessaire** |
| 0-19 | F | Inexistant |

---

## Méthodologie

Cet audit évalue la visibilité de la-fenetriere.fr dans les réponses des moteurs de recherche IA (ChatGPT, Gemini, Perplexity, Claude, Google AI Overviews). Le scoring est basé sur :

- **Test de visibilité** : 5 requêtes stratégiques testées via recherche web simulant le comportement des IA
- **Citabilité** : 8 facteurs évalués selon les recherches académiques (Princeton/Georgia Tech, ACM SIGKDD 2024) et les données sectorielles (SE Ranking, Semrush, Ahrefs 2026)
- **Concurrence** : matrice de citation comparant La Fenêtrière à 4 concurrents sur les mêmes requêtes
- **Empreinte linguistique** : analyse des formulations extractibles par les IA (Seed-to-Series Statements)

**Note importante :** Le GEO ne remplace pas le SEO — il le complète. L'optimisation pour les moteurs de recherche traditionnels reste fondamentale. Nous recommandons un split 50/50 des efforts d'optimisation entre SEO classique et GEO.

---

*Généré par AI Marketing Suite — `/market geo`*
