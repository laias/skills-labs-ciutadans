---
title: "Setup entorn de desenvolupament — Mac nou"
created: 2026-04-01
classificació-org: N3-personal
classificació-tec: NT1-prompt
tags: [setup, entorn, mac, git, github, vscode, node]
---

# Setup entorn de desenvolupament en un Mac nou

## Context

Procés per replicar un entorn de desenvolupament complet en un ordinador nou
(macOS). Executat al MacBook portàtil a partir del Mac de Citilab com a referència.

## Prerequisits

- Compte GitHub existent amb repos creats
- Clau SSH ja generada a l'altre ordinador (no cal exportar-la, es crea una de nova)

## Passos

### 1. Verificar el que ja hi ha
```bash
brew --version
git --version
node --version
```

### 2. Instal·lar nvm i Node
```bash
brew install nvm
echo 'export NVM_DIR="$HOME/.nvm"' >> ~/.zshrc
echo '[ -s "/opt/homebrew/opt/nvm/nvm.sh" ] && \. "/opt/homebrew/opt/nvm/nvm.sh"' >> ~/.zshrc
source ~/.zshrc
nvm install 24
```

### 3. Instal·lar VS Code
```bash
brew install --cask visual-studio-code
```

### 4. Crear clau SSH i connectar a GitHub
```bash
ssh-keygen -t ed25519 -C "el-teu-email@gmail.com"
cat ~/.ssh/id_ed25519.pub | pbcopy
```

Anar a github.com/settings/ssh/new → enganxar → verificar:
```bash
ssh -T git@github.com
```

### 5. Clonar els repos
```bash
cd ~/Documents/citilab/Skills
git clone git@github.com:laias/skills-educacio.git
git clone git@github.com:laias/skills-creacio-av.git
git clone git@github.com:laias/skills-labs-ciutadans.git
```

### 6. Configurar identitat Git
```bash
git config --global user.name "Laia Sánchez"
git config --global user.email "laia.sanchez@gmail.com"
```

### 7. Instal·lar extensions VS Code
```bash
code --install-extension ms-python.python
code --install-extension esbenp.prettier-vscode
code --install-extension eamodio.gitlens
code --install-extension rangav.vscode-thunder-client
code --install-extension usernamehw.errorlens
```

### 8. Verificar commit i push
```bash
echo "test" > test.md
git add test.md
git commit -m "test: verificar connexió"
git push
git rm test.md
git commit -m "chore: eliminar test"
git push
```

## Notes de seguretat

Abans d'instal·lar qualsevol paquet, verificar incidents recents:
`[nom paquet] compromised OR hacked OR malware 2026`

## Resultat

Entorn operatiu complet: Homebrew + Git + nvm + Node v24 + VS Code
+ SSH GitHub + repos clonats + identitat Git configurada.