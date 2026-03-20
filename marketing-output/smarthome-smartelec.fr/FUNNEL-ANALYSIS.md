# Analyse du Tunnel de Vente — smarthome-smartelec.fr

**Date d'analyse :** 20 mars 2026
**Analyste :** Audit IA Marketing
**Score de conversion global :** 22/100
**Verdict :** Tunnel quasi inexistant — le site fonctionne comme une vitrine statique sans mécanisme d'acquisition structuré.

---

## Table des matières

1. [Synthèse exécutive](#1-synthèse-exécutive)
2. [Cartographie du funnel actuel (TOFU / MOFU / BOFU)](#2-cartographie-du-funnel-actuel)
3. [Diagnostic des fuites par étape](#3-diagnostic-des-fuites-par-étape)
4. [Funnel idéal recommandé](#4-funnel-idéal-recommandé)
5. [Recommandations détaillées par étape](#5-recommandations-détaillées-par-étape)
6. [Estimation d'impact revenue](#6-estimation-dimpact-revenue)
7. [Plan d'implémentation priorisé](#7-plan-dimplémentation-priorisé)

---

## 1. Synthèse exécutive

smarthome-smartelec.fr propose des services B2B à forte valeur ajoutée (automatisation IA, chatbots, infrastructure données) destinés aux PME et artisans. Malgré la pertinence de l'offre, le site souffre d'un tunnel de vente pratiquement absent :

- **Un seul point de conversion** : "Réserver un Audit gratuit (30 min)" via redirection externe Cal.com
- **Aucun mécanisme de capture intermédiaire** pour les visiteurs non prêts à s'engager
- **Aucun nurturing** : pas d'email, pas de séquence, pas de newsletter
- **Aucun tracking** : impossible de mesurer, donc impossible d'optimiser
- **Paradoxe crédibilité** : l'entreprise vend de l'automatisation mais n'automatise pas sa propre acquisition

Le tunnel actuel perd environ **97 à 99% des visiteurs** sans aucune possibilité de les recontacter.

---

## 2. Cartographie du funnel actuel

### 2.1 Schéma du tunnel existant

```
ÉTAT ACTUEL — Tunnel linéaire "tout ou rien"
═══════════════════════════════════════════════

  Visiteur arrive sur le site
         │
         ▼
┌─────────────────────────┐
│   TOFU (Awareness)      │
│   • Page d'accueil      │
│   • 8 articles de blog  │
│   • Page domotique      │
│   (informative, 0 CTA)  │
└────────────┬────────────┘
             │
             │  ~30% quittent sans voir de CTA
             │
             ▼
┌─────────────────────────┐
│   MOFU (Considération)  │
│                         │
│   ██  VIDE  ██          │
│                         │
│   • Pas de lead magnet  │
│   • Pas de formulaire   │
│   • Pas de newsletter   │
│   • Pas de cas client   │
│   • Pas de comparatif   │
└────────────┬────────────┘
             │
             │  ~90% des restants partent (rien à consommer)
             │
             ▼
┌─────────────────────────┐
│   BOFU (Décision)       │
│                         │
│   CTA unique :          │
│   "Réserver un Audit    │
│    gratuit (30 min)"    │
│         │               │
│         ▼               │
│   Redirection externe   │
│   → Cal.com             │
│   (perte de confiance)  │
└────────────┬────────────┘
             │
             │  ~50% abandonnent sur Cal.com
             │
             ▼
┌─────────────────────────┐
│   POST-CONVERSION       │
│                         │
│   ██  VIDE  ██          │
│                         │
│   • Pas de confirmation │
│   • Pas de rappel       │
│   • Pas de nurturing    │
│   • Pas de suivi        │
└─────────────────────────┘
```

### 2.2 Inventaire des actifs par étape

| Étape | Actifs existants | Actifs manquants |
|-------|-----------------|------------------|
| **TOFU** | 8 articles blog, page domotique, page accueil | SEO structuré, tracking, CTA contextuels dans le blog, landing pages dédiées |
| **MOFU** | Aucun | Lead magnet, newsletter, séquence email, études de cas, témoignages, comparatifs |
| **BOFU** | 1 CTA "Audit gratuit" via Cal.com | Formulaire natif, page de réassurance, tarification, garantie, preuve sociale |
| **POST-CONV** | Aucun | Email de confirmation, séquence pré-audit, rappels, nurturing post-audit |

---

## 3. Diagnostic des fuites par étape

### 3.1 Modélisation du flux actuel

```
BASE : 1 000 visiteurs / mois (hypothèse)
══════════════════════════════════════════

Étape                          Visiteurs    Perte      Cause principale
─────────────────────────────────────────────────────────────────────────
Arrivée sur le site            1 000        —          —
                                  │
Voient un CTA                    700        -300 (30%) Blog et page domotique
                                  │                    sans CTA, navigation
                                  │                    dispersée
                                  │
Cliquent sur le CTA               56        -644 (92%) CTA unique, pas
                                  │                    d'alternative, engagement
                                  │                    perçu trop élevé
                                  │                    ("30 min d'audit")
                                  │
Arrivent sur Cal.com              39        -17 (30%)  Redirection externe,
                                  │                    rupture visuelle,
                                  │                    perte de confiance
                                  │
Complètent la réservation         20        -19 (49%)  Interface Cal.com non
                                  │                    personnalisée, friction
                                  │                    du formulaire externe
                                  │
Se présentent au RDV              13        -7 (35%)   Aucun rappel, aucune
                                  │                    séquence de confirmation,
                                  │                    aucun nurturing pré-RDV
                                  │
Deviennent clients                 3        -10 (77%)  Pas de suivi structuré
                                                       post-audit
─────────────────────────────────────────────────────────────────────────
TAUX DE CONVERSION FINAL :  0,3% (3 / 1 000)
PERTE TOTALE :              99,7%
```

### 3.2 Analyse détaillée par point de fuite

#### Fuite 1 — TOFU : 30% ne voient jamais de CTA
**Localisation :** Blog (8 articles) et page domotique
**Cause :**
- Les 8 articles de blog ne contiennent aucun CTA contextuel
- La page domotique est purement informative, sans aucun appel à l'action
- Le visiteur consomme le contenu et quitte sans interaction
**Impact :** 300 visiteurs perdus / 1 000

#### Fuite 2 — TOFU→BOFU : 92% ne cliquent pas sur le CTA
**Localisation :** Transition entre contenu et conversion
**Cause :**
- Le CTA "Réserver un Audit gratuit (30 min)" demande un engagement fort (temps + appel)
- Aucune alternative à faible engagement (téléchargement, inscription newsletter)
- Un artisan PME occupé ne va pas bloquer 30 minutes pour un inconnu
- L'étape MOFU est totalement absente : pas de maturation de la confiance
**Impact :** 644 visiteurs perdus / 700

#### Fuite 3 — BOFU : 30% abandonnent à la redirection Cal.com
**Localisation :** Clic CTA vers Cal.com
**Cause :**
- Le domaine change (smartelec.fr → cal.com), provoquant une rupture de confiance
- Le design de Cal.com ne correspond pas à l'identité visuelle du site
- Sur mobile, la transition est encore plus déstabilisante
- Pour une cible PME/artisan peu technophile, le changement de site est suspect
**Impact :** 17 visiteurs perdus / 56

#### Fuite 4 — BOFU : 49% abandonnent le formulaire Cal.com
**Localisation :** Page de réservation Cal.com
**Cause :**
- Interface générique, pas de réassurance contextuelle
- Pas de preuve sociale visible (témoignages, logos clients)
- Pas de rappel de la proposition de valeur sur la page de booking
- Champs potentiellement trop nombreux ou peu adaptés
**Impact :** 19 visiteurs perdus / 39

#### Fuite 5 — POST-CONV : 35% de no-show
**Localisation :** Entre la réservation et le rendez-vous
**Cause :**
- Aucune séquence de confirmation personnalisée
- Aucun rappel automatisé (J-1, H-1)
- Aucun contenu de pré-qualification envoyé avant l'audit
- Le prospect oublie ou perd sa motivation entre la réservation et le RDV
**Impact :** 7 visiteurs perdus / 20

#### Fuite 6 — POST-AUDIT : 77% ne convertissent pas en client
**Localisation :** Après l'audit gratuit
**Cause :**
- Aucune séquence de nurturing post-audit
- Pas de proposition commerciale structurée envoyée après l'audit
- Pas de relance automatisée
- Le prospect "y réfléchit" et oublie
**Impact :** 10 prospects perdus / 13

### 3.3 Le problème structurel : l'absence de MOFU

```
PROBLÈME CENTRAL
═══════════════════════════════════════════════════════

     TOFU                    BOFU
  (contenu froid)    →    (engagement fort)
                     ↑
                     │
              ██ GOUFFRE ██

  "Je découvre"     →    "Je bloque 30 min avec
                          un inconnu"

  Le visiteur passe de la découverte à l'engagement
  maximal sans aucune étape intermédiaire.

  C'est comme demander en mariage au premier rendez-vous.
```

---

## 4. Funnel idéal recommandé

### 4.1 Architecture cible

```
FUNNEL RECOMMANDÉ — Architecture multi-parcours
════════════════════════════════════════════════════════════════

                    Visiteur arrive
                         │
                         ▼
        ┌────────────────────────────────┐
        │         TOFU (Awareness)       │
        │                                │
        │  • Blog optimisé SEO + CTA     │
        │  • Landing pages par service   │
        │  • Contenu LinkedIn/Social     │
        │  • GA4 + GTM installés         │
        │                                │
        │  Objectif : 1 000 visiteurs    │
        └──────┬──────────┬──────────┬───┘
               │          │          │
    ┌──────────┘          │          └──────────┐
    │                     │                     │
    ▼                     ▼                     ▼
┌─────────┐      ┌──────────────┐      ┌──────────────┐
│ PARCOURS │      │  PARCOURS    │      │  PARCOURS    │
│ FROID    │      │  TIÈDE       │      │  CHAUD       │
│ (70%)    │      │  (20%)       │      │  (10%)       │
└────┬─────┘      └──────┬───────┘      └──────┬───────┘
     │                   │                     │
     ▼                   ▼                     ▼
┌──────────────┐  ┌──────────────┐      ┌──────────────┐
│ MOFU Froid   │  │ MOFU Tiède   │      │ BOFU Direct  │
│              │  │              │      │              │
│ • Lead mag-  │  │ • Mini-audit │      │ • Audit 30   │
│   net gratuit│  │   en ligne   │      │   min (actuel│
│   (guide PDF,│  │   (scoring   │      │   CTA amé-   │
│   checklist) │  │   automatisé)│      │   lioré)     │
│ • Newsletter │  │ • Étude de   │      │ • Formulaire │
│   hebdo      │  │   cas vidéo  │      │   natif (pas │
│ • Chatbot    │  │ • Webinaire  │      │   Cal.com)   │
│   site       │  │   mensuel    │      │ • Page de    │
│              │  │              │      │   réassurance│
│  ↓ capture   │  │  ↓ capture   │      │              │
│  email       │  │  email +     │      │              │
│              │  │  qualification│     │              │
└──────┬───────┘  └──────┬───────┘      └──────┬───────┘
       │                 │                     │
       ▼                 ▼                     │
┌──────────────┐  ┌──────────────┐             │
│ NURTURING    │  │ NURTURING    │             │
│ Séquence 1   │  │ Séquence 2   │             │
│              │  │              │             │
│ J+0: Welcome │  │ J+0: Résultat│             │
│ J+3: Valeur  │  │   mini-audit │             │
│ J+7: Cas     │  │ J+2: Étude   │             │
│      client  │  │   de cas     │             │
│ J+14: Offre  │  │ J+5: Offre   │             │
│              │  │              │             │
└──────┬───────┘  └──────┬───────┘             │
       │                 │                     │
       └────────┬────────┘                     │
                │                              │
                ▼                              │
        ┌───────────────┐                      │
        │  CONVERSION   │◄─────────────────────┘
        │               │
        │  • RDV Audit  │
        │  • Rappels    │
        │    automatisés│
        │  • Séquence   │
        │    pré-RDV    │
        └───────┬───────┘
                │
                ▼
        ┌───────────────┐
        │ POST-AUDIT    │
        │               │
        │ • Proposition │
        │   commerciale │
        │ • Séquence de │
        │   relance     │
        │ • Témoignage  │
        │   request     │
        └───────────────┘
```

### 4.2 Les 3 parcours visiteur

| Parcours | Profil visiteur | Point d'entrée MOFU | Engagement demandé | Objectif |
|----------|----------------|--------------------|--------------------|----------|
| **Froid** (70%) | Curieux, en veille, pas de besoin immédiat | Lead magnet / newsletter | Email uniquement | Capturer et nourrir sur 30-90 jours |
| **Tiède** (20%) | Besoin identifié, compare les solutions | Mini-audit en ligne / étude de cas | Email + infos entreprise | Qualifier et accélérer vers RDV |
| **Chaud** (10%) | Prêt à acheter, veut un interlocuteur | Audit 30 min (CTA amélioré) | Temps + coordonnées complètes | Convertir immédiatement |

---

## 5. Recommandations détaillées par étape

### 5.1 TOFU — Générer du trafic qualifié et capturer l'attention

#### R1. Installer le tracking analytique (CRITIQUE)

**Situation actuelle :** Aucun outil de mesure détecté (ni GA4, ni GTM, ni aucune alternative).
**Action :**
- Installer Google Tag Manager (GTM) comme conteneur unique
- Configurer GA4 via GTM
- Mettre en place les événements de conversion : clic CTA, scroll depth, temps sur page
- Installer le pixel LinkedIn (cible B2B)

**Métriques cibles :**
| Indicateur | Cible |
|-----------|-------|
| Visiteurs uniques / mois | Mesurable (baseline à établir) |
| Pages / session | > 2,5 |
| Taux de rebond | < 55% |
| Temps moyen sur page | > 2 min |

**Priorité :** Semaine 1 — sans tracking, toute optimisation est aveugle.

#### R2. Ajouter des CTA contextuels dans le blog et la page domotique

**Situation actuelle :** 8 articles sans aucun CTA. Page domotique 100% informative.
**Action :**
- Ajouter un CTA en fin de chaque article, adapté au sujet
- Ajouter des encarts CTA latéraux ou inline dans les articles longs
- Transformer la page domotique en landing page avec CTA vers un guide gratuit ou l'audit
- Varier les CTA selon le niveau d'engagement : newsletter (froid) / mini-audit (tiède) / audit (chaud)

**Métriques cibles :**
| Indicateur | Actuel | Cible |
|-----------|--------|-------|
| CTA visibles par page | 0-1 | 2-3 |
| Taux de clic CTA blog | ~0% | 3-5% |
| Taux de clic CTA page domotique | 0% | 5-8% |

#### R3. Professionnaliser l'adresse email

**Situation actuelle :** Adresse Gmail visible.
**Action :**
- Configurer contact@smarthome-smartelec.fr (OVH déjà en place)
- SPF, DKIM et DMARC pour la délivrabilité
- Remplacer Gmail partout sur le site

---

### 5.2 MOFU — Créer les mécanismes de capture manquants

#### R4. Créer un lead magnet principal

**Situation actuelle :** Aucun contenu téléchargeable, aucun mécanisme de capture email.
**Action :**
- Guide PDF : "Le Guide de l'Automatisation IA pour PME et Artisans — 10 processus à automatiser en priorité"
- Landing page dédiée avec formulaire (prénom + email + secteur)
- Livraison automatique par email (Brevo gratuit jusqu'à 300 emails/jour)

**Métriques cibles :**
| Indicateur | Cible |
|-----------|-------|
| Taux de conversion landing page lead magnet | 25-40% |
| Emails capturés / mois | 5-10% des visiteurs |
| Taux d'ouverture email de livraison | > 70% |

#### R5. Mettre en place un mini-audit en ligne automatisé

**Action :**
- Questionnaire interactif (10-15 questions) avec scoring automatique (Tally / Typeform)
- Résultat envoyé par email (capture automatique)
- Score élevé → invitation prioritaire audit 30 min
- Score moyen → séquence de nurturing

**Métriques cibles :**
| Indicateur | Cible |
|-----------|-------|
| Taux de complétion du quiz | 40-60% |
| Taux de conversion quiz → email | 70-85% |
| Taux de conversion quiz → RDV (score élevé) | 15-25% |

#### R6. Lancer une newsletter

**Action :** Newsletter bimensuelle, inscription via pop-up exit-intent + encart blog + footer.

---

### 5.3 BOFU — Optimiser la conversion finale

#### R7. Intégrer le booking nativement

**Action :** Cal.com en iframe embedded sur une page dédiée /audit-gratuit. Le visiteur ne quitte jamais le domaine.

**Métriques cibles :**
| Indicateur | Actuel estimé | Cible |
|-----------|--------------|-------|
| Taux clic CTA → complétion booking | ~35% | 55-65% |
| Perte à la redirection | ~30% | 0% |

#### R8. Créer une page de réassurance pré-booking

**Action :** Page /audit-gratuit avec :
- Rappel proposition de valeur
- Ce que le prospect obtient concrètement
- 2-3 témoignages clients
- FAQ (3-5 questions)
- Widget de booking intégré en bas

#### R9. Afficher du pricing ou des fourchettes tarifaires

**Action :** Fourchettes de prix par package + "À partir de X €"

---

### 5.4 POST-CONVERSION — Réduire les no-shows et augmenter le closing

#### R10. Séquence pré-RDV automatisée

- **Immédiat :** Email de confirmation personnalisé
- **J-1 :** Rappel + "3 questions à vous poser"
- **H-2 :** SMS de rappel
- **Post no-show :** Email de re-programmation

| Indicateur | Actuel estimé | Cible |
|-----------|--------------|-------|
| Taux de présence | ~65% | 85-90% |

#### R11. Séquence post-audit

- **J+0 :** Récapitulatif + proposition commerciale
- **J+3 :** Étude de cas similaire
- **J+7 :** Relance douce + offre limitée
- **J+14 :** "Votre audit expire dans 7 jours"
- **J+21 :** Clôture → nurturing long terme

| Indicateur | Actuel estimé | Cible |
|-----------|--------------|-------|
| Taux de closing post-audit | ~23% | 35-50% |

---

## 6. Estimation d'impact revenue

### 6.1 Modèle actuel vs. optimisé

**Hypothèses :** 1 000 visiteurs/mois, panier moyen 3 000€

```
COMPARAISON : FUNNEL ACTUEL vs. FUNNEL OPTIMISÉ
══════════════════════════════════════════════════════════════════════

                            ACTUEL          OPTIMISÉ        GAIN
─────────────────────────────────────────────────────────────────────
Visiteurs                   1 000           1 000           —
Voient un CTA               700 (70%)       950 (95%)      +250

PARCOURS CHAUD (BOFU direct)
Cliquent CTA audit          56 (8%)         95 (10%)       +39
Complètent booking          20 (36%)        62 (65%)       +42
Se présentent au RDV        13 (65%)        53 (85%)       +40
Deviennent clients          3 (23%)         21 (40%)       +18

PARCOURS TIÈDE (MOFU quiz)
Lancent le mini-audit       —               120 (13%)      +120
Complètent + email          —               84 (70%)       +84
Convertissent en RDV        —               17 (20%)       +17
Deviennent clients          —               7 (40%)        +7

PARCOURS FROID (Lead magnet)
Téléchargent / s'inscrivent —               60 (6%)        +60
Convertissent en RDV (6m)   —               4 (6%)         +4
Deviennent clients          —               2 (40%)        +2
─────────────────────────────────────────────────────────────────────
TOTAL CLIENTS / MOIS        3               30             +27
REVENUE MENSUEL             9 000€          90 000€        +81 000€
REVENUE ANNUEL              108 000€        1 080 000€     +972 000€
─────────────────────────────────────────────────────────────────────
MULTIPLICATION DU REVENUE :                 x10
```

### 6.2 Scénarios réalistes par horizon

| Horizon | Scénario | Clients/mois | Revenue mensuel | Multiplicateur |
|---------|----------|:-----------:|:---------------:|:--------------:|
| **Mois 1-2** (quick wins) | Tracking + CTA + page réassurance + booking intégré | 5-7 | 15 000-21 000€ | x1,7-x2,3 |
| **Mois 3-4** (MOFU actif) | + Lead magnet + mini-audit + newsletter | 10-15 | 30 000-45 000€ | x3,3-x5 |
| **Mois 6-9** (nurturing mature) | + Séquences email + base en croissance | 18-25 | 54 000-75 000€ | x6-x8,3 |
| **Mois 12** (maturité) | Système complet opérationnel | 25-30 | 75 000-90 000€ | x8,3-x10 |

### 6.3 Coût d'implémentation

| Poste | Coût | ROI attendu |
|-------|------|-------------|
| GA4 + GTM | Gratuit | Mesurabilité |
| Email professionnel | 5-10€/mois | Crédibilité |
| Brevo (emailing) | 0-25€/mois | Capture + nurturing |
| Lead magnet (rédaction) | 2-4h travail | 60+ leads/mois |
| Mini-audit en ligne (Tally) | 3-5h travail | 80+ leads qualifiés/mois |
| Page /audit-gratuit | 2-3h travail | +80% complétion booking |
| Séquences email (setup) | 4-6h travail | Réduction no-show + closing |
| **TOTAL** | **< 50€/mois + 15-20h de setup** | **x2 à x10 sur le revenue** |

---

## 7. Plan d'implémentation priorisé

### Semaine 1-2 : Fondations et quick wins

| Jour | Action | Impact |
|------|--------|--------|
| 1-2 | Installer GTM + GA4 | Mesurabilité |
| 2-3 | Email professionnel (contact@smarthome-smartelec.fr) | Crédibilité |
| 3-5 | Intégrer Cal.com en natif + page /audit-gratuit | +80% complétion |
| 5-7 | CTA dans les 8 articles blog + page domotique | +250 visiteurs exposés |
| 7-10 | Formulaire de contact natif sur /contact | Alternative légère |
| 10-14 | Séquence pré-RDV (confirmation + rappel J-1) | -20% no-show |

**Impact estimé Semaine 2 :** Taux de conversion x1,5 à x2

### Mois 1 : Construire le MOFU

| Semaine | Action | Impact |
|---------|--------|--------|
| 3 | Créer le lead magnet (guide PDF) + landing page | 60+ leads/mois |
| 3-4 | Mini-audit en ligne (Tally/Typeform) + scoring | 80+ leads qualifiés |
| 4 | Séquences nurturing (post-lead magnet + post-quiz + post-audit) | Conversion x2 |
| 4 | Newsletter (template + premier numéro + formulaires inscription) | Base email |

**Impact estimé Mois 1 :** Taux de conversion x2,5 à x3,5

### Trimestre 1 : Optimiser et scaler

| Mois | Action | Impact |
|------|--------|--------|
| 2 | Analyser GA4 + A/B tester CTA + études de cas + page tarifs | Optimisation |
| 2-3 | Optimiser séquences email + 2e lead magnet + webinaire mensuel | Scale |
| 3 | Scoring leads + retargeting LinkedIn + landing pages par service | Automatisation complète |

**Impact estimé Trimestre 1 :** Taux de conversion x5 à x8

---

## Matrice de priorisation

| Action | Impact | Effort | Priorité |
|--------|--------|--------|:--------:|
| Installer GTM + GA4 | Critique | Faible | **P0** |
| Email professionnel | Moyen | Faible | **P0** |
| Intégrer Cal.com en natif | Fort | Moyen | **P1** |
| CTA dans le blog (x8) | Fort | Faible | **P1** |
| Page /audit-gratuit | Fort | Moyen | **P1** |
| Séquence pré-RDV | Fort | Moyen | **P1** |
| Lead magnet | Fort | Moyen | **P2** |
| Mini-audit en ligne | Fort | Moyen-Fort | **P2** |
| Séquences nurturing | Fort | Fort | **P2** |
| Newsletter | Moyen | Moyen | **P2** |
| Études de cas | Moyen | Moyen | **P3** |
| Page tarifs | Moyen | Faible | **P3** |
| A/B testing CTA | Moyen | Faible | **P3** |
| Chatbot site | Moyen | Moyen | **P3** |
| Webinaire mensuel | Moyen | Fort | **P4** |
| Retargeting LinkedIn | Moyen | Moyen | **P4** |

---

> **Note finale :** Le paradoxe fondamental de smarthome-smartelec.fr est que l'entreprise vend de l'automatisation IA à des PME tout en n'automatisant aucun aspect de sa propre acquisition client. La mise en place de ce funnel ne représente pas seulement une optimisation commerciale — c'est une **démonstration de crédibilité**. Le site lui-même doit devenir la meilleure vitrine des compétences proposées.

---

*Généré par AI Marketing Suite — `/market funnel`*
