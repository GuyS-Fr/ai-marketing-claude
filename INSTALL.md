# Guide d'Installation — AI Marketing Suite + CLI

Guide complet pour installer le projet sur n'importe quel PC (Windows, macOS, Linux).

---

## Ce que ce projet contient

```
ai-marketing-claude/
├── scripts/                    ← Scripts Python d'analyse web (scraping, PDF)
│   ├── analyze_page.py         ← Scraper de pages marketing
│   ├── competitor_scanner.py   ← Analyse des concurrents
│   └── generate_pdf_report.py  ← Générateur de rapport PDF
│
├── skills/                     ← Skills Claude Code (slash commands)
│   └── market-report-pdf/
│       └── SKILL.md            ← Skill /market report-pdf
│
├── agent-harness/              ← CLI installable en ligne de commande
│   ├── setup.py
│   └── cli_anything/aimarketing/
│       ├── aimarketing_cli.py  ← Point d'entrée CLI
│       ├── core/               ← Modules : audit, SEO, email, social...
│       └── utils/scraper.py    ← Pont vers les scripts Python
│
└── marketing-output/           ← Dossier de sortie (rapports générés)
```

---

## Prérequis

| Outil | Version minimum | Vérification |
|---|---|---|
| Python | 3.9+ | `python --version` |
| pip | inclus avec Python | `pip --version` |
| Git | toute version récente | `git --version` |
| Claude Code (optionnel) | dernière version | `claude --version` |

> **Windows :** utilisez PowerShell ou Git Bash (pas CMD).
> **macOS/Linux :** le terminal natif convient parfaitement.

---

## Installation — Étape par Étape

### Étape 1 — Cloner le dépôt

```bash
git clone https://github.com/zubair-trabzada/ai-marketing-claude.git
cd ai-marketing-claude
```

> Si vous avez déjà le dossier en local, passez directement à l'étape 2.

---

### Étape 2 — Installer les dépendances Python de base

Le scraper et les scripts Python n'ont besoin que de la bibliothèque standard Python.
Vérifiez simplement que Python est bien installé :

```bash
python --version
# → Python 3.9.x ou supérieur
```

Si Python n'est pas installé :
- **Windows :** télécharger sur [python.org](https://www.python.org/downloads/) — cocher "Add Python to PATH" pendant l'installation
- **macOS :** `brew install python3`
- **Ubuntu/Debian :** `sudo apt install python3 python3-pip`

---

### Étape 3 — Installer le CLI (`cli-anything-aimarketing`)

```bash
cd agent-harness
pip install -e .
```

> `-e` = mode "editable" — les modifications du code source sont immédiatement prises en compte sans réinstallation.

**Vérification :**
```bash
cli-anything-aimarketing --help
```

Vous devez voir la liste des commandes disponibles. Si la commande n'est pas trouvée, voir la section [Dépannage](#dépannage) ci-dessous.

---

### Étape 4 — Installer le support PDF (reportlab)

Le rapport PDF nécessite `reportlab` :

```bash
pip install reportlab
```

**Vérification :**
```bash
python -c "import reportlab; print('reportlab', reportlab.__version__, 'OK')"
# → reportlab 4.x.x OK
```

---

### Étape 5 — Tester l'installation complète

```bash
# Depuis le dossier agent-harness/
cd agent-harness

# Test 1 : audit rapide (sans réseau)
cli-anything-aimarketing quick https://example.com

# Test 2 : générer un rapport PDF de démonstration
python ../scripts/generate_pdf_report.py
# → Crée : MARKETING-REPORT-sample.pdf dans le dossier courant

# Test 3 : audit complet avec sauvegarde
cli-anything-aimarketing --output-dir "../marketing-output" audit https://example.com --save
```

---

## Utilisation Rapide

### Lancer une commande depuis n'importe où

```bash
# Audit complet d'un site
cli-anything-aimarketing audit https://monsite.com

# Audit SEO
cli-anything-aimarketing seo https://monsite.com

# Calendrier social 30 jours Instagram
cli-anything-aimarketing social "hôtel luxe alsace" --platform instagram --days 30

# Rapport PDF
cli-anything-aimarketing --output-dir "./rapports" pdf https://monsite.com

# Proposition commerciale
cli-anything-aimarketing --output-dir "./rapports" proposal "Mon Client" \
  --service "audit SEO et stratégie digitale" --save

# Mode interactif (REPL)
cli-anything-aimarketing repl
```

### Sortie JSON (pour intégration)

Ajoutez `--json` avant toute commande pour obtenir un JSON machine-readable :

```bash
cli-anything-aimarketing --json audit https://monsite.com
cli-anything-aimarketing --json seo https://monsite.com | python -m json.tool
```

---

## Générer un Rapport PDF Directement

Sans passer par le CLI, vous pouvez générer un PDF manuellement :

### 1. Créer un fichier JSON de données

Créez un fichier `mes-donnees.json` avec la structure suivante :

```json
{
  "url": "https://monsite.com",
  "date": "18 mars 2026",
  "brand_name": "Mon Entreprise",
  "overall_score": 62,
  "executive_summary": "Résumé de 2-4 phrases sur l'état du marketing.",
  "categories": {
    "Content & Messaging":     {"score": 68, "weight": "25%"},
    "Conversion Optimization": {"score": 52, "weight": "20%"},
    "SEO & Discoverability":   {"score": 74, "weight": "20%"},
    "Competitive Positioning": {"score": 48, "weight": "15%"},
    "Brand & Trust":           {"score": 70, "weight": "10%"},
    "Growth & Strategy":       {"score": 55, "weight": "10%"}
  },
  "findings": [
    {"severity": "Critical", "finding": "Description du problème critique"},
    {"severity": "High",     "finding": "Problème important"},
    {"severity": "Medium",   "finding": "Amélioration possible"},
    {"severity": "Low",      "finding": "Optimisation mineure"}
  ],
  "quick_wins": [
    "Action rapide 1 (cette semaine)",
    "Action rapide 2"
  ],
  "medium_term": [
    "Action moyen terme 1 (1-3 mois)"
  ],
  "strategic": [
    "Action stratégique 1 (3-6 mois)"
  ],
  "client": {
    "positioning": "Notre positionnement",
    "pricing":     "Nos tarifs",
    "social_proof":"Nos preuves sociales",
    "content":     "Notre approche contenu"
  },
  "competitors": [
    {
      "name": "Concurrent A",
      "positioning": "Son positionnement",
      "pricing":     "Ses tarifs",
      "social_proof":"Ses preuves sociales",
      "content":     "Son approche contenu"
    }
  ]
}
```

> ⚠️ Les clés des catégories doivent être exactement en anglais :
> `Content & Messaging`, `Conversion Optimization`, `SEO & Discoverability`,
> `Competitive Positioning`, `Brand & Trust`, `Growth & Strategy`

### 2. Générer le PDF

```bash
python scripts/generate_pdf_report.py mes-donnees.json RAPPORT-MON-CLIENT.pdf
```

### 3. Rapport de démonstration (sans données)

```bash
python scripts/generate_pdf_report.py
# → Génère : MARKETING-REPORT-sample.pdf
```

---

## Structure des Fichiers Générés

Tous les fichiers sont sauvegardés dans `./marketing-output/` par défaut (configurable avec `--output-dir`) :

| Fichier | Commande CLI |
|---|---|
| `MARKETING-AUDIT-*.md` | `audit --save` |
| `MARKETING-SEO-*.md` | `seo --save` |
| `MARKETING-PROPOSAL-*.md` | `proposal --save` |
| `MARKETING-EMAILS-*.md` | `emails --save` |
| `MARKETING-SOCIAL-*.md` | `social --save` |
| `MARKETING-REPORT-*.pdf` | `pdf` |
| `marketing-*.json` | export JSON interne |

---

## Toutes les Commandes Disponibles

```bash
# Audits
cli-anything-aimarketing audit <url>          # Audit marketing complet (6 dimensions)
cli-anything-aimarketing quick <url>          # Audit express 60 secondes
cli-anything-aimarketing seo <url>            # Audit SEO technique
cli-anything-aimarketing landing <url>        # Analyse CRO landing page
cli-anything-aimarketing brand <url>          # Analyse brand voice
cli-anything-aimarketing copy <url>           # Analyse et optimisation du copy

# Contenu
cli-anything-aimarketing emails <sujet>       # Séquences email (welcome, nurture, launch...)
cli-anything-aimarketing social <sujet>       # Calendrier social 30 jours
cli-anything-aimarketing ads <url>            # Campagnes publicitaires
cli-anything-aimarketing funnel <url>         # Analyse du funnel

# Concurrents & Stratégie
cli-anything-aimarketing competitors <url>    # Analyse concurrentielle
cli-anything-aimarketing launch <produit>     # Plan de lancement produit
cli-anything-aimarketing proposal <client>    # Proposition commerciale

# Rapports
cli-anything-aimarketing report <url>         # Rapport Markdown
cli-anything-aimarketing pdf <url>            # Rapport PDF visuel

# Session & REPL
cli-anything-aimarketing session show         # Voir la session courante
cli-anything-aimarketing session clear        # Effacer la session
cli-anything-aimarketing repl                 # Mode interactif
```

### Options globales

```bash
--json                        # Sortie JSON (toutes commandes)
--output-dir <chemin>         # Dossier de sortie (défaut : ./marketing-output)
-h / --help                   # Aide sur n'importe quelle commande
```

### Options par commande

```bash
# emails
--type [welcome|nurture|launch|cart-abandonment|cold-outreach|onboarding|re-engagement]
--audience <description>

# social
--platform [linkedin|twitter/x|instagram|tiktok|youtube]
--audience <description>
--days <nombre>

# ads
--platform [Google|Meta|LinkedIn|TikTok|YouTube]

# competitors
--main-url <votre-url>       # Votre site pour comparaison

# proposal
--service <description>
```

---

## Dépannage

### `cli-anything-aimarketing : command not found`

**Cause :** pip a installé le script dans un dossier non dans le PATH.

**Windows (PowerShell) :**
```powershell
# Trouver où pip installe les scripts
python -m site --user-scripts
# Ajouter ce chemin au PATH dans Paramètres > Système > Variables d'environnement
```

**Solution alternative (toutes plateformes) :**
```bash
# Utiliser python -m à la place
python -m cli_anything.aimarketing.aimarketing_cli --help
```

**Ou réinstaller avec sudo/admin :**
```bash
# macOS/Linux
sudo pip install -e .

# Windows : ouvrir PowerShell en tant qu'administrateur, puis
pip install -e .
```

---

### `Error: reportlab is required`

```bash
pip install reportlab
# ou
pip install "cli-anything-aimarketing[pdf]"
```

---

### Le CLI retourne `status: stub` (données vides)

**Cause :** le scraper ne trouve pas `analyze_page.py`.

**Vérification :**
```bash
python -c "
import os
here = os.path.abspath('cli_anything/aimarketing/utils')
scripts = os.path.normpath(os.path.join(here, '..', '..', '..', '..', 'scripts'))
print('Scripts dir:', scripts)
print('Existe:', os.path.exists(scripts))
print('analyze_page.py:', os.path.exists(os.path.join(scripts, 'analyze_page.py')))
"
```

**Solution :** toujours lancer le CLI depuis le dossier `agent-harness/` :
```bash
cd chemin/vers/ai-marketing-claude/agent-harness
cli-anything-aimarketing seo https://example.com
```

---

### Erreur SSL / réseau

```bash
# Désactiver la vérification SSL (non recommandé en production)
python -c "import ssl; ssl._create_default_https_context = ssl._create_unverified_context"
```

Le scraper intégré gère déjà les contextes SSL non vérifiés pour les sites avec certificats problématiques.

---

### Tests qui échouent

```bash
cd agent-harness

# Tests unitaires seulement (pas de réseau requis)
pytest cli_anything/aimarketing/tests/test_core.py -v

# Tests E2E (réseau requis)
pytest cli_anything/aimarketing/tests/test_full_e2e.py -v

# Tests subprocess (CLI installé requis)
CLI_ANYTHING_FORCE_INSTALLED=1 pytest cli_anything/aimarketing/tests/test_full_e2e.py -v -k "Subprocess"
```

---

## Installation Rapide — Résumé en 4 Commandes

```bash
# 1. Cloner
git clone https://github.com/zubair-trabzada/ai-marketing-claude.git
cd ai-marketing-claude/agent-harness

# 2. Installer le CLI
pip install -e .

# 3. Installer le support PDF
pip install reportlab

# 4. Vérifier
cli-anything-aimarketing --help
```

---

## Avec Claude Code (optionnel)

Si vous utilisez Claude Code (le CLI officiel d'Anthropic) :

```bash
# Installer Claude Code
npm install -g @anthropic-ai/claude-code

# Lancer depuis le dossier du projet
cd ai-marketing-claude
claude

# Les skills sont disponibles via slash commands dans Claude Code
# /market audit <url>
# /market report-pdf <url>
```

Les skills se trouvent dans `skills/market-report-pdf/SKILL.md` et sont automatiquement détectés par Claude Code.

---

## Informations Techniques

| Composant | Détail |
|---|---|
| Python requis | 3.9+ |
| Dépendance principale | `click>=7.0` |
| PDF | `reportlab>=4.0` |
| Scraping | `urllib` (bibliothèque standard — aucune installation) |
| Session | Fichier JSON dans `~/.cli_anything_aimarketing_session.json` |
| Namespace Python | `cli_anything.aimarketing.*` (PEP 420) |
| Tests | pytest 9.0+ — 66 tests, 100% pass |

---

*AI Marketing Suite — cli-anything-aimarketing v0.1.0*
*Dépôt source : https://github.com/zubair-trabzada/ai-marketing-claude*
