# LAUNCH PLAYBOOK — MechaHelp (mechahelp-ai.com)
**Marketplace d'accompagnements personnalisés en IA & automatisation**
Julien Bergé — VanLyxe Corp — Colmar (68000)
Rédigé le : 19 mars 2026 | Lancement cible : J-0 = **19 avril 2026**

---

## TABLE DES MATIÈRES

1. [Vision et objectifs du lancement](#1-vision-et-objectifs)
2. [Pré-lancement J-30 à J-0](#2-pré-lancement-j-30-à-j-0)
3. [Semaine de lancement J-0 à J+7](#3-semaine-de-lancement)
4. [Post-lancement J+7 à J+30](#4-post-lancement-j7-à-j30)
5. [Stratégie de contenu](#5-stratégie-de-contenu)
6. [Stratégie d'acquisition](#6-stratégie-dacquisition)
7. [Stratégie email](#7-stratégie-email)
8. [Stratégie prix et offres de lancement](#8-stratégie-prix-et-offres)
9. [Budget estimé et allocation](#9-budget-et-allocation)
10. [Timeline visuelle](#10-timeline-visuelle)
11. [Checklist complète](#11-checklist-de-lancement)
12. [KPIs et tableau de bord](#12-kpis-et-tableau-de-bord)

---

## 1. VISION ET OBJECTIFS

### Vision du lancement

MechaHelp doit s'imposer comme **la première marketplace francophone d'accompagnement IA & automatisation**, clairement distincte de la communauté MechaPizzAI. Le lancement officiel vise à transformer une base communautaire de 384 membres Skool en un moteur commercial actif, tout en captant une audience nouvelle via le contenu et l'acquisition.

**Positionnement central :**
> "Le premier endroit en France où les professionnels trouvent l'expert IA qu'il leur faut — en 24h, au bon prix, avec un résultat garanti."

### Problèmes critiques à résoudre AVANT le lancement

| Problème | Impact | Priorité |
|---|---|---|
| Prix cachés derrière login | Bloque 70-80% des visiteurs | CRITIQUE |
| Zéro social proof / témoignages | Brise la confiance | CRITIQUE |
| SPA sans SSR = zéro SEO | Invisibilité Google | HAUTE |
| Confusion MechaHelp vs MechaPizzAI | Dilution de marque | HAUTE |
| Pas de capture email / lead magnet | Zéro liste propre | HAUTE |
| Absent des sites de comparaison | Manque crédibilité | MOYENNE |

### KPIs SMART par horizon

#### Objectifs J+30 (19 mai 2026)
| KPI | Baseline | Objectif J+30 | Méthode de mesure |
|---|---|---|---|
| Score marketing | 53/100 | 72/100 | Audit mensuel |
| Membres Skool | 384 | 600 | Dashboard Skool |
| Abonnés liste email | 0 | 500 | Brevo / Mailerlite |
| Ventes de services | Inconnu | 20 commandes | Stripe Dashboard |
| CA mensuel | Inconnu | 3 000 € | Stripe |
| Visiteurs/mois (site) | Inconnu | 2 000 sessions | Google Analytics |
| Taux de conversion visiteur→lead | 0% | 5% | GA + CRM |
| Abonnés YouTube | Inconnu | +200 | YouTube Studio |
| Abonnés TikTok | Inconnu | +500 | TikTok Analytics |

#### Objectifs J+60 (19 juin 2026)
| KPI | Objectif |
|---|---|
| Membres Skool | 1 000 |
| Liste email | 1 500 |
| CA mensuel | 8 000 € |
| Experts actifs | 10+ |
| Témoignages collectés | 15+ |
| Trafic organique | 500 sessions/mois |
| Score marketing | 80/100 |

#### Objectifs J+90 (19 juillet 2026)
| KPI | Objectif |
|---|---|
| Membres Skool | 2 000 |
| Liste email | 3 000 |
| CA mensuel | 15 000 € |
| Taux de satisfaction clients | >4,7/5 |
| Positionnement SEO | Top 10 sur 5 KWs cibles |
| Mentions presse / partenariats | 3+ |
| Score marketing | 88/100 |

---

## 2. PRÉ-LANCEMENT (J-30 À J-0)

**Période : 20 mars → 18 avril 2026**

### SEMAINE 1 (J-30 à J-23) — Fondations techniques

#### Corrections techniques prioritaires

**TÂCHE T-01 : Rendre les prix publics**
- Responsable : Julien Bergé (développeur / agence)
- Deadline : J-25 (25 mars)
- Action : Afficher les prix de tous les 24 services sans obligation de connexion. Si la page de détail reste derrière login, créer une page publique `/tarifs` avec tableau récapitulatif.
- Livrable : URL `/tarifs` accessible sans compte, testée sur mobile et desktop

**TÂCHE T-02 : Mise en place Google Analytics 4 + Search Console**
- Responsable : Julien Bergé
- Deadline : J-28 (22 mars)
- Action : Installer GA4 avec tracking des events clés (inscription, clic service, paiement). Vérifier Search Console. Créer un sitemap.xml même pour SPA.
- Livrable : Tableau de bord GA4 opérationnel

**TÂCHE T-03 : Solution SEO pour SPA**
- Responsable : Julien Bergé + développeur
- Deadline : J-20 (30 mars)
- Options par ordre de priorité :
  1. Activer le SSR (Next.js / Nuxt si applicable) — solution idéale
  2. Pré-rendu statique (Prerender.io, ~50€/mois) — solution intermédiaire
  3. Créer un blog WordPress sur `blog.mechahelp-ai.com` — solution rapide
- Livrable : Au moins 3 pages indexables par Google (accueil, tarifs, à propos)

**TÂCHE T-04 : Installer une solution email marketing**
- Responsable : Julien Bergé
- Deadline : J-27 (23 mars)
- Outil recommandé : **Brevo** (gratuit jusqu'à 300 emails/jour, interface française)
- Action : Créer le compte, paramétrer le domaine d'envoi, créer la première liste "MechaHelp Prospects"
- Livrable : Formulaire d'inscription fonctionnel sur le site

**TÂCHE T-05 : Création du lead magnet**
- Responsable : Julien Bergé + experts MechaHelp
- Deadline : J-22 (28 mars)
- Contenu : **"Les 10 automatisations IA qui font gagner 5h/semaine aux PME françaises"** (PDF de 12-15 pages)
- Format : Canva Pro → PDF professionnel avec branding MechaHelp
- Livrable : PDF téléchargeable + landing page dédiée `/guide-gratuit`

**TÂCHE T-06 : Clarification de marque MechaHelp vs MechaPizzAI**
- Responsable : Julien Bergé
- Deadline : J-25 (25 mars)
- Action :
  1. Créer une page `/communaute` qui explique l'écosystème (MechaPizzAI = communauté YouTube/TikTok/Skool ; MechaHelp = marketplace de services)
  2. Dans toutes les bios réseaux sociaux : ajouter "Services pro → mechahelp-ai.com"
  3. Sur Skool : épingler un post expliquant la différence
- Livrable : Charte de clarification marque documentée

#### Collecte de social proof (urgent)

**TÂCHE T-07 : Campagne témoignages membres Skool**
- Responsable : Julien Bergé
- Deadline : J-21 (29 mars)
- Action :
  1. Message privé aux 50 membres les plus actifs sur Skool
  2. Template message : "Salut [Prénom], tu fais partie des membres les plus investis de la communauté. Est-ce que tu aurais 3 minutes pour répondre à 3 questions sur ce que tu as accompli grâce à MechaHelp ? Je valorise ton témoignage sur le site et te donne un accès prioritaire aux nouveaux services."
  3. Formulaire Google Forms ou Typeform pour collecter : nom, photo, résultat obtenu, recommandation
- Objectif : 10 témoignages minimum avant lancement
- Livrable : Section témoignages sur la homepage

**TÂCHE T-08 : Cas d'usage et résultats chiffrés**
- Responsable : Julien + Experts marketplace
- Deadline : J-18 (1er avril)
- Action : Documenter 3 cas concrets (avant/après) avec chiffres réels pour chaque domaine clé (automatisation, ChatGPT, création de contenu IA)
- Livrable : 3 mini-études de cas sur le site

---

### SEMAINE 2 (J-22 à J-15) — Contenu et assets

**TÂCHE C-01 : Créer 8 vidéos de teasing pré-lancement**
- Responsable : Julien Bergé
- Deadline : 4 vidéos prêtes à J-18, 4 autres à J-10
- Format TikTok/Reels (60-90 secondes) :
  - Vidéo 1 : "Pourquoi j'ai créé MechaHelp" (histoire fondateur)
  - Vidéo 2 : "Les 5 choses que l'IA peut automatiser pour toi dès demain"
  - Vidéo 3 : "Rencontre avec [Expert 1] — ce qu'il fait pour nos clients"
  - Vidéo 4 : "On vous révèle nos 24 services IA (avant tout le monde)"
  - Vidéo 5-8 : Démos courtes de cas d'usage par domaine

**TÂCHE C-02 : Créer la page de pré-inscription (waitlist)**
- Responsable : Julien Bergé
- Deadline : J-20 (30 mars)
- Page `/lancement` avec :
  - Headline choc : "La marketplace IA qui va transformer votre business — Accès prioritaire dès le 19 avril"
  - Formulaire email (prénom + email)
  - Promesse : "Les 100 premiers inscrits reçoivent -20% sur leur premier service"
  - Compteur de personnes déjà inscrites (social proof dynamique)
- Outil : Carrd, Systeme.io, ou page dédiée sur le site

**TÂCHE C-03 : Rédaction des 5 premiers articles de blog**
- Responsable : Julien Bergé (+ IA pour accélérer)
- Deadline : J-10 (9 avril)
- Sujets ciblant des mots-clés à fort volume :
  1. "Comment automatiser votre facturation avec l'IA en 2026" (KW: automatisation facturation IA)
  2. "Les meilleurs outils IA pour les TPE/PME françaises en 2026" (KW: outils IA PME France)
  3. "ChatGPT pour les nuls : guide complet pour débutants" (KW: ChatGPT débutant guide)
  4. "Combien coûte un consultant IA en France ?" (KW: consultant IA tarif France)
  5. "Make vs Zapier : lequel choisir pour automatiser ?" (KW: Make vs Zapier comparaison)
- Format : 1 200-1 800 mots, structurés H1/H2/H3, méta-description optimisée

**TÂCHE C-04 : Préparer le kit presse / partenariats**
- Responsable : Julien Bergé
- Deadline : J-12 (7 avril)
- Contenu :
  - One-pager PDF MechaHelp (chiffres, vision, services)
  - Logos en haute définition (fond blanc, fond transparent, fond sombre)
  - 3 visuels de la plateforme (captures d'écran annotées)
  - Email template de prise de contact partenaires

---

### SEMAINE 3 (J-14 à J-7) — Activation de la communauté

**TÂCHE A-01 : Campagne de pré-inscription Skool**
- Responsable : Julien Bergé
- Deadline : J-14 (5 avril)
- Action :
  1. Post Skool épinglé : "LANCEMENT OFFICIEL dans 14 jours — Voici ce qui arrive"
  2. Révéler progressivement les nouveautés (1 post/jour pendant 7 jours)
  3. Sondage Skool : "Quel service IA vous manque le plus ?" → crée l'engagement et qualifie les besoins
  4. Créer un canal dédié #lancement-mechahelp sur Skool

**TÂCHE A-02 : Outreach YouTubers et créateurs IA francophones**
- Responsable : Julien Bergé
- Deadline : J-10 (9 avril)
- Liste cible :
  - Créateurs IA FR avec 5k-100k abonnés (micro-influenceurs plus accessibles)
  - Podcasts business/tech français (Génération Do It Yourself, Underscore_, etc.)
  - Newsletters tech françaises (Morning Tech, La Lettre IA, etc.)
- Message clé : proposition de partenariat (affiliation 15% ou échange de visibilité)
- Objectif : 3 confirmations de collaboration pour le jour du lancement

**TÂCHE A-03 : Inscription sur les plateformes de référencement**
- Responsable : Julien Bergé
- Deadline : J-7 (12 avril)
- Sites à soumettre :
  - Product Hunt (créer le profil, préparer le lancement pour J-0)
  - Indie Hackers (post de présentation)
  - Capsule (annuaire outils IA français)
  - There's An AI For That (si applicable)
  - LinkedIn Company Page (créer ou optimiser)
  - Google My Business (pour visibilité locale Colmar/Alsace)

**TÂCHE A-04 : Setup séquences email automatisées**
- Responsable : Julien Bergé
- Deadline : J-7 (12 avril)
- Créer dans Brevo :
  - Séquence 1 : Bienvenue pré-inscription (3 emails sur 7 jours)
  - Séquence 2 : Onboarding post-inscription (5 emails sur 14 jours)
  - Séquence 3 : Nurturing mensuel
- Détail complet en [Section 7](#7-stratégie-email)

---

### SEMAINE 4 (J-7 à J-0) — Sprint final

**TÂCHE F-01 : Répétition générale du parcours utilisateur**
- Responsable : Julien Bergé + 2 bêta-testeurs externes (hors communauté)
- Deadline : J-3 (16 avril)
- Scénarios à tester :
  1. Arriver sur le site → comprendre l'offre → voir les prix → s'inscrire → acheter un service
  2. Voir une vidéo TikTok → cliquer le lien → télécharger le lead magnet → recevoir les emails
  3. Venir de Skool → trouver le bon expert → réserver une session
- Documenter tous les points de friction et les corriger

**TÂCHE F-02 : Préparer le contenu du jour J**
- Responsable : Julien Bergé
- Deadline : J-2 (17 avril)
- Préparer en avance et programmer :
  - 1 vidéo YouTube (10-15 min) : "MechaHelp est officiellement lancé"
  - 2 TikToks pour le jour J
  - 1 Reel Instagram
  - Post LinkedIn personnel (Julien)
  - Email à toute la liste pré-inscription
  - Post Skool announcement
  - Product Hunt launch post

**TÂCHE F-03 : Configuration monitoring et alertes**
- Responsable : Julien Bergé
- Deadline : J-1 (18 avril)
- Actions :
  - Uptime Robot (gratuit) : alerte si le site tombe
  - Activer les notifications Stripe pour chaque vente
  - Créer un Google Sheet de suivi KPIs quotidien
  - Préparer les réponses types aux questions fréquentes (FAQ Notion)

**TÂCHE F-04 : Brief des experts MechaHelp**
- Responsable : Julien Bergé
- Deadline : J-2 (17 avril)
- Actions :
  1. Call vidéo collectif avec les 7+ experts
  2. Expliquer le plan de lancement et leurs rôles
  3. Leur demander de partager le lancement sur leurs propres réseaux
  4. Préparer leurs fiches profil optimisées (photo pro, bio, spécialités, 1 cas client)

---

## 3. SEMAINE DE LANCEMENT (J-0 À J+7)

**Période : 19 avril → 25 avril 2026**

### Samedi 19 avril — Jour J (J-0) : LE LANCEMENT

**06h00** — Vérification finale du site (tous les liens, le paiement Stripe, les formulaires)
**07h00** — Envoi email à toute la liste de pré-inscrits (objet : "C'est parti — votre accès prioritaire MechaHelp")
**08h00** — Publication de la vidéo YouTube principale (10-15 min : le pitch complet MechaHelp)
**09h00** — Post Skool épinglé : lancement officiel + offre early bird
**10h00** — Publication TikTok #1 : "Voilà pourquoi j'ai passé 6 mois à construire MechaHelp"
**11h00** — Lancement Product Hunt (l'horaire 00h01 PST = 09h01 en France — prévoir la veille)
**12h00** — Post LinkedIn Julien Bergé (post personnel avec histoire du projet)
**14h00** — TikTok #2 : "Vous pouvez maintenant réserver une session avec nos experts IA"
**16h00** — Story Instagram/Reels : derrière les coulisses du lancement
**18h00** — Premier bilan : vérifier les métriques, répondre aux premiers commentaires
**20h00** — Post de gratitude Skool : résultats du J-0, premières commandes célébrées

**Objectif du jour J :** 50 inscriptions email, 5 premières commandes, 500 vues YouTube

---

### Dimanche 20 avril (J+1) : Momentum

- Répondre à TOUS les commentaires YouTube, TikTok, Skool du jour J
- TikTok : "24h après le lancement — voici ce qui s'est passé" (transparence radicale)
- Email de relance aux non-ouvreurs du J-0 (objet différent)
- Contacter individuellement les premiers acheteurs pour leur demander un feedback immédiat
- Ajuster la page d'accueil si des questions récurrentes sont apparues

---

### Lundi 21 avril (J+2) : Contenu valeur

- YouTube Shorts : extrait de la vidéo principale
- TikTok : Présentation d'un expert (format 60s)
- Email #2 de la séquence (contenu : "Quel service choisir selon votre situation ?")
- Outreach vers 5 créateurs IA de la liste de partenaires (follow-up si contactés avant)
- Mise à jour Product Hunt (répondre aux commentaires, upvotes)

---

### Mardi 22 avril (J+3) : Expertise

- Vidéo TikTok : Démo live d'un service (ex: "Je crée un chatbot en 15 minutes avec notre expert")
- Post Skool : "Les 3 questions les plus posées depuis le lancement" → FAQ publique
- Email #3 : Témoignage client (si disponible) ou cas d'usage chiffré
- Contacter 3 journalistes/blogueurs tech français (email kit presse)

---

### Mercredi 23 avril (J+4) : Milieu de semaine — Push communauté

- YouTube : Vidéo "Rencontre avec [Expert 1] — ce qu'il accomplit pour ses clients"
- TikTok : Format "POV : tu discovers MechaHelp pour la première fois"
- Sondage Instagram Stories : "Quel domaine IA vous intéresse le plus ?"
- Réengagement Skool : demande de témoignages aux membres satisfaits
- Email #4 : Lead magnet (si pas encore envoyé) ou contenu exclusif

---

### Jeudi 24 avril (J+5) : Social proof

- Publier les premiers témoignages collectés (vidéo ou screenshot anonymisé avec permission)
- TikTok : "Voici ce que nos experts ont accompli cette semaine"
- Email : Partage d'un résultat client (avec permission)
- LinkedIn : Julien partage un insight sur le marché IA France

---

### Vendredi 25 avril (J+6) : Récap et urgence

- TikTok : "Il reste 48h pour bénéficier de l'offre de lancement -20%"
- Email : Rappel offre early bird avec deadline (dimanche minuit)
- Post Skool : Bilan de la semaine en chiffres (transparence)
- YouTube : Vidéo récap "Les leçons du lancement"

---

### Dimanche 26 avril (J+7) : Clôture early bird

- Email matin : "Dernières heures — offre early bird se termine ce soir"
- Email soir 20h : "Offre terminée — mais voici ce qui arrive ensuite"
- TikTok : "On ferme l'offre de lancement — voici les résultats"
- Bilan interne complet : KPIs vs objectifs, ajustements semaine suivante

---

## 4. POST-LANCEMENT (J+7 À J+30)

**Période : 26 avril → 19 mai 2026**

### Consolidation (J+7 à J+14)

**Analyse et ajustement :**
- Audit des données GA4 : quelles pages convertissent, d'où vient le trafic
- Analyse Stripe : quels services se vendent le mieux, panier moyen
- Heat maps (Hotjar gratuit) sur la page d'accueil : où les gens cliquent, où ils abandonnent
- Interviews courtes (15 min) des 5 premiers clients : qu'est-ce qui les a convaincus ?

**Optimisation du tunnel de conversion :**
- A/B test headline de la homepage (2 versions pendant 7 jours)
- Optimiser la page `/tarifs` : ajouter FAQ, garanties, moyens de paiement
- Installer un chat live ou bot (Crisp, gratuit jusqu'à 2 opérateurs) pour qualifier les leads
- Créer une page dédiée pour les 3 services les plus populaires (SEO + conversion)

**Développement du contenu :**
- Rythme de publication stabilisé : 1 YouTube/semaine, 5 TikToks/semaine, 2 posts LinkedIn/semaine
- Premier article de blog publié avec tracking positions
- Newsletter hebdomadaire lancée (chaque mardi, "Le Mardi IA")

### Optimisation (J+14 à J+21)

**Activation des partenariats :**
- Finaliser 1-2 partenariats d'affiliation avec créateurs IA (commissions tracking Tapfiliate ou FirstPromoter)
- Soumettre MechaHelp à 5 annuaires et sites comparatifs supplémentaires
- Guest post sur 1 blog tech français (article invité avec backlink)

**Programme de referral :**
- Lancer "Parrainez un ami, gagnez 50€ de crédit MechaHelp"
- Email à tous les clients existants pour présenter le programme
- Intégration dans Brevo : automatisation des emails de parrainage

**Montée en gamme :**
- Créer une offre "Pack Découverte" (3 services bundlés à -15%)
- Créer une offre "Abonnement Expert" (accès mensuel illimité à un expert)
- Lancer une vente flash de 48h sur un service phare

### Institutionnalisation (J+21 à J+30)

**SEO & contenu long terme :**
- Publier article de blog #2 et #3
- Soumettre le sitemap mis à jour à Google Search Console
- Commencer le netlinking (échanges de liens avec partenaires)
- Créer une FAQ publique optimisée SEO (longue traîne)

**Scaling communautaire :**
- Objectif 600 membres Skool : campagne d'invitation ciblée
- Créer des "Défis IA" hebdomadaires sur Skool (engagement + recrutement)
- Live mensuel sur YouTube : "Questions/Réponses avec les experts MechaHelp"

**Reporting J+30 :**
- Rapport complet de performance vs objectifs
- Présentation aux experts du bilan et des priorités suivantes
- Ajustement du budget marketing selon les canaux performants
- Planification des 60 jours suivants

---

## 5. STRATÉGIE DE CONTENU

### Piliers de contenu (brand content framework)

| Pilier | Part du contenu | Exemples de sujets |
|---|---|---|
| **Éducation IA** | 40% | Tutoriels outils IA, guides débutants, comparatifs |
| **Expertise métier** | 25% | Portraits d'experts, cas clients, démos de services |
| **Coulisses & humanité** | 20% | Julien raconte, behind-the-scenes, transparence radicale |
| **Communauté & social** | 15% | Succès membres, UGC, témoignages, sondages |

### Calendrier éditorial — Avril & Mai 2026

#### Semaine type (rythme de croisière, à partir de J+7)

| Jour | Format | Canal | Sujet type |
|---|---|---|---|
| Lundi | TikTok (60s) | TikTok + Reels | Astuce IA de la semaine |
| Mardi | Newsletter | Email | "Le Mardi IA" — résumé actu + tip exclusif |
| Mardi | Article blog | Blog | Contenu SEO long (1500 mots) |
| Mercredi | YouTube (10-15 min) | YouTube | Tutoriel ou interview expert |
| Jeudi | TikTok (60-90s) | TikTok + Reels | Démo service ou POV client |
| Vendredi | Post LinkedIn | LinkedIn | Réflexion marché IA + expertise Julien |
| Vendredi | TikTok (30s) | TikTok | Format "Saviez-vous que..." |
| Samedi | TikTok (60s) | TikTok | Contenu communauté / testimonial |
| Dimanche | Post Skool | Skool | Défi de la semaine + engagement |

#### Calendrier spécifique Avril 2026

| Date | Contenu | Canal | Thème |
|---|---|---|---|
| 19 avr | Vidéo lancement (15 min) | YouTube | Histoire + vision MechaHelp |
| 19 avr | TikTok x2 | TikTok | Annonce lancement |
| 20 avr | TikTok "24h après" | TikTok | Transparence résultats |
| 22 avr | Vidéo Expert #1 | YouTube | Portrait expert |
| 23 avr | Article #1 | Blog | SEO — automatisation facturation |
| 24 avr | Témoignage client | TikTok + Skool | Social proof |
| 26 avr | Newsletter #1 | Email | "Le Mardi IA" — lancement spécial |
| 28 avr | YouTube tuto | YouTube | Comment utiliser MechaHelp |
| 29 avr | Article #2 | Blog | SEO — outils IA PME |
| 30 avr | TikTok bilan avril | TikTok | Transparence chiffres mois |

#### Calendrier spécifique Mai 2026

| Date | Contenu | Canal | Thème |
|---|---|---|---|
| 2 mai | Newsletter #2 | Email | Tips IA de la semaine |
| 5 mai | YouTube | YouTube | Tutoriel ChatGPT avancé |
| 6 mai | Article #3 | Blog | SEO — ChatGPT débutant |
| 7 mai | Live Q&A | YouTube Live / Skool | Questions communauté |
| 9 mai | Newsletter #3 | Email | Cas client + offre semaine |
| 12 mai | Portrait expert #2 | YouTube | Expert Make/Zapier |
| 13 mai | Article #4 | Blog | SEO — consultant IA tarifs |
| 16 mai | Newsletter #4 | Email | "Spécial 1 mois de lancement" |
| 19 mai | Bilan J+30 | YouTube + Skool | Résultats transparents |
| 20 mai | Article #5 | Blog | SEO — Make vs Zapier |

### Formats TikTok prioritaires

1. **"Tu savais que..."** : fait surprenant sur l'IA + call-to-action service
2. **POV** : "POV : tu découvres que tu peux automatiser ça avec l'IA"
3. **Avant/Après** : process manuel vs automatisé (avec chrono)
4. **Défi** : "Je génère une semaine de contenu en 20 minutes avec l'IA"
5. **Interview flash** : 60 secondes avec un expert, 1 conseil actionnable
6. **Réaction** : réagir à des outils IA nouveaux ou à des news du secteur

### Mots-clés SEO cibles (prioritaires)

| Mot-clé | Volume estimé/mois | Difficulté | Priorité |
|---|---|---|---|
| consultant IA France | 1 200 | Moyenne | HAUTE |
| automatisation IA PME | 800 | Faible | HAUTE |
| formation IA professionnelle | 2 000 | Haute | MOYENNE |
| expert ChatGPT | 600 | Faible | HAUTE |
| marketplace IA française | 300 | Faible | HAUTE |
| make automatisation tutoriel | 1 000 | Faible | HAUTE |
| chatgpt pour entreprise | 3 000 | Haute | MOYENNE |
| coaching IA personnalisé | 400 | Faible | HAUTE |

---

## 6. STRATÉGIE D'ACQUISITION

### Canal 1 : Organique (priorité absolue)

**TikTok (@mechapizzai_official)**
- Fréquence : 5 vidéos/semaine minimum
- Stratégie hook : les 3 premières secondes sont décisives — commencer avec un chiffre, une question ou un défi
- Hashtags permanents : #IA #automatisation #productivité #entrepreneur #PME #france
- Objectif J+30 : +500 abonnés, 3 vidéos à +10 000 vues

**YouTube (@mechapizzai)**
- Fréquence : 1 vidéo longue/semaine + 2-3 Shorts/semaine
- Types de vidéos les mieux converties :
  - Tutoriels "Comment faire..." (trafic de recherche)
  - Comparatifs outils (décision d'achat)
  - Portraits d'experts (trust building)
- CTA systématique en fin de vidéo : "Réservez une session sur mechahelp-ai.com"
- Objectif J+30 : +200 abonnés, 3 vidéos à +500 vues

**SEO / Blog**
- Priorité : article de longue traîne à faible concurrence
- Internal linking systématique vers les pages de services
- Objectif J+30 : 5 articles publiés, 200 sessions organiques

### Canal 2 : Communauté Skool

**Stratégie d'activation des 384 membres existants :**
1. Segmentation : identifier les 20% les plus actifs (futurs ambassadeurs)
2. Programme "MechaHelper" : statut spécial pour les membres qui recommandent des clients
3. Contenu exclusif Skool en avance de phase (avant YouTube)
4. Défi mensuel avec prix (service gratuit ou crédit)

**Recrutement de nouveaux membres :**
- Post hebdomadaire sur les réseaux avec lien d'invitation Skool
- Lead magnet → email → invitation Skool dans la séquence d'onboarding
- Partenariats avec d'autres communautés Skool complémentaires

### Canal 3 : Email marketing

- Objectif de liste : 500 contacts J+30, 1 500 à J+60
- Sources d'acquisition :
  1. Lead magnet (PDF) : principal driver
  2. Newsletter "Le Mardi IA" : promotion organique
  3. Pop-up exit intent sur le site (déclenché après 30 secondes)
  4. Signature email de tous les experts avec lien
- Taux d'ouverture cible : >30% (benchmark secteur)
- Voir détail en [Section 7](#7-stratégie-email)

### Canal 4 : Partenariats & Affiliation

**Programme d'affiliation :**
- Commission : 15% sur le premier achat référé
- Outil : Tapfiliate (49€/mois) ou FirstPromoter (79€/mois)
- Cibles prioritaires :
  - Créateurs YouTube IA francophones (5k-100k abonnés)
  - Formateurs en ligne sur les outils IA
  - Consultants freelance qui peuvent sous-traiter à MechaHelp

**Partenariats médias :**
- Podcasts cibles : "Génération Do It Yourself", "Les Digitals Nomads", "Indie Hackers France"
- Pitch : Julien Bergé comme invité expert IA + marketplace
- Objectif : 1 apparition J+30, 3 apparitions J+90

**Co-marketing :**
- Partenariats avec outils IA complémentaires (Make, Brevo, Notion, etc.)
- Échanges de newsletters avec créateurs de même audience
- Webinaires co-animés avec des experts de l'écosystème

### Canal 5 : Paid (secondaire, à activer à J+30)

**Budget initial recommandé : 300€/mois**

- **Meta Ads (Facebook/Instagram)** : 150€/mois
  - Audience : entrepreneurs, dirigeants PME, 30-55 ans, France
  - Format : vidéo 15s (extrait TikTok best performer) + CTA lead magnet
  - Objectif : lead < 2€

- **TikTok Ads** : 100€/mois
  - Booster les vidéos organiques qui performent déjà bien (Spark Ads)
  - Audience similaire à l'audience TikTok existante

- **LinkedIn Ads** (à partir de J+60) : 200€/mois
  - Ciblage directeurs/gérants de PME, responsables RH, DSI
  - Format : Sponsored Content avec lead form intégré

### Canal 6 : Relations presse & Product Hunt

**Product Hunt :**
- Préparer le lancement complet (maker profile, tagline, description, visuels)
- Demander à la communauté Skool d'upvoter le jour J
- Objectif : Top 5 du jour dans la catégorie "Productivity" ou "AI"

**Presse spécialisée :**
- Cibler : Frenchweb.fr, BFM Business Tech, L'Usine Digitale, Siècle Digital
- Angle : "La première marketplace française d'experts IA"
- Communiqué de presse à envoyer : J-5 pour les annonces, J-0 pour le lancement

---

## 7. STRATÉGIE EMAIL

### Architecture des séquences

#### Séquence 1 : Pré-inscription (Waitlist) — 3 emails

**Email W-1 : Confirmation + Lead Magnet**
- Timing : Immédiat (trigger automatique)
- Objet : "Votre guide gratuit est prêt + ce qui arrive le 19 avril"
- Contenu :
  - Lien download du PDF lead magnet
  - Annonce du lancement avec date exacte
  - Ce qu'ils obtiendront en avant-première (offre early bird -20%)
  - PS : "Répondez à cet email avec votre plus grand défi IA" (engage les réponses = réputation email)

**Email W-2 : Teasing (J-10)**
- Timing : J-10 avant le lancement
- Objet : "On vous présente les experts qui vous attendent"
- Contenu :
  - 3 mini-portraits d'experts (photo, spécialité, 1 résultat client)
  - Teasing du catalogue de 24 services
  - Rappel early bird

**Email W-3 : Dernier rappel (J-1)**
- Timing : Veille du lancement (18 avril)
- Objet : "Demain, ça change tout — préparez-vous"
- Contenu :
  - Ce qui se passe demain
  - Comment accéder à la plateforme
  - Rappel de l'offre early bird (limitée aux 100 premiers)
  - Ton : excitation, imminence, exclusivité

---

#### Séquence 2 : Onboarding nouveaux inscrits — 7 emails sur 14 jours

**Email O-1 : Bienvenue (J+0)**
- Objet : "Bienvenue dans la communauté MechaHelp, [Prénom] !"
- Contenu :
  - Histoire de Julien Bergé en 3 paragraphes (connexion humaine)
  - Ce que MechaHelp peut faire pour eux
  - 3 actions immédiates suggérées (voir les services, rejoindre Skool, regarder la vidéo YouTube)
  - CTA principal : "Découvrez nos 24 services →"

**Email O-2 : Valeur pure (J+2)**
- Objet : "5 automatisations IA que vous pouvez mettre en place ce week-end"
- Contenu :
  - 5 tips actionnables (extrait du lead magnet)
  - Pour chaque tip : lien vers le service MechaHelp correspondant
  - CTA : "Vous voulez de l'aide pour l'un d'eux ? Réservez une session →"

**Email O-3 : Social proof (J+4)**
- Objet : "Ce que [Prénom client] a accompli en 2 semaines avec MechaHelp"
- Contenu :
  - Un cas client détaillé (avant/après/résultat chiffré)
  - Citation du client
  - CTA : "Obtenez le même résultat →"

**Email O-4 : Choix du bon service (J+6)**
- Objet : "Comment savoir quel service IA vous convient ?"
- Contenu :
  - Quiz simple (3 questions) ou arbre de décision textuel
  - Guide "Si vous êtes X, commencez par Y"
  - CTA : "Parlez à un expert gratuitement →"

**Email O-5 : Expertise Julien (J+8)**
- Objet : "Ce que j'ai appris en construisant MechaHelp (et ce que ça change pour vous)"
- Contenu :
  - Email personnel de Julien, ton authentique
  - 3 insights sur le marché IA en France
  - Vision à 6 mois
  - CTA : "Rejoignez la communauté Skool →"

**Email O-6 : Offre spéciale (J+10)**
- Objet : "Un cadeau pour vous — parce que vous avez fait confiance dès le début"
- Contenu :
  - Code promo exclusif (-10%) pour les inscrits email
  - Durée limitée : 48h
  - 3 services recommandés selon le profil (segmentation si possible)
  - CTA : "Utiliser mon code →"

**Email O-7 : Invitation communauté (J+14)**
- Objet : "384 personnes attendent de vous rencontrer sur Skool"
- Contenu :
  - Présentation de la communauté Skool (valeur ajoutée)
  - Ce qu'ils y trouveront (contenus exclusifs, experts, entraide)
  - CTA : "Rejoindre gratuitement →"

---

#### Séquence 3 : Newsletter "Le Mardi IA" (nurturing hebdomadaire)

**Format standard (600-800 mots) :**
- Section 1 : "L'insight de la semaine" — 1 grande idée sur l'IA (100 mots)
- Section 2 : "Outil à tester" — 1 outil IA gratuit ou freemium (150 mots)
- Section 3 : "Coulisses MechaHelp" — ce qui se passe dans la marketplace (150 mots)
- Section 4 : "La ressource" — 1 article, vidéo ou podcast externe (50 mots)
- Section 5 : CTA de la semaine — 1 seul (service, article blog, événement)

**Fréquence :** Chaque mardi matin (8h00)
**Objectif taux d'ouverture :** >30%
**Objectif taux de clic :** >5%

---

#### Séquence 4 : Relance inactifs (à partir de J+45)

**Email R-1 : "Vous nous manquez"**
- Trigger : Aucune ouverture depuis 30 jours
- Objet : "On a créé quelque chose pour vous, [Prénom]"
- Contenu : Nouveau lead magnet ou contenu exclusif

**Email R-2 : Dernière chance**
- Trigger : 7 jours après R-1 sans ouverture
- Objet : "On va se dire au revoir... ou pas ?"
- Contenu : Proposition simple, CTA clair, option de désabonnement facilement visible

**Règle de nettoyage :** Supprimer les contacts sans ouverture depuis 60 jours (améliore la délivrabilité)

---

## 8. STRATÉGIE PRIX ET OFFRES DE LANCEMENT

### Problème actuel à résoudre en priorité

Les prix sont cachés derrière le login — c'est le premier frein à la conversion. La solution est d'afficher les prix sur une page publique `/tarifs` avant même le lancement.

### Structure de prix recommandée

#### Offre Découverte (nouvelle — à créer)
**Prix : 49€ (lancement) → 69€ (prix normal)**
- 1 session de diagnostic de 45 minutes avec un expert
- Rapport personnalisé de recommandations
- Idéal pour : prospects qui ne savent pas par où commencer
- Objectif : convertir les prospects hésitants, créer une relation

#### Services Standards (catalogue existant)
- Afficher les fourchettes de prix clairement : "À partir de 149€"
- Créer 3 niveaux (Starter / Pro / Expert) pour chaque domaine
- Garantie satisfaction : "Remboursé si non satisfait sous 7 jours"

#### Pack Lancement (offre temporaire — 30 jours)
**Prix : -20% sur le premier service pour les early birds**
- Valable uniquement sur inscription depuis la liste de pré-inscrits
- Code promo : MECHAHELP-EARLY
- Limite : 100 utilisations ou 30 jours après lancement

#### Abonnement Expert (à créer — lancer à J+30)
**Prix : 299€/mois**
- Accès prioritaire à un expert attitré
- 4 sessions/mois (1/semaine)
- Révisions illimitées sur les livrables
- Canal de communication directe (Slack ou Discord privé)
- Rapport mensuel d'avancement

#### Offre PME / Entreprise (à créer — lancer à J+60)
**Prix : Sur devis (min. 1 000€/mois)**
- Audit complet + plan d'action IA personnalisé
- Accompagnement d'une équipe (jusqu'à 10 personnes)
- Accès multi-experts
- SLA de réponse garanti (< 4h)

### Politique de garantie et confiance

- Garantie satisfait ou remboursé : 7 jours sans condition
- Afficher clairement sur la page tarifs :
  - Modes de paiement acceptés (Stripe : CB, Apple Pay, Google Pay)
  - Possibilité de paiement en 3x sans frais (via Stripe)
  - SIRET VanLyxe Corp visible (conformité française)
  - Mentions légales et CGV à jour

### Stratégie d'upsell

| Premier achat | Upsell proposé | Timing |
|---|---|---|
| Session Découverte (49€) | Service complet (149€+) | J+3 après la session |
| Service ponctuel | Abonnement Expert (299€) | J+7 après livraison |
| Abonnement Expert | Pack Entreprise (sur devis) | J+60 de fidélité |

---

## 9. BUDGET ESTIMÉ ET ALLOCATION

### Budget total recommandé : 1 500€ pour le lancement (J-30 à J+30)

#### Répartition détaillée

| Poste | Coût estimé | Période | Priorité |
|---|---|---|---|
| **Outils indispensables** | | | |
| Brevo (email marketing) | 0€ (plan gratuit) | J-30 → J+30 | CRITIQUE |
| Google Analytics 4 | 0€ (gratuit) | J-30 | CRITIQUE |
| Hotjar (heatmaps) | 0€ (plan basique) | J+7 | HAUTE |
| Uptime Robot | 0€ (gratuit) | J-1 | HAUTE |
| Canva Pro (design) | 13€/mois | J-30 | HAUTE |
| **Contenu & production** | | | |
| Microphone + éclairage TikTok/YouTube | 100-200€ (si pas déjà équipé) | J-25 | HAUTE |
| Montage vidéo (si sous-traité) | 0-150€/vidéo | J-20 | MOYENNE |
| **Visibilité & acquisition** | | | |
| Product Hunt (gratuit) | 0€ | J-0 | HAUTE |
| Meta Ads (démarrage) | 150€/mois | J+30 | MOYENNE |
| TikTok Spark Ads | 100€/mois | J+30 | MOYENNE |
| **SEO & technique** | | | |
| Prerender.io (si SSR impossible) | 49€/mois | J-20 | HAUTE |
| Ahrefs / Semrush (audit SEO) | 0€ (essai gratuit 7j) | J-25 | HAUTE |
| **Partenariats & affiliation** | | | |
| Tapfiliate (gestion affiliation) | 49€/mois | J+14 | MOYENNE |
| **Événements & communauté** | | | |
| Prix concours Skool (crédit services) | 100€ équivalent | J+14 | FAIBLE |
| **TOTAL J-30 à J-0** | ~400€ | | |
| **TOTAL J-0 à J+30** | ~600€ | | |
| **TOTAL GLOBAL** | **~1 000€** | | |
| **Réserve imprévus (30%)** | ~300€ | | |
| **BUDGET TOTAL RECOMMANDÉ** | **~1 300€** | | |

#### Allocation par priorité

```
CRITIQUE (ne pas couper)   : 13€/mois (Canva Pro) + outils gratuits
HAUTE (lancer dès J-30)    : Prerender/SSR si nécessaire (49€)
MOYENNE (activer à J+30)   : Paid ads (250€/mois), Tapfiliate (49€)
FAIBLE (nice-to-have)      : Prix communauté, créations graphiques premium
```

#### ROI attendu

| Scénario | Ventes J+30 | CA J+30 | ROI sur budget 1 300€ |
|---|---|---|---|
| Pessimiste | 10 commandes | 1 500€ | -1x (investissement long terme) |
| Réaliste | 20 commandes | 3 000€ | +2,3x |
| Optimiste | 40 commandes | 6 000€ | +4,6x |

---

## 10. TIMELINE VISUELLE

```
MARS 2026
============================================================
Sem.1 │ 20-22 mar │ ████ TECHNIQUE (GA4, prix publics, email)
      │ 23-26 mar │ ████ BRANDING (MechaHelp vs MechaPizzAI)
Sem.2 │ 27-29 mar │ ████ CONTENU (lead magnet, vidéos teasing)
      │ 30 mar    │ ████ WAITLIST PAGE live
Sem.3 │ 31 mar    │ ████ TÉMOIGNAGES (campagne membres Skool)
      │ 1-5 avr  │ ████ ARTICLES BLOG (rédaction x5)
      │ 5 avr    │ ████ SKOOL ACTIVATION (posts teasing J-14)
Sem.4 │ 7-9 avr  │ ████ OUTREACH (partenaires, presse, Product Hunt)
      │ 9 avr    │ ████ SÉQUENCES EMAIL configurées dans Brevo
      │ 10-12 avr│ ████ ANNUAIRES (soumission plateformes)
AVRIL 2026
============================================================
J-7   │ 12 avr   │ ████ RÉPÉTITION GÉNÉRALE du tunnel
J-5   │ 14 avr   │ ████ COMMUNIQUÉ DE PRESSE envoyé
J-3   │ 16 avr   │ ████ BÊTA-TEST utilisateurs externes
J-2   │ 17 avr   │ ████ CONTENU J-0 programmé (emails, posts)
J-1   │ 18 avr   │ ████ BRIEF EXPERTS + VÉRIFICATIONS FINALES
J-0   │ 19 avr   │ ████████████████ LANCEMENT OFFICIEL
J+1   │ 20 avr   │ ████ Relance, réponses, ajustements
J+2   │ 21 avr   │ ████ Contenu valeur + outreach partenaires
J+3   │ 22 avr   │ ████ Expertise + presse
J+4   │ 23 avr   │ ████ Communauté + blog #1
J+5   │ 24 avr   │ ████ Social proof
J+6   │ 25 avr   │ ████ Urgence early bird
J+7   │ 26 avr   │ ████ Clôture early bird + bilan
MAI 2026
============================================================
J+8   │ 27 avr   │ ████ Analyse données + heat maps
J+14  │ 3 mai    │ ████ A/B test homepage + programme referral
J+14  │ 3 mai    │ ████ AFFILIATION lancée (Tapfiliate)
J+21  │ 10 mai   │ ████ Paid ads activés (Meta + TikTok)
J+28  │ 17 mai   │ ████ Blog #4 + #5 publiés
J+30  │ 19 mai   │ ████████████████ BILAN 30 JOURS + planif. J+60
```

---

## 11. CHECKLIST DE LANCEMENT

### Phase 1 : Technique (à compléter avant J-20)

#### Site web
- [ ] Prix publics affichés sans connexion obligatoire
- [ ] Page `/tarifs` créée et optimisée
- [ ] Google Analytics 4 installé et vérifié
- [ ] Google Search Console configurée
- [ ] Sitemap.xml généré et soumis
- [ ] Solution SEO pour SPA (SSR ou prerender) activée
- [ ] Meta-descriptions et balises OG sur toutes les pages clés
- [ ] Page 404 personnalisée avec liens utiles
- [ ] Formulaire de contact fonctionnel
- [ ] SSL valide et HTTPS actif
- [ ] Pages légales à jour (CGV, mentions légales, RGPD)
- [ ] SIRET VanLyxe Corp visible dans le footer
- [ ] Chat Crisp ou équivalent installé
- [ ] Uptime Robot configuré avec alertes email/SMS

#### Email marketing
- [ ] Compte Brevo créé et domaine vérifié (SPF, DKIM)
- [ ] Liste "MechaHelp Prospects" créée
- [ ] Formulaire d'inscription intégré sur le site
- [ ] Pop-up exit intent configuré (délai 30s)
- [ ] Lead magnet PDF finalisé et hébergé
- [ ] Page `/guide-gratuit` avec formulaire opérationnelle
- [ ] Séquence W (pré-inscription) configurée et testée
- [ ] Séquence O (onboarding) configurée et testée
- [ ] Template newsletter "Le Mardi IA" créé

#### Stripe & paiement
- [ ] Stripe en mode live (pas test)
- [ ] Notifications email pour chaque vente activées
- [ ] Liens de paiement testés sur mobile et desktop
- [ ] Paiement en 3x sans frais configuré si possible
- [ ] Factures automatiques Stripe paramétrées

### Phase 2 : Contenu (à compléter avant J-10)

#### Avant lancement
- [ ] Lead magnet "10 automatisations IA" finalisé (PDF)
- [ ] 8 vidéos TikTok/Reels de pré-lancement produites
- [ ] 4 vidéos TikTok programmées pour J-7 à J-1
- [ ] Vidéo YouTube principale de lancement prête (10-15 min)
- [ ] 5 articles de blog rédigés et prêts à publier
- [ ] Kit presse finalisé (one-pager, logos, visuels)

#### Social proof
- [ ] 10 témoignages collectés (texte + photo minimum)
- [ ] Section témoignages ajoutée sur la homepage
- [ ] 3 études de cas (avant/après chiffré) rédigées
- [ ] Fiches profil des 7+ experts complètes et publiées

### Phase 3 : Communauté & Partenariats (avant J-5)

- [ ] Post Skool épinglé : annonce lancement
- [ ] Série de posts Skool pré-lancement (1/jour, J-14 à J-1)
- [ ] Outreach envoyé à 10 créateurs/podcasters
- [ ] 2 partenariats confirmés (affiliation ou visibilité)
- [ ] Profil Product Hunt créé et configuré
- [ ] MechaHelp soumis à 5 annuaires
- [ ] Google My Business créé/optimisé
- [ ] Page LinkedIn Company créée
- [ ] Communiqué de presse rédigé et liste médias cibles identifiée

### Phase 4 : Brief équipe (avant J-2)

- [ ] Call collectif avec les 7+ experts fait
- [ ] Chaque expert a partagé le lancement sur ses réseaux
- [ ] FAQ interne créée (réponses aux 20 questions les plus probables)
- [ ] Planning de permanence J-0 à J+7 (quelqu'un disponible pour répondre)
- [ ] Google Sheet de suivi KPIs quotidien créé et partagé

### Phase 5 : Jour J (19 avril)

- [ ] 06h00 — Vérification complète du site (checklist en 10 points)
- [ ] 07h00 — Email à toute la liste envoyé
- [ ] 08h00 — Vidéo YouTube publiée
- [ ] 09h00 — Post Skool épinglé publié
- [ ] 10h00 — TikTok #1 posté
- [ ] 11h00 — Product Hunt lancé (ou J-1 à minuit PST)
- [ ] 12h00 — Post LinkedIn Julien posté
- [ ] 14h00 — TikTok #2 posté
- [ ] 16h00 — Stories Instagram publiées
- [ ] 18h00 — Premier bilan intermédiaire noté dans le Google Sheet
- [ ] 20h00 — Post de gratitude Skool + chiffres J-0

### Phase 6 : Post-lancement (J+1 à J+30)

- [ ] Réponses à TOUS les commentaires sous 24h (J+1 à J+7)
- [ ] Bilan hebdomadaire KPIs (chaque dimanche)
- [ ] A/B test homepage lancé (J+7)
- [ ] Hotjar heatmaps activé (J+7)
- [ ] Programme referral lancé (J+14)
- [ ] Affiliation Tapfiliate lancé (J+14)
- [ ] Paid ads lancés (J+21)
- [ ] Articles blog #2 et #3 publiés (J+14, J+21)
- [ ] Live YouTube mensuel planifié (J+30)
- [ ] Rapport complet J+30 rédigé et partagé avec les experts

---

## 12. KPIS ET TABLEAU DE BORD DE SUIVI

### Tableau de bord quotidien (J-0 à J+30)

À remplir chaque soir dans un Google Sheet partagé avec les experts.

| Métrique | J-0 | J+1 | J+7 | J+14 | J+30 | Objectif J+30 |
|---|---|---|---|---|---|---|
| **ACQUISITION** | | | | | | |
| Visiteurs uniques (site) | — | — | — | — | — | 2 000 |
| Nouvelles inscriptions email | — | — | — | — | — | 500 |
| Membres Skool | 384 | — | — | — | — | 600 |
| Abonnés YouTube | — | — | — | — | — | +200 |
| Abonnés TikTok | — | — | — | — | — | +500 |
| **ENGAGEMENT** | | | | | | |
| Taux ouverture emails | — | — | — | — | — | >30% |
| Taux de clic emails | — | — | — | — | — | >5% |
| Vues TikTok (semaine) | — | — | — | — | — | 10 000 |
| Vues YouTube (semaine) | — | — | — | — | — | 2 000 |
| **CONVERSION** | | | | | | |
| Sessions → leads (%) | — | — | — | — | — | >5% |
| Leads → acheteurs (%) | — | — | — | — | — | >10% |
| Nouvelles commandes | — | — | — | — | — | 20 total |
| CA (€) | — | — | — | — | — | 3 000 € |
| Panier moyen (€) | — | — | — | — | — | 150 € |
| **SATISFACTION** | | | | | | |
| Note clients (NPS) | — | — | — | — | — | >7/10 |
| Témoignages collectés | — | — | — | — | — | 15 |
| Taux de remboursement | — | — | — | — | — | <5% |
| **SEO** | | | | | | |
| Pages indexées Google | — | — | — | — | — | 10+ |
| Positions KW prioritaires | — | — | — | — | — | Top 20 |
| Backlinks acquis | — | — | — | — | — | 5+ |

### Rapport hebdomadaire (modèle)

**Semaine du [DATE] — Résumé exécutif MechaHelp**

**Faits marquants :**
- [ Résultat 1 ]
- [ Résultat 2 ]
- [ Résultat 3 ]

**KPIs vs objectifs :**
- CA semaine : X€ / Objectif : Y€ (Z%)
- Nouveaux leads : X / Objectif : Y
- Commandes : X / Objectif : Y

**Ce qui a fonctionné :**
- [Canal ou contenu le plus performant]

**Ce qui n'a pas fonctionné :**
- [Point de friction ou performance décevante]

**Actions de la semaine suivante :**
1. [Action prioritaire 1]
2. [Action prioritaire 2]
3. [Action prioritaire 3]

---

### Score marketing — Évolution cible

| Critère | Score actuel | Cible J+30 | Cible J+90 |
|---|---|---|---|
| SEO & visibilité | Faible | Moyen | Bon |
| Conversion site | Faible (prix cachés) | Moyen | Bon |
| Social proof | Faible (0 avis) | Moyen | Excellent |
| Email marketing | Nul | Bon | Excellent |
| Contenu & blog | Faible | Moyen | Bon |
| Communauté | Moyen (384 Skool) | Bon | Excellent |
| Acquisition payante | Nulle | Démarrée | Active |
| Partenariats | Nuls | 2-3 actifs | 5+ actifs |
| **Score global** | **53/100** | **72/100** | **88/100** |

---

### Alertes et seuils de réaction

| Si... | Alors... |
|---|---|
| Taux de conversion < 2% après J+7 | Revoir la homepage, ajouter la garantie et les témoignages en above-the-fold |
| Taux d'ouverture email < 15% | Tester un nouvel objet, nettoyer la liste, vérifier la délivrabilité |
| 0 vente après 7 jours | Appel urgent avec les experts, vérifier le tunnel Stripe, proposer une offre flash |
| Site down > 15 min | Alerter immédiatement, activer la page de maintenance, prévenir Skool |
| TikTok vidéo > 50 000 vues | Booster en Spark Ads immédiatement (50-100€) |
| Témoignage négatif public | Répondre en moins de 2h, proposer une solution, ne jamais supprimer |

---

## CONTACTS ET RESSOURCES CLÉS

| Rôle | Nom | Responsabilité principale |
|---|---|---|
| Fondateur & chef de projet | Julien Bergé | Toutes les décisions stratégiques |
| Experts marketplace | 7+ experts (à nommer) | Livraison services, témoignages, contenu |
| Développeur (si externe) | À identifier | Corrections techniques SEO/SPA |
| Outil email | Brevo | Automation et newsletters |
| Paiement | Stripe | Transactions et reporting financier |
| Analytics | Google Analytics 4 | Mesure de performance |
| Communauté | Skool (mechapizzai) | Base d'audience et activation |

---

*Document rédigé le 19 mars 2026 — VanLyxe Corp / MechaHelp*
*Mise à jour recommandée à J+30 (19 mai 2026) pour ajuster la stratégie J+60*

---

**Priorité absolue avant tout autre action :**
1. Rendre les prix publics (T-01)
2. Installer GA4 (T-02)
3. Créer le lead magnet et la page de capture (T-05)
4. Collecter 10 témoignages (T-07)
5. Clarifier la marque MechaHelp / MechaPizzAI (T-06)
