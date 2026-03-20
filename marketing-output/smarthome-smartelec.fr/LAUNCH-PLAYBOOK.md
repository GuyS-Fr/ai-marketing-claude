# Playbook de Lancement / Relancement
## SMARTHOME SMARTELEC — smarthome-smartelec.fr
### Services B2B d'automatisation IA pour PME et artisans — Drôme
### Date : 20 mars 2026

---

## Sommaire

1. [Phase 0 — Préparation (Semaine 0)](#phase-0--préparation-semaine-0)
2. [Phase 1 — Fondation (Semaines 1-2)](#phase-1--fondation-semaines-1-2)
3. [Phase 2 — Construction (Semaines 3-4)](#phase-2--construction-semaines-3-4)
4. [Phase 3 — Activation (Mois 2)](#phase-3--activation-mois-2)
5. [Phase 4 — Scale (Mois 3)](#phase-4--scale-mois-3)
6. [KPIs et jalons par phase](#kpis-et-jalons-par-phase)
7. [Budget estimé par phase](#budget-estimé-par-phase)
8. [Risques et mitigation](#risques-et-mitigation)

---

## Situation de Départ

| Indicateur | Valeur actuelle |
|---|---|
| **Score marketing global** | 32/100 (Grade F) |
| **Score GEO** | 18/100 |
| **Content & Messaging** | 38/100 |
| **Conversion** | 22/100 |
| **SEO** | 38/100 |
| **Competitive** | 32/100 |
| **Brand & Trust** | 32/100 |
| **Growth & Strategy** | 28/100 |
| **CA estimé actuel** | ~3 000 €/mois |
| **Liste email** | 0 contact |
| **Preuve sociale** | 0 témoignage, 0 avis Google |
| **LinkedIn** | Inactif |

**Diagnostic en une phrase :** Un avantage concurrentiel structurel réel (triple légitimité artisan + consultant SI + expert IA) totalement invisible en ligne, sur un marché de niche quasi vierge en Drôme-Ardèche.

**Objectif global à 90 jours :** Passer de 32/100 à 55-65/100 en score marketing et de ~3 000 € à 14 000-24 000 €/mois de CA.

---

## Phase 0 — Préparation (Semaine 0)

**Objectif :** Valider les prérequis, rassembler les ressources, planifier l'exécution.

### Checklist prérequis

#### Stratégie et positionnement
- [ ] Valider le positionnement cible : "Automatisation IA pour artisans et PME de services"
- [ ] Définir le persona principal : artisan/gérant PME, 1-15 salariés, 10+ h/semaine sur l'admin, Drôme puis France
- [ ] Rédiger la déclaration de positionnement :
  > "Pour les artisans et gérants de PME de services qui passent trop de temps sur la paperasse, SMARTHOME SMARTELEC configure des systèmes d'automatisation IA qui font le travail administratif à votre place. Contrairement aux agences digitales classiques, nous combinons une expérience terrain d'artisan, un parcours de consultant SI/CRM en grand groupe et des outils open-source hébergés en Europe que vous contrôlez."
- [ ] Lister 3-5 cas d'usage prioritaires à illustrer (devis, relances, chatbot, facturation, planning)
- [ ] Décider du modèle tarifaire : forfait projet + maintenance mensuelle

#### Ressources techniques
- [ ] Vérifier l'accès admin au site WordPress + OVH
- [ ] Vérifier les accès n8n, Airtable/NocoDB, Supabase, Softr
- [ ] S'assurer que Cal.com est configuré avec les bons créneaux
- [ ] Préparer un environnement de test pour le funnel email (n8n + Airtable)

#### Ressources créatives
- [ ] Planifier une séance photo professionnelle de Guy (ou smartphone + trépied en B-plan)
- [ ] Collecter tout résultat chiffré de projets passés (même domotique)
- [ ] Lister les contacts existants : anciens clients, partenaires, prescripteurs
- [ ] Préparer 2-3 études de cas anonymisées (résultats avant/après)

#### Administratif
- [ ] Créer l'email professionnel contact@smarthome-smartelec.fr (OVH, inclus)
- [ ] Vérifier la conformité RGPD du site (mentions légales, politique de confidentialité, cookies)
- [ ] Préparer un devis-type et un contrat de prestation standard

**Livrable Phase 0 :** Document de brief validé, accès techniques vérifiés, ressources rassemblées.

**Durée estimée :** 2-3 jours de travail effectif.

---

## Phase 1 — Fondation (Semaines 1-2)

**Objectif :** Corriger les quick wins techniques et poser les bases du branding.

### Quick wins techniques — Site web (PRIORITÉ ABSOLUE)

#### Jour 1-2 : Corrections CRO critiques
- [ ] Réécrire le headline H1 : "Vous passez vos soirées sur les devis ? On automatise tout — vous récupérez vos week-ends."
- [ ] Réécrire le sous-titre : "Automatisation des devis, relances et service client pour artisans et PME — configurée en 2-4 semaines."
- [ ] Supprimer "Nous changeons de cap" du hero (message interne, pas commercial)
- [ ] Embed Cal.com en inline (widget intégré, pas de redirection externe)
- [ ] Ajouter l'anti-risque sous le CTA : "Sans engagement. Vous repartez avec un plan d'action concret, même si on ne travaille pas ensemble."
- [ ] Rendre le numéro de téléphone cliquable (balise `tel:`)

#### Jour 2-3 : Nettoyage navigation et SEO technique
- [ ] Purger la navigation : retirer alarme, domotique, électricité, maintien à domicile
- [ ] Rediriger les anciennes pages en 301 vers la homepage
- [ ] Rédiger les meta descriptions manquantes (homepage, blog, pages clés)
- [ ] Ajouter les attributs `alt` sur toutes les images
- [ ] Corriger le copyright "AI Automation" en "SMARTHOME SMARTELEC"
- [ ] Supprimer l'article en anglais ou ajouter hreflang
- [ ] Ajouter le schema LocalBusiness JSON-LD (Rank Math)

#### Jour 3-4 : Infrastructure de conversion
- [ ] Installer Google Analytics 4 avec événements de conversion (clic CTA, booking complété)
- [ ] Installer Google Search Console et soumettre le sitemap
- [ ] Installer le pixel Facebook
- [ ] Installer le LinkedIn Insight Tag
- [ ] Créer le formulaire de capture email (prénom + email) via n8n + Airtable
- [ ] Configurer le popup exit-intent avec lead magnet

### Quick wins branding

#### Jour 4-5 : Identité et preuve sociale
- [ ] Photo professionnelle de Guy (accessible mais pro)
- [ ] Créer / revendiquer le profil Google Business (catégorie : Consultant en informatique)
- [ ] Demander 2-3 avis Google à d'anciens clients satisfaits (même domotique)
- [ ] Solliciter 2-3 témoignages écrits pour le site
- [ ] Rédiger l'étude de cas #1 : artisan chauffagiste, réduction du temps de devis de 45 min à 12 min
- [ ] Ajouter sur le site : section "Pourquoi me faire confiance" avec la triple légitimité

#### Jour 5-7 : Lead magnet et séquence email
- [ ] Rédiger le lead magnet PDF : "10 tâches que l'IA peut automatiser dans votre PME cette semaine" (8-12 pages)
- [ ] Créer le design sur Canva (simple, pro, pas surchargé)
- [ ] Configurer la séquence email de bienvenue (7 emails via n8n) :
  - E1 (J+0) : Livraison du PDF + présentation de Guy
  - E2 (J+2) : Étude de cas artisan chauffagiste
  - E3 (J+4) : "3 erreurs que font les artisans avec l'automatisation"
  - E4 (J+7) : FAQ — coûts, délais, RGPD
  - E5 (J+10) : Témoignage client
  - E6 (J+14) : "Votre entreprise est-elle prête pour l'automatisation ?" (quiz)
  - E7 (J+21) : Invitation audit gratuit (CTA final)

**Livrables Phase 1 :**
- Site web corrigé (11 quick wins CRO)
- Google Business actif avec 2-3 avis
- Lead magnet PDF finalisé + formulaire opérationnel
- Séquence de 7 emails programmée
- Étude de cas #1 publiée
- Photo pro de Guy disponible
- Tracking GA4 + Facebook Pixel + LinkedIn Tag installés

**Impact estimé :** Conversion site x2-3 (de ~1% à 2-3%), score marketing +10-15 points.

---

## Phase 2 — Construction (Semaines 3-4)

**Objectif :** Construire le funnel complet, créer les lead magnets secondaires, et produire le contenu fondateur.

### Funnel de conversion

#### Pages et assets à créer
- [ ] Créer la landing page `/audit-gratuit` dédiée :
  - Headline : "30 minutes pour identifier vos 3 gains rapides en automatisation"
  - 3 bénéfices concrets
  - Cal.com embedded
  - Témoignage + anti-risque
  - FAQ 6-8 questions
- [ ] Créer la page `/tarifs` avec grille indicative :
  - Audit découverte : Gratuit (30 min)
  - Pack Démarrage : à partir de 500 € (1-2 automatisations)
  - Pack Croissance : à partir de 1 500 € (système complet)
  - Maintenance : à partir de 150 €/mois
- [ ] Créer la page `/cas-clients` avec études de cas structurées
- [ ] Créer la page `/a-propos` avec le parcours de Guy et la triple légitimité
- [ ] Créer la FAQ complète (8-10 questions clés)

#### Lead magnets secondaires
- [ ] Checklist PDF : "Audit express : 15 questions pour évaluer votre maturité digitale" (en échange d'un email)
- [ ] Calculateur en ligne : "Combien d'heures par semaine pourriez-vous récupérer ?" (Softr + Airtable)
- [ ] Mini-vidéo (2-3 min) : "Comment fonctionne un workflow d'automatisation n8n" (screen recording)

### Contenu fondateur

#### Blog — 4 articles SEO à rédiger
- [ ] "Automatisation pour artisans : par où commencer ? (Guide complet 2026)"
  → Mot-clé : automatisation artisan PME
- [ ] "n8n vs Make vs Zapier : quel outil d'automatisation choisir pour une PME ?"
  → Mot-clé : comparatif automatisation PME
- [ ] "Comment un chatbot IA peut répondre à vos clients 24/7 (même le dimanche)"
  → Mot-clé : chatbot PME artisan
- [ ] "RGPD et IA : 6 questions à poser à votre prestataire avant de signer"
  → Mot-clé : RGPD automatisation données

#### Pages locales SEO
- [ ] Créer `/automatisation-valence` — "Automatisation IA pour PME à Valence et en Drôme"
- [ ] Créer `/automatisation-drome-ardeche` — "Expert automatisation IA Drôme-Ardèche"

### Funnel email avancé
- [ ] Configurer les relances automatiques post-audit non converti (J+3, J+7 via n8n)
- [ ] Créer la séquence de nurturing pour les leads "froids" (téléchargement lead magnet mais pas de booking)
- [ ] Tester le funnel complet bout en bout : visite → lead magnet → email → booking → confirmation

**Livrables Phase 2 :**
- Landing page `/audit-gratuit` live
- Page `/tarifs` avec grille indicative
- 4 articles de blog SEO publiés
- 2 pages locales SEO créées
- 2 lead magnets secondaires opérationnels
- Funnel email avancé configuré
- Calculateur en ligne fonctionnel

**Impact estimé :** Score marketing +10-12 points, premiers leads organiques, taux de conversion funnel 5-10%.

---

## Phase 3 — Activation (Mois 2)

**Objectif :** Activer LinkedIn comme canal principal, renforcer le SEO local, et développer les partenariats.

### LinkedIn — Canal n°1

#### Semaine 5-6 : Lancement LinkedIn
- [ ] Optimiser le profil LinkedIn de Guy :
  - Photo pro
  - Bannière personnalisée "Automatisation IA pour artisans et PME"
  - Titre : "J'aide les artisans et PME à récupérer 10h/semaine grâce à l'automatisation IA | n8n • Airtable • Chatbots"
  - Section "À propos" avec la triple légitimité + CTA audit gratuit
  - Section "Sélection" avec lead magnet + étude de cas
- [ ] Publier 3-5 posts/semaine selon le calendrier éditorial :
  - **Lundi** : Post "douleur" (résonance avec le quotidien artisan)
  - **Mercredi** : Post éducatif (astuce, comparatif, tutoriel)
  - **Vendredi** : Post preuve (étude de cas, témoignage, résultat chiffré)
- [ ] Engager quotidiennement : 15-20 min de commentaires sur des posts de la cible
- [ ] Envoyer 5-10 messages personnalisés/semaine aux prospects qualifiés

#### Calendrier de posts LinkedIn — Semaines 5-8

| Semaine | Post 1 (Lundi) | Post 2 (Mercredi) | Post 3 (Vendredi) |
|---|---|---|---|
| S5 | "Un plombier m'a dit : je passe plus de temps sur mes devis que sous les éviers." | Carrousel : "5 tâches qu'un artisan peut automatiser cette semaine" | Étude de cas chauffagiste : 45 min → 12 min par devis |
| S6 | "Pourquoi un ancien électricien parle d'IA en 2026" | "Zapier, Make, n8n — lequel choisir pour une PME ?" | Sondage : "Combien d'heures/semaine sur l'administratif ?" |
| S7 | "La plupart des artisans n'ont PAS besoin d'un site web refait." | "RGPD : 6 questions à poser avant de choisir un prestataire IA" | Annonce : "3 places ouvertes pour mai — offre de lancement" |
| S8 | Post de lancement officiel | Étude de cas #2 avec résultats | "Il reste 1 place — voici ce que ça inclut" |

### SEO local

- [ ] Optimiser le profil Google Business : description, photos, catégories, horaires, zone de service
- [ ] Publier 1 Google Post/semaine (offre, article, actualité)
- [ ] S'inscrire sur les annuaires locaux : PagesJaunes, Yelp, Malt, CyberMalveillance.gouv.fr
- [ ] Demander systématiquement un avis Google après chaque audit gratuit
- [ ] Cibler 5 avis Google d'ici la fin du mois 2

### Partenariats prescripteurs

- [ ] Contacter 3 experts-comptables locaux (Valence, Romans, Montélimar) :
  > "Vos clients artisans perdent du temps sur la gestion administrative. Je configure des systèmes d'automatisation qui leur font gagner 10h/semaine. Si ça intéresse l'un de vos clients, je lui offre un audit de 30 min — et je vous reverse 10% du premier projet."
- [ ] Contacter la CCI de la Drôme (ateliers numériques, label France Num)
- [ ] Contacter la CAPEB Drôme pour intervention lors d'une réunion adhérents
- [ ] S'inscrire sur Malt.fr comme expert n8n / automatisation / Drôme
- [ ] Candidater au label France Num — Activateur numérique

### Email marketing

- [ ] Envoyer 1 newsletter/semaine à la liste (condensé du meilleur post LinkedIn + lien article blog)
- [ ] Lancer la campagne de pré-lancement (2 emails teasing avant la semaine de lancement officiel)
- [ ] Configurer le programme de parrainage : "Recommandez un artisan → 1 mois de maintenance offert"

**Livrables Phase 3 :**
- Profil LinkedIn optimisé + 12-15 posts publiés
- 100-200 abonnés LinkedIn
- Google Business optimisé avec 5+ avis
- 3+ contacts prescripteurs actifs
- Profil Malt créé
- Candidature France Num envoyée
- Newsletter hebdomadaire lancée

**Impact estimé :** 5-15 conversations qualifiées/mois, score marketing +8-10 points, 10-30 leads email.

---

## Phase 4 — Scale (Mois 3)

**Objectif :** Lancer les campagnes payantes, systématiser le content marketing, et commencer la productisation.

### Publicité payante

#### Google Ads — Budget 200-500 €/mois
- [ ] Campagne Search — Requêtes haute intention :
  - "automatisation PME [ville]" (Valence, Romans, Montélimar, Grenoble, Lyon)
  - "chatbot artisan"
  - "automatisation devis factures"
  - "consultant IA PME"
- [ ] Campagne Search — Requêtes locales :
  - "consultant informatique Valence"
  - "digitalisation PME Drôme"
  - "transformation numérique artisan"
- [ ] Landing page dédiée par groupe d'annonces (reprendre `/audit-gratuit` avec variantes)
- [ ] CPA cible : 30-50 € par audit booké

#### Facebook/Instagram Ads — Budget 100-300 €/mois
- [ ] Campagne retargeting : visiteurs du site qui n'ont pas booké
- [ ] Campagne lookalike : basée sur les visiteurs du site et la liste email
- [ ] Créatives : vidéo témoignage + carrousel résultats + image avant/après

#### LinkedIn Ads — Budget 50-150 €/mois
- [ ] Booster les 2-3 meilleurs posts organiques
- [ ] Ciblage : gérants de PME, artisans, Drôme-Ardèche-Isère-Rhône

### Content marketing systématisé

- [ ] Publier 2 articles de blog/mois (SEO long-tail)
- [ ] Créer les pages "versus" : `/vs/make-com`, `/vs/zapier`, `/vs/agence-web-classique`
- [ ] Publier 1 étude de cas/mois (avec résultats chiffrés des clients de mai-juin)
- [ ] Lancer une série vidéo courte (2-3 min) : "1 automatisation en 3 minutes"
- [ ] Créer un webinaire mensuel : "Comment automatiser votre PME sans coder" (en partenariat CCI si possible)

### Productisation de l'offre

- [ ] Créer des "packs" standardisés avec périmètre et tarif fixe :
  - **Pack Devis Express** (500-800 €) : automatisation devis + relances
  - **Pack Chatbot 24/7** (800-1 200 €) : chatbot site + FAQ automatique
  - **Pack Gestion Complète** (1 500-3 000 €) : CRM + devis + factures + chatbot + relances
  - **Maintenance** : 150-300 €/mois selon le pack
- [ ] Créer les fiches produit correspondantes sur le site
- [ ] Automatiser le processus d'onboarding client (questionnaire Softr + workflow n8n)

### Expansion géographique

- [ ] Créer les pages SEO régionales : `/automatisation-lyon`, `/automatisation-grenoble`, `/automatisation-auvergne-rhone-alpes`
- [ ] Tester Google Ads sur Lyon et Grenoble (si les résultats Drôme sont positifs)
- [ ] Prospecter les réseaux d'artisans régionaux (CAPEB AURA, FFB, CNAMS)

**Livrables Phase 4 :**
- Campagnes Google Ads + Facebook Ads + LinkedIn Ads actives
- 4+ articles de blog publiés (total : 8+)
- Pages "versus" et pages régionales créées
- Packs productisés avec fiches sur le site
- Webinaire lancé
- Processus d'onboarding automatisé

**Impact estimé :** 10-25 leads qualifiés/mois, 5-10 audits/mois, 3-8 clients signés/mois, CA 14 000-24 000 €/mois.

---

## KPIs et jalons par phase

### Tableau récapitulatif

| KPI | Phase 0 | Phase 1 (S1-2) | Phase 2 (S3-4) | Phase 3 (Mois 2) | Phase 4 (Mois 3) |
|---|---|---|---|---|---|
| **Score marketing** | 32/100 | 42-47/100 | 52-57/100 | 58-65/100 | 65-75/100 |
| **Visites site/mois** | ~100 | 150-250 | 300-500 | 500-1 000 | 1 000-2 500 |
| **Leads email** | 0 | 10-20 | 30-60 | 60-120 | 120-250 |
| **Audits bookés/mois** | 0-1 | 3-5 | 5-8 | 8-15 | 15-25 |
| **Clients signés/mois** | 0 | 1-2 | 2-4 | 3-6 | 5-10 |
| **CA mensuel** | ~3 000 € | 4 000-6 000 € | 6 000-10 000 € | 10 000-16 000 € | 14 000-24 000 € |
| **Avis Google** | 0 | 2-3 | 4-6 | 6-10 | 10-15 |
| **Abonnés LinkedIn** | 0 | 50-100 | 100-200 | 200-500 | 500-1 000 |
| **Articles blog** | 0 | 0 | 4 | 6 | 8+ |

### Jalons critiques (go/no-go)

| Jalon | Date cible | Critère de succès | Action si non atteint |
|---|---|---|---|
| Site web corrigé | Fin S2 | 11 corrections CRO appliquées | Reporter le lancement LinkedIn |
| Premier lead email | Fin S2 | ≥1 téléchargement du lead magnet | Revoir le positionnement du popup |
| Premier audit booké (digital) | Fin S4 | ≥1 audit venant du site ou LinkedIn | Revoir le CTA et le ciblage |
| 5 avis Google | Fin mois 2 | ≥5 avis avec note ≥4.5 | Intensifier les demandes post-audit |
| 10 audits/mois | Fin mois 2 | ≥10 audits bookés en mois 2 | Lancer les ads plus tôt |
| Rentabilité ads | Fin mois 3 | CPA < 50 € par audit | Optimiser les landing pages et ciblages |
| CA 15 000 €/mois | Fin mois 3 | ≥15 000 € de CA | Évaluer le pricing et le taux de conversion |

---

## Budget estimé par phase

### Option A — Bootstrap (investissement minimal)

| Phase | Budget | Détail |
|---|---|---|
| **Phase 0** | 0 € | Travail de préparation uniquement |
| **Phase 1** | 0-100 € | Email OVH (inclus) + photo smartphone + Canva gratuit |
| **Phase 2** | 0-50 € | Canva Pro optionnel (13 €/mois) + domaine landing page |
| **Phase 3** | 0-100 € | Boost LinkedIn occasionnel |
| **Phase 4** | 200-500 €/mois | Google Ads (200-300 €) + LinkedIn boost (50-100 €) + Facebook retargeting (50-100 €) |
| **Total 3 mois** | **200-750 €** | |

*Adapté si Guy fait tout lui-même. Temps estimé : 15-20h/semaine les 4 premières semaines, 8-12h/semaine ensuite.*

### Option B — Investissement modéré

| Phase | Budget | Détail |
|---|---|---|
| **Phase 0** | 0 € | — |
| **Phase 1** | 200-500 € | Photo pro (150 €) + design lead magnet freelance (50-100 €) + mini-vidéo (100-200 €) |
| **Phase 2** | 200-400 € | Rédaction articles SEO freelance (4 × 50-100 €) |
| **Phase 3** | 300-600 € | Google Ads test (150 €) + LinkedIn boost (100 €) + Malt premium (50 €) |
| **Phase 4** | 500-1 500 €/mois | Google Ads (300-500 €) + Facebook (100-300 €) + LinkedIn (100-200 €) + contenu (200-500 €) |
| **Total 3 mois** | **1 200-3 000 €** | |

*Adapté si Guy délègue certaines tâches. Temps Guy : 10-15h/semaine.*

### Option C — Accéléré (avec accompagnement marketing)

| Phase | Budget | Détail |
|---|---|---|
| **Phase 0-1** | 1 500-3 000 € | Consultant marketing (refonte site + branding + funnel) |
| **Phase 2** | 1 000-2 000 € | Rédaction contenu + design + configuration funnel avancé |
| **Phase 3** | 1 500-3 000 € | Gestion LinkedIn + SEO + partenariats + ads setup |
| **Phase 4** | 2 000-4 000 €/mois | Gestion ads + content + community management |
| **Total 3 mois** | **6 000-12 000 €** | |

*ROI attendu : 14 000-24 000 €/mois de CA dès le mois 3, soit un retour sur investissement en 1-2 mois.*

---

## Risques et mitigation

### Risques stratégiques

| # | Risque | Probabilité | Impact | Mitigation |
|---|---|---|---|---|
| 1 | **Confusion identitaire persistante** — Le nom "SMARTHOME SMARTELEC" et l'historique domotique continuent de brouiller le message | Élevée | Élevé | Purger la navigation dès S1. À moyen terme (mois 6), envisager une sous-marque ou un renommage (ex: "SmartElec AI", "SHSE Automatisation") |
| 2 | **Marché local trop petit** — Pas assez d'artisans/PME en Drôme-Ardèche prêts à investir dans l'IA | Moyenne | Élevé | Étendre à AURA dès le mois 2, puis France entière (remote). Le local est le tremplin, pas la destination finale |
| 3 | **Concurrence des plateformes no-code** — Les artisans font eux-mêmes avec Zapier/Make | Faible | Moyen | Positionner le service sur "on le fait pour vous" et non "on vous donne les outils". L'artisan veut le résultat, pas la technique |
| 4 | **Dépendance à Guy** — Tout repose sur une seule personne | Moyenne | Élevé | Productiser les offres (packs standardisés) pour réduire le temps par client. Documenter les process. Recruter un assistant technique à partir de 15 000 €/mois de CA |

### Risques opérationnels

| # | Risque | Probabilité | Impact | Mitigation |
|---|---|---|---|---|
| 5 | **Manque de temps** — Guy gère les clients existants + le marketing | Élevée | Élevé | Prioriser la version "Lancement Minimum Viable" (2 semaines, voir ci-dessous). Déléguer la rédaction de contenu si possible |
| 6 | **Pas de preuve sociale initiale** — Difficile de convaincre sans témoignage | Élevée | Élevé | Faire 2-3 projets pilotes gratuits ou à prix réduit en échange d'un témoignage détaillé et d'un avis Google. ROI immédiat en crédibilité |
| 7 | **CPA Google Ads trop élevé** — Requêtes trop concurrentielles | Moyenne | Moyen | Commencer par les requêtes long-tail locales. Optimiser les landing pages avant d'augmenter le budget. Tester Facebook et LinkedIn en parallèle |
| 8 | **WordPress lent / instable** — Hébergement mutualisé OVH + Elementor | Moyenne | Moyen | Optimiser les images (WebP), installer un cache (WP Rocket), envisager un passage Softr ou migration hébergeur si < 2s impossible |

### Risques concurrentiels

| # | Risque | Probabilité | Impact | Mitigation |
|---|---|---|---|---|
| 9 | **Entrée de concurrents nationaux** — Synapze, Volteyr, ou Hyperstack ciblent la Drôme | Faible | Moyen | Avancer vite sur le SEO local et les partenariats prescripteurs. La proximité terrain est un avantage structurel contre les acteurs parisiens |
| 10 | **Artisan'IA ou Pragma-IA copie le positionnement artisan** | Moyenne | Moyen | Construire la preuve sociale rapidement (témoignages, études de cas). La triple légitimité de Guy est impossible à copier |

### Plan de contingence — Lancement Minimum Viable (si manque de temps)

Si les 12 semaines complètes sont irréalistes, voici le **strict minimum en 2 semaines** :

**Semaine 1 (3-4h) :**
1. Embed Cal.com inline + anti-risque sous le CTA (30 min)
2. Réécrire le headline H1 (15 min)
3. Purger la navigation obsolète (1h)
4. Créer le profil LinkedIn avec nouveau positionnement (2h)
5. Créer / revendiquer Google Business (1h)

**Semaine 2 (3-4h) :**
6. Publier 3 posts LinkedIn (douleur + parcours + offre)
7. Envoyer 10 messages LinkedIn personnalisés
8. Contacter 3 prescripteurs locaux (experts-comptables, CCI)
9. Publier l'annonce "3 places ce mois-ci" sur LinkedIn

**Résultat minimum viable :** 3-5 audits bookés, 1-2 clients signés. Ce n'est pas optimal, mais c'est infiniment mieux que l'état actuel.

---

## Analyse concurrentielle — Positionnement différentiel

| Concurrent | Localisation | Force | Faiblesse vs SMARTHOME SMARTELEC |
|---|---|---|---|
| **Synapze** | Var | Présence web établie | Pas d'expérience terrain artisan |
| **Volteyr** | Nice | Branding moderne | Pas de connaissance métier PME services |
| **Artisan'IA** | Hauts-de-France | Nom parlant, ciblage artisan | Pas de présence Sud-Est, pas de background SI/CRM |
| **Pragma-IA** | Lyon | Proximité géographique | Positionnement entreprises moyennes, pas artisans |
| **Hyperstack** | Paris | Moyens importants | Tarifs élevés, pas de proximité locale, pas d'ancrage terrain |

**Avantage compétitif de Guy SALVATORE :** Triple légitimité unique (artisan terrain + consultant SI/CRM grand groupe + expert IA open-source) + ancrage local Drôme + stack 100% EU/RGPD. Aucun concurrent ne réplique cette combinaison.

---

*Playbook de Lancement — SMARTHOME SMARTELEC*
*Généré le 20 mars 2026 — AI Marketing Suite*
