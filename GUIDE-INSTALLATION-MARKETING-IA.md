# Guide d'Installation — Suite Marketing IA + Rapport PDF Consolidé

**Version :** 2.0 — 19 mars 2026
**Prérequis :** VS Code + Claude Code déjà installés, plan Claude Max
**OS :** Windows (PowerShell)

---

## Vue d'ensemble

Ce guide permet d'installer un environnement complet d'analyse marketing automatisée avec Claude Code. À la fin de l'installation, la commande `/audit-complet https://example.com` lancera 17 étapes automatiques et produira un rapport PDF professionnel de 150-250 pages, prêt à remettre à un prospect.

### Ce que vous obtiendrez

- 16 skills d'analyse marketing (audit, SEO, GEO, concurrents, copywriting, etc.)
- 5 agents IA parallèles pour l'audit complet
- 1 slash command `/audit-complet` qui orchestre les 17 étapes
- 1 script Python de génération de rapport PDF consolidé (page de garde, sommaire, sections stylisées, numérotation globale)
- Possibilité de lancer plusieurs analyses en parallèle

### Les 17 étapes de l'audit complet

| Phase | N° | Commande | Fichier généré |
|-------|-----|----------|---------------|
| **Diagnostic** | 1 | /market audit | MARKETING-AUDIT.md |
| | 2 | /market quick | QUICK-AUDIT.md |
| | 3 | /market seo | SEO-AUDIT.md |
| | 4 | /market geo | GEO-AUDIT.md |
| | 5 | /market brand | BRAND-VOICE.md |
| **Stratégie** | 6 | /market competitors | COMPETITOR-REPORT.md |
| | 7 | /market funnel | FUNNEL-ANALYSIS.md |
| | 8 | /market landing | LANDING-CRO.md |
| **Production** | 9 | /market copy | COPY-SUGGESTIONS.md |
| | 10 | /market emails | EMAIL-SEQUENCES.md |
| | 11 | /market social | SOCIAL-CALENDAR.md |
| | 12 | /market ads | AD-CAMPAIGNS.md |
| **Livrables** | 13 | /market launch | LAUNCH-PLAYBOOK.md |
| | 14 | /market proposal | CLIENT-PROPOSAL.md |
| | 15 | /market report | MARKETING-REPORT.md |
| | 16 | /market report-pdf | MARKETING-REPORT-*.pdf |
| **Consolidation** | 17 | merge_full_report.py | RAPPORT-COMPLET-*.pdf |

### Architecture des fichiers

```
C:\DevClaude\Marketing\
├── .claude/
│   ├── commands/
│   │   └── audit-complet.md          ← Slash command principale (17 étapes)
│   ├── skills/
│   │   ├── market/SKILL.md           ← Orchestrateur principal
│   │   ├── market-audit/SKILL.md     ← Audit complet 360°
│   │   ├── market-seo/SKILL.md       ← Audit SEO (visibilité Google)
│   │   ├── market-geo/SKILL.md       ← Audit GEO (visibilité IA) ★ CUSTOM
│   │   ├── market-brand/SKILL.md     ← Voix de marque
│   │   ├── market-competitors/SKILL.md
│   │   ├── market-funnel/SKILL.md
│   │   ├── market-landing/SKILL.md
│   │   ├── market-copy/SKILL.md
│   │   ├── market-emails/SKILL.md
│   │   ├── market-social/SKILL.md
│   │   ├── market-ads/SKILL.md
│   │   ├── market-launch/SKILL.md
│   │   ├── market-proposal/SKILL.md
│   │   ├── market-report/SKILL.md
│   │   └── market-report-pdf/SKILL.md
│   ├── agents/
│   │   ├── market-content.md
│   │   ├── market-conversion.md
│   │   ├── market-competitive.md
│   │   ├── market-technical.md
│   │   └── market-strategy.md
│   ├── scripts/
│   │   ├── merge_full_report.py      ← Script PDF consolidé ★ CUSTOM
│   │   ├── generate_pdf_report.py    ← Script PDF scores (d'origine)
│   │   ├── analyze_page.py
│   │   ├── competitor_scanner.py
│   │   └── social_calendar.py
│   ├── templates/
│   │   ├── content-calendar.md
│   │   ├── email-launch.md
│   │   ├── email-nurture.md
│   │   ├── email-welcome.md
│   │   ├── launch-checklist.md
│   │   └── proposal-template.md
│   └── settings.local.json           ← Permissions projet
├── marketing-output/
│   ├── onpulse.fr/                   ← Résultats par domaine
│   │   ├── MARKETING-AUDIT.md
│   │   ├── GEO-AUDIT.md
│   │   ├── ...
│   │   └── RAPPORT-COMPLET-onpulse-fr.pdf
│   └── autre-site.com/
└── CLAUDE.md                         ← (optionnel) Instructions projet
```

> **★ CUSTOM** = fichiers développés sur mesure, non inclus dans le dépôt d'origine.

---

## Étape 1 — Prérequis logiciels

### 1.1 Vérifier les installations existantes

```powershell
# Claude Code
claude --version

# Python (3.9+ requis)
python --version

# Node.js (pour Claude Code)
node --version

# Git
git --version

# Chrome (requis pour la génération PDF)
Test-Path "C:\Program Files\Google\Chrome\Application\chrome.exe"
# Doit retourner True
```

### 1.2 Mettre à jour Claude Code

```powershell
npm update -g @anthropic-ai/claude-code
```

### 1.3 Installer les bibliothèques Python

```powershell
pip install reportlab
pip install pypdf
```

**Vérification :**
```powershell
python -c "import reportlab; print('reportlab OK')"
python -c "from pypdf import PdfReader; print('pypdf OK')"
```

### 1.4 Extensions VS Code recommandées

Installer via `Ctrl+Shift+X` dans VS Code :

| Extension | Identifiant | Rôle |
|-----------|-------------|------|
| Claude Code for VS Code | `anthropic.claude-code` | Outil principal |
| Claude Usage Monitor | `wilendar.claude-usage-monitor` | Suivi consommation tokens |
| GitLens | `eamodio.gitlens` | Historique des modifications |

---

## Étape 2 — Activer le contexte 1M tokens

Dans Claude Code (terminal VS Code), taper :

```
/model opus[1m]
```

**Vérification :** le sélecteur de modèle doit afficher `opus[1m]`.

> **Note :** Ceci est automatique sur les plans Max, Team et Enterprise. Si le modèle n'apparaît pas, vérifier que Claude Code est à jour et que la variable d'environnement `CLAUDE_CODE_DISABLE_1M_CONTEXT` n'est pas définie.

---

## Étape 3 — Configurer le settings.json global Claude Code

```powershell
notepad "$env:USERPROFILE\.claude\settings.json"
```

Contenu minimal recommandé :

```json
{
  "alwaysThinkingEnabled": true
}
```

> **Important :** Ne pas mettre de `statusLine` pointant vers un script `.sh` (Bash) sur Windows. Si vous voulez une statusline, utilisez un script Node.js ou ccstatusline.

---

## Étape 4 — Créer le projet Marketing

### 4.1 Créer la structure de dossiers

```powershell
mkdir C:\DevClaude\Marketing
cd C:\DevClaude\Marketing

# Initialiser Git
git init
```

### 4.2 Cloner le dépôt source AI Marketing Suite

```powershell
git clone https://github.com/zubair-trabzada/ai-marketing-claude.git temp-marketing
```

### 4.3 Copier les fichiers dans la structure projet

```powershell
# Créer les dossiers cibles
mkdir -Force .claude\skills
mkdir -Force .claude\agents
mkdir -Force .claude\scripts
mkdir -Force .claude\templates
mkdir -Force .claude\commands
mkdir -Force marketing-output

# Copier les skills (orchestrateur + 14 sub-skills)
Copy-Item -Recurse temp-marketing\market .claude\skills\market
Copy-Item -Recurse temp-marketing\skills\* .claude\skills\

# Copier les agents (5 agents parallèles)
Copy-Item temp-marketing\agents\*.md .claude\agents\

# Copier les scripts Python
Copy-Item temp-marketing\scripts\*.py .claude\scripts\

# Copier les templates
Copy-Item temp-marketing\templates\*.md .claude\templates\
```

### 4.4 Nettoyer le dépôt temporaire

```powershell
Remove-Item -Recurse -Force temp-marketing
```

---

## Étape 5 — Installer les fichiers custom

Trois fichiers custom sont fournis séparément (non inclus dans le dépôt d'origine) :

| Fichier | Emplacement | Description |
|---------|-------------|-------------|
| `merge_full_report.py` | `.claude/scripts/` | Script de génération PDF consolidé |
| `audit-complet.md` | `.claude/commands/` | Slash command 17 étapes |
| `SKILL.md` (market-geo) | `.claude/skills/market-geo/` | Skill GEO — Visibilité IA |

### 5.1 Installer le script PDF consolidé

```powershell
Copy-Item "chemin\vers\merge_full_report.py" "C:\DevClaude\Marketing\.claude\scripts\merge_full_report.py"
```

**Vérification :**
```powershell
python .claude\scripts\merge_full_report.py
# Doit afficher : Usage: python merge_full_report.py <report_dir> [output.pdf]
```

**Ce que fait le script :**
1. Crée une **page de garde** premium (nom du site, date, type de document)
2. Intègre le **PDF de scores** avec jauges visuelles (s'il existe)
3. Génère un **sommaire** professionnel
4. Convertit chaque fichier **Markdown → HTML** avec un template CSS consulting premium
5. Rend chaque HTML en **PDF** via Chrome headless
6. **Fusionne** le tout en un seul PDF avec numérotation globale
7. Ajoute un **pied de page** sur chaque page : `Section XX — Nom | CONFIDENTIEL — domaine | Page X / Total`

### 5.2 Installer la slash command

```powershell
mkdir -Force C:\DevClaude\Marketing\.claude\commands
Copy-Item "chemin\vers\audit-complet.md" "C:\DevClaude\Marketing\.claude\commands\audit-complet.md"
```

**Vérification :** dans Claude Code, taper `/` — la commande `audit-complet` doit apparaître.

### 5.3 Installer le skill GEO

```powershell
mkdir -Force C:\DevClaude\Marketing\.claude\skills\market-geo
Copy-Item "chemin\vers\SKILL.md" "C:\DevClaude\Marketing\.claude\skills\market-geo\SKILL.md"
```

**Ce que le skill GEO audite :**
- Test de visibilité sur ChatGPT, Gemini, Perplexity, Claude
- Citabilité du contenu (statistiques, sources, structure extractible)
- Données structurées (schema.org) et accessibilité aux crawlers IA
- Autorité d'entité (E-E-A-T) et mentions tierces
- Avis et sentiment en ligne
- Fraîcheur du contenu
- Empreinte linguistique (Seed-to-Series Statements)
- Score GEO global sur 100 avec plan d'action priorisé

---

## Étape 6 — Configurer les permissions du projet

```powershell
notepad C:\DevClaude\Marketing\.claude\settings.local.json
```

Contenu :

```json
{
  "permissions": {
    "allow": [
      "Bash(*)",
      "WebFetch(*)",
      "WebSearch(*)",
      "Read(*)",
      "Write(*)",
      "mcp__*"
    ]
  }
}
```

> **Note :** Ces permissions sont larges (mode "yolo"). Elles évitent que Claude Code pose des questions à chaque action. À restreindre si nécessaire dans un contexte d'équipe.

---

## Étape 7 — Installer le CLI Python (optionnel)

Le CLI `cli-anything-aimarketing` permet de lancer des analyses depuis la ligne de commande sans Claude Code.

```powershell
cd C:\DevClaude\Marketing\temp-marketing\agent-harness
pip install -e .
```

**Vérification :**
```powershell
cli-anything-aimarketing --help
```

> **Note :** Si la commande n'est pas trouvée, vérifier que le dossier Scripts de Python est dans le PATH :
> ```powershell
> python -m site --user-scripts
> ```

---

## Étape 8 — Test complet

### 8.1 Lancer un audit complet

Dans VS Code, ouvrir le dossier `C:\DevClaude\Marketing`, puis dans le terminal Claude Code :

```
/audit-complet https://example.com
```

### 8.2 Vérifier les fichiers générés

```powershell
Get-ChildItem .\marketing-output\example.com\ -Recurse
```

Fichiers attendus :

| N° | Fichier | Phase |
|----|---------|-------|
| 1 | MARKETING-AUDIT.md | Diagnostic |
| 2 | QUICK-AUDIT.md | Diagnostic |
| 3 | SEO-AUDIT.md | Diagnostic |
| 4 | GEO-AUDIT.md | Diagnostic |
| 5 | BRAND-VOICE.md | Diagnostic |
| 6 | COMPETITOR-REPORT.md | Stratégie |
| 7 | FUNNEL-ANALYSIS.md | Stratégie |
| 8 | LANDING-CRO.md | Stratégie |
| 9 | COPY-SUGGESTIONS.md | Production |
| 10 | EMAIL-SEQUENCES.md | Production |
| 11 | SOCIAL-CALENDAR.md | Production |
| 12 | AD-CAMPAIGNS.md | Production |
| 13 | LAUNCH-PLAYBOOK.md | Livrables |
| 14 | CLIENT-PROPOSAL.md | Livrables |
| 15 | MARKETING-REPORT.md | Livrables |
| 16 | MARKETING-REPORT-*.pdf | Livrables |
| 17 | RAPPORT-COMPLET-*.pdf | Consolidation |

### 8.3 Régénérer le PDF seul (sans relancer l'audit)

Si les fichiers Markdown existent déjà :

```powershell
python .claude\scripts\merge_full_report.py ".\marketing-output\example.com"
```

---

## Étape 9 — Lancer plusieurs analyses en parallèle

Ouvrir plusieurs terminaux Claude Code dans VS Code (bouton `+`) et lancer un audit par terminal :

```
Terminal 1 → /audit-complet https://site1.com
Terminal 2 → /audit-complet https://site2.com
Terminal 3 → /audit-complet https://site3.com
```

Chaque analyse crée son propre sous-dossier dans `marketing-output/`, donc pas de conflit.

---

## Étape 10 — Commandes individuelles

Chaque étape peut être lancée séparément :

```
/market audit https://example.com        # Audit 360° (5 agents parallèles)
/market quick https://example.com        # Évaluation flash 60 secondes
/market seo https://example.com          # Audit SEO (visibilité Google)
/market geo https://example.com          # Audit GEO (visibilité IA) ★ NOUVEAU
/market brand https://example.com        # Voix de marque
/market competitors https://example.com  # Analyse concurrentielle
/market funnel https://example.com       # Tunnel de vente
/market landing https://example.com      # CRO landing page
/market copy https://example.com         # Suggestions copywriting
/market emails https://example.com       # Séquences email
/market social https://example.com       # Calendrier social 30 jours
/market ads https://example.com          # Campagnes publicitaires
/market launch https://example.com       # Plan de lancement
/market proposal https://example.com     # Proposition commerciale
/market report https://example.com       # Rapport texte Markdown
/market report-pdf https://example.com   # Rapport PDF avec scores
```

---

## Dépannage

### Le terminal PowerShell boucle à l'ouverture

**Cause probable :** un script de statusline cassé dans `settings.json`.

**Solution :**
```powershell
notepad "$env:USERPROFILE\.claude\settings.json"
```
Supprimer toute entrée `statusLine` pointant vers un fichier `.sh`. Remplacer par :
```json
{
  "alwaysThinkingEnabled": true
}
```

### Claude Code pose des questions pendant l'audit

**Solution :** à chaque question, choisir l'option "Yes, and don't ask again for...". Ou vérifier que le fichier `settings.local.json` contient bien les permissions larges (voir étape 6).

### Le script PDF échoue avec "Permission denied"

**Cause :** le PDF précédent est ouvert dans un lecteur.

**Solution :** fermer le PDF, puis relancer le script.

### Le script PDF échoue avec "Chrome not found"

**Solution :** vérifier que Chrome est installé :
```powershell
Test-Path "C:\Program Files\Google\Chrome\Application\chrome.exe"
```

### Les tableaux sont mal formatés dans le PDF

Le script `merge_full_report.py` attribue automatiquement les largeurs de colonnes proportionnellement au contenu. Si un tableau est toujours mal rendu, c'est que le Markdown source contient des cellules très longues. Solution : réduire le texte dans les cellules ou splitter le tableau.

### Le skill GEO ne se déclenche pas

**Vérifier :**
```powershell
Test-Path "C:\DevClaude\Marketing\.claude\skills\market-geo\SKILL.md"
```
Si le fichier existe, relancer une nouvelle session Claude Code (le chargement des skills se fait au démarrage).

---

## Récapitulatif des fichiers custom

| Fichier | Emplacement | Description | Origine |
|---------|-------------|-------------|---------|
| `merge_full_report.py` | `.claude/scripts/` | Script PDF consolidé (page de garde, sommaire, Chrome headless, numérotation globale) | Développement custom |
| `audit-complet.md` | `.claude/commands/` | Slash command 17 étapes (5 phases) | Développement custom |
| `SKILL.md` (market-geo) | `.claude/skills/market-geo/` | Audit GEO — visibilité dans les réponses IA | Développement custom |

Ces trois fichiers ne sont pas inclus dans le dépôt `ai-marketing-claude` d'origine. Ils doivent être fournis séparément au collaborateur.

---

*Guide d'installation — Suite Marketing IA v2.0 — Mars 2026*
