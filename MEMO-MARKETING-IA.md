# Mémo — Suite Marketing IA (setup rapide)

## Prérequis

```powershell
npm update -g @anthropic-ai/claude-code
pip install reportlab pypdf
```

Extensions VS Code : `anthropic.claude-code`, `wilendar.claude-usage-monitor`, `eamodio.gitlens`

## Contexte 1M

Dans Claude Code : `/model opus[1m]`

## Settings global

`~/.claude/settings.json` :
```json
{
  "alwaysThinkingEnabled": true
}
```

## Structure projet

```powershell
mkdir C:\DevClaude\Marketing
cd C:\DevClaude\Marketing
git init

git clone https://github.com/zubair-trabzada/ai-marketing-claude.git temp-marketing

mkdir -Force .claude\skills, .claude\agents, .claude\scripts, .claude\templates, .claude\commands, marketing-output

Copy-Item -Recurse temp-marketing\market .claude\skills\market
Copy-Item -Recurse temp-marketing\skills\* .claude\skills\
Copy-Item temp-marketing\agents\*.md .claude\agents\
Copy-Item temp-marketing\scripts\*.py .claude\scripts\
Copy-Item temp-marketing\templates\*.md .claude\templates\

Remove-Item -Recurse -Force temp-marketing
```

## Fichiers custom (fournis séparément)

```
.claude\scripts\merge_full_report.py        ← Script PDF consolidé
.claude\commands\audit-complet.md            ← Slash command 17 étapes
.claude\skills\market-geo\SKILL.md           ← Skill GEO (visibilité IA)
```

## Installer le skill GEO

```powershell
mkdir -Force .claude\skills\market-geo
# Copier SKILL.md dans .claude\skills\market-geo\
```

## Permissions projet

`.claude\settings.local.json` :
```json
{
  "permissions": {
    "allow": ["Bash(*)", "WebFetch(*)", "WebSearch(*)", "Read(*)", "Write(*)", "mcp__*"]
  }
}
```

## Utilisation

```
/audit-complet https://example.com
```

17 étapes en 5 phases :
1. **Diagnostic** (5) : audit 360°, quick, SEO, GEO, brand
2. **Stratégie** (3) : competitors, funnel, landing
3. **Production** (4) : copy, emails, social, ads
4. **Livrables** (4) : launch, proposal, report, report-pdf
5. **Consolidation** (1) : merge_full_report.py → PDF final

Régénérer le PDF seul :
```powershell
python .claude\scripts\merge_full_report.py ".\marketing-output\example.com"
```

Parallèle : ouvrir plusieurs terminaux Claude Code, un audit par terminal.

## Dépannage

| Problème | Solution |
|----------|----------|
| Terminal boucle | Supprimer `statusLine` dans `~/.claude/settings.json` |
| Claude pose des questions | Choisir "Yes, and don't ask again" ou vérifier `settings.local.json` |
| PDF "Permission denied" | Fermer le PDF ouvert, relancer |
| Chrome not found | Vérifier : `Test-Path "C:\Program Files\Google\Chrome\Application\chrome.exe"` |
