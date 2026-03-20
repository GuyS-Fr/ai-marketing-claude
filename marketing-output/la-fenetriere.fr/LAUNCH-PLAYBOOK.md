# LAUNCH PLAYBOOK — La Fenêtrière
## Plan de Relance Digitale 90 Jours
**Site :** https://www.la-fenetriere.fr/
**Date de départ :** Mars 2026
**Auteur du diagnostic :** AI Marketing Suite
**Score de départ :** 38/100 — Score cible J+90 : 72/100

---

## Avant-Propos : Pourquoi une "Relance" et Non un Lancement

La Fenêtrière n'est pas une startup. C'est une entreprise de 42 ans, dirigée par Catherine Guerniou depuis 2005, certifiée Origine France Garantie, lauréate Fabriqué en France 2025 (exposition à l'Élysée), titulaire du Prix Madame Engagée et du Prix Étienne Marcel. Son carnet de commandes repose aujourd'hui sur des relations B2B historiques et le bouche-à-oreille.

Le problème est précis et opérationnel : **son site web sabote activement sa conversion**. Un blog en erreur 404, des pages produits vides de tout contenu, un formulaire de contact à 11 champs, zéro call-to-action visible sur les pages stratégiques. Une entreprise de ce calibre — avec ce positionnement — convertit 0,3 à 0,8% de ses visiteurs. Le benchmark sectoriel pour un artisan local est de 3 à 6%.

Ce playbook est donc un **plan de relance digitale**, pas un lancement de zéro. L'objectif est de mettre la vitrine en accord avec la réalité : une entreprise artisanale francilienne unique, certifiée, responsable, dont les menuiseries ont été exposées à l'Élysée.

**Le contexte de marché 2026 renforce l'urgence :**
- Rebond du logement neuf prévu à +9,5% en 2026 après trois années de contraction
- MaPrimeRénov' réouverte (après suspension janvier-mi-février 2026)
- RE2020 qui pousse les critères de carbone embarqué — là où La Fenêtrière excelle
- Tendance Made in France et circuit court en accélération

L'entreprise a tous les actifs. Ce playbook organise leur activation.

---

## Vue d'Ensemble : Architecture des 90 Jours

```
SEMAINE 1-2       SEMAINE 3-4        MOIS 2              MOIS 3
[QUICK WINS]  →  [FONDATIONS]   →   [ACQUISITION]   →  [ACCÉLÉRATION]

Corrections      Contenu &           SEO content         Email nurturing
critiques site   pages produits      LinkedIn B2B        Publicité ciblée
CRO immédiat     SEO technique       Programme           Partenariats
Score: 38→50     Score: 50→58        prescripteurs       Scoring: 58→72
```

---

## CHECKLIST DE PRÉ-LANCEMENT

À valider avant de démarrer les actions, idéalement en Semaine 0 :

### Accès et outils (obligatoires)
- [ ] Accès back-office CMS du site (WordPress ou autre) — avec droits admin
- [ ] Accès Google Search Console — si absent, créer et vérifier le site immédiatement
- [ ] Accès Google Analytics 4 (GTM est détecté — vérifier la configuration GA4)
- [ ] Accès à la boîte email professionnelle @la-fenetriere.fr
- [ ] Accès page LinkedIn entreprise et profil personnel Catherine Guerniou
- [ ] Accès compte Google My Business (fiche Google Maps)
- [ ] Identifiants hébergeur web (pour génération du sitemap.xml et modification robots.txt)

### Ressources contenu (à préparer)
- [ ] 10 à 20 photos de chantiers livrés (avec autorisation client si nécessaire)
- [ ] 5 à 8 photos de l'atelier en activité (compagnons, machines, produits finis)
- [ ] Photo professionnelle ou de bonne qualité de Catherine Guerniou
- [ ] Photos des badges de certification (OFG, Fabriqué en France 2025, Madame Engagée)
- [ ] Photos de l'exposition à l'Élysée (fenêtre bas carbone) — actif majeur
- [ ] 3 à 5 témoignages clients (écrits ou à recueillir par téléphone cette semaine)
- [ ] Chiffres clés internes : année de fondation (1984), nombre de menuiseries/an, nombre de chantiers, effectif, tonnes CO2 économisées si disponible

### Vérifications techniques initiales
- [ ] Vérifier l'indexation actuelle sur Google : taper `site:la-fenetriere.fr` — noter le nombre de pages indexées
- [ ] Lancer un test PageSpeed Insights (pagespeed.web.dev) et noter les scores mobile/desktop
- [ ] Confirmer que HTTPS est actif et redirige correctement depuis HTTP
- [ ] Documenter l'état actuel du formulaire (capture d'écran) pour mesurer l'avant/après
- [ ] Vérifier si une Google Search Console est déjà configurée (et si des erreurs sont signalées)

### Budget validé
- [ ] Budget alloué aux 90 jours confirmé (voir section Budget ci-dessous)
- [ ] Décision : gestion interne, prestataire externe ou hybride
- [ ] Responsable interne de pilotage nommé (recommandé : Catherine Guerniou ou personne déléguée)

---

## PHASE 1 — SEMAINES 1 ET 2 : QUICK WINS
### Objectif : Stopper les hémorragies et multiplier les contacts par 3 sans refonte

**Score visé en fin de phase : 50/100**
**Budget phase 1 : 0 à 500 € (actions internes + éventuellement 1 prestataire ponctuel)**

---

### Action 1.1 — Corriger le blog "Le Mag" (erreur 404)
**Responsable suggéré :** Prestataire web ou webmaster interne
**Délai :** J+1 (urgence absolue)
**Effort :** 30 minutes à 2 heures selon cause technique

La page `/le-mag` retourne une erreur 404. Chaque visiteur qui clique sur ce lien depuis la navigation principale voit un message d'erreur — signal de non-sérieux qui détruit immédiatement la confiance. Chaque jour de 404 est une perte de positionnement SEO.

**Actions concrètes :**
1. Identifier la cause : plugin désactivé ? Slug modifié ? Hébergement partiel ?
2. Si réactivation possible immédiatement : réactiver le module blog
3. Si réactivation impossible sous 48h : créer une page intermédiaire `/le-mag` avec message "Notre blog est en cours de refonte — revenez dans quelques semaines" + CTA devis
4. Retirer temporairement le lien "Le Mag" du menu de navigation principal si la page reste cassée
5. Vérifier dans Google Search Console si des URLs d'articles existants sont indexées (et les rediriger vers la homepage en 301 si le contenu n'existe plus)

**KPI :** Retour HTTP 200 (ou 301) sur l'URL `/le-mag` sous 48h

---

### Action 1.2 — Simplifier le formulaire de contact (11 champs → 5 champs)
**Responsable suggéré :** Webmaster / Catherine Guerniou
**Délai :** J+2
**Effort :** 30 minutes

C'est l'action avec le meilleur ratio effort/impact de tout ce playbook. Le formulaire actuel à 11 champs (incluant SIRET, Adresse professionnelle, Téléphone bureau, Ville, Pays) génère un taux de complétion estimé à 2-5%. En passant à 5 champs, on vise 15-25%.

**Formulaire B2B recommandé (à conserver, 5 champs) :**
```
1. Prénom / Nom*
2. Société*
3. Email professionnel*
4. Téléphone*
5. Décrivez votre besoin* (textarea libre)
[Demander mon devis gratuit]
"Réponse sous 48h ouvrées — Sans engagement"
```

**Champs à supprimer immédiatement :** SIRET, Adresse professionnelle, Téléphone bureau, CP, Ville, Pays

**Ajouter sous le bouton :**
- "Devis gratuit — sans engagement — réponse sous 48h ouvrées"
- Badges visuels OFG et Fabriqué en France 2025

**KPI :** Taux de complétion formulaire mesuré via GA4 (événement form_submit). Cible : passer de < 5% à > 12% en 30 jours.

---

### Action 1.3 — Ajouter un CTA "Demander un devis" sur la homepage
**Responsable suggéré :** Webmaster / Catherine Guerniou
**Délai :** J+2
**Effort :** 1 heure

La homepage n'a actuellement aucun call-to-action vers une demande de devis. Le visiteur n'a pas de chemin clair vers la conversion.

**Actions concrètes :**
1. Ajouter un bouton "Demander mon devis gratuit" dans la zone hero, au-dessus de la ligne de flottaison (visible sans scroll)
2. Ajouter un second bouton CTA en milieu de page, après la section valeurs/certifications
3. Relier ces boutons directement à la page `/contact` (ou créer une ancre vers le formulaire)
4. Texte du bouton recommandé : "Demander mon devis gratuit" — couleur contrastée (pas la même que le fond)
5. Microcopy optionnel sous le bouton : "Sans engagement. Réponse sous 48h."

**KPI :** Clics sur CTA homepage (événement GA4 click + URL). Cible : > 3% des visiteurs homepage cliquent sur le CTA.

---

### Action 1.4 — Afficher les certifications en position hero
**Responsable suggéré :** Webmaster / Catherine Guerniou
**Délai :** J+3
**Effort :** 1 heure

Les badges "Lauréate Fabriqué en France 2025" et "Origine France Garantie" sont des actifs de confiance rares dans le secteur. Ils doivent être visibles immédiatement, dès le premier écran, avant tout scroll.

**Actions concrètes :**
1. Remonter les badges de certification dans la zone hero ou juste en dessous
2. Ajouter le texte "Exposée à l'Élysée — Fabriqué en France 2025" en sous-headline ou en bandeau de confiance
3. Si possible : lier les badges vers une page dédiée (à créer en Phase 2)

**KPI :** Qualitatif (A/B test si possible) — mesurable via heatmap Hotjar ou Microsoft Clarity (outil gratuit)

---

### Action 1.5 — Baliser le numéro de téléphone en click-to-call
**Responsable suggéré :** Webmaster
**Délai :** J+2
**Effort :** 15 minutes

Le numéro 01 48 82 44 11 doit être cliquable sur mobile avec la balise `<a href="tel:+33148824411">`. Actuellement, les visiteurs mobiles (qui représentent probablement 50 à 65% du trafic) ne peuvent pas appeler en un clic.

**Actions concrètes :**
1. Rechercher toutes les occurrences du numéro dans le code HTML
2. Envelopper chaque occurrence avec `<a href="tel:+33148824411">01 48 82 44 11</a>`
3. S'assurer que le numéro est visible dans le header (desktop et mobile)
4. Ajouter le numéro en footer avec click-to-call

**KPI :** Événement GA4 `outbound_click` sur les liens `tel:`. Cible : > 5 appels trackés/mois.

---

### Action 1.6 — Implémenter les balises title et meta description
**Responsable suggéré :** Webmaster / prestataire SEO
**Délai :** J+3 à J+5
**Effort :** 2 à 3 heures (toutes les pages principales)

**Correction critique :** Il existe actuellement une coquille dans le title HTML — "Fenêtière" au lieu de "Fenêtrière". Chaque impression Google affiche cette faute.

**Title recommandé pour la homepage :**
`Fenêtres PVC, Bois & ALU sur mesure | La Fenêtrière – Champigny (94)`

**Meta description recommandée (157 caractères) :**
`Fabricant artisanal de fenêtres PVC, bois et ALU à Champigny-sur-Marne. Certifié Origine France Garantie. Devis gratuit pour professionnels du bâtiment.`

**Pages à traiter en priorité :** Homepage, /nos-produits ou équivalent, /contact, /notre-atelier

**KPI :** CTR moyen sur Google Search Console. Cible : CTR > 3% sur les requêtes positionnées en 30 jours.

---

### Action 1.7 — Générer et soumettre un sitemap.xml
**Responsable suggéré :** Webmaster
**Délai :** J+3
**Effort :** 30 minutes (via plugin WordPress si applicable)

Le sitemap est actuellement absent (erreur 404 sur `/sitemap.xml`). Sans sitemap, Google découvre les pages uniquement par exploration de liens, sans priorisation. C'est la raison probable d'une indexation partielle.

**Actions concrètes :**
1. Générer le sitemap (via Yoast SEO, Rank Math, ou sitemap-generator.net si pas de plugin)
2. Uploader à l'URL `/sitemap.xml`
3. Ajouter la directive `Sitemap: https://www.la-fenetriere.fr/sitemap.xml` dans `robots.txt`
4. Soumettre le sitemap dans Google Search Console (onglet "Sitemaps")
5. Inscrire le site dans Bing Webmaster Tools si ce n'est pas fait

**KPI :** Pages indexées dans Google Search Console. Cible : nombre de pages indexées + 30% en 4 semaines.

---

### Action 1.8 — Ajouter les attributs alt sur toutes les images
**Responsable suggéré :** Webmaster / responsable contenu
**Délai :** J+4 à J+7
**Effort :** 2 à 3 heures

20 images sur 21 n'ont pas d'attribut alt — c'est 95% des images. C'est la plus grosse faille technique du site, avec un double impact : SEO images et accessibilité.

**Format recommandé des alt :**
- Logo : `alt="Logo La Fenêtrière — Fabricant de menuiseries Champigny-sur-Marne"`
- Photos atelier : `alt="Atelier de fabrication La Fenêtrière à Champigny-sur-Marne"`
- Certifications : `alt="Certification Origine France Garantie — La Fenêtrière"`
- Produits (quand disponibles) : `alt="Fenêtre PVC sur mesure fabriquée dans l'atelier La Fenêtrière"`

**KPI :** 0 image sans attribut alt (vérifiable via les outils de diagnostic Screaming Frog ou directement dans le CMS).

---

### Récapitulatif Phase 1

| Action | Responsable | Délai | Effort | Budget |
|--------|-------------|-------|--------|--------|
| 1.1 Corriger blog 404 | Webmaster | J+1 | 30 min–2h | 0–200€ |
| 1.2 Simplifier formulaire | Webmaster | J+2 | 30 min | 0€ |
| 1.3 Ajouter CTA homepage | Webmaster | J+2 | 1h | 0€ |
| 1.4 Certifications en hero | Webmaster | J+3 | 1h | 0€ |
| 1.5 Click-to-call téléphone | Webmaster | J+2 | 15 min | 0€ |
| 1.6 Title + meta description | Webmaster | J+3–5 | 2–3h | 0€ |
| 1.7 Sitemap.xml + GSC | Webmaster | J+3 | 30 min | 0€ |
| 1.8 Attributs alt images | Webmaster | J+4–7 | 2–3h | 0€ |

**Budget total Phase 1 : 0 à 500 € selon prestataire ponctuel**
**Impact attendu :** Taux de conversion site x2,5 à x4 — de 3-8 contacts/mois à 10-20 contacts/mois

### Risques Phase 1

| Risque | Probabilité | Impact | Mitigation |
|--------|-------------|--------|------------|
| Webmaster indisponible | Moyen | Bloquant | Identifier un prestataire de secours en amont ; la plupart de ces actions sont réalisables via l'interface admin WordPress sans développeur |
| Blog 404 causé par problème d'hébergement complexe | Faible | Moyen | Retirer le lien du menu immédiatement (< 5 min) en attendant le diagnostic technique |
| Formulaire simplifié refusé par Catherine Guerniou (besoin d'info SIRET) | Faible | Moyen | Conserver le SIRET en champ optionnel non obligatoire, ou créer un formulaire long uniquement accessible depuis une page Pro |

---

## PHASE 2 — SEMAINES 3 ET 4 : FONDATIONS
### Objectif : Construire les fondations de contenu et SEO qui transformeront le trafic en devis

**Score visé en fin de phase : 58/100**
**Budget phase 2 : 800 à 2 500 €**

---

### Action 2.1 — Créer des pages produits riches (6 pages)
**Responsable suggéré :** Responsable contenu interne + photos atelier
**Délai :** J+10 à J+21
**Effort :** 3 à 5 jours de travail total
**Budget :** 0 (interne) à 1 500 € (rédaction externalisée)

C'est **la correction qui aura le plus grand impact sur le chiffre d'affaires**. La page produits actuelle ne contient aucun visuel, aucune description, aucun CTA. Le taux d'abandon estimé est de 85 à 95%.

**6 pages à créer ou enrichir :**
1. Fenêtres PVC — avantages isolation, délais, prix indicatif, badge OFG
2. Fenêtres Aluminium — avantages esthétiques, durabilité, double vitrage, RE2020
3. Fenêtres Bois — avantages écologiques, charme, entretien, circuit Normandie
4. Portes d'entrée — sécurité, isolation, sur mesure, exemples visuels
5. Volets (roulants/battants) — isolation thermique, occultation, motorisation
6. Portails — sur mesure, aluminium, automatisation, délais

**Structure minimum pour chaque page :**
```
• Photo hero de bonne qualité (atelier ou chantier réel)
• Headline bénéfice : "La fenêtre PVC qui tient 40 ans — fabriquée à Champigny"
• 3 à 5 bénéfices clés avec icônes
• Matériaux et origines (circuit court France)
• Certification applicable (OFG, Fabriqué en France)
• 1 exemple de réalisation avec photo
• 1 CTA "Demander un devis pour cette gamme" (bouton contrasté)
• Prix indicatif ou fourchette (optionnel mais recommandé)
```

**KPI :** Durée de session sur pages produits (cible : > 45 secondes), taux de clic vers /contact depuis ces pages (cible : > 5%).

---

### Action 2.2 — Créer une section témoignages clients
**Responsable suggéré :** Catherine Guerniou (collecte) + webmaster (intégration)
**Délai :** J+10 à J+21
**Effort :** 2 à 4 heures de collecte + 2 heures d'intégration
**Budget :** 0 €

Dans un secteur où la commande précède la confiance (projets de 5 000 à 50 000 €), l'absence de témoignages est une faiblesse structurelle. 3 à 5 témoignages bien positionnés augmentent le taux de conversion de 20 à 30%.

**Comment collecter les témoignages (script simple) :**
- Contacter 5 à 10 clients récents par téléphone : "Nous refaisons notre site web. Accepteriez-vous de laisser un avis en 2-3 phrases ?"
- Poser 3 questions : "Quel était votre besoin ? Qu'est-ce qui vous a convaincu de choisir La Fenêtrière ? Quel résultat après installation ?"
- Demander l'autorisation de publier prénom + métier + ville (pas obligatoirement photo)

**Format recommandé :**
```
"Nous avons remplacé 12 fenêtres sur un chantier de rénovation à Vincennes.
Délai tenu, produits solides, interlocuteur direct. On recommande."
— Marc T., Artisan menuisier, Vincennes (94)
```

**Placements :** Homepage (section dédiée), page Contact (près du formulaire), pages produits (en bas de chaque fiche).

**KPI :** Section visible sur les pages concernées. Mesure qualitative : évolution du taux de conversion du formulaire (objectif J+45 : > 10%).

---

### Action 2.3 — Implémenter le schema markup JSON-LD
**Responsable suggéré :** Développeur web ou plugin SEO (Yoast/Rank Math)
**Délai :** J+10 à J+14
**Effort :** 2 à 3 heures
**Budget :** 0 (plugin) à 300 € (développeur)

**Schémas à implémenter en priorité :**

```json
// Schema LocalBusiness (homepage + page contact)
{
  "@context": "https://schema.org",
  "@type": "HomeAndConstructionBusiness",
  "name": "La Fenêtrière",
  "url": "https://www.la-fenetriere.fr",
  "telephone": "+33148824411",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "[adresse]",
    "addressLocality": "Champigny-sur-Marne",
    "postalCode": "94500",
    "addressCountry": "FR"
  },
  "foundingDate": "1984",
  "areaServed": "Île-de-France",
  "hasCredential": ["Origine France Garantie", "Fabriqué en France 2025"]
}
```

**Autres schémas à ajouter :** `Organization`, `BreadcrumbList`, `FAQPage` (sur la page FAQ existante), `Article` (pour les futurs articles du blog).

**KPI :** Validation via Google Rich Results Test (search.google.com/test/rich-results). 0 erreur de schema.

---

### Action 2.4 — Créer une page dédiée "Lauréate Élysée 2025"
**Responsable suggéré :** Catherine Guerniou (contenu) + webmaster
**Délai :** J+12 à J+21
**Effort :** 1 journée
**Budget :** 0 € (contenu interne)

C'est l'actif de marque le plus différenciant de La Fenêtrière — **une fenêtre bas carbone exposée à l'Élysée parmi 123 produits sélectionnés nationalement**. Cet événement n'est actuellement qu'une mention dans la navigation, sans page dédiée.

**Contenu de la page :**
- Photos de l'exposition à l'Élysée (obligatoire)
- Story du produit : la fenêtre deux vantaux bas carbone, son processus de fabrication, son bilan carbone
- Texte de Catherine Guerniou en première personne : "Ce que cette distinction représente pour notre équipe..."
- Communiqué de presse ou article presse existant (Batiweb, Verre & Menuiserie...)
- CTA vers les pages produits gamme bas carbone

**Pourquoi c'est stratégique :**
- Référencement sur les requêtes "Fabriqué en France menuiserie 2025" et variantes
- Argument de vente direct pour les marchés publics, les bailleurs sociaux, les professionnels engagés RE2020
- Base d'un communiqué de presse pour relancer les relations médias

**KPI :** Page indexée dans Google Search Console. Trafic organique sur cette URL (suivi mensuel).

---

### Action 2.5 — Créer deux parcours distincts B2B / B2C
**Responsable suggéré :** Webmaster + Catherine Guerniou
**Délai :** J+14 à J+21
**Effort :** 2 à 3 jours
**Budget :** 0 à 500 € selon complexité CMS

La cible est à 95% professionnels du bâtiment, mais les particuliers représentent un segment complémentaire à fort panier. Ces deux audiences ont des besoins, des mots-clés et des objections radicalement différents.

**Deux entrées depuis la homepage :**
```
┌─────────────────────────┐    ┌─────────────────────────┐
│   Je suis professionnel │    │   Je suis particulier   │
│      du bâtiment        │    │                         │
│                         │    │                         │
│  → Délais fournisseur   │    │  → Devis personnalisé   │
│  → Conditions pro       │    │  → MaPrimeRénov'        │
│  → Programme partenaires│    │  → Garanties produit    │
│  → Formulaire B2B       │    │  → Formulaire B2C       │
└─────────────────────────┘    └─────────────────────────┘
```

**KPI :** Taux de clic sur chaque parcours depuis la homepage. Taux de conversion formulaire par segment.

---

### Action 2.6 — Optimisation SEO technique complémentaire
**Responsable suggéré :** Webmaster
**Délai :** J+10 à J+21
**Effort :** 3 à 4 heures
**Budget :** 0 €

**Actions SEO technique restantes :**
1. Ajouter les balises canonical sur toutes les pages (prévenir le contenu dupliqué)
2. Corriger le H1 de la homepage : "La Fenêtrière" → "Fabricant de menuiseries extérieures à Champigny-sur-Marne"
3. Corriger la balise og:image (chemin relatif → URL absolue)
4. Implémenter `loading="lazy"` sur toutes les images sous la ligne de flottaison
5. Restructurer la hiérarchie H1/H2 (le H2 de 460 caractères sur la raison d'être doit devenir un paragraphe `<p>`)
6. Réécrire les titres H2 avec des mots-clés SEO : "Nos fenêtres PVC, bois et aluminium sur mesure", "Un atelier de proximité en Île-de-France"

**KPI :** Score PageSpeed Insights mobile (cible : > 65). Score SEO on-page via Screaming Frog ou Semrush (cible : 0 erreur critique).

---

### Récapitulatif Phase 2

| Action | Responsable | Délai | Effort | Budget estimé |
|--------|-------------|-------|--------|---------------|
| 2.1 Pages produits (x6) | Contenu + Webmaster | J+10–21 | 3–5 jours | 0–1 500 € |
| 2.2 Témoignages clients | Catherine Guerniou | J+10–21 | 4–6h | 0 € |
| 2.3 Schema markup | Dev web / Plugin | J+10–14 | 2–3h | 0–300 € |
| 2.4 Page Élysée 2025 | Catherine + WM | J+12–21 | 1 jour | 0 € |
| 2.5 Parcours B2B / B2C | Webmaster | J+14–21 | 2–3 jours | 0–500 € |
| 2.6 SEO technique suite | Webmaster | J+10–21 | 3–4h | 0 € |

**Budget total Phase 2 : 0 à 2 300 €**
**Impact attendu :** Taux de conversion x2 supplémentaire — de 10-20 contacts/mois à 20-35 contacts/mois

### Risques Phase 2

| Risque | Probabilité | Impact | Mitigation |
|--------|-------------|--------|------------|
| Manque de photos de chantiers pour les pages produits | Moyen | Élevé | Planifier une session photo dans l'atelier (1/2 journée, photographe local 200-400€) ou utiliser des photos libres de droits dans un premier temps avec remplacement prévu |
| Difficulté à collecter des témoignages | Moyen | Moyen | Catherine Guerniou contacter directement 3 clients fidèles par téléphone — objectif : 3 témoignages minimum en 1 semaine |
| Délai de réalisation des 6 pages produits dépasse 21 jours | Moyen | Faible | Prioriser les 2 pages les plus vendues (PVC + ALU) et publier les 4 autres dans les semaines suivantes |

---

## PHASE 3 — MOIS 2 : ACQUISITION
### Objectif : Générer du trafic qualifié via SEO, LinkedIn B2B et programme prescripteurs

**Score visé en fin de phase : 65/100**
**Budget phase 3 : 1 500 à 4 000 €**

---

### Action 3.1 — Lancement du blog avec 4 articles SEO prioritaires
**Responsable suggéré :** Rédacteur externe spécialisé BTP ou Catherine Guerniou (si bonne plume)
**Délai :** J+22 à J+52 (2 articles/semaine pendant 2 semaines puis 1/semaine)
**Budget :** 600 à 1 200 € (4 articles × 150-300€ par article externalisé) ou 0 € (rédaction interne)

Le blog "Le Mag" est le principal levier de trafic organique à moyen terme. Une fois réparé (Phase 1), il doit être alimenté avec des articles ciblant des requêtes à fort potentiel commercial.

**4 articles fondateurs (ordre de priorité) :**

**Article 1 — Guide MaPrimeRénov' fenêtres 2026** *(priorité absolue)*
- Titre cible : "Comment profiter de MaPrimeRénov' pour remplacer ses fenêtres en 2026"
- Volume de recherche : Élevé (rebond post-suspension janvier 2026)
- Longueur cible : 1 500 à 2 000 mots
- Structure : éligibilité, montants, démarches, artisans RGE, exemples de projets
- CTA : "Demander un devis à La Fenêtrière — artisan certifié IDF"
- SEO technique : FAQ schema, 3 à 5 liens internes vers pages produits

**Article 2 — Comparatif PVC vs ALU vs Bois**
- Titre cible : "Fenêtre PVC, aluminium ou bois : quel matériau choisir en 2026 ?"
- Volume de recherche : Élevé, forte intention d'achat
- Longueur cible : 2 000 mots
- Structure : tableau comparatif, critères (coût, entretien, isolation, esthétique, durabilité, bilan carbone)
- CTA : "Demander conseil à notre atelier"

**Article 3 — RE2020 et menuiseries : ce qui change pour les professionnels**
- Titre cible : "RE2020 et menuiseries : les critères carbone embarqué que tout pro doit connaître"
- Volume de recherche : Moyen, très qualifié B2B
- Longueur cible : 1 200 mots
- Structure : explication RE2020, impact sur le choix des menuiseries, avantage produits bas carbone, argument circuit court
- CTA : "Télécharger notre guide pro" (lead magnet à créer) ou "Demander un devis professionnel"

**Article 4 — Fabrication artisanale à l'Élysée : coulisses**
- Titre cible : "Notre fenêtre bas carbone à l'Élysée : la fabrication qui a convaincu l'État"
- Volume de recherche : Faible mais backlink potentiel élevé (presse)
- Longueur cible : 1 000 mots
- Structure : récit de la sélection, process de fabrication, bilan carbone, équipe
- Valeur principale : autorité de marque + partage réseaux sociaux + potentiel RP

**KPI :**
- Trafic organique sur les articles publiés (cible : > 50 sessions/article/mois à J+60)
- Position moyenne dans Google Search Console (cible : top 30 pour les mots-clés cibles à J+60)
- Taux de clic vers la page contact depuis les articles (cible : > 2%)

---

### Action 3.2 — Stratégie LinkedIn B2B
**Responsable suggéré :** Catherine Guerniou (voix principale) + assistant éditorial
**Délai :** Démarrage J+22, rythme 2 posts/semaine en continu
**Budget :** 0 à 500 € (création de visuels si externalisé)

LinkedIn est **le canal B2B le plus pertinent** pour toucher les architectes, maîtres d'œuvre, promoteurs et conducteurs de travaux d'Île-de-France. La page entreprise existe. Il faut l'activer avec une stratégie éditoriale cohérente.

**Format des posts recommandés :**

| Type de post | Fréquence | Exemple |
|---|---|---|
| Coulisses fabrication | 1/semaine | "Voilà comment on fabrique une fenêtre ALU bas carbone à Champigny — 8 étapes en photos" |
| Portrait équipe | 1/2 semaines | "Fabrice est dans notre atelier depuis 1991. Voilà ce qu'il nous a appris sur la qualité." |
| Actualité normative | 1/2 semaines | "RE2020 Seuil 2025 : ce que ça change concrètement pour vos commandes de menuiseries" |
| Chantier livré | 1/semaine | "12 fenêtres PVC posées à Vincennes — résultat après 3 semaines de chantier" |
| Prise de position / opinion | 1/mois | "Pourquoi Made in France n'est pas une option dans la menuiserie de demain" |

**Optimisation du profil LinkedIn :**
1. Page entreprise : ajouter bannière avec certifications, compléter le descriptif avec mots-clés sectoriels
2. Profil Catherine Guerniou : ajouter "Dirigeante La Fenêtrière — Menuiseries artisanales Made in France — Lauréate Élysée 2025"
3. Activer l'option "Abonnez-vous aux actualités de La Fenêtrière" en page entreprise
4. Identifier et suivre : 50 profils cibles (architectes, MOE, promoteurs IDF) à J+22

**KPI :**
- Abonnés page LinkedIn (cible : +50 abonnés/mois)
- Portée moyenne des posts (cible : > 200 vues/post)
- Prises de contact via LinkedIn (cible : > 3 leads qualifiés/mois à J+60)

---

### Action 3.3 — Programme Prescripteurs B2B
**Responsable suggéré :** Catherine Guerniou
**Délai :** J+30 à J+52 (structuration + 1ers contacts)
**Budget :** 0 (temps interne) à 500 € (création d'un support de présentation)

Le réseau de prescripteurs — architectes, maîtres d'œuvre, conducteurs de travaux, bureaux d'études — est probablement déjà le canal principal de La Fenêtrière. Ce programme vise à le formaliser et à l'amplifier.

**Structure du programme prescripteurs :**

```
NIVEAU 1 — PARTENAIRE RÉFÉRENT
• Référencement officiel sur le site de La Fenêtrière (page dédiée)
• Conditions tarifaires préférentielles (remise ou délai prioritaire)
• Accès à un catalogue produits numérique à jour
• Contact direct Catherine Guerniou / atelier

NIVEAU 2 — AMBASSADEUR
• Tout le niveau 1
• Commission sur chaque chantier recommandé (à définir : 2-5%)
• Badge "Partenaire La Fenêtrière" utilisable sur leur site/devis
• Invitation à la visite de l'atelier 1x/an

NIVEAU 3 — CO-MARKETING
• Co-signature d'articles LinkedIn
• Mention dans les études de cas publiées
• Accès aux nouveautés gamme en avant-première
```

**Cible initiale :** 10 à 15 prescripteurs qualifiés en Île-de-France, recrutés parmi les clients existants satisfaits.

**KPI :**
- Nombre de prescripteurs inscrits (cible : 10 à J+60)
- Chantiers apportés par les prescripteurs (cible : 3 à 5 chantiers/trimestre dès le Mois 3)

---

### Action 3.4 — Optimiser la fiche Google My Business
**Responsable suggéré :** Catherine Guerniou / webmaster
**Délai :** J+22 à J+30
**Effort :** 2 à 4 heures
**Budget :** 0 €

La fiche Google My Business est le premier point de contact pour les recherches locales. Elle est probablement sous-optimisée.

**Actions concrètes :**
1. Vérifier que la fiche est bien revendiquée et vérifiée
2. Ajouter 10 à 20 photos de l'atelier et des chantiers
3. Compléter toutes les catégories : "Fabricant de fenêtres", "Menuisier", "Magasin de fenêtres"
4. Ajouter les horaires complets et actuels
5. Activer la fonctionnalité "Demander un devis" directement sur la fiche
6. Répondre à tous les avis existants (même anciens)
7. Publier un post Google My Business par semaine (reprendre les posts LinkedIn)
8. Ajouter les attributs : "Entreprise française", "Produit Made in France", etc.

**KPI :**
- Nombre d'actions sur la fiche GMB (appels, clics vers site, demandes d'itinéraire) — visible dans le tableau de bord Google My Business
- Cible : +30% d'actions mensuelles depuis la fiche en 60 jours

---

### Action 3.5 — Créer un lead magnet "Guide Pro Menuiseries RE2020"
**Responsable suggéré :** Catherine Guerniou (expertise) + rédacteur externe
**Délai :** J+30 à J+52
**Budget :** 200 à 500 € (mise en forme PDF professionnelle)

Un guide téléchargeable permet de capturer les emails de prospects qui ne sont pas encore prêts à demander un devis — et de les nourrir ensuite.

**Format recommandé :**
- Titre : "Menuiseries RE2020 : le guide du professionnel du bâtiment 2026"
- 8 à 12 pages PDF
- Contenu : critères RE2020, comparatif matériaux par bilan carbone, MaPrimeRénov' 2026, comment choisir un fabricant Made in France, checklist chantier menuiseries
- Disponible en échange d'un email professionnel
- Placé sur la page "Professionnels" et dans les articles de blog

**KPI :**
- Nombre de téléchargements (cible : > 20/mois à J+60)
- Taux d'ouverture de l'email de suivi (cible : > 40%)

---

### Récapitulatif Phase 3

| Action | Responsable | Délai | Budget estimé |
|--------|-------------|-------|---------------|
| 3.1 Blog — 4 articles SEO | Rédacteur / Catherine | J+22–52 | 0–1 200 € |
| 3.2 Stratégie LinkedIn B2B | Catherine Guerniou | J+22 → continu | 0–500 € |
| 3.3 Programme prescripteurs | Catherine Guerniou | J+30–52 | 0–500 € |
| 3.4 Google My Business | Catherine / WM | J+22–30 | 0 € |
| 3.5 Lead magnet "Guide Pro" | Catherine + rédacteur | J+30–52 | 200–500 € |

**Budget total Phase 3 : 200 à 2 700 €**
**Impact attendu :** Trafic organique x1,5 — leads qualifiés 25 à 45/mois à J+60

### Risques Phase 3

| Risque | Probabilité | Impact | Mitigation |
|--------|-------------|--------|------------|
| SEO lent à démarrer (résultats à 3-6 mois) | Élevé (normal) | Moyen | Communiquer en amont que le SEO est un investissement long terme — résultats visibles à M+3 pour les quick wins, M+6 pour les positions de fond |
| Catherine Guerniou manque de temps pour LinkedIn | Élevé | Moyen | Préparer 4 semaines de posts en avance lors d'une session dédiée de 3h ; envisager un assistant ou un community manager 2h/semaine |
| Programme prescripteurs difficile à formaliser avec des clients existants | Faible | Faible | Commencer par un email informel envoyé à 5 clients fidèles : "On formalise notre programme partenaires — intéressé ?" |

---

## PHASE 4 — MOIS 3 : ACCÉLÉRATION
### Objectif : Amplifier l'acquisition, activer la rétention et préparer la croissance long terme

**Score visé en fin de phase : 72/100**
**Budget phase 4 : 1 500 à 5 000 €**

---

### Action 4.1 — Email nurturing B2B (séquence automatisée)
**Responsable suggéré :** Catherine Guerniou + webmaster (configuration)
**Délai :** J+53 à J+75
**Budget :** 0 à 200 €/mois (Brevo/Mailchimp plan payant si > 500 contacts)

Les prospects B2B ont souvent un cycle de décision long (plusieurs semaines à plusieurs mois). Une séquence d'emails automatisée permet de maintenir le contact sans effort.

**Séquence pour les leads du formulaire pro (déclenchée à la soumission du formulaire) :**

```
EMAIL 1 — J+0 (immédiat) : Confirmation de réception
Objet : "Votre demande La Fenêtrière — nous revenons vers vous sous 48h"
Contenu : Confirmation, présentation rapide de l'atelier, numéro direct Catherine

EMAIL 2 — J+3 : Contenu de valeur
Objet : "En attendant votre devis : notre guide RE2020 pour les pros"
Contenu : Lien vers le guide téléchargeable, 3 exemples de chantiers, témoignage B2B

EMAIL 3 — J+10 : Social proof
Objet : "Ce que disent les artisans qui travaillent avec nous depuis 10 ans"
Contenu : 2 témoignages clients B2B, photos chantiers, présentation programme prescripteurs

EMAIL 4 — J+21 : Réactivation (si pas de réponse au devis)
Objet : "Votre projet de menuiseries — une question ?"
Contenu : Offre de rappel gratuit, question ouverte sur le projet, CTA simple
```

**Séquence pour les téléchargeurs du guide pro (leads inbound) :**
```
EMAIL 1 — J+0 : Livraison du guide
EMAIL 2 — J+5 : Article de blog pertinent lié au contenu du guide
EMAIL 3 — J+14 : CTA vers demande de devis
```

**KPI :**
- Taux d'ouverture des emails (cible : > 35% pour une liste qualifiée)
- Taux de clic (cible : > 8%)
- Conversions email → demande de devis (cible : > 5% de la liste active)

---

### Action 4.2 — Publicité ciblée Google Ads (campagne locale)
**Responsable suggéré :** Prestataire Google Ads ou Catherine Guerniou (avec formation)
**Délai :** J+60 à J+90
**Budget :** 500 à 1 500 €/mois selon scénario

**Uniquement recommandé après la mise en place des Phases 1 et 2.** Faire de la publicité vers un site sans pages produits et avec un formulaire à 11 champs aurait été du gaspillage.

**Campagnes recommandées :**

**Campagne 1 — Search local (priorité absolue)**
- Mots-clés cibles : "fenêtres sur mesure Champigny", "fabricant fenêtres Île-de-France", "menuiseries PVC Val-de-Marne", "devis fenêtres pro IDF"
- Géociblage : Île-de-France, rayon 30 km de Champigny-sur-Marne
- Budget recommandé : 300-600 €/mois
- Extension d'annonce : numéro de téléphone + adresse + sitelinks vers pages produits

**Campagne 2 — MaPrimeRénov' (saisonnière)**
- Mots-clés : "MaPrimeRénov' fenêtres 2026", "aide remplacement fenêtres", "fenêtre PVC MaPrimeRénov Île-de-France"
- Timing : Mars à juin 2026 (post-réouverture du dispositif)
- Budget recommandé : 200-400 €/mois
- Landing page dédiée : l'article de blog créé en Phase 3 (avec formulaire intégré)

**Campagne 3 — Remarketing (si Volume suffisant)**
- Audience : visiteurs du site n'ayant pas rempli le formulaire
- Format : bannières Google Display avec message "Vous souhaitiez un devis ? Revenez — réponse sous 48h"
- Budget : 100-200 €/mois

**KPI :**
- Coût par clic (CPC) cible : < 2,50 € sur les mots-clés locaux
- Coût par lead (CPL) cible : < 50 € (pour un panier moyen de 3 000-8 000 €, le ROI est très favorable)
- Taux de conversion annonces → formulaire (cible : > 5%)

---

### Action 4.3 — Relations presse et partenariats médias
**Responsable suggéré :** Catherine Guerniou
**Délai :** J+53 à J+90
**Budget :** 0 à 200 € (temps interne + envoi d'un communiqué)

La Fenêtrière a un actif RP sous-exploité exceptionnel : l'exposition à l'Élysée en 2025. Un communiqué de presse bien formulé peut générer des retombées dans des médias spécialisés et généralistes.

**Médias cibles :**
- Presse spécialisée BTP : Batiactu, Le Moniteur, Construction21, Batirama
- Presse économique locale : Le Parisien Économie, BFM Business, Les Échos PME
- Presse grand public Made in France : France 2 "C'est possible", Capital Made in France, 60 Millions de Consommateurs
- Presse engagée / RSE : L'Obs, Causette, Novethic

**Angles RP disponibles :**
1. "Une PME artisanale de Champigny expose à l'Élysée — et continue à fabriquer local"
2. "RE2020 : comment un atelier francilien anticipe les critères carbone que les grands groupes ignorent"
3. "Économie circulaire dans la menuiserie : La Fenêtrière inscrit la réparabilité dans ses statuts"
4. "MaPrimeRénov' : l'artisanat de proximité, grande oubliée du dispositif ?"

**KPI :**
- 2 à 3 retombées presse en 90 jours (objectif réaliste avec un bon angle)
- Backlinks de qualité vers le site (impact SEO à 6 mois)

---

### Action 4.4 — Partenariats locaux et institutionnels
**Responsable suggéré :** Catherine Guerniou
**Délai :** J+60 à J+90
**Budget :** 0 €

**Partenariats à activer ou formaliser :**

| Partenaire | Type | Valeur |
|---|---|---|
| Chambre de Commerce et d'Industrie du Val-de-Marne | Réseau | Réseau PME locales, mise en relation promoteurs |
| FFB (Fédération Française du Bâtiment IDF) | Réseau | Accès conducteurs de travaux, réseau artisans |
| CAPEB Val-de-Marne | Réseau | Artisans prescripteurs locaux |
| Bailleurs sociaux IDF (I3F, Valophis, Paris Habitat) | Commercial | Marchés publics répétitifs, volumes |
| Architectes DPLG IDF (annuaire CROA IDF) | Prescripteurs | Recommandations premium |
| Label Entreprises du Patrimoine Vivant | Certification | Différenciation, accès marchés publics |

**KPI :** 2 à 3 partenariats formalisés en 90 jours. 1 appel d'offre marché public déposé ou en cours.

---

### Action 4.5 — Calculateur bilan carbone (prototype)
**Responsable suggéré :** Développeur web + Catherine Guerniou (données)
**Délai :** J+75 à J+90 (prototype) — livraison complète M+4
**Budget :** 500 à 2 000 €

Un outil interactif de comparaison du bilan carbone (fenêtre La Fenêtrière vs menuiserie importée) serait un outil de vente différenciant majeur, particulièrement auprès des donneurs d'ordre engagés RE2020.

**Fonctionnalité minimum viable :**
```
Input : Type de menuiserie + Matériau + Quantité
Output : Bilan carbone estimé La Fenêtrière (circuit court) vs
         Bilan carbone moyen du marché (import Asie/Europe Est)
         → Économie CO2 en kg
         → Équivalent km de voiture
CTA : "Demander un devis pour ce projet"
```

**KPI :** Nombre d'utilisations de l'outil (cible : > 30/mois à M+4). Taux de conversion outil → devis (cible : > 15%).

---

### Récapitulatif Phase 4

| Action | Responsable | Délai | Budget estimé |
|--------|-------------|-------|---------------|
| 4.1 Email nurturing | Catherine + WM | J+53–75 | 0–200 € |
| 4.2 Google Ads local | Prestataire / CG | J+60–90 | 500–1 500 €/mois |
| 4.3 Relations presse | Catherine Guerniou | J+53–90 | 0–200 € |
| 4.4 Partenariats locaux | Catherine Guerniou | J+60–90 | 0 € |
| 4.5 Calculateur carbone | Dev web | J+75–90 | 500–2 000 € |

**Budget total Phase 4 : 1 000 à 3 900 €**
**Impact attendu :** 40 à 70 leads qualifiés/mois à J+90, panier moyen 3 000–8 000 €

### Risques Phase 4

| Risque | Probabilité | Impact | Mitigation |
|--------|-------------|--------|------------|
| Google Ads trop coûteux en IDF (CPC élevé menuiserie) | Moyen | Moyen | Tester avec budget minimal (300€/mois) le premier mois, optimiser avant de scaler |
| Relations presse sans retombées | Moyen | Faible | Aucun coût si interne — angle Élysée est objectivement fort ; même 1 article dans Batiactu vaut le temps investi |
| Calculateur carbone : données insuffisantes pour le prototype | Moyen | Faible | Version simplifiée avec données sectorielles génériques (INIES, base carbone ADEME) en attendant les mesures internes précises |

---

## CALENDRIER VISUEL DES 90 JOURS

```
MARS 2026
══════════════════════════════════════════════════════════════
Sem 1 (J1-7)   [██████████] QUICK WINS URGENTS
               Blog 404 corrigé ✓
               Formulaire 11→5 champs ✓
               CTA "Devis" ajouté homepage ✓
               Click-to-call ✓

Sem 2 (J8-14)  [██████████] QUICK WINS TECHNIQUES
               Title/Meta corrigés ✓
               Sitemap.xml soumis GSC ✓
               Attributs alt images ✓
               Certifications en hero ✓

AVRIL 2026
══════════════════════════════════════════════════════════════
Sem 3 (J15-21) [████████████████] FONDATIONS CONTENU
               Pages produits PVC + ALU (priorité 1) ✓
               Témoignages clients collectés ✓
               Schema LocalBusiness implémenté ✓

Sem 4 (J22-28) [████████████████] FONDATIONS SEO + LANCEMENT ACQU.
               Pages produits restantes (Bois, Portes, Volets, Portails) ✓
               Page Élysée 2025 publiée ✓
               Parcours B2B/B2C homepage ✓
               LinkedIn : 1er post ✓
               GMB optimisé ✓

MAI 2026
══════════════════════════════════════════════════════════════
Sem 5-6        [████████████████████████] ACQUISITION SEO
(J29-42)       Article 1 : Guide MaPrimeRénov' 2026 ✓
               Article 2 : Comparatif PVC/ALU/Bois ✓
               LinkedIn : 2 posts/semaine en rythme ✓
               Programme prescripteurs : 5 premiers contacts ✓

Sem 7-8        [████████████████████████] ACQUISITION AVANCÉE
(J43-56)       Article 3 : RE2020 et pros ✓
               Article 4 : Élysée — coulisses ✓
               Lead magnet "Guide Pro" disponible ✓
               Email nurturing configuré ✓
               Relations presse : communiqué envoyé ✓

JUIN 2026
══════════════════════════════════════════════════════════════
Sem 9-10       [████████████████████████████] ACCÉLÉRATION
(J57-70)       Google Ads local lancé (test budget minimal) ✓
               Programme prescripteurs : 10 partenaires ✓
               LinkedIn : continuité + 1er résultat mesurable ✓
               Articles blog : 2 nouveaux (entretien menuiseries + RSE) ✓

Sem 11-12      [████████████████████████████] BILAN + OPTIMISATION
(J71-90)       Calculateur carbone prototype ✓
               Partenariats institutionnels engagés ✓
               Bilan 90 jours : mesure des KPIs
               Révision du plan pour les 90 jours suivants ✓
══════════════════════════════════════════════════════════════
```

---

## BUDGET TOTAL — 3 SCÉNARIOS

### Scénario Bootstrap (DIY maximum)
**Total 90 jours : 500 à 1 500 €**

| Phase | Budget |
|-------|--------|
| Phase 1 — Quick Wins | 0–300 € (webmaster ponctuel si nécessaire) |
| Phase 2 — Fondations | 0–500 € (photos si nécessaire, plugin SEO) |
| Phase 3 — Acquisition | 0–400 € (outil emailing si > 500 contacts) |
| Phase 4 — Accélération | 500–1 500 € (Google Ads minimal) |

**Convient si :** Catherine Guerniou ou un membre de l'équipe peut consacrer 3 à 5 heures/semaine au projet. Résultats plus lents mais ROI maximal.

---

### Scénario Standard (Hybride interne + prestataires ponctuels)
**Total 90 jours : 4 000 à 8 000 €**

| Phase | Budget | Détail |
|-------|--------|--------|
| Phase 1 — Quick Wins | 500–800 € | Webmaster 5-8h + plugin |
| Phase 2 — Fondations | 1 500–2 500 € | Rédaction 4 pages produits + photos |
| Phase 3 — Acquisition | 800–1 500 € | 4 articles blog externalisés + outil email |
| Phase 4 — Accélération | 1 200–3 200 € | Google Ads 1 mois + RP + calculateur V1 |

**Convient si :** L'entreprise veut aller vite sur les fondations sans créer un poste interne dédié. Résultats dans les délais prévus.

---

### Scénario Ambitieux (Agence ou ressource dédiée)
**Total 90 jours : 12 000 à 20 000 €**

| Phase | Budget | Détail |
|-------|--------|--------|
| Phase 1 — Quick Wins | 1 000–1 500 € | Prestataire web senior + audit technique complet |
| Phase 2 — Fondations | 3 000–5 000 € | Refonte partielle + photos pro + 6 pages produits |
| Phase 3 — Acquisition | 3 000–5 000 € | SEO + LinkedIn managé + programme prescripteurs |
| Phase 4 — Accélération | 5 000–8 500 € | Google Ads géré + RP agence + calculateur carbone complet |

**Convient si :** La Fenêtrière identifie la croissance digitale comme une priorité stratégique à 12-24 mois et est prête à investir en conséquence. ROI projeté le plus fort (mais exige un suivi régulier des KPIs pour éviter le gaspillage).

---

## ROI PROJETÉ

### Hypothèses de base
- Trafic actuel estimé : 800 à 1 200 visiteurs/mois
- Taux de conversion actuel : 0,3 à 0,8% = 3 à 8 contacts/mois
- Taux de transformation contact → devis signé (estimé) : 25 à 40%
- Panier moyen commande : 3 000 à 8 000 € HT (menuiseries sur mesure B2B)
- Panier moyen estimé retenu : 5 000 € HT

**CA mensuel actuel estimé (base contacts web) :** 3 000 à 16 000 € HT

---

### Projections à 6 mois (Septembre 2026)

**Impact de la relance :**
- Trafic organique : +40 à 80% (SEO fondamentaux + blog 4 articles)
- Taux de conversion site : 0,8% → 3,5% (pages produits + formulaire simplifié + CTAs)
- Leads B2B qualifiés via prescripteurs et LinkedIn : +10 à 15/mois supplémentaires

| Scénario | Contacts/mois | Devis signés/mois | CA mensuel web estimé |
|----------|---------------|-------------------|------------------------|
| **Conservateur** | 25 | 6 | 30 000 € HT |
| **Médian** | 40 | 10 | 50 000 € HT |
| **Optimiste** | 60 | 15 | 75 000 € HT |

**ROI à 6 mois (scénario Standard 8 000€ investis) :**
- Gain mensuel conservateur vs actuel : +20 000 € HT/mois
- ROI break-even : 1,5 mois après la mise en place des fondations

---

### Projections à 12 mois (Mars 2027)

**Impact cumulé :**
- Trafic organique : x2,5 à x3,5 (SEO blog mature, 10+ articles indexés)
- Programme prescripteurs : 15 à 25 partenaires actifs
- Notoriété LinkedIn : 300 à 500 abonnés pro IDF, flux régulier de leads
- Google Ads : optimisé, CPL < 40 €

| Scénario | CA mensuel web estimé (M+12) | CA annuel incrémental |
|----------|------------------------------|------------------------|
| **Conservateur** | 40 000 € HT | +240 000 € HT/an |
| **Médian** | 70 000 € HT | +480 000 € HT/an |
| **Optimiste** | 120 000 € HT | +840 000 € HT/an |

**ROI à 12 mois (scénario Standard, investissement total ~ 15 000 € sur 12 mois) :**
- Ratio ROI conservateur : **16:1**
- Ratio ROI médian : **32:1**

> **Note :** Ces projections s'entendent comme l'ensemble du chiffre d'affaires potentiellement attribuable aux canaux digitaux (web, LinkedIn, email). Elles ne reflètent pas la totalité du CA de l'entreprise, qui inclut les commandes récurrentes des clients existants.

---

## GOUVERNANCE ET SUIVI

### Réunion de pilotage bimensuelle
Tous les 15 jours, 30 minutes de revue des indicateurs :
- Contacts reçus (formulaire + téléphone + LinkedIn)
- Trafic Google Analytics (sessions, sources, pages vues)
- Positions SEO via Google Search Console
- Performance LinkedIn (impressions, engagements, messages reçus)

### Tableau de bord KPIs cibles

| KPI | Aujourd'hui | J+30 | J+60 | J+90 |
|-----|-------------|------|------|------|
| Score marketing global | 38/100 | 50/100 | 62/100 | 72/100 |
| Taux de conversion site | 0,3–0,8% | 1,5–2,5% | 3–4% | 4–6% |
| Contacts/mois (web) | 3–8 | 15–25 | 25–40 | 40–65 |
| Pages indexées Google | ~10 | ~15 | ~25 | ~40 |
| Abonnés LinkedIn | — | +30 | +80 | +150 |
| Articles blog publiés | 0 | 0 | 4 | 8 |
| Prescripteurs actifs | 0 | 0 | 5 | 12 |
| Avis Google (note + nb) | Baseline | +2 avis | +5 avis | +10 avis |

### Critère de succès à J+90
La relance sera considérée comme réussie si l'entreprise reçoit **30 contacts qualifiés par mois via les canaux digitaux** (formulaire web + LinkedIn + téléphone trackable), contre 3 à 8 actuellement.

---

## SYNTHÈSE EXÉCUTIVE POUR CATHERINE GUERNIOU

La Fenêtrière entre dans sa relance digitale avec une **position de force rare** : 42 ans d'histoire, une certification OFG, une fenêtre bas carbone exposée à l'Élysée, une équipe stable et une gamme MIF que très peu de concurrents franciliens peuvent imiter.

**Le diagnostic est sans appel :** le site web ne reflète pas cette réalité. Il fuit les contacts à chaque page. Mais c'est une bonne nouvelle — cela signifie que les gains sont immédiats et que chaque correction produit un résultat mesurable.

**Les 5 actions les plus importantes (dans l'ordre) :**
1. **Corriger le blog 404 et simplifier le formulaire** — impact en 48h, zéro budget
2. **Créer des pages produits avec photos et CTAs** — c'est la correction qui transforme le trafic en devis
3. **Publier un article guide MaPrimeRénov'** — le meilleur levier SEO de 2026 dans le secteur
4. **Activer LinkedIn avec la voix de Catherine** — le seul canal B2B où une PME artisanale peut gagner face aux industriels
5. **Formaliser le programme prescripteurs** — structurer ce qui fonctionne déjà informellement

**Le marché 2026 est favorable** : rebond du logement neuf, MaPrimeRénov' relancée, RE2020 qui valorise exactement ce que La Fenêtrière produit. La fenêtre d'opportunité est ouverte. Ce playbook est le plan pour la franchir.

---

*Playbook généré le 20 mars 2026 — AI Marketing Suite*
*Site : la-fenetriere.fr — Score de départ : 38/100 — Score cible J+90 : 72/100*
*Basé sur l'analyse : MARKETING-AUDIT.md, SEO-AUDIT.md, LANDING-CRO.md, BRAND-STRATEGY.md*
