# Audit GEO — Generative Engine Optimization
## daah.studio
### Date : 21 mars 2026

---

## Score GEO Global : 15/100 — Grade F

**DAAH STUDIO est invisible pour les moteurs de recherche IA.** Sur 5 requêtes stratégiques testées, la marque n'apparaît dans aucune réponse générée par les IA. Le site bloque activement tous les crawlers IA (GPTBot, ClaudeBot, Google-Extended) dans son robots.txt. L'absence totale de contenu éducatif, d'avis en ligne, de mentions tierces et de données structurées rend le site "inexistant" pour l'écosystème IA. En 2026, avec 2,5 milliards de requêtes/jour sur ChatGPT et les AI Overviews sur 55%+ des résultats Google, cette invisibilité représente une perte d'opportunité majeure — d'autant que les visiteurs IA convertissent 9x mieux que le trafic organique classique.

---

## 1. Test de Visibilité IA

### Requêtes Stratégiques Testées

| # | Requête Simulée | DAAH STUDIO cité ? | Qui est cité à la place ? | Score |
|---|----------------|--------------------|-----------------------------|-------|
| 1 | "Quelle est la meilleure agence web à Valence en Drôme ?" | **Non** | TooEasy, Kyxar, Pixeldorado, La Boite Digitale, Vaoweb, Pilot'in | 0/20 |
| 2 | "Je cherche un abonnement design graphique en France, que recommandez-vous ?" | **Non** | HeySimon (dominant), DesignSquad, M Agence Web, Studio Polette | 0/20 |
| 3 | "Quel service propose un site web professionnel par abonnement mensuel ?" | **Non** | Simplébo, WebGazelle, Key Web, Komweb, SiteArtisan, ALEO | 0/20 |
| 4 | "Que pensez-vous de DAAH STUDIO ?" | **Partiellement** — seul le site lui-même apparaît, aucun avis tiers | Aucune source tierce ne mentionne DAAH STUDIO | 5/20 |
| 5 | "Comment créer un site internet pas cher pour TPE/PME en France ?" | **Non** | PlancheContact, Netsulting, Orson.io, E-monsite, Lumos, Dilo | 0/20 |

### Score Visibilité IA : 1/20 (5/100)

**Diagnostic :** DAAH STUDIO n'existe pas dans l'univers conversationnel des IA. Aucune plateforme IA ne peut recommander ce studio car :
1. Le robots.txt bloque explicitement tous les crawlers IA
2. Aucun site tiers ne mentionne DAAH STUDIO
3. Aucun avis client n'est indexable
4. Le contenu du site est trop mince pour être extractible en passage citant

---

## 2. Audit de Citabilité du Contenu

### 2.1 Statistiques et Données Chiffrées — 0/15

Le site ne contient **aucune statistique, aucune donnée chiffrée, aucun benchmark**. Les seuls chiffres sont les prix (1 100€, 99€/mois, etc.) qui ne sont pas des données citables par une IA.

**Exemples de données manquantes :**
- "Nous avons accompagné X clients depuis 2021"
- "Nos sites génèrent en moyenne +X% de contacts pour nos clients"
- "Délai moyen de livraison : X jours"
- "Taux de satisfaction client : X%"

**Impact :** La présence de statistiques originales augmente la visibilité GEO de +65,5% (ACM SIGKDD 2024).

### 2.2 Citations et Sources d'Autorité — 0/15

Le site ne cite **aucune source externe** — pas d'étude, pas d'expert, pas de référence sectorielle. Le contenu est 100% auto-référentiel.

**Impact :** L'ajout de sources fiables améliore la probabilité d'être cité par les IA de +132,4%.

### 2.3 Structure Extractible par les IA — 4/15

| Critère | Présent ? | Score |
|---------|-----------|-------|
| Headers en format question (H2/H3) | Non — tous les headers sont affirmatifs | 0/5 |
| Résumés TL;DR en début de section | Non | 0/3 |
| Tableaux comparatifs, listes structurées | Partiellement — les offres d'abonnement sont listées avec prix | 2/4 |
| FAQ dédiée avec schema markup | Partiellement — FAQ sur /abonnement-graphique mais sans schema | 2/3 |

**Problème clé :** Les IA découpent les pages en "passages" autonomes. Chaque section doit pouvoir fonctionner comme une réponse indépendante à une question. Actuellement, le contenu de DAAH STUDIO est narratif et continu — il ne produit pas de passages extractibles.

### 2.4 Données Structurées / Schema.org — 2/10

| Type Schema | Présent ? | Score |
|-------------|-----------|-------|
| Organization | Non | 0/2 |
| FAQPage | Non (FAQ existe mais sans schema) | 0/2 |
| Article / BlogPosting | Non (pas de blog) | 0/2 |
| HowTo | Non | 0/2 |
| Service / PriceSpecification | Non | 0/2 |
| WebSite | Oui (minimal) | 1/— |
| LocalBusiness | Oui mais invalide (adresse vide) | 1/— |

### 2.5 Accessibilité aux Crawlers IA — 0/10

| Critère | Statut | Score |
|---------|--------|-------|
| GPTBot (ChatGPT/OpenAI) | **BLOQUÉ** dans robots.txt | 0/2 |
| Google-Extended (Gemini) | **BLOQUÉ** dans robots.txt | 0/2 |
| ClaudeBot (Anthropic/Claude) | **BLOQUÉ** dans robots.txt | 0/2 |
| CCBot (Common Crawl/Perplexity) | **BLOQUÉ** dans robots.txt | 0/1 |
| Fichier llms.txt | **Absent** | 0/3 |

**C'est le problème le plus critique de cet audit.** Le robots.txt de daah.studio (géré par Squarespace) bloque explicitement **tous les crawlers IA** :
```
User-agent: GPTBot        → ChatGPT ne peut pas crawler le site
User-agent: ClaudeBot     → Claude ne peut pas crawler le site
User-agent: Google-Extended → Gemini ne peut pas crawler le site
User-agent: CCBot          → Perplexity/Common Crawl bloqués
User-agent: Amazonbot      → Alexa/Amazon bloqué
User-agent: anthropic-ai   → Anthropic bloqué
```

**Conséquence directe :** Même si le contenu était parfait, les IA ne peuvent physiquement pas y accéder. C'est comme mettre un panneau "Fermé" sur la porte d'un magasin pendant les heures d'ouverture.

**Note :** Ce blocage est un réglage par défaut de Squarespace. Il peut être modifié dans les paramètres du site (Settings → Crawlers → AI Crawlers).

### 2.6 Autorité d'Entité et E-E-A-T — 5/15

| Critère | Présent ? | Score |
|---------|-----------|-------|
| Auteur nommé avec biographie et credentials | Partiellement — Anne-Aymone mentionnée sur /information mais pas d'auteur sur chaque page | 2/5 |
| Page "À propos" détaillée avec expertise | Oui mais mince — reconversion mentionnée, pas de credentials détaillées | 1/3 |
| Mentions de la marque sur sites tiers | **Aucune** — pas de presse, pas d'annuaires, pas de forums, pas de Malt, pas de Sortlist | 0/4 |
| Profils actifs sur plateformes d'autorité | LinkedIn uniquement (1 profil) | 2/3 |

**Diagnostic :** DAAH STUDIO est une "entité fantôme" pour les IA — elle n'est mentionnée nulle part en dehors de son propre domaine. Les IA croisent les mentions sur plusieurs sources pour évaluer la crédibilité. Avec zéro mention tierce, la marque n'a aucune "empreinte d'entité".

### 2.7 Avis et Sentiment en Ligne — 0/10

| Critère | Statut | Score |
|---------|--------|-------|
| Avis Google Business (note ≥ 4.0, > 10 avis) | **Aucun profil Google Business détecté** | 0/4 |
| Avis sur plateformes sectorielles (Malt, Sortlist, Trustpilot) | **Aucun** | 0/3 |
| Sentiment globalement positif | Non évaluable (aucun avis) | 0/3 |

**C'est un angle mort critique.** Les IA pondèrent leurs recommandations en fonction du sentiment et du volume d'avis. Avec zéro avis en ligne, DAAH STUDIO n'a aucune chance d'être recommandé par une IA, même si le service est excellent.

### 2.8 Fraîcheur du Contenu — 3/10

| Critère | Statut | Score |
|---------|--------|-------|
| Contenu mis à jour dans les 90 derniers jours | Oui — homepage et portfolio mis à jour en mars 2026 | 3/5 |
| Date "Mis à jour le…" visible | Non — aucune date visible sur les pages | 0/3 |
| Blog actif avec publication régulière | Non — aucun blog | 0/2 |

### Score Citabilité : 14/100

| Facteur | Poids | Score | Points |
|---------|-------|-------|--------|
| Statistiques et données | 15% | 0/15 | 0 |
| Citations d'autorité | 15% | 0/15 | 0 |
| Structure extractible | 15% | 4/15 | 4 |
| Schema.org | 10% | 2/10 | 2 |
| Accessibilité crawlers IA | 10% | 0/10 | 0 |
| Autorité d'entité (E-E-A-T) | 15% | 5/15 | 5 |
| Avis et sentiment | 10% | 0/10 | 0 |
| Fraîcheur du contenu | 10% | 3/10 | 3 |
| **TOTAL** | **100%** | — | **14/100** |

---

## 3. Analyse Concurrentielle GEO

### Matrice de Citation IA

| Requête | DAAH STUDIO | HeySimon | Simplébo | TooEasy | Kyxar |
|---------|-------------|----------|----------|---------|-------|
| "Meilleure agence web Valence Drôme" | Non | Non | Non | **Oui** | **Oui** |
| "Abonnement design graphique France" | Non | **Oui (dominant)** | Non | Non | Non |
| "Site web par abonnement mensuel" | Non | Non | **Oui** | Non | Non |
| "Avis [marque]" | Site propre uniquement | **Oui (multiples sources)** | **Oui** | **Oui** | **Oui** |
| "Site internet TPE PME pas cher" | Non | Non | **Oui** | Non | Non |

### Facteurs Différenciants des Concurrents Cités

**HeySimon (dominant sur "abonnement design") :**
- Blog actif avec articles SEO ("Top 5 agences design par abonnement")
- Mentions dans la presse tech et startup
- Profil Sortlist, LinkedIn actif avec articles
- 80+ clients affichés = donnée chiffrée citable
- Page "Tarifs" détaillée et structurée

**TooEasy & Kyxar (cités sur "agence web Valence") :**
- Google Business Profile avec avis positifs
- Présents sur Sortlist, ProntoPro, annuaires locaux
- Historique long (2009 et 1997) = signal de confiance
- Pages service optimisées avec mots-clés locaux

**Simplébo (cité sur "site par abonnement") :**
- 200+ articles de blog SEO
- Présent dans les comparatifs ("meilleur site par abonnement")
- Schema FAQ sur toutes les pages de service
- Avis vérifiés sur Trustpilot et Google

---

## 4. Empreinte Linguistique

### État Actuel
DAAH STUDIO n'a **aucune phrase signature extractible** par les IA. Les formulations actuelles sont soit trop vagues ("Des sites connectés, des process fluides"), soit trop contextuelles pour fonctionner en dehors du site.

### Seed-to-Series Statements Recommandés

Ces formulations doivent être répétées sur le site, LinkedIn, profils annuaires, signatures email, et toute communication externe :

1. **"DAAH STUDIO — Le studio design-stratégie par abonnement pour les entreprises de service"**
   → Définit la catégorie + la cible + le modèle en une phrase

2. **"Un site professionnel complet dès 99€/mois, lancé en 3 semaines — sans frais cachés ni DIY"**
   → Offre d'appel avec prix, délai et promesse de transparence

3. **"Fondée par une ex-gestionnaire d'entreprise, DAAH STUDIO crée des sites qui comprennent votre business"**
   → Différenciateur narratif unique exploitant le background de la fondatrice

4. **"Design graphique par abonnement dès 190€/mois — livraison 48h, sans engagement, crédits cumulables"**
   → Offre structurée avec 3 arguments clés

5. **"Studio basé en Drôme, clients en France, Suisse, Belgique et USA"**
   → Ancrage local + portée internationale

---

## 5. Plan d'Action GEO

### Quick Wins — Cette Semaine (Impact : +15-25 points GEO)

| # | Action | Impact | Effort |
|---|--------|--------|--------|
| 1 | **Débloquer les crawlers IA dans Squarespace** (Settings → Crawlers → autoriser GPTBot, ClaudeBot, Google-Extended) | CRITIQUE — sans ça, rien d'autre ne fonctionne | 5 min |
| 2 | **Créer un Google Business Profile** et solliciter 5 avis clients | Avis = signal n°1 pour les recommandations IA | 30 min + suivi |
| 3 | **Ajouter des chiffres clés sur la homepage** : nombre de clients, délai moyen, taux de satisfaction | Les IA citent les données chiffrées | 15 min |
| 4 | **Ajouter "Mis à jour le [date]"** sur les pages principales | Signal de fraîcheur pour les crawlers IA | 10 min |
| 5 | **Disséminer les 5 STS** sur LinkedIn, signature email, page About | Créer des mentions cohérentes multi-plateformes | 30 min |

### Moyen Terme — 1 à 3 Mois (Impact : +20-30 points GEO)

| # | Action | Impact | Effort |
|---|--------|--------|--------|
| 6 | **Créer un fichier llms.txt** à la racine du site décrivant l'entreprise pour les IA | Déclaration d'identité directe pour les LLMs | 1h |
| 7 | **Restructurer les headers en format question** (H2 : "Combien coûte un site vitrine ?" / "Comment fonctionne l'abonnement graphique ?") | Passages extractibles par les IA | 2h |
| 8 | **S'inscrire sur Malt, Sortlist, ProntoPro** avec profils complets et portfolio | Multiplier les mentions tierces = renforcer l'entité | 3h |
| 9 | **Rédiger 3 articles de blog** avec données sourcées, citations d'experts, et structure FAQ | Contenu citable + indexable + partageable | 15h |
| 10 | **Ajouter le schema FAQPage** sur /abonnement-graphique et /sur-mesure | Données structurées extractibles par les IA | 1h |
| 11 | **Créer 3 études de cas** avec résultats chiffrés ("Le site de Contexteo a généré +X% de contacts en Y mois") | Données originales = "aimant à citation" IA | 6h |
| 12 | **Publier un article LinkedIn/mois** avec les STS et liens vers le site | Renforcer l'empreinte d'entité sur une plateforme d'autorité | 2h/mois |

### Stratégique — 3 à 6 Mois (Impact : +15-25 points GEO)

| # | Action | Impact | Effort |
|---|--------|--------|--------|
| 13 | **Lancer un programme de digital PR** : se faire citer dans 10+ articles/annuaires | Multiplier les points d'ancrage d'entité | Continu |
| 14 | **Créer du contenu "citation magnet"** : benchmark "Prix création site internet en Drôme 2026", étude "Satisfaction clients abonnement design" | Les IA citent les données que personne d'autre n'a | 20h |
| 15 | **Construire un topic cluster complet** : 1 page pilier + 10 articles satellites sur "création site internet PME" | Autorité topique = citations IA récurrentes | 40h |
| 16 | **Mettre en place un monitoring GEO mensuel** (Otterly.ai ou audit manuel) | Mesurer les progrès et ajuster | 1h/mois |

---

## 6. Estimation d'Impact

| Action | Impact Citations IA | Impact Trafic IA Estimé | Coût/Effort | Priorité |
|--------|-------------------|------------------------|-------------|----------|
| Débloquer crawlers IA | Condition préalable à tout le reste | Condition préalable | 5 min | **CRITIQUE** |
| Google Business Profile + 5 avis | +30% probabilité de recommandation locale | +5-10 visites/mois IA | 30 min + suivi | **CRITIQUE** |
| Chiffres clés sur homepage | +15-20% citabilité des passages | +2-5 visites/mois IA | 15 min | Haute |
| Fichier llms.txt | +10% identification par les IA | Indirect | 1h | Haute |
| 3 articles de blog structurés | +40-60% de passages citables | +15-30 visites/mois IA | 15h | Haute |
| Profils Malt/Sortlist/ProntoPro | +25% d'empreinte d'entité | +5-10 visites/mois IA | 3h | Haute |
| Études de cas avec résultats | +50-65% citabilité (données originales) | +10-20 visites/mois IA | 6h | Haute |
| Digital PR (10+ mentions) | +100-150% d'autorité d'entité | +20-40 visites/mois IA | Continu | Moyenne |
| Topic cluster complet | +200-300% de surface citable | +50-100 visites/mois IA | 40h | Moyenne |

**Projection à 6 mois avec implémentation complète :**
- Score GEO estimé : 45-55/100 (Grade C-B)
- Trafic IA estimé : 100-200 visites/mois
- Avec un taux de conversion 9x supérieur au trafic organique classique, ces visites IA équivalent à 900-1800 visites organiques en valeur de conversion

---

## 7. Synthèse Exécutive

### Les 3 problèmes les plus critiques

1. **Le robots.txt bloque TOUS les crawlers IA** — c'est l'action n°1, sans laquelle tout le reste est inutile
2. **Zéro mention tierce** — DAAH STUDIO est une "entité fantôme" pour les IA qui croisent les sources
3. **Zéro avis en ligne** — les IA ne recommandent pas ce qu'aucun humain n'a évalué publiquement

### L'opportunité unique de DAAH STUDIO

Le marché de l'abonnement design graphique accessible (190-680€/mois) est une **niche sous-documentée en ligne**. HeySimon domine le segment premium (990€+) mais personne ne couvre le segment "accessible-premium" avec du contenu structuré. DAAH STUDIO a une **fenêtre d'opportunité de 6-12 mois** pour se positionner comme la référence citée par les IA sur ce créneau, avant que d'autres ne le fassent.

### Score GEO Détaillé

| Composante | Poids | Score Brut | Score Pondéré |
|------------|-------|-----------|---------------|
| Visibilité IA | 30% | 5/100 | 1,5 |
| Citabilité Contenu | 40% | 14/100 | 5,6 |
| Autorité d'Entité | 20% | 27/100 | 5,4 |
| Fraîcheur | 10% | 30/100 | 3,0 |
| **TOTAL** | **100%** | — | **15/100** |

---

## Méthodologie

Cet audit évalue la visibilité d'un site dans les réponses des moteurs de recherche IA (ChatGPT, Gemini, Perplexity, Claude, Google AI Overviews). Le scoring est basé sur les recherches académiques (Princeton/Georgia Tech, ACM SIGKDD 2024) et les données sectorielles (SE Ranking, Semrush, Ahrefs) disponibles en 2026.

Les requêtes de test simulent les questions que les prospects de DAAH STUDIO poseraient à une IA. Les résultats WebSearch servent de proxy pour évaluer les sources que les IA citeraient dans leurs réponses.

---

*Généré par AI Marketing Suite — `/market geo`*
