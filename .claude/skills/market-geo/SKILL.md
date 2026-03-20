# Audit GEO — Generative Engine Optimization

## Skill Purpose
Analyser la visibilité d'un site web dans les réponses des moteurs de recherche IA (ChatGPT, Gemini, Perplexity, Claude, Google AI Overviews). Produire un audit complet avec score GEO, constats, et plan d'action priorisé pour être cité par les IA génératives.

## When to Use
- L'utilisateur veut savoir si son site est cité par les IA
- L'utilisateur demande un audit GEO, un audit de visibilité IA, ou une analyse de présence dans les chatbots
- Triggered by `/market geo` or `/market geo <url>`
- Complémentaire au SEO : le SEO optimise pour Google, le GEO optimise pour ChatGPT/Gemini/Perplexity/Claude

## Contexte : Pourquoi le GEO est critique en 2026

- ChatGPT : 800M+ utilisateurs hebdomadaires, 2,5 milliards de requêtes/jour
- Google AI Overviews : présents sur 55%+ des résultats de recherche
- Moins de 10% des sources citées par les IA recoupent le top 10 Google
- Le trafic organique pourrait chuter de 25% d'ici fin 2026 (Gartner)
- Les visiteurs venant des IA convertissent 9x mieux que le trafic organique classique

## Comment Exécuter

### Étape 1 : Test de Visibilité IA (Score sur 100)

Tester la marque sur 4 plateformes IA en posant des requêtes clés liées au secteur du site.

**Méthode :**

1. Identifier 5-10 requêtes stratégiques que les prospects pourraient poser à une IA (formulées en langage conversationnel, pas en mots-clés SEO)
2. Pour chaque requête, utiliser WebSearch pour simuler ce qu'une IA trouverait
3. Évaluer si le site ou la marque apparaîtrait comme source

**Requêtes types à tester :**
- "[secteur] + recommandation" → ex: "quel est le meilleur outil de domotique en France ?"
- "[problème client] + solution" → ex: "comment automatiser mes devis d'artisan ?"
- "[concurrent] + alternative" → ex: "alternative à [concurrent] pour [besoin]"
- "[marque] + avis" → ex: "avis sur [marque]"
- "[secteur] + comparatif" → ex: "comparatif des solutions IA pour PME en France"

**Scoring visibilité :**
| Résultat | Points |
|----------|--------|
| Marque citée en première position | 20 |
| Marque citée parmi les sources | 15 |
| Marque mentionnée sans lien | 10 |
| Secteur couvert mais marque absente | 5 |
| Aucune mention du secteur | 0 |

Score Visibilité = moyenne des scores sur les requêtes testées (sur 20)

### Étape 2 : Audit de Citabilité du Contenu (Score sur 100)

Analyser le site avec WebFetch et évaluer 8 facteurs de citabilité.

#### 2.1 — Statistiques et données chiffrées (Poids : 15%)

| Critère | Score |
|---------|-------|
| Statistiques originales avec sources | 15/15 |
| Statistiques sans sources | 10/15 |
| Quelques chiffres vagues | 5/15 |
| Aucune donnée chiffrée | 0/15 |

La présence de statistiques améliore de 65,5% la visibilité dans les réponses génératives.

#### 2.2 — Citations et sources d'autorité (Poids : 15%)

| Critère | Score |
|---------|-------|
| Citations d'experts, études, institutions | 15/15 |
| Quelques références génériques | 8/15 |
| Aucune citation externe | 0/15 |

L'ajout de sources fiables améliore de 132,4% la probabilité d'être cité par les chatbots.

#### 2.3 — Structure extractible par les IA (Poids : 15%)

| Critère | Score |
|---------|-------|
| Headers en format question (H2/H3) | 5/15 |
| Résumés TL;DR en début de section | 3/15 |
| Tableaux comparatifs, listes structurées | 4/15 |
| FAQ dédiée avec schema markup | 3/15 |

Les IA découpent les pages en passages — chaque section doit pouvoir fonctionner comme une réponse autonome.

#### 2.4 — Données structurées / Schema.org (Poids : 10%)

| Type de schema | Points |
|----------------|--------|
| Organization | 2/10 |
| FAQPage | 2/10 |
| Article / BlogPosting | 2/10 |
| HowTo | 2/10 |
| Product / Service | 2/10 |

#### 2.5 — Accessibilité aux crawlers IA (Poids : 10%)

| Critère | Score |
|---------|-------|
| robots.txt autorise les bots IA (GPTBot, Google-Extended, ClaudeBot, PerplexityBot) | 5/10 |
| Fichier llms.txt présent | 3/10 |
| Sitemap XML à jour | 2/10 |

Vérifier robots.txt pour les directives spécifiques aux bots IA :
- `User-agent: GPTBot` (OpenAI/ChatGPT)
- `User-agent: Google-Extended` (Gemini)
- `User-agent: ClaudeBot` (Anthropic/Claude)
- `User-agent: PerplexityBot` (Perplexity)
- `User-agent: CCBot` (Common Crawl)

#### 2.6 — Autorité d'entité et E-E-A-T (Poids : 15%)

| Critère | Score |
|---------|-------|
| Auteur nommé avec biographie et credentials | 5/15 |
| Page "À propos" détaillée avec expertise | 3/15 |
| Mentions de la marque sur des sites tiers (presse, forums, annuaires) | 4/15 |
| Profils actifs sur plateformes d'autorité (LinkedIn, Wikipedia, Wikidata) | 3/15 |

Les IA évaluent la crédibilité d'une source en croisant les mentions sur plusieurs plateformes.

#### 2.7 — Avis et sentiment en ligne (Poids : 10%)

| Critère | Score |
|---------|-------|
| Avis Google Business (note ≥ 4.0, > 10 avis) | 4/10 |
| Avis sur plateformes sectorielles | 3/10 |
| Sentiment globalement positif | 3/10 |

Les IA pondèrent les recommandations en fonction du sentiment. Ce facteur est ignoré en SEO classique mais majeur en GEO.

#### 2.8 — Fraîcheur du contenu (Poids : 10%)

| Critère | Score |
|---------|-------|
| Contenu mis à jour dans les 90 derniers jours | 5/10 |
| Date de mise à jour visible | 3/10 |
| Blog actif avec publication régulière | 2/10 |

Les IA favorisent les contenus récents. Rafraîchir le contenu clé tous les 60-90 jours.

### Étape 3 : Analyse Concurrentielle GEO

Pour les 3 principaux concurrents identifiés (via `/market competitors` si disponible) :

1. Tester les mêmes 5-10 requêtes stratégiques
2. Comparer qui est cité vs qui ne l'est pas
3. Identifier les facteurs différenciants (contenu plus structuré, plus de données, plus de mentions tierces)

**Matrice de Citation IA :**

| Requête | Client | Concurrent 1 | Concurrent 2 | Concurrent 3 |
|---------|--------|-------------|-------------|-------------|
| [requête 1] | Cité/Non | Cité/Non | Cité/Non | Cité/Non |
| [requête 2] | ... | ... | ... | ... |

### Étape 4 : Empreinte Linguistique (Seed-to-Series)

Identifier les formulations clés que les IA pourraient reprendre pour parler de la marque.

**Analyser :**
- Le site utilise-t-il des formulations uniques et mémorables ?
- Existe-t-il des "phrases signature" (Seed-to-Series Statements) répétées sur le site ET sur les plateformes externes ?
- La proposition de valeur est-elle formulée de manière extractible en une phrase ?

**Exemples de bonnes STS :**
- "Le seul parcours en France combinant film de compétences + handicap + CPF"
- "Devis automatisés en 2 clics — 45 min → 2 min"

**Recommander 3-5 STS** à disséminer sur le site, LinkedIn, communiqués, profils annuaires.

### Étape 5 : Score GEO Global

**Calcul :**
```
Score GEO = (Visibilité IA * 0.30) + (Citabilité Contenu * 0.40) + (Autorité Entité * 0.20) + (Fraîcheur * 0.10)
```

**Interprétation :**
| Score | Grade | Signification |
|-------|-------|---------------|
| 80-100 | A | Leader GEO — votre marque est activement citée par les IA |
| 60-79 | B | Bien positionné — optimisations ciblées pour maximiser les citations |
| 40-59 | C | Présent mais sous-exploité — potentiel important non réalisé |
| 20-39 | D | Quasi invisible pour les IA — travail de fond nécessaire |
| 0-19 | F | Inexistant dans l'écosystème IA — action urgente requise |

### Étape 6 : Plan d'Action GEO Priorisé

#### Quick Wins (Cette Semaine)
Actions à fort impact, faible effort :
- Ajouter des statistiques sourcées aux pages clés
- Renseigner les balises schema.org manquantes (FAQPage, Organization)
- Vérifier/corriger le robots.txt pour les bots IA
- Ajouter une date "Mis à jour le..." visible sur les pages principales
- Créer/revendiquer le profil Google Business et solliciter 3-5 avis

#### Moyen Terme (1-3 Mois)
- Restructurer les headers en format question
- Créer un fichier llms.txt à la racine du site
- Rédiger 3-5 articles de fond avec données originales, citations d'experts, et structure extractible
- Développer la présence sur les plateformes d'autorité (LinkedIn articles, annuaires sectoriels, Malt, etc.)
- Créer des pages FAQ complètes avec schema markup
- Solliciter des mentions dans la presse spécialisée ou des blogs sectoriels
- Publier des études de cas avec métriques chiffrées

#### Stratégique (3-6 Mois)
- Lancer un programme de digital PR ciblé pour obtenir des mentions sur 10+ domaines référents
- Créer du contenu "citation magnet" : études originales, benchmarks sectoriels, données propriétaires
- Construire des topic clusters complets (page pilier + 10-15 articles satellites)
- Mettre en place un processus de rafraîchissement du contenu tous les 60-90 jours
- Monitorer la visibilité IA mensuellement (Otterly.ai, Ahrefs Brand Radar, ou audit manuel)
- Développer une stratégie de Seed-to-Series Statements multi-plateforme

### Étape 7 : Estimation d'Impact

Pour chaque recommandation, estimer :
- L'augmentation potentielle de citations IA
- L'impact sur le trafic référent IA (les visiteurs IA convertissent 9x mieux)
- Le coût et le délai de mise en œuvre
- La priorité (Critique / Haute / Moyenne / Basse)

## Output Format

Générer un fichier `GEO-AUDIT.md` avec :

```markdown
# Audit GEO — Generative Engine Optimization
## [Domaine]
### Date : [Date]

---

## Score GEO Global : [X/100] — Grade [A-F]

[Résumé exécutif 3-4 phrases : état de la visibilité IA, principaux constats, potentiel estimé]

---

## 1. Test de Visibilité IA

### Requêtes testées
[Tableau des requêtes avec résultats par plateforme]

### Score Visibilité : [X/20]

---

## 2. Audit de Citabilité

### 2.1 Statistiques et données — [X/15]
### 2.2 Citations d'autorité — [X/15]
### 2.3 Structure extractible — [X/15]
### 2.4 Schema.org — [X/10]
### 2.5 Accessibilité crawlers IA — [X/10]
### 2.6 Autorité d'entité (E-E-A-T) — [X/15]
### 2.7 Avis et sentiment — [X/10]
### 2.8 Fraîcheur du contenu — [X/10]

### Score Citabilité : [X/100]

---

## 3. Analyse Concurrentielle GEO

[Matrice de citation IA]
[Analyse des facteurs différenciants]

---

## 4. Empreinte Linguistique

### Seed-to-Series Statements recommandés
[3-5 formulations clés à disséminer]

---

## 5. Plan d'Action GEO

### Quick Wins (Cette Semaine)
[Actions avec impact estimé]

### Moyen Terme (1-3 Mois)
[Actions avec impact estimé]

### Stratégique (3-6 Mois)
[Actions avec impact estimé]

---

## 6. Estimation d'Impact Revenue

| Action | Impact Citations IA | Impact Trafic IA | Coût | Priorité |
|--------|-------------------|-----------------|------|----------|
| ... | ... | ... | ... | ... |

---

## Méthodologie

Cet audit évalue la visibilité d'un site dans les réponses des moteurs de recherche IA (ChatGPT, Gemini, Perplexity, Claude, Google AI Overviews). Le scoring est basé sur les recherches académiques (Princeton/Georgia Tech, ACM SIGKDD 2024) et les données sectorielles (SE Ranking, Semrush, Ahrefs) disponibles en 2026.
```

## Key Principles

- Le GEO ne remplace pas le SEO — il le complète. Recommander un split 50/50 des efforts d'optimisation.
- Être premier sur Google ne garantit pas d'être cité par ChatGPT. Les deux systèmes fonctionnent sur des logiques différentes.
- La citabilité est plus importante que le classement. Un contenu cité par une IA est perçu comme une référence dans son domaine.
- Les données originales sont des "aimants à citation" — les IA citent ce que personne d'autre n'a.
- Toujours quantifier : "$X de revenus potentiels" est plus convaincant que "amélioration de la visibilité".
- Le GEO est un travail de fond qui se mesure sur 3-6 mois, pas en jours.

## Integration with Other Skills

- `/market seo` → fondation technique nécessaire au GEO
- `/market brand` → voix de marque et empreinte linguistique
- `/market competitors` → données pour la matrice concurrentielle GEO
- `/market copy` → reformulation des contenus pour la citabilité
- `/market report` et `/market report-pdf` → inclusion des scores GEO dans le rapport final
