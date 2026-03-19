# Analyse Landing Page CRO — SMARTHOME SMARTELEC
**URL :** https://smarthome-smartelec.fr
**Date :** 19 mars 2026
**Score Conversion : 28/100**

---

## Synthèse

Le site fonctionne sur un modèle binaire catastrophique : le visiteur réserve un audit gratuit ou il disparaît définitivement. Estimation : **97-99% des visiteurs repartent sans laisser de trace**. Le CTA unique est bien formulé mais sans filet de sécurité ni preuve sociale à proximité.

---

## Forces

- **CTA principal bien formulé** : "Réserver un Audit gratuit (30 minutes)" — explicite, engagement faible, valeur perçue élevée
- **Méthode en 3 étapes visible** : Analyse → Plan → Déploiement — rassure sur le processus
- **Cal.com** élimine l'aller-retour email
- **Numéro de téléphone visible** (06 72 13 91 37)
- **Conformité RGPD + DPO** déclaré (CNIL DPO-50061)
- **Logos partenaires tech** (n8n, Airtable, Supabase, etc.)

---

## Faiblesses Critiques

### 1. Point de conversion unique sans alternative (1/10)
Si le visiteur n'est pas prêt à booker, il n'existe aucun plan B :
- Aucun formulaire de contact classique
- Aucune capture d'email / newsletter
- Aucun lead magnet (PDF, checklist, quiz)
- Aucun content upgrade dans les articles de blog

### 2. Zéro preuve sociale au point de conversion (2/10)
- Aucun témoignage client (texte, vidéo, étoiles)
- Aucune photo du fondateur avec contexte
- Aucun badge de certification visible au moment de la décision
- Aucune garantie explicite ("sans engagement")
- Aucune référence au projet Activage
- Background consultant SI/CRM non présenté comme story convaincante

### 3. Redirection externe vers cal.com (3/10)
Le tunnel actuel :
```
Homepage → Clic CTA → Redirection cal.com → Sélection créneaux → Saisie infos → Confirmation
= 5 étapes avec rupture de domaine à l'étape 3
```

**Risques d'abandon par étape :**

| Étape | Risque | Cause |
|---|---|---|
| Arrivée page | Élevé | Navigation contradictoire |
| Lecture CTA | Moyen | Pas de preuve sociale ni anti-risque |
| Clic vers cal.com | **Élevé** | **Changement de domaine** |
| Calendrier cal.com | Moyen | Interface générique sans branding |
| Saisie informations | Faible | Standard |

### 4. Email Gmail (2/10)
`smarthome.smartelec@gmail.com` = signal d'amateurisme rédhibitoire en B2B

### 5. Aucune urgence ou rareté (1/10)
Rien n'incite à agir maintenant : pas de mention de disponibilité limitée, pas de fenêtre temporelle

### 6. Navigation contradictoire (3/10)
Les entrées "alarme, domotique, électricité" brouillent l'identité IA/automatisation

### 7. Blog sans conversion (1/10)
9 articles sans CTA, sans content upgrade = trafic 100% en fuite

### 8. Pas de pricing (2/10)
Les PME veulent se qualifier avant d'engager une conversation

### 9. Mobile non optimisé pour la conversion (4/10)
- Pas de CTA sticky
- Pas de click-to-call (`tel:`)
- Pas de WhatsApp Business
- Redirection cal.com encore plus problématique sur mobile

### 10. Zéro traitement des objections (2/10)

| Objection probable | Réponse sur le site |
|---|---|
| "C'est trop compliqué pour moi" | Absente |
| "Je n'ai pas le temps" | Absente |
| "Combien ça coûte ?" | Absente |
| "Et si ça ne marche pas ?" | Absente |
| "Je ne connais pas cet interlocuteur" | Partiellement (certifications) |
| "Mes données sont-elles en sécurité ?" | RGPD mentionné (seul point positif) |
| "Combien de temps pour voir des résultats ?" | Absente |
| "Qu'est-ce qu'on fait pendant l'audit ?" | Absente |

---

## Recommandations par Impact

| Priorité | Action | Impact estimé | Délai |
|----------|--------|---------------|-------|
| 1 | Statement anti-risque sous le CTA | +5-10% taux de clic | 30 min |
| 2 | Embed Cal.com inline (pas redirection) | +10-20% complétion booking | 1h |
| 3 | 1 témoignage client au-dessus du CTA | +15-25% confiance | 1 jour |
| 4 | Lead magnet PDF + formulaire email | ×5-10 leads capturés | 1 semaine |
| 5 | Click-to-call sur le numéro | +10-15% contacts mobile | 15 min |
| 6 | CTA en pied de chaque article blog | 2-5% lecteurs → leads | 2h |
| 7 | Email pro @smarthome-smartelec.fr | Signal de confiance immédiat | 1h |
| 8 | FAQ 5-8 objections courantes | Réduction abandon | 2h |
| 9 | CTA sticky mobile | +5-10% interactions mobile | 1h |
| 10 | WhatsApp Business | Canal artisan natif | 30 min |

---

## Architecture de Conversion Recommandée

### Tunnel principal optimisé
```
Homepage (anti-risque + témoignage + CTA)
    → Cal.com embed inline (pas de redirection)
        → Confirmation (email auto avec récapitulatif)
= 3 étapes, même domaine
```

### Tunnels secondaires (capture les non-prêts)
```
Blog → Content upgrade (PDF) → Email capturé → Séquence nurturing → Booking
Homepage → Lead magnet ("10 tâches à automatiser") → Email → Nurturing → Booking
Homepage → WhatsApp → Conversation → Booking
Mobile → Click-to-call → Appel direct
```

### Éléments à ajouter au-dessus du CTA
```
[Photo Guy + titre "Ancien consultant SI/CRM, certifié Jeedom & Delta Dore"]
[Témoignage : "Nous avons réduit le temps de traitement de nos devis de 60%"]
[Badges : RGPD | Hébergement EU | Certifié]
[ BOUTON : Réserver un Audit gratuit (30 minutes) ]
[Texte : "Sans engagement — vous repartez avec un plan d'action concret"]
```

---

## Métriques Cibles

| Métrique | Actuel (estimé) | Cible à 3 mois |
|---|---|---|
| Taux de conversion visiteur → booking | 0,5-1% | 3-5% |
| Taux de capture email | 0% | 5-10% |
| Taux d'abandon CTA | 80-90% | 50-60% |
| Visiteurs identifiés (email ou booking) | 1-3% | 10-15% |

---

*Analyse Landing Page CRO — AI Marketing Suite `/market landing`*
*Date : 19 mars 2026*
