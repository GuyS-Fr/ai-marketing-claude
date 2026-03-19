Lance un audit marketing complet pour l'URL suivante : $ARGUMENTS

## Préparation

Avant de commencer, extrais le nom de domaine de l'URL (ex: calendly.com, notion.so) et crée un sous-dossier dédié : ./marketing-output/{nom-de-domaine}/
Tous les fichiers générés doivent être sauvegardés dans ce sous-dossier.

## Phase 1 — AUDITS & ANALYSES (Diagnostic)

1. **Audit complet à 360°** — /market audit $ARGUMENTS
   Lancer les 5 agents IA en parallèle (content, conversion, competitive, technical, strategy).
   Sauvegarder dans ./marketing-output/{nom-de-domaine}/MARKETING-AUDIT.md

2. **Évaluation flash** — /market quick $ARGUMENTS
   Audit rapide en 60 secondes avec scorecard.
   Sauvegarder dans ./marketing-output/{nom-de-domaine}/QUICK-AUDIT.md

3. **Audit SEO** — /market seo $ARGUMENTS
   Scan d'optimisation pour les moteurs de recherche organiques (Google).
   Sauvegarder dans ./marketing-output/{nom-de-domaine}/SEO-AUDIT.md

4. **Analyse de marque** — /market brand $ARGUMENTS
   Analyse de l'ADN et de la voix de la marque.
   Sauvegarder dans ./marketing-output/{nom-de-domaine}/BRAND-VOICE.md

## Phase 2 — CONVERSION & STRATÉGIE (Plan d'Attaque)

5. **Veille concurrentielle** — /market competitors $ARGUMENTS
   Veille concurrentielle et classement.
   Sauvegarder dans ./marketing-output/{nom-de-domaine}/COMPETITOR-REPORT.md

6. **Analyse du tunnel de vente** — /market funnel $ARGUMENTS
   Analyse des fuites dans le tunnel de vente.
   Sauvegarder dans ./marketing-output/{nom-de-domaine}/FUNNEL-ANALYSIS.md

7. **Optimisation landing page** — /market landing $ARGUMENTS
   Optimisation du taux de conversion des pages.
   Sauvegarder dans ./marketing-output/{nom-de-domaine}/LANDING-CRO.md

8. **Plan de lancement** — /market launch $ARGUMENTS
   Plan d'action étape par étape pour un lancement.
   Sauvegarder dans ./marketing-output/{nom-de-domaine}/LAUNCH-PLAYBOOK.md

## Phase 3 — CRÉATION & RÉDACTION (Production)

9. **Copies de vente** — /market copy $ARGUMENTS
   Réécriture de copies de vente (Avant/Après).
   Sauvegarder dans ./marketing-output/{nom-de-domaine}/COPY-SUGGESTIONS.md

10. **Séquences email** — /market emails $ARGUMENTS
    Séquences d'emails prêtes à envoyer.
    Sauvegarder dans ./marketing-output/{nom-de-domaine}/EMAIL-SEQUENCES.md

11. **Calendrier social** — /market social $ARGUMENTS
    Calendrier de publication de 30 jours.
    Sauvegarder dans ./marketing-output/{nom-de-domaine}/SOCIAL-CALENDAR.md

12. **Copies publicitaires** — /market ads $ARGUMENTS
    Angles créatifs et copies publicitaires.
    Sauvegarder dans ./marketing-output/{nom-de-domaine}/AD-CAMPAIGNS.md

## Phase 4 — AFFAIRES & LIVRABLES (Ventes Clients)

13. **Proposition commerciale** — /market proposal $ARGUMENTS
    Génération automatique de devis commercial.
    Sauvegarder dans ./marketing-output/{nom-de-domaine}/CLIENT-PROPOSAL.md

14. **Rapport texte** — /market report $ARGUMENTS
    Résumé de l'audit en format texte brut.
    Sauvegarder dans ./marketing-output/{nom-de-domaine}/MARKETING-REPORT.md

15. **Rapport PDF final** — /market report-pdf $ARGUMENTS
    Rapport d'audit graphique finalisé en PDF.
    Sauvegarder dans ./marketing-output/{nom-de-domaine}/

## Consignes

- Ne demande aucune confirmation entre les étapes
- Si une étape échoue, note l'erreur et passe à la suivante
- À la fin, affiche un résumé avec :
  - Le nom de domaine analysé
  - Le score marketing global
  - La liste des fichiers générés avec leur chemin complet
  - Les 3 points forts et les 3 axes d'amélioration prioritaires
- Tous les rapports doivent être rédigés en français
