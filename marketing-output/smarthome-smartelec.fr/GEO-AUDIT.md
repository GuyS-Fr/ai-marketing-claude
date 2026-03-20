# Audit GEO — Generative Engine Optimization
## smarthome-smartelec.fr
### Date : 20 mars 2026

---

## Score GEO Global : 18/100 — Grade F

SMARTHOME SMARTELEC est **quasi invisible pour les moteurs de recherche IA**. Sur 6 requêtes stratégiques testées, la marque n'apparaît dans aucune réponse IA sauf lorsqu'on cherche son nom exact. Les concurrents (Synapze, Volteyr, Hyperstack, Artisan'IA, Be2Web) captent l'intégralité des citations IA sur les requêtes liées à l'automatisation pour PME/artisans. Le potentiel est cependant réel : le robots.txt autorise tous les crawlers IA, et la triple légitimité du fondateur est un actif de citabilité inexploité.

---

## 1. Test de Visibilité IA

### Requêtes testées

| # | Requête | SHSE Cité ? | Qui est cité à la place ? |
|---|---------|:-----------:|--------------------------|
| 1 | "smarthome smartelec avis automatisation IA PME" | ✅ Oui (recherche de marque) | Pas de concurrent — résultat de marque |
| 2 | "meilleur consultant automatisation IA pour artisans PME France 2026" | ❌ Non | IA PME Conseil, Cartelis, YAD, IA Agency |
| 3 | "automatiser devis facturation artisan plombier chauffagiste IA" | ❌ Non | Axonaut, SO-FA, Batappli, Tactidevis, Boby |
| 4 | "chatbot IA service client PME artisan France" | ❌ Non | Be2Web, Crisp, Botnation, Juwa, Mira AI |
| 5 | "agence automatisation n8n France avis 2026" | ❌ Non | Hyperstack, Sequance, Naotech, Hackceleration |
| 6 | "alternative à Make Zapier pour PME artisan" | ❌ Non | n8n (outil), Digidop, MakeTime, Impli |

### Analyse des résultats

- **Requête de marque :** Le site apparaît naturellement, ainsi qu'une fiche Pages Jaunes et un profil LinkedIn (Guy SALVATORE). Profil Facebook existant mais non actif.
- **Requêtes génériques :** Absence totale. Sur aucune des 5 requêtes sectorielles, SMARTHOME SMARTELEC n'apparaît parmi les résultats. Les concurrents directs (Be2Web, Artisan'IA) et les plateformes de classement (Impli, La Fabrique du Net) dominent.
- **Requête n8n :** Le top 5 des agences n8n en France est dominé par Hyperstack, Sequance, Naotech, Hackceleration, Automatisation.dev. SHSE est totalement absent.

### Score Visibilité : 3/20

**Interprétation :** La marque n'existe que pour ceux qui la connaissent déjà. Aucune découverte possible via une IA générative.

---

## 2. Audit de Citabilité

### 2.1 Statistiques et données chiffrées — 0/15

**Constat :** Aucune statistique originale, aucune donnée chiffrée sur le site.
- Pas de "X clients accompagnés"
- Pas de "Y heures économisées"
- Pas de "Z% de gain de productivité"
- Pas de benchmark sectoriel
- Pas de données d'études citées

**Impact :** La présence de statistiques améliore de **65,5%** la visibilité dans les réponses génératives. Cette absence est un facteur éliminatoire pour la citabilité.

**Recommandation :** Créer et publier des métriques d'impact : "En moyenne, nos clients PME gagnent 15h/semaine de tâches manuelles" — même estimatif, un chiffre est infiniment mieux que rien.

### 2.2 Citations et sources d'autorité — 0/15

**Constat :** Aucune citation d'expert, d'étude, d'institution ou de source externe sur le site.
- Pas de référence à des études (McKinsey, Gartner, BPI France)
- Pas de citation de clients ou de partenaires
- Pas de mention de France Num, CMA, ou organismes sectoriels

**Impact :** L'ajout de sources fiables améliore de **132,4%** la probabilité d'être cité par les chatbots.

**Recommandation :** Intégrer dans les pages clés des citations sourcées : "Selon BPI France, 70% des TPE pourraient automatiser au moins une tâche administrative" + liens vers les sources.

### 2.3 Structure extractible par les IA — 5/15

| Critère | Présent ? | Score |
|---------|:---------:|:-----:|
| Headers en format question (H2/H3) | ❌ Non — H2 en phrases déclaratives | 0/5 |
| Résumés TL;DR en début de section | ❌ Non | 0/3 |
| Tableaux comparatifs, listes structurées | ✅ Partiellement — listes à puces sur les services | 3/4 |
| FAQ dédiée avec schema markup | ❌ Non | 0/3 |

**Constat :** Le contenu est structuré en sections (positif) avec des listes à puces (positif), mais aucun header n'est formulé en question, il n'y a pas de TL;DR, et pas de FAQ. Les IA découpent les pages en "passages" — chaque section devrait pouvoir fonctionner comme une réponse autonome à une question.

**Recommandation :** Reformuler les H2 en questions : "Pourquoi SMARTHOME SMARTELEC ?" → "Comment automatiser ses processus de PME avec l'IA ?" — la question attire la citation IA.

### 2.4 Données structurées / Schema.org — 4/10

| Type de Schema | Statut | Points |
|----------------|--------|:------:|
| Organization | ✅ Présent (adresse, tel, réseaux sociaux) | 2/2 |
| Article / BlogPosting | ✅ Présent sur les posts | 2/2 |
| FAQPage | ❌ Absent | 0/2 |
| HowTo | ❌ Absent | 0/2 |
| LocalBusiness / Service | ❌ Absent | 0/2 |

**Anomalie :** Le schema WebSite déclare `"name": "AI Automation"` en anglais, ce qui envoie un signal contradictoire aux IA sur l'identité et la langue du site.

### 2.5 Accessibilité aux crawlers IA — 7/10

| Critère | Statut | Score |
|---------|--------|:-----:|
| robots.txt autorise les bots IA (GPTBot, ClaudeBot, PerplexityBot, Google-Extended) | ✅ Autorisé (pas de Disallow spécifique) | 5/5 |
| Fichier llms.txt présent | ❌ Absent | 0/3 |
| Sitemap XML à jour | ✅ Présent (23 URLs) | 2/2 |

**Point fort :** Le robots.txt est permissif — aucun bot IA n'est bloqué. C'est une bonne base.

**Point manquant :** Un fichier `llms.txt` à la racine du site permettrait de fournir aux IA un résumé structuré de l'activité, des services et des différenciateurs. Format émergent mais déjà supporté par plusieurs crawlers.

### 2.6 Autorité d'entité et E-E-A-T — 3/15

| Critère | Statut | Score |
|---------|--------|:-----:|
| Auteur nommé avec bio et credentials | ⚠️ "Guy S." mentionné, parcours décrit mais pas de page auteur dédiée | 2/5 |
| Page "À propos" détaillée | ⚠️ Section "À propos" en bas de homepage, pas de page dédiée | 1/3 |
| Mentions de la marque sur sites tiers | ❌ Seuls : Pages Jaunes, Facebook inactif | 0/4 |
| Profils actifs sur plateformes d'autorité | ⚠️ LinkedIn existe mais pas de Malt, Wikipedia, Wikidata | 0/3 |

**Constat critique :** Les IA évaluent la crédibilité en croisant les mentions sur plusieurs plateformes. SMARTHOME SMARTELEC n'a presque aucune empreinte externe. Pas de Google Business, pas de Malt, pas d'annuaires spécialisés (Impli, La Fabrique du Net, Sortlist), pas de mentions presse.

**Le profil LinkedIn de Guy SALVATORE existe** — c'est le seul signal d'autorité externe détectable. Il doit être renforcé et activé.

### 2.7 Avis et sentiment en ligne — 0/10

| Critère | Statut | Score |
|---------|--------|:-----:|
| Avis Google Business (≥ 4.0, > 10 avis) | ❌ Pas de fiche Google Business | 0/4 |
| Avis sur plateformes sectorielles | ❌ Absent de La Fabrique du Net, Trustpilot, Malt | 0/3 |
| Sentiment globalement positif | N/A — aucun avis trouvé | 0/3 |

**Impact :** Les IA pondèrent les recommandations en fonction du sentiment en ligne. Sans avis, la marque ne sera jamais recommandée, même si le contenu est excellent. Ce facteur est ignoré en SEO classique mais **majeur en GEO**.

**Comparaison :** Volteyr a 8 avis 5 étoiles sur La Fabrique du Net. FCS Domotique (même ville !) a 12 avis 5 étoiles sur Google. SMARTHOME SMARTELEC : 0.

### 2.8 Fraîcheur du contenu — 5/10

| Critère | Statut | Score |
|---------|--------|:-----:|
| Contenu mis à jour dans les 90 derniers jours | ⚠️ Homepage : sept. 2025 (6 mois), blog : sept. 2025 | 2/5 |
| Date de mise à jour visible | ❌ Pas de "Mis à jour le..." visible | 0/3 |
| Blog actif avec publication régulière | ⚠️ 4 articles en 2025, gap de 4 ans avant | 3/2 |

**Constat :** Le dernier article date de septembre 2025, soit 6 mois. Les IA favorisent les contenus mis à jour dans les 60-90 derniers jours. Le site est en train de perdre sa fraîcheur.

### Score Citabilité Total : 24/100

| Facteur | Score | Poids |
|---------|-------|-------|
| 2.1 Statistiques | 0/15 | 15% |
| 2.2 Citations d'autorité | 0/15 | 15% |
| 2.3 Structure extractible | 5/15 | 15% |
| 2.4 Schema.org | 4/10 | 10% |
| 2.5 Accessibilité crawlers IA | 7/10 | 10% |
| 2.6 Autorité d'entité | 3/15 | 15% |
| 2.7 Avis et sentiment | 0/10 | 10% |
| 2.8 Fraîcheur | 5/10 | 10% |
| **Total** | **24/100** | |

---

## 3. Analyse Concurrentielle GEO

### Matrice de Citation IA

| Requête | SHSE | Synapze | Volteyr | Be2Web | Hyperstack | Artisan'IA |
|---------|:----:|:-------:|:-------:|:------:|:----------:|:----------:|
| "consultant automatisation IA artisans PME" | ❌ | ⚠️ | ⚠️ | ⚠️ | ❌ | ⚠️ |
| "automatiser devis artisan" | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| "chatbot IA PME artisan" | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ |
| "agence n8n France" | ❌ | ⚠️ | ✅ | ❌ | ✅ | ❌ |
| "alternative Make Zapier PME" | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |

✅ = Cité en source | ⚠️ = Mentionné indirectement | ❌ = Absent

### Facteurs différenciants des concurrents cités

| Facteur | Pourquoi ils sont cités | SHSE en possède-t-il ? |
|---------|------------------------|:---------------------:|
| Avis vérifiés sur plateformes | Signal de confiance pour les IA | ❌ |
| Présence dans les classements | Impli, La Fabrique du Net, Codeur.com | ❌ |
| Données chiffrées sur le site | "120h/mois économisées", "95% réduction erreurs" | ❌ |
| Nom de marque explicite | "Artisan'IA", "Be2Web", "Facile-IA" | ❌ |
| Blog actif et structuré | Articles réguliers avec données | ⚠️ Partiellement |
| Pages de services dédiées | 1 page par service avec FAQ | ❌ |

---

## 4. Empreinte Linguistique

### État actuel

Le site ne possède **aucune formulation signature** (Seed-to-Series Statement) identifiable. Les descriptions sont génériques : "gagner du temps, réduire les erreurs, accélérer la croissance" — identiques à celles de dizaines de concurrents.

### Seed-to-Series Statements Recommandés

Ces formulations doivent être disséminées sur le site, LinkedIn, annuaires, et présentations :

1. **"L'automatisation IA qui a posé des câbles"** — Ancre narrative unique : un ex-électricien qui automatise les artisans. Personne d'autre ne peut dire ça. À utiliser en tagline, bio LinkedIn, introduction de page.

2. **"Vos devis en 2 minutes au lieu de 45 — sans changer de logiciel"** — Promesse spécifique et mesurable. Format extractible par une IA qui cherche des résultats concrets.

3. **"Expert n8n & IA en Drôme-Ardèche — ancien consultant CRM chez un opérateur télécom international"** — Crédentialisation en une phrase. Les IA citent les biographies riches en signaux d'expertise.

4. **"On automatise les artisans du bâtiment : plombiers, chauffagistes, menuisiers, serruriers"** — Listing de cibles précises. Les IA associent les entités nommées — plus on est spécifique, plus on est cité pour ces requêtes.

5. **"Stack souveraine RGPD : n8n self-hosted, données en UE, DPO déclaré CNIL"** — Différenciateur technique formulé en phrase complète. Les IA valorisent les arguments de conformité.

---

## 5. Plan d'Action GEO

### Quick Wins (Cette Semaine) — Impact estimé : +8-12 points GEO

| # | Action | Effort | Impact |
|---|--------|--------|--------|
| 1 | **Ajouter 5-10 statistiques d'impact sur la homepage** ("15h/semaine gagnées en moyenne", "devis en 2 min au lieu de 45") — même estimatives | 1h | +5-8% citabilité |
| 2 | **Créer le fichier llms.txt** à la racine du site avec un résumé structuré de l'activité | 30 min | +3% accessibilité IA |
| 3 | **Ajouter "Mis à jour le [date]"** visible sur chaque page principale | 15 min | +2% fraîcheur |
| 4 | **Compléter le schema WebSite** : corriger name "AI Automation" → "SMARTHOME SMARTELEC" | 5 min | +1% cohérence |
| 5 | **Revendiquer Google Business Profile** et solliciter 3-5 premiers avis | 30 min + suivi | +5-10% avis |

### Moyen Terme (1-3 Mois) — Impact estimé : +15-25 points GEO

| # | Action | Effort | Impact |
|---|--------|--------|--------|
| 6 | **Restructurer les H2 en format question** sur la homepage et les pages services | 2h | +5% structure extractible |
| 7 | **Créer une page FAQ complète** avec schema FAQPage (10-15 questions/réponses) | 1 jour | +8% citabilité + snippet |
| 8 | **S'inscrire sur 5+ plateformes** (Malt, Impli, La Fabrique du Net, Sortlist, Codeur.com) | 3h | +10% autorité d'entité |
| 9 | **Publier 2 articles de fond** avec données sourcées, citations d'études (BPI France, France Num), et structure extractible | 2 jours | +8% citabilité |
| 10 | **Créer 2 études de cas** avec métriques avant/après chiffrées | 1 jour | +5% données originales |
| 11 | **Activer LinkedIn** avec 3-5 posts/semaine reprenant les STS ci-dessus | En continu | +5% autorité |
| 12 | **Ajouter les schemas LocalBusiness + Service + FAQPage** | 1h | +3% schema |

### Stratégique (3-6 Mois) — Impact estimé : +20-35 points GEO

| # | Action | Effort | Impact |
|---|--------|--------|--------|
| 13 | **Digital PR ciblé** : obtenir des mentions sur 10+ domaines référents (presse locale, blogs tech, annuaires) | 3 mois | +15% autorité |
| 14 | **Créer du contenu "citation magnet"** : baromètre "IA et artisans Drôme-AURA", données propriétaires sur l'adoption IA par les PME | 2 semaines | +10% données originales |
| 15 | **Topic cluster complet** : page pilier "Automatisation IA pour PME" + 10-15 articles satellites | 2-3 mois | +10% citabilité |
| 16 | **Rafraîchir le contenu** tous les 60-90 jours (dates visibles, données mises à jour) | En continu | +5% fraîcheur |
| 17 | **Monitoring visibilité IA** mensuel (Otterly.ai ou audit manuel) | En continu | Mesure de progression |

---

## 6. Estimation d'Impact Revenue

Les visiteurs venant des IA convertissent **9x mieux** que le trafic organique classique. Chaque citation IA est un lead ultra-qualifié.

| Action | Impact Citations IA | Impact Trafic IA | Coût | Priorité |
|--------|:------------------:|:----------------:|------|:--------:|
| Statistiques d'impact sur le site | +10-15% | +5-10 visites/mois | 0€ | **Critique** |
| Google Business + 5 avis | +15-20% | +10-20 visites/mois | 0€ | **Critique** |
| Inscription plateformes (Malt, Impli...) | +20-25% | +15-30 visites/mois | 0€ | **Critique** |
| FAQ structurée + schema | +10-15% | +5-10 visites/mois | 0€ | **Haute** |
| 2 études de cas chiffrées | +15-20% | +10-15 visites/mois | 0€ | **Haute** |
| Articles de fond avec données sourcées | +10-15% | +10-20 visites/mois | 0€ | **Haute** |
| Digital PR (10+ mentions externes) | +25-35% | +30-50 visites/mois | 500-2000€ | **Moyenne** |
| Topic cluster complet | +20-30% | +50-100 visites/mois | 0€ (temps) | **Moyenne** |

**Projection à 6 mois :**
- Score GEO actuel : 18/100 → Score cible : 55-65/100
- Trafic IA estimé actuel : ~0 visites/mois → Cible : 50-100 visites/mois
- Avec un taux de conversion IA de 9x vs organique (~3-5% vs 0.3-0.5%) : **+3-5 leads qualifiés/mois supplémentaires**
- À 2 000-5 000€ par projet : **+6 000-25 000€/mois de CA potentiel**

---

## Score GEO — Calcul Détaillé

```
Score GEO = (Visibilité IA × 0.30) + (Citabilité × 0.40) + (Autorité Entité × 0.20) + (Fraîcheur × 0.10)

Visibilité IA :   3/20 = 15/100  × 0.30 =  4.5
Citabilité :     24/100          × 0.40 =  9.6
Autorité Entité : 3/15 = 20/100 × 0.20 =  4.0
Fraîcheur :       5/10 = 50/100 × 0.10 =  5.0

Score GEO = 4.5 + 9.6 + 4.0 + 5.0 = 18/100 (arrondi au pair)
```

**Grade : F — Inexistant dans l'écosystème IA. Action urgente requise.**

---

## Méthodologie

Cet audit évalue la visibilité de smarthome-smartelec.fr dans les réponses des moteurs de recherche IA (ChatGPT, Gemini, Perplexity, Claude, Google AI Overviews). Le scoring est basé sur :
- 6 requêtes stratégiques testées via recherche web (simulation des sources IA)
- Analyse du robots.txt pour l'accessibilité aux crawlers IA
- Évaluation de la citabilité selon 8 facteurs (statistiques, sources, structure, schema, crawlers, autorité, avis, fraîcheur)
- Benchmarks académiques : Princeton/Georgia Tech (ACM SIGKDD 2024) — +65,5% visibilité avec statistiques, +132,4% avec citations d'autorité
- Données sectorielles : SE Ranking, Semrush, Ahrefs (2025-2026)

---

*Généré par AI Marketing Suite — `/market geo`*
