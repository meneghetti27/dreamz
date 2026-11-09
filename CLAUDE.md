# dreamz — galeria de design conceitual

Leia `BRIEFING.md` (marca, paleta, portfólio, contato) antes de criar qualquer coisa. Quando o dono corrigir algo, atualize este arquivo e faça commit.

## Site
- Publicado em: https://claude.ai/artifact/FEP3y2ytdLKQCJHgE3oEir — código em `index.html` + `assets/`. Para editar, republique nesse mesmo link.
- Conceito aprovado: **"perdendo o sono"**. O site é uma noite: relógio vai de **23:47 → 06:00** conforme a rolagem e o fundo vai do preto
  ao marinho, lavanda, azul-céu e creme do amanhecer. Seções: 23:47 entrada (pálpebras abrindo, logo com brilho nas estrelas) ·
  00:00 manifesto ("Lo$ing $leep…") · 01:00 técnicas · 02:00 acervo (13 "sonhos" com etiqueta de museu e visor) · 05:00 quem sonha ·
  06:00 "Conte seu sonho." (orçamento → WhatsApp).
- Idiomas: PT principal + EN (botão "acordado · PT / dreaming · EN"). Todo texto novo precisa das duas versões (`<span lang="pt">` / `<span lang="en">`).
- Fontes: o dono quer **fonte gorda** nos títulos → **Fraunces 900** (SOFT 100, opsz 144; itálico nas palavras de destaque) + **Manrope** no texto/rótulos.
  Reprovadas: Marcellus, Instrument Serif/Sans, IBM Plex Mono ("muito feias"), Cormorant Garamond (fina demais).
- Abertura: pálpebras abrindo **devagar** (~6 s), com piscadas e a visão **embaçada** clareando, como alguém acordando de verdade.
- Relógio = **mini visor LCD** (7 segmentos, contorno fino em cápsula, "AL") **ao lado do logo DREAMZ no topo**; a hora anda com a rolagem
  e pisca às 06:00. Reprovados: despertador analógico de sinos, despertador Y2K grande no canto (verde-limão e depois verde escuro: "feio").
- Céu: via láctea, estrelas de vários tamanhos piscando, **sem lua** (o dono pediu para tirar; as luas desenhadas e a foto foram reprovadas), **estrelas cadentes e cometas**.
  Amanhecer (refeito, o 1º com sol de raios desenhados foi reprovado): céu pêssego/rosa, sol com brilho difuso, fiapos de nuvem, **mar de nuvens** embaixo e **passarinhos**.
- **Acervo no site (aprovado)**: 4 atos seguidos, todos em PT/EN, todos abrem o visor com as peças:
  02:00 **índice gigante** (13 nomes em Fraunces 900, peça flutua no cursor; miniatura no celular) ·
  02:45 **partidas para o sonho** (painel split-flap de aeroporto + cartão de embarque; status muda com o idioma) ·
  03:30 **tarô dos sonhos** (13 cartas, virar revela, embaralhar) · 04:15 **sonhos em looping** (faixas infinitas de nomes vazados e fotos).
  Saíram do site: TV da madrugada e diário de sonhos. Reprovados: grade de cards ("horrível"), túnel de sonhos.
- **Laboratório do acervo**: https://claude.ai/artifact/FxTWhcN8vGXG2nhasKxgr8 (`acervo-lab.html`, só PT, para comparar): 6 versões em abas —
  1 sonho que desembaça (tela cheia, blur↔foco na rolagem) · 2 cartela de remédio dreamz® + bula · 3 lambe-lambe na parede com flash ·
  4 quarto escuro (varal, fotos revelam no hover) · 5 bolhas de sabão iridescentes que estouram · 6 máquina de cápsulas (gashapon).
  Rodada 1 (versões 1–6) foi reprovada ("não gostei"); está no histórico do git (commit fee21bf).
  Rodada 2 (sem resposta clara, dono pediu "outras 10"; git 80e64f8): 7 índice gigante de nomes com a peça flutuando no cursor · 8 nuvens de pensamento saindo do menino da logo dormindo ·
  9 painel de aeroporto split-flap "Partidas para o sonho" + cartão de embarque · 10 elevador pro céu (13 andares, portas abrem) ·
  11 dreamz zine nº 01 (revista que folheia) · 12 drops em fundo de estúdio, estilo marca de roupa (destaques redondos + carrossel).
  Rodada 3 (git d12cf3b): 13 constelações · 14 persiana que abre · 15 roda-gigante · 16 dreamz OS (desktop Y2K com pastas e janelas) ·
  17 tela de bloqueio às 3h12 com notificações · 18 vidro embaçado que se limpa com o dedo · 19 iPod com click wheel · 20 tarô dos sonhos ·
  21 faixas infinitas (nomes vazados + fotos correndo) · 22 fotos espalhadas no lençol para arrastar.
  **Rodada 4 (no ar)** — o dono mandou manter 7 índice gigante, 9 partidas, 20 tarô e 21 faixas, e fazer 5 novas:
  23 do rabisco ao sonho (esboço a lápis via filtro SVG → final, linha arrastável) · 25 rua de letreiros neon com vitrines ·
  26 filmadora VHS (REC, data, tracking, fitas com etiqueta) · 27 luneta que procura os sonhos como planetas · 28 cabine de fotos 3x4 que solta tirinhas.
  Ideias só propostas (não feitas): 24 álbum de figurinhas, 29 mapa do metrô, 30 globo de neve, 31 projetor de estrelas no teto, 32 stories.
  O dono escolheu 7, 9, 20 e 21 → foram para o site (acima).
- WhatsApp: **+55 17 99108-9367** (constante `WHATSAPP = "5517991089367"` no script).
- Imagens do acervo: `assets/obras/<projeto>/NN.webp` (01 = capa, 02 = aparece no hover). Originais no Drive "PROJETOS DREAMZ 2026".
- Ideias guardadas para a v2: cursor de estrela, contador "noites sem dormir", mesa de luz com peças arrastáveis.
