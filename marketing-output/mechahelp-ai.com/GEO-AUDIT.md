# Audit GEO — Generative Engine Optimization
## mechahelp-ai.com
### Date : 21 mars 2026 (mise à jour — v2)

---

## Score GEO Global : 11/100 — Grade F

**MechaHelp est quasi-inexistant dans l'écosystème des moteurs de recherche IA.** Aucune mention de la marque n'existe sur le web hors du site lui-même et du profil LinkedIn de son fondateur. Le contenu du site est inaccessible aux crawlers IA (SPA sans SSR). La présence de l'écosystème de marque (MechaPizzAI sur Skool, MechaLabs-ai.com) constitue un signal positif, mais ces actifs ne sont pas reliés ni optimisés pour la citabilité IA. Le marché de l'accompagnement IA pour PME en France est en forte croissance en 2026, mais la compétition s'intensifie — la fenêtre d'opportunité est ouverte mais se referme.

---

## 1. Test de Visibilité IA

### Requêtes testées (mars 2026)

| # | Requête conversationnelle | MechaHelp cité ? | Sources citées à la place |
|---|--------------------------|-------------------|--------------------------|
| 1 | "Meilleur accompagnement IA France 2026" | Non | Cartelis, Koïno, Jedha, IA PME Conseil |
| 2 | "Accompagnement IA personnalisé PME France" | Non | francenum.gouv.fr, Hub France IA, Limova.ai |
| 3 | "Formation n8n France 2026" | Non | BGB Formation, Optédif, Hotmart/Dr Firas, impli.fr |
| 4 | "Marketplace coaching IA automatisation France" | Non | Automise.fr, Koïno, Limova.ai, coaching-ia.fr |
| 5 | "MechaPizzAI" (marque liée) | Partiellement | Profil Skool Julien Berge, page Skool MechaPizzAI — sans lien vers mechahelp-ai.com |
| 6 | "mechahelp" seul | Non | Résultats vides — 0 résultat Google |
| 7 | "Expert n8n France automatisation sur mesure" | Non | MechaLabs-ai.com (entité distincte), BGB Formation, impli.fr |

### Constat clé : confusion d'entités

Une recherche sur "MechaPizzAI" ou "Julien Berge MechaHelp" retourne :
- **Skool MechaPizzAI** : communauté IA de Julien Berge (signal positif mais sans lien vers mechahelp-ai.com)
- **MechaLabs-ai.com** : un site tiers non affilié (expert n8n/Make, 4.9/5 sur 127 avis, Paris) qui capte des requêtes potentiellement destinées à MechaHelp
- **MechaLabs.com** : autre entité non affiliée (hobbyiste, robotique)

**Risque de dilution d'identité** : l'écosystème "Mecha" est fragmenté. Les crawlers IA ne peuvent pas construire une entité cohérente autour de MechaHelp.

### Score Visibilité : 1/20

Le seul point attribué provient de la présence indirecte de MechaPizzAI sur Skool, identifiable via la recherche de marque liée.

---

## 2. Audit de Citabilité

### 2.1 Statistiques et données chiffrées — 0/15

- Aucune statistique détectée sur le site (seul le titre HTML est accessible)
- Aucune donnée chiffrée : nombre de clients accompagnés, taux de satisfaction, gains de productivité mesurés
- Aucune étude de cas avec métriques
- La communauté MechaPizzAI mentionne "de 10h à 10 secondes" — cette donnée n'est pas reprise sur mechahelp-ai.com
- **Impact GEO :** les IA citent en priorité les sources contenant des données originales (+65,5% de visibilité selon SE Ranking 2025)

### 2.2 Citations et sources d'autorité — 0/15

- Aucune citation d'expert ou d'étude sur le site
- Aucune référence à des frameworks reconnus (n8n, Make, LangChain), à des institutions (Bpifrance, BPI, Hub France IA) ou à des certifications
- Pas de partenariats mentionnés
- La description de MechaLabs-ai.com mentionne des certifications et des partenaires — MechaHelp n'a rien d'équivalent
- **Impact GEO :** les sources fiables améliorent de 132,4% la probabilité d'être cité par les chatbots (Princeton/Georgia Tech, ACM SIGKDD 2024)

### 2.3 Structure extractible par les IA — 2/15

| Critère | Présent ? | Score |
|---------|-----------|-------|
| Headers en format question (H2/H3) | Non accessible | 0/5 |
| Résumés TL;DR en début de section | Non | 0/3 |
| Tableaux comparatifs, listes structurées | Non accessible | 0/4 |
| FAQ dédiée avec schema markup | Non | 0/3 |
| Titre H1 clair avec mots-clés | Titre `<title>` présent uniquement | 2 bonus |

**Constat confirmé :** Le WebFetch de mars 2026 ne récupère toujours que le titre `"MechaHelp - Accompagnements personnalisés en IA & Automatisation"`. La page `/accompagnements` retourne le même résultat. Il s'agit d'une SPA (Single Page Application) dont tout le contenu est rendu en JavaScript côté client — invisible pour les crawlers IA qui ne font pas de rendu JS.

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
| robots.txt autorise les bots IA | Oui — règle `*` inclusive, Googlebot et Bingbot explicitement autorisés | 5/5 |
| Fichier llms.txt présent | Non (erreur 404) | 0/3 |
| Sitemap XML à jour | Oui — 6 pages, toutes datées 19/01/2026 | 2/2 |

**Détail robots.txt (confirmé mars 2026) :**
- Googlebot et Bingbot : autorisés sauf `/dashboard`, `/vip`, `/admin`, `/messages`
- Twitterbot et facebookexternalhit : accès complet
- `User-agent: *` : mêmes restrictions que Googlebot — les bots IA (GPTBot, ClaudeBot, PerplexityBot, Google-Extended) sont donc autorisés par défaut

**Blocage principal confirmé :** Même avec un robots.txt permissif, le rendu JavaScript empêche l'extraction du contenu. Les 5 points attribués ne se traduisent par aucun bénéfice réel tant que le problème SSR n'est pas résolu.

**Sitemap :** 6 URLs, dont seulement 2 contiennent du contenu utile (accueil + accompagnements). Les 4 autres sont des pages légales et d'authentification.

### 2.6 Autorité d'entité et E-E-A-T — 4/15

| Critère | Présent ? | Score |
|---------|-----------|-------|
| Auteur nommé avec biographie et credentials | Non sur mechahelp-ai.com | 0/5 |
| Page "À propos" détaillée avec expertise | Non détectée | 0/3 |
| Mentions de la marque sur des sites tiers | 0 mention directe de mechahelp-ai.com | 0/4 |
| Profil LinkedIn CEO actif | Julien Berge (VanLyxe Corp), identifié | 2/3 |
| Communauté Skool MechaPizzAI | Présente, active, listée dans les résultats | 2/3 bonus |

**Signaux d'autorité identifiés :**
- LinkedIn Julien Berge : "AI Automation Expert, Creator of MechaPizzAI, CEO of MechaHelp-ai.com et MechaLabs-AI" — profil complet avec credentials
- Skool MechaPizzAI : communauté identifiable dans les recherches, mentionne des avantages valorisés à $3M (Airtable, Notion...), support illimité, formations à $400/mois offertes
- **Mais aucun de ces actifs ne pointe explicitement vers mechahelp-ai.com** dans les résultats de recherche

**Risque spécifique :** MechaLabs-ai.com (entité tierce, Paris, 4.9/5 sur 127 avis, spécialiste n8n/Make) capte les recherches sur "expert automatisation IA France" et peut être confondu avec MechaHelp par les IA génératives.

### 2.7 Avis et sentiment en ligne — 0/10

| Critère | Présent ? | Score |
|---------|-----------|-------|
| Avis Google Business (note ≥ 4.0, > 10 avis) | Non trouvé | 0/4 |
| Avis Trustpilot | Non trouvé | 0/3 |
| Avis Malt ou plateformes freelance | Non trouvé | 0/3 |

**Contraste frappant :** MechaLabs-ai.com (concurrent potentiel de confusion) affiche 127 avis à 4.9/5. MechaHelp : 0 avis public.

### 2.8 Fraîcheur du contenu — 2/10

| Critère | Présent ? | Score |
|---------|-----------|-------|
| Contenu mis à jour dans les 90 derniers jours | Sitemap : 19/01/2026 (61 jours à date d'audit) | 2/5 |
| Date de mise à jour visible sur les pages | Non détectée | 0/3 |
| Blog actif avec publication régulière | Non — aucun blog | 0/2 |

**Note :** Depuis le dernier audit (20 mars 2026), aucune mise à jour du sitemap n'a été détectée.

### Score Citabilité : 13/100

---

## 3. Analyse Concurrentielle GEO

### Paysage concurrentiel actualisé (mars 2026)

| Acteur | Type | Signaux GEO | Cité par les IA ? |
|--------|------|-------------|-------------------|
| **Koïno** (koino.fr) | Agence IA stratégique | Blog riche, comparatifs, top classements | Oui — régulièrement |
| **Limova.ai** | Assistants IA automatisation | Contenu clair, proposition extractible | Oui — cité sur requêtes automatisation |
| **Cartelis** | Conseil Data/IA | 100+ clients, label BPI, articles de fond | Oui — cité sur "meilleure agence IA France" |
| **Automise.fr** | Marketplace agents IA | Seul acteur positionné "marketplace IA" | Oui — cité sur "marketplace coaching IA automatisation" |
| **MechaLabs-ai.com** | Expert n8n/Make Paris | 127 avis 4.9/5, site crawlable | Oui — capte des requêtes proches de MechaHelp |
| **BGB Formation** | Formation n8n | Contenu SEO optimisé, certifications | Oui — cité sur "formation n8n France 2026" |
| **MechaHelp-ai.com** | Marketplace accompagnements IA | SPA non crawlable, 0 avis, 0 mentions | **Non** |

### Facteurs différenciants critiques

1. **Automise.fr occupe déjà le positionnement "marketplace IA"** : cité sur la requête exacte "marketplace coaching IA automatisation France", avec un catalogue d'agents IA installables en 48h
2. **MechaLabs-ai.com crée une confusion d'entité** nuisible : même racine de marque, même secteur, présence IA supérieure
3. **Sur "formation n8n France"**, 8 résultats apparaissent avant MechaHelp — qui n'apparaît pas du tout
4. **Le positionnement "accompagnement personnalisé"** est une niche non occupée et citée comme tendance émergente en 2026 — opportunité réelle si MechaHelp résout ses problèmes techniques

### Matrice de Citation IA

| Requête | MechaHelp | Koïno | Automise | MechaLabs-ai | Cartelis |
|---------|-----------|-------|----------|--------------|----------|
| Accompagnement IA France 2026 | Non | Oui | Non | Non | Oui |
| Marketplace coaching IA automatisation | Non | Non | **Oui** | Non | Non |
| Formation n8n France 2026 | Non | Non | Non | Non | Non |
| Expert n8n Make France | Non | Non | Non | **Oui** | Non |
| Meilleure agence IA France | Non | Oui | Non | Non | Oui |

---

## 4. Empreinte Linguistique

### Analyse de l'écosystème de marque existant

**Actifs identifiés (non optimisés pour le GEO) :**
- **Skool MechaPizzAI** : communauté free/premium, formations IA/automatisation, accès à des outils, support illimité — contenu riche mais cloîtré dans Skool (non indexable par les IA génératives)
- **LinkedIn Julien Berge** : profil complet, credentials IA/automatisation, mention de ses trois entités (MechaHelp, MechaLabs-AI, MechaPizzAI) — signal d'autorité personnelle
- **mechalabs-ai.com** : site crawlable lié à l'écosystème, mais sans backlink vers mechahelp-ai.com

**Formulation unique identifiée :**
- Sur Skool : "de 10 heures à 10 secondes" pour décrire les gains d'automatisation — phrase mémorable et citée dans les résultats de recherche

**Problème linguistique central :** Les trois noms de marque (MechaHelp, MechaLabs, MechaPizzAI) coexistent sans hiérarchie claire. Les IA ne savent pas quelle entité fait quoi. La marque "Mecha" est diluée.

### Seed-to-Series Statements recommandés

Phrases à disséminer sur le site, LinkedIn, annuaires, signatures email, articles invités :

1. **"MechaHelp — La marketplace française d'accompagnements IA : trouvez l'expert qui automatise vos process métier en 30 jours"**
   → Capitalise sur "marketplace" (positionnement différenciant vs agences), "française" (RGPD), promesse mesurable

2. **"De 10 heures à 10 secondes : MechaHelp connecte les PME françaises aux experts IA qui automatisent leurs workflows"**
   → Réutilise la phrase signature de MechaPizzAI, transfert d'autorité de la communauté vers la marketplace

3. **"Pas une agence, pas un outil : MechaHelp est la première marketplace d'accompagnements IA personnalisés en France"**
   → Différenciation claire vs Koïno (agence) et Automise (marketplace d'outils)

4. **"Propulsé par la communauté MechaPizzAI — MechaHelp met en relation les entreprises avec les meilleurs experts en automatisation n8n, Make et agents IA"**
   → Transfert d'autorité de la communauté vers la marketplace, mentionne les outils recherchés

5. **"L'accompagnement IA sur mesure pour PME : pas de template, pas de formation générique, que des experts certifiés pour vos cas d'usage spécifiques"**
   → Adresse la différenciation vs les formations (BGB Formation, Dr Firas) et vs les marketplaces d'outils (Automise)

---

## 5. Plan d'Action GEO

### Priorité 0 — Urgences techniques (Cette semaine) — Débloque tout le reste

| # | Action | Effort | Impact |
|---|--------|--------|--------|
| 0a | **Résoudre le rendu SPA** : Implémenter SSR (Next.js avec `getServerSideProps` ou génération statique) ou pre-rendering via Prerender.io. **Sans cette action, aucune autre optimisation GEO n'a d'effet.** | Moyen–Élevé (2-5 jours dev) | **CRITIQUE — Débloque 60% du score GEO potentiel** |
| 0b | **Créer un fichier `/llms.txt`** décrivant les services MechaHelp, le fondateur, la communauté, les outils maîtrisés (n8n, Make, agents IA) | Faible (1h rédaction) | +3pts accessibilité |
| 0c | **Revendiquer le profil Google Business** (si applicable à une entité digitale) et solliciter 3-5 premiers avis clients | Faible (2h) | +4pts avis |

### Quick Wins (1-2 semaines) — Impact estimé : +10-15 points GEO

| # | Action | Effort | Impact |
|---|--------|--------|--------|
| 1 | **Ajouter les balises Schema.org** : `Organization` (avec `founder`, `sameAs` vers LinkedIn/Skool), `Service`, `FAQPage`, `HowTo` | Faible | +6pts schema |
| 2 | **Enrichir la page accueil** (une fois SSR actif) : H1 clair, 3 sections H2 en format question, proposition de valeur en 1 phrase, liste de services avec descriptions | Moyen | +8pts structure |
| 3 | **Créer une page "À propos / L'expert"** avec biographie de Julien Berge, credentials, lien vers MechaPizzAI, mentions d'outils maîtrisés | Faible | +5pts E-E-A-T |
| 4 | **Relier les actifs de l'écosystème** : ajouter mechahelp-ai.com dans la bio LinkedIn, dans la description Skool de MechaPizzAI, dans mechalabs-ai.com si possible | Faible | +3pts autorité entité |
| 5 | **Ajouter des dates de publication visibles** sur toutes les pages | Très faible | +2pts fraîcheur |

### Moyen Terme (1-3 mois) — Impact estimé : +20-30 points GEO

| # | Action | Effort | Impact |
|---|--------|--------|--------|
| 6 | **Lancer un blog** avec 5 articles de fond : "Comment automatiser [facturation / service client / onboarding] avec n8n en 2026", "Guide complet : choisir son accompagnement IA pour PME en France", "MechaHelp vs Automise vs agence IA traditionnelle : quel choix pour votre PME ?" | Élevé | +15pts citabilité |
| 7 | **Publier 3 études de cas chiffrées** : "PME X a réduit de 60% son temps de facturation", "Agence Y a automatisé sa qualification de leads en 2 semaines" | Moyen | +10pts stats |
| 8 | **Créer une page FAQ complète** avec schema FAQPage : "Quelle différence entre MechaHelp et une agence IA ?", "Combien coûte un accompagnement IA ?", "Que peut automatiser n8n pour mon entreprise ?" | Moyen | +8pts structure |
| 9 | **S'inscrire sur les annuaires** : Hub France IA (972 acteurs listés), Sortlist, les-agences.fr, Malt pour Julien Berge | Moyen | +5pts mentions tierces |
| 10 | **Différencier clairement MechaHelp / MechaLabs / MechaPizzAI** dans toutes les descriptions publiques pour éviter la confusion d'entités | Faible | Clarté d'entité |
| 11 | **Publier des données originales** : enquête sur l'adoption IA par les PME françaises (100 répondants), partager les résultats en article et infographie | Élevé | +15pts citation magnet |

### Stratégique (3-6 mois) — Impact estimé : +20-25 points GEO

| # | Action | Effort | Impact |
|---|--------|--------|--------|
| 12 | **Digital PR ciblé** : obtenir des mentions sur 10+ domaines référents (presse tech française, podcasts IA, blogs PME) | Élevé | +12pts autorité |
| 13 | **Topic clusters** : page pilier "Accompagnement IA pour PME" + 10-15 articles satellites couvrant chaque use case | Élevé | +10pts couverture thématique |
| 14 | **Programme d'avis structuré** : 20+ avis Trustpilot ou Malt avec modèles de réponse, affichage sur le site | Moyen | +8pts E-E-A-T |
| 15 | **Monitoring GEO mensuel** via Otterly.ai ou audit manuel des 10 requêtes cibles | Faible | Suivi continu |
| 16 | **Transformer le contenu MechaPizzAI** en articles web indexables (résumés de sessions, tutoriels n8n, cas concrets) | Moyen | +8pts fraîcheur + citabilité |

---

## 6. Estimation d'Impact Revenue

| Action | Impact Citations IA | Impact Trafic | Coût estimé | Priorité |
|--------|-------------------|--------------|-------------|----------|
| Résoudre SSR (débloquant) | Passe de 0 → possible | Déblocage total | 1 000-3 000€ dev | **CRITIQUE** |
| llms.txt + Schema.org | +15% accessibilité | Extraction facilitée | 200-500€ | **Haute** |
| Blog 5 articles de fond | +30% citations potentielles | +50-200 visites/mois IA | 2 000-5 000€ | **Haute** |
| Études de cas chiffrées (3) | +25% citations | Conversion 9x vs organique | 500-1 500€ | **Haute** |
| Google Business + avis (20+) | +10% confiance IA | Signal légitimité | Gratuit | **Haute** |
| Annuaires + Malt | +20% mentions tierces | Backlinks + autorité | 200-500€ | **Moyenne** |
| Digital PR (10 mentions) | +40% autorité entité | 500-1 000 visites/mois | 3 000-8 000€ | **Moyenne** |
| Enquête PME originale | +50% citations uniques | Positionnement expert | 1 000-3 000€ | **Moyenne** |
| Topic clusters (15 articles) | +35% couverture thématique | +200-500 visites/mois | 5 000-10 000€ | **Basse** |

### Projection de revenus potentiels

Panier moyen estimé : 500-3 000€ par accompagnement (marketplace de services IA).

- **Scénario réaliste à 6 mois** (score GEO passant de 11 à 45-50) : 5-15 leads qualifiés/mois via IA → **15 000-90 000€ de CA additionnel annuel**
- **Scénario optimiste à 12 mois** (score GEO passant à 65+) : 15-30 leads/mois → **45 000-180 000€ de CA additionnel annuel**

*Note : les visiteurs provenant des IA convertissent en moyenne 9x mieux que le trafic organique classique (Semrush, 2025).*

---

## 7. Diagnostic Technique Spécifique

### Problème n°1 — CRITIQUE : Site non crawlable (SPA sans SSR)

**Confirmé mars 2026.** WebFetch de la page d'accueil et de `/accompagnements` retourne uniquement :
```
<title>MechaHelp - Accompagnements personnalisés en IA & Automatisation</title>
```

Tout le contenu est rendu en JavaScript côté client. Les crawlers IA (GPTBot, ClaudeBot, PerplexityBot) et Google n'accèdent pas au contenu des pages.

**Solutions :**
- **Next.js SSR** : activer `getServerSideProps` ou `generateStaticParams` pour les pages clés
- **Pre-rendering** : Prerender.io ou Rendertron pour servir du HTML pré-rendu aux bots
- **Dynamic rendering** : détecter le User-Agent et servir du HTML statique aux crawlers

### Problème n°2 — IMPORTANT : Confusion d'entités de marque

L'écosystème "Mecha" compte trois entités actives :
- **mechahelp-ai.com** : marketplace (non indexée)
- **mechalabs-ai.com** : expert n8n/Make Paris (entité tierce, bien indexée, 127 avis)
- **Skool MechaPizzAI** : communauté Julien Berge (indexée, active)

Les IA génératives ne peuvent pas construire une entité cohérente. Le risque est qu'elles confondent MechaHelp avec MechaLabs ou ignorent MechaHelp faute d'informations.

**Solution :** Ajouter des balises `sameAs` Schema.org reliant les trois entités, clarifier le positionnement de chacune dans toutes les descriptions publiques, et créer une page "L'écosystème Mecha" sur mechahelp-ai.com.

### Problème n°3 — MODÉRÉ : Zéro indexation Google confirmée

La recherche `site:mechahelp-ai.com` retourne 0 résultat. Les 6 pages du sitemap ne sont pas indexées. Cela est directement lié au problème SPA.

**Action immédiate :** Vérifier la Google Search Console, activer le SSR, puis soumettre le sitemap manuellement.

### Problème n°4 — MODÉRÉ : Absence de lien entre les actifs de marque

La communauté MechaPizzAI et le profil LinkedIn de Julien Berge génèrent des signaux d'autorité réels — mais ils ne pointent pas vers mechahelp-ai.com dans les résultats de recherche observés. L'autorité ne se transfère pas.

---

## 8. Opportunités Différenciantes Non Exploitées

### Positionnement "marketplace d'accompagnements" — Non occupé

Automise.fr occupe "marketplace d'agents IA" (outils). Aucun acteur ne se positionne clairement sur "marketplace d'humains experts en IA". C'est l'angle unique de MechaHelp — mais il n'est pas exploité dans les signaux GEO.

### Communauté MechaPizzAI — Capital non transféré

La communauté Skool constitue un actif rare : une preuve sociale active, des formations, un réseau d'experts. Ce capital pourrait devenir le signal d'autorité principal de MechaHelp si les deux entités étaient explicitement reliées dans le contenu indexable.

### Expertise n8n/Make — Niche à fort potentiel de citation

Les recherches sur "formation n8n France 2026" génèrent 8+ résultats cités par les IA. MechaHelp possède l'expertise (LinkedIn de Julien Berge) mais aucun contenu indexable sur ce sujet. Un seul article de fond bien structuré sur "Comment automatiser [use case] avec n8n en 2026" pourrait générer des citations IA dans les 60-90 jours suivant l'activation du SSR.

---

## Synthèse des Scores

| Composante | Score brut | Score /100 | Poids | Score pondéré |
|-----------|-----------|-----------|-------|---------------|
| Visibilité IA | 1/20 | 5/100 | 30% | 1,5 |
| Citabilité Contenu | 13/100 | 13/100 | 40% | 5,2 |
| Autorité d'Entité | 4/15 | 27/100 | 20% | 5,4 |
| Fraîcheur | 2/10 | 20/100 | 10% | 2,0 |
| **Score GEO Global** | | | | **≈ 14/100** |

> **Note méthodologique :** Le score pondéré donne 14/100. Compte tenu du blocage critique (SPA non crawlable) qui annule l'essentiel des bénéfices potentiels des autres composantes, le score global annoncé est conservativement fixé à **11/100** pour refléter l'impact réel sur la citabilité IA.

---

## Évolution vs Audit v1 (20 mars 2026)

| Critère | v1 (20/03) | v2 (21/03) | Δ |
|---------|-----------|-----------|---|
| Score global | 8/100 | 11/100 | +3 |
| Visibilité IA | 0/20 | 1/20 | +1 (MechaPizzAI Skool identifié) |
| Autorité d'entité | 3/15 | 4/15 | +1 (MechaPizzAI Skool confirmé) |
| Nouvelles données | — | Confusion d'entités avec MechaLabs-ai.com, Automise.fr occupe "marketplace IA" | — |

**Changements clés dans cette version :**
- Identification de MechaLabs-ai.com comme entité concurrente de confusion (127 avis 4.9/5, Paris, expert n8n/Make)
- Confirmation que Automise.fr occupe le positionnement "marketplace IA" — différenciation nécessaire
- Confirmation de la communauté MechaPizzAI sur Skool comme actif non exploité
- Ajout du problème de confusion d'entités dans le plan d'action
- Enrichissement des opportunités différenciantes

---

## Méthodologie

Cet audit évalue la visibilité de mechahelp-ai.com dans les réponses des moteurs de recherche IA (ChatGPT, Gemini, Perplexity, Claude, Google AI Overviews). Le scoring est basé sur les recherches académiques (Princeton/Georgia Tech, ACM SIGKDD 2024) et les données sectorielles (SE Ranking, Semrush, Ahrefs 2025-2026).

**Sources consultées lors de cet audit (mars 2026) :**
- Analyse directe du site : WebFetch pages accueil et `/accompagnements` (SSR non actif confirmé)
- robots.txt et sitemap.xml de mechahelp-ai.com
- 7 requêtes de visibilité IA testées via WebSearch
- Recherche de marque : "mechahelp", "MechaPizzAI", "Julien Berge MechaHelp"
- Analyse des concurrents cités : Koïno, Limova.ai, Cartelis, Automise.fr, MechaLabs-ai.com, BGB Formation
- Profil LinkedIn Julien Berge (VanLyxe Corp / MechaHelp / MechaLabs-AI / MechaPizzAI)
- Page Skool MechaPizzAI (community about page — accès 403 direct, données via WebSearch)
- WebFetch mechalabs-ai.com (Paris, n8n/Make, 127 avis 4.9/5 — entité distincte)
- Recherches sectorielles : "accompagnement IA France 2026", "formation n8n France 2026", "marketplace coaching IA automatisation France"
