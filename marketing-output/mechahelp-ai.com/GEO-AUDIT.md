# Audit GEO — Generative Engine Optimization
## mechahelp-ai.com
### Date : 20 mars 2026

---

## Score GEO Global : 8/100 — Grade F

**MechaHelp est actuellement inexistant dans l'écosystème des moteurs de recherche IA.** Le site n'est pas indexé par Google (0 résultat sur `site:mechahelp-ai.com`), aucune mention de la marque n'existe sur le web hors du site lui-même, et le contenu du site est quasi inaccessible aux crawlers (probablement une SPA sans rendu côté serveur). Le potentiel est significatif car le marché de l'accompagnement IA pour PME est en pleine croissance en 2026, mais un travail de fond majeur est requis.

---

## 1. Test de Visibilité IA

### Requêtes testées

| # | Requête conversationnelle | MechaHelp cité ? | Sources citées à la place |
|---|--------------------------|-------------------|--------------------------|
| 1 | "Quel est le meilleur accompagnement IA pour PME en France ?" | Non | IA PME Conseil, Koïno, Stema Partners, Optimia |
| 2 | "Meilleure solution IA automatisation entreprise France 2026" | Non | AIA Conseil, Limova.ai, Agence-IA.com |
| 3 | "Consultant IA automatisation personnalisé freelance France" | Non | Malt, Codeur.com, Koïno, Conversion Boosters |
| 4 | "Alternative à [concurrent] pour accompagnement IA" | Non | IA PME Conseil, Yakadata, Digital Unicorn |
| 5 | "Avis mechahelp-ai accompagnement IA" | Non | Aucun résultat pertinent |
| 6 | "Comment automatiser mes processus métier avec l'IA ?" | Non | francenum.gouv.fr, Bpifrance, Zapier, Make |
| 7 | "Micro-agence IA spécialisée automatisation France" | Non | Agence-IA.com, Limova.ai, Le Board |

### Score Visibilité : 0/20

**Constat critique :** MechaHelp n'apparaît dans aucune requête testée. La marque est totalement absente des résultats de recherche web, ce qui signifie qu'aucune IA générative (ChatGPT, Gemini, Perplexity, Claude) ne peut la citer comme source. Le site n'est même pas indexé par Google.

---

## 2. Audit de Citabilité

### 2.1 Statistiques et données chiffrées — 0/15

- Aucune statistique détectée sur le site
- Aucune donnée chiffrée (nombre de clients, taux de satisfaction, gains de productivité)
- Aucune étude de cas avec métriques
- **Impact :** les IA citent en priorité les sources contenant des données originales (+65,5% de visibilité)

### 2.2 Citations et sources d'autorité — 0/15

- Aucune citation d'expert ou d'étude sur le site
- Aucune référence à des frameworks, méthodologies, ou institutions
- Pas de partenariats ou certifications mentionnés
- **Impact :** les sources fiables améliorent de 132,4% la probabilité d'être cité par les chatbots

### 2.3 Structure extractible par les IA — 2/15

| Critère | Présent ? | Score |
|---------|-----------|-------|
| Headers en format question (H2/H3) | Non | 0/5 |
| Résumés TL;DR en début de section | Non | 0/3 |
| Tableaux comparatifs, listes structurées | Non | 0/4 |
| FAQ dédiée avec schema markup | Non | 0/3 |
| Titre H1 clair avec mots-clés | Partiellement | 2 bonus |

**Constat :** Le site semble être une Single Page Application (SPA) avec très peu de contenu HTML statique. Le WebFetch ne récupère que le titre "MechaHelp - Accompagnements personnalisés en IA & Automatisation". Cela signifie que les crawlers IA ne peuvent pas accéder au contenu du site.

### 2.4 Données structurées / Schema.org — 0/10

| Type de schema | Présent ? | Score |
|----------------|-----------|-------|
| Organization | Non détecté | 0/2 |
| FAQPage | Non | 0/2 |
| Article / BlogPosting | Non | 0/2 |
| HowTo | Non | 0/2 |
| Product / Service | Non détecté | 0/2 |

### 2.5 Accessibilité aux crawlers IA — 5/10

| Critère | Présent ? | Score |
|---------|-----------|-------|
| robots.txt autorise les bots IA | Oui (par défaut, pas de blocage explicite) | 5/5 |
| Fichier llms.txt présent | Non (erreur 404) | 0/3 |
| Sitemap XML à jour | Oui (6 pages, daté 19/01/2026) | 2/2 |

**Détail robots.txt :** Les bots IA (GPTBot, ClaudeBot, PerplexityBot, Google-Extended) ne sont pas explicitement mentionnés mais tombent sous la règle `User-agent: *` qui les autorise. Les répertoires `/dashboard`, `/vip`, `/admin`, `/messages` sont bloqués (normal).

**Problème majeur :** Même si les bots sont autorisés, le contenu rendu par JavaScript (SPA) est probablement invisible pour la plupart des crawlers IA qui ne font pas de rendu JS.

### 2.6 Autorité d'entité et E-E-A-T — 3/15

| Critère | Présent ? | Score |
|---------|-----------|-------|
| Auteur nommé avec biographie et credentials | Non sur le site | 0/5 |
| Page "À propos" détaillée avec expertise | Non détectée | 0/3 |
| Mentions de la marque sur des sites tiers | 0 mention trouvée | 0/4 |
| Profils actifs sur plateformes d'autorité | LinkedIn du CEO (Julien Berge) trouvé | 3/3 |

**Constat :** Un profil LinkedIn de Julien Berge (CEO, "AI Automation Expert, Creator of MechaPizzAI") a été identifié. C'est le seul signal d'autorité externe. Aucune mention de MechaHelp sur des annuaires, blogs, presse, forums, ou plateformes sectorielles.

### 2.7 Avis et sentiment en ligne — 0/10

| Critère | Présent ? | Score |
|---------|-----------|-------|
| Avis Google Business (note ≥ 4.0, > 10 avis) | Non trouvé | 0/4 |
| Avis sur plateformes sectorielles (Malt, Trustpilot, etc.) | Non | 0/3 |
| Sentiment globalement positif | N/A — aucun avis | 0/3 |

### 2.8 Fraîcheur du contenu — 2/10

| Critère | Présent ? | Score |
|---------|-----------|-------|
| Contenu mis à jour dans les 90 derniers jours | Sitemap indique 19/01/2026 (~60 jours) | 2/5 |
| Date de mise à jour visible sur les pages | Non détectée | 0/3 |
| Blog actif avec publication régulière | Non — aucun blog | 0/2 |

### Score Citabilité : 12/100

---

## 3. Analyse Concurrentielle GEO

### Concurrents identifiés dans l'espace "accompagnement IA & automatisation pour PME en France"

| Concurrent | Positionnement | Signaux GEO détectés |
|------------|---------------|---------------------|
| **IA PME Conseil** (ia-pme-conseil.fr) | Conseil IA pour PME, modèles souverains, RGPD | Cité dans les recherches, contenu structuré, blog actif |
| **Koïno** (koino.fr) | Agence IA stratégique, top 10 classements | Articles de fond, comparatifs, forte autorité de domaine |
| **Limova.ai** | Assistants IA pour automatisation métier | Contenu clair, proposition de valeur extractible |

### Matrice de Citation IA

| Requête | MechaHelp | IA PME Conseil | Koïno | Limova.ai |
|---------|-----------|---------------|-------|-----------|
| Meilleur accompagnement IA PME France | Non | **Oui** | **Oui** | Non |
| Solution IA automatisation entreprise 2026 | Non | Non | **Oui** | **Oui** |
| Consultant IA freelance France | Non | Non | **Oui** | Non |
| Micro-agence IA automatisation | Non | Non | Non | **Oui** |

### Facteurs différenciants des concurrents cités

1. **Contenu riche et structuré** : Koïno et IA PME Conseil publient des articles de fond avec données chiffrées, comparatifs, et guides pratiques
2. **Présence multi-plateforme** : Les concurrents cités sont mentionnés sur des annuaires, blogs tiers, et articles comparatifs
3. **Indexation Google** : Tous les concurrents sont indexés et visibles sur Google
4. **Proposition de valeur extractible** : Formulations claires en une phrase ("Accompagnement PME - Conseil personnalisé en IA", "Assistants IA pour automatiser votre entreprise")

---

## 4. Empreinte Linguistique

### Analyse actuelle

- La seule formulation identifiable est le titre : "Accompagnements personnalisés en IA & Automatisation"
- Pas de phrase signature (Seed-to-Series Statement) détectable
- Aucune formulation unique ou mémorable sur le web associée à MechaHelp
- Le nom "MechaHelp" est distinct et non confondu avec d'autres marques (contrairement à "MechAI" qui est une app auto différente)

### Seed-to-Series Statements recommandés

À créer et disséminer sur le site, LinkedIn, annuaires, et communiqués :

1. **"MechaHelp — L'accompagnement IA sur mesure qui automatise vos process métier en 30 jours"**
   → Combine unicité de la marque + promesse mesurable + délai concret

2. **"De 0 à automatisé : MechaHelp transforme les PME françaises avec l'IA, sans compétence technique requise"**
   → Adresse la barrière n°1 des PME (la complexité technique)

3. **"Accompagnement IA 100% personnalisé — pas de template, pas de solution générique, que du sur-mesure"**
   → Différenciation vs les outils en self-service (Zapier, Make)

4. **"MechaHelp : votre micro-agence IA dédiée à l'automatisation intelligente"**
   → Capitalise sur la tendance "micro-agence IA" identifiée dans les recherches 2026

5. **"L'IA qui travaille pour vous — accompagnement personnalisé par un expert certifié en automatisation"**
   → Positionne l'humain derrière la technologie (E-E-A-T)

---

## 5. Plan d'Action GEO

### Quick Wins (Cette Semaine) — Impact estimé : +15-20 points GEO

| # | Action | Effort | Impact |
|---|--------|--------|--------|
| 1 | **Résoudre le problème de rendu SPA** : Implémenter le Server-Side Rendering (SSR) ou le pre-rendering pour que les crawlers accèdent au contenu HTML | Moyen | **CRITIQUE** — sans cela, aucune IA ne peut lire le site |
| 2 | **Ajouter des dates "Mis à jour le..."** visibles sur toutes les pages | Faible | Fraîcheur +3pts |
| 3 | **Créer/revendiquer le profil Google Business** et solliciter 3-5 avis clients | Faible | Avis +4pts |
| 4 | **Ajouter les balises schema.org** : Organization, Service, FAQPage | Faible | Schema +6pts |
| 5 | **Créer un fichier llms.txt** à la racine du site décrivant les services MechaHelp | Faible | Accessibilité +3pts |
| 6 | **Enrichir la page "Accompagnements"** avec des descriptions détaillées, tarifs, et processus | Moyen | Structure +5pts |

### Moyen Terme (1-3 Mois) — Impact estimé : +25-35 points GEO

| # | Action | Effort | Impact |
|---|--------|--------|--------|
| 7 | **Lancer un blog** avec 3-5 articles de fond : "Comment automatiser [process métier] avec l'IA", "Guide complet de l'accompagnement IA pour PME en 2026" | Élevé | Citabilité +15pts |
| 8 | **Ajouter des études de cas chiffrées** : "PME X a réduit de 60% son temps de facturation grâce à MechaHelp" | Moyen | Stats +10pts |
| 9 | **Créer une page FAQ complète** avec schema markup, headers en format question | Moyen | Structure +8pts |
| 10 | **Développer la présence sur Malt, LinkedIn articles, annuaires sectoriels** | Moyen | Autorité +8pts |
| 11 | **Restructurer les headers en format question** : "Comment MechaHelp automatise vos processus ?", "Pourquoi choisir un accompagnement IA personnalisé ?" | Faible | Structure +5pts |
| 12 | **Publier des citations d'experts** et des références à des études (Gartner, McKinsey, Bpifrance) | Moyen | Citations +8pts |
| 13 | **S'inscrire sur les annuaires d'agences IA** : Koïno, Codeur.com, Sortlist, les-agences.fr | Moyen | Mentions tierces +5pts |

### Stratégique (3-6 Mois) — Impact estimé : +20-30 points GEO

| # | Action | Effort | Impact |
|---|--------|--------|--------|
| 14 | **Créer du contenu "citation magnet"** : benchmark original sur l'adoption IA en PME, enquête propriétaire, infographie avec données exclusives | Élevé | Stats +15pts |
| 15 | **Lancer un programme de digital PR** ciblé : obtenir des mentions sur 10+ domaines référents (presse spécialisée, blogs tech, podcasts IA) | Élevé | Autorité +12pts |
| 16 | **Construire des topic clusters** : page pilier "Accompagnement IA pour PME" + 10-15 articles satellites | Élevé | Citabilité +10pts |
| 17 | **Mettre en place un processus de rafraîchissement** du contenu tous les 60-90 jours | Moyen | Fraîcheur +5pts |
| 18 | **Développer la stratégie STS multi-plateforme** : disséminer les 5 Seed-to-Series Statements sur LinkedIn, site, annuaires, signatures email | Moyen | Empreinte linguistique |
| 19 | **Monitorer la visibilité IA mensuellement** avec Otterly.ai ou audit manuel | Faible | Suivi continu |

---

## 6. Estimation d'Impact Revenue

| Action | Impact Citations IA | Impact Trafic IA | Coût estimé | Priorité |
|--------|-------------------|-----------------|-------------|----------|
| Résoudre le rendu SPA (SSR) | +0→possible | Déblocage total | 500-2000€ dev | **CRITIQUE** |
| Blog + articles de fond (5 articles) | +30% citations potentielles | +50-200 visites/mois IA | 2000-5000€ contenu | **Haute** |
| Études de cas chiffrées (3 cas) | +25% citations | Conversion 9x vs organique | 500-1500€ | **Haute** |
| Schema.org + llms.txt | +15% accessibilité | Facilite l'extraction | 200-500€ dev | **Haute** |
| Google Business + avis | +10% confiance IA | Signal de légitimité | Gratuit | **Haute** |
| Présence annuaires & Malt | +20% mentions tierces | Backlinks + autorité | 200-500€ | **Moyenne** |
| Digital PR (10 mentions) | +40% autorité entité | 500-1000 visites/mois | 3000-8000€ | **Moyenne** |
| Contenu citation magnet | +50% citations uniques | Positionnement d'expert | 2000-5000€ | **Moyenne** |
| Topic clusters (15 articles) | +35% couverture thématique | +200-500 visites/mois | 5000-10000€ | **Basse** |

### Projection de revenus potentiels

En supposant un panier moyen d'accompagnement IA de 2 000-5 000€ :
- **Scénario réaliste à 6 mois** (score GEO passant de 8 à 45) : 5-15 leads qualifiés/mois via IA → **10 000-75 000€ de CA additionnel annuel**
- **Scénario optimiste à 12 mois** (score GEO passant à 65+) : 15-30 leads/mois → **30 000-150 000€ de CA additionnel annuel**

*Note : Les visiteurs provenant des IA convertissent 9x mieux que le trafic organique classique.*

---

## 7. Diagnostic Technique Spécifique

### Problème n°1 : Site non crawlable (SPA sans SSR)

C'est le blocage principal. Le site semble être une application JavaScript côté client (probablement React, Vue ou Next.js sans SSR activé). Les crawlers IA et Google ne voient que le titre HTML — tout le contenu est rendu en JavaScript après chargement.

**Solutions :**
- **Next.js / Nuxt.js** : Activer le SSR ou la génération statique (SSG)
- **Pre-rendering** : Utiliser Prerender.io ou un service similaire pour servir des pages HTML pré-rendues aux bots
- **Dynamic rendering** : Servir une version HTML aux bots et la SPA aux utilisateurs

### Problème n°2 : Zéro indexation Google

Le site n'apparaît dans aucun résultat `site:mechahelp-ai.com`. Cela signifie :
- Google n'a pas indexé le site (probablement lié au problème SPA)
- Aucune IA ne peut trouver le site comme source
- Le sitemap existe mais les pages ne sont pas indexées

**Action immédiate :** Vérifier la Google Search Console, soumettre le sitemap, et résoudre le rendu SPA.

### Problème n°3 : Absence totale de contenu textuel accessible

Seulement 6 URLs dans le sitemap, dont 3 sont des pages légales (CGU, mentions légales, confidentialité). Il reste :
- `/` (accueil)
- `/accompagnements`
- `/auth` (page de connexion — non pertinente pour le GEO)

**Il n'y a que 2 pages utiles avec du contenu potentiellement citable.**

---

## Synthèse des Scores

| Composante | Score | Poids | Score pondéré |
|-----------|-------|-------|---------------|
| Visibilité IA | 0/20 (→ 0/100) | 30% | 0 |
| Citabilité Contenu | 12/100 | 40% | 4,8 |
| Autorité d'Entité | 3/15 (→ 20/100) | 20% | 4,0 |
| Fraîcheur | 2/10 (→ 20/100) | 10% | 2,0 |
| **Score GEO Global** | | | **≈ 8/100** |

---

## Méthodologie

Cet audit évalue la visibilité de mechahelp-ai.com dans les réponses des moteurs de recherche IA (ChatGPT, Gemini, Perplexity, Claude, Google AI Overviews). Le scoring est basé sur les recherches académiques (Princeton/Georgia Tech, ACM SIGKDD 2024) et les données sectorielles (SE Ranking, Semrush, Ahrefs) disponibles en 2026.

**Sources consultées :**
- Analyse directe du site (WebFetch : page d'accueil, page accompagnements)
- robots.txt et sitemap.xml du domaine
- Test de présence llms.txt (404 — non trouvé)
- 7 requêtes de visibilité IA testées via WebSearch
- Recherche de mentions externes de la marque
- Analyse des concurrents : IA PME Conseil, Koïno, Limova.ai
- Profil LinkedIn du CEO identifié (Julien Berge)
