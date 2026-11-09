#!/usr/bin/env python3
"""Gera dist/ (site estático completo) a partir de index.html (formato artifact) + assets/.
Uso: python3 tools/build.py   → depois a Vercel publica a pasta dist/ (ver vercel.json)."""
import os, shutil
raiz = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src = open(os.path.join(raiz, "index.html"), encoding="utf-8").read()
corte = src.index("</style>") + len("</style>")
cabeca, corpo = src[:corte], src[corte:]
html = ('<!doctype html>\n<html lang="pt-BR">\n<head>\n' + cabeca +
        '\n<meta property="og:title" content="dreamz — galeria de design conceitual">'
        '\n<meta property="og:description" content="Identidade visual e social media. Toda marca começa como o sonho de alguém.">'
        '\n<link rel="icon" href="assets/marca/simbolo.png">'
        '\n</head>\n<body>\n' + corpo + '\n</body>\n</html>\n')
dist = os.path.join(raiz, "dist")
shutil.rmtree(dist, ignore_errors=True)
shutil.copytree(os.path.join(raiz, "assets"), os.path.join(dist, "assets"))
open(os.path.join(dist, "index.html"), "w", encoding="utf-8").write(html)
print("dist/ pronto:", sum(len(f) for _, _, f in os.walk(dist)), "arquivos")
