# dreamz — galeria de design conceitual

Leia `BRIEFING.md` (marca, paleta, portfólio, contato) antes de criar qualquer coisa. Quando o dono corrigir algo, atualize este arquivo e faça commit.

## Site
- Publicado em: https://claude.ai/artifact/FEP3y2ytdLKQCJHgE3oEir — código em `index.html` + `assets/`. Para editar, republique nesse mesmo link.
- **Vercel**: `index.html` está no formato artifact (sem doctype/head/body). Depois de qualquer mudança rode `python3 tools/build.py`,
  que gera `dist/` (página completa + assets) e faça commit do `dist/` junto. `vercel.json` publica a pasta `dist/` sem build.
- Conceito aprovado: **"perdendo o sono"**. O site é uma noite: relógio vai de **23:47 → 06:00** conforme a rolagem e o fundo vai do preto
  ao marinho, lavanda, azul-céu e creme do amanhecer. Seções: 23:47 entrada · 00:00 manifesto · 00:30 o vidro · 01:00 o que fazemos ·
  04:15 faixas · 05:00 a logo (o menino) · 05:15 no que a gente acredita · 05:30 FAQ · 06:00 orçamento.
- **Texto oficial** (enviado pelo dono): `TEXTO-OFICIAL.md`. Usar essas palavras no site; traduções EN feitas pelo Claude.
  Nome: **Dreamz Gallery**. Frase: "Arte para quem sonha acordado." Autor da logo/marca: **Enzo Maldonado (@maldonaenz)**.
- Idiomas: PT principal + EN (botão "acordado · PT / dreaming · EN"). Todo texto novo precisa das duas versões (`<span lang="pt">` / `<span lang="en">`).
- Fontes: o dono quer **fonte gorda** nos títulos → **Fraunces 900** (SOFT 100, opsz 144; itálico nas palavras de destaque) + **Manrope** no texto/rótulos.
  Reprovadas: Marcellus, Instrument Serif/Sans, IBM Plex Mono ("muito feias"), Cormorant Garamond (fina demais).
- Entrada: "por @maldonaenz" (link do Instagram, o dono pediu crédito ao autor) acima do título "Arte para quem sonha acordado."; embaixo,
  **as 3 estrelas exatas do logo** (recortadas do arquivo: `assets/marca/estrela-1/2/3.png`, brancas) cintilando sobre "role pra sonhar".
  O "z z z" foi tirado. Estrelas desenhadas à mão foram recusadas: "tem que ser as estrelas que tem no logo".
- **00:30 O vidro**: texto "Você já se sentiu preso…" + "Esse vidro tem nome:" e a palavra **"medo."** gigante, **cheia, na tipografia dos títulos**
  (Fraunces 900 itálico, cor de destaque, brilho passando e um tremidinho de vez em quando). Tocar trinca e estilhaça a palavra a partir do ponto do toque
  (cacos caem, som de vidro + tilintar) e no lugar aparecem as **3 estrelas do logo** brilhando; o resto do texto acende.
  Reprovados: placa de vidro cinza com trincas por cima de "medo." desfocado ("horrível"); letras de vidro só com contorno ("muito feia").
- **01:00 O que fazemos**: lista dos 6 serviços oficiais (criação de marca, identidade visual, sites, redes sociais, mídia off, estampas/roupas) +
  blocos i Identidade visual · ii Redes sociais · **iii Sites** (pedido do dono: navegador mostrando este próprio site rolando, `assets/tecnicas/site-dreamz.webp`;
  se o site mudar muito, refazer esse print).
- **05:00 A logo conta nossa história**: só o menino (O Pequeno Príncipe reinterpretado) + crédito @maldonaenz.
  A parte "As três estrelas" (corpo, mente e alma, com as estrelas grandes e 3 colunas) foi feita e **removida** a pedido do dono.
- **05:15 No que a gente acredita**: missão, visão e os 6 valores oficiais.
- Topo: **só o símbolo do menino** (sem a palavra DREAMZ) + relógio LCD + botão de idioma.
- Abertura: pálpebras abrindo **devagar** (~6 s), com piscadas e a visão **embaçada** clareando, como alguém acordando de verdade.
- Relógio = **mini visor LCD** (7 segmentos, contorno fino em cápsula, "AL") **ao lado do logo DREAMZ no topo**; a hora anda com a rolagem
  e pisca às 06:00. Reprovados: despertador analógico de sinos, despertador Y2K grande no canto (verde-limão e depois verde escuro: "feio").
- Céu: via láctea, estrelas de vários tamanhos piscando, **sem lua** (o dono pediu para tirar; as luas desenhadas e a foto foram reprovadas), **estrelas cadentes e cometas**.
  Amanhecer (refeito, o 1º com sol de raios desenhados foi reprovado): céu pêssego/rosa, sol com brilho difuso, fiapos de nuvem, **mar de nuvens** embaixo e **passarinhos**.
- **01:00 Técnicas (refeita)**: título "O que a gente faz enquanto você dorme." (o 1º, "Duas coisas, bem feitas.", foi reprovado) + blocos alternados com trabalho real:
  i. Identidade visual = pilha de 4 pranchas da Bross Motors (`assets/tecnicas/`) que se abre em grade;
  ii. Redes sociais = celular com feed rolando sozinho com posts reais dos 9 clientes de social; iii. Sites (acima). Reprovado: placas com borda e pílulas ("ruim").
- Chat do orçamento: opções = criação de marca, identidade visual, site, redes sociais, mídia off, estampas/roupas, outra coisa.
- **Acervo no site**: só 04:15 **sonhos em looping** (faixas infinitas de nomes vazados e fotos; abre o visor com as peças).
  **Partidas para o sonho (aeroporto) foi removida inteira** ("tá feio, tira"): painel split-flap, cartão de embarque, mala, aviõezinhos e pista.
  Antes disso passou por: painel gigante com colunas (feio no celular), cena compacta com painel em páginas + cartão de papel + mala no chão,
  bolinhas e aviõezinhos de status (reprovados). O código está no histórico do git (commit d7b33b2) se um dia voltar.
  Saíram do site também: **tarô dos sonhos** ("pode tirar"), índice gigante "13 sonhos" ("ruim"), TV da madrugada, diário de sonhos. Reprovados: grade de cards, túnel de sonhos.
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
- Antes × depois (celular com linha arrastável) foi feito e **removido** ("muito feio").
- **05:30 Perguntas de insônia** (FAQ em abre-e-fecha, horários 05:31…05:52). Respostas escritas pelo Claude sem prometer preço/prazo/número de ajustes —
  **o dono precisa conferir** (principalmente "atendem fora da cidade?" e "o que recebo no final?").
- **06:00 Orçamento (refeito)**: "Acordou? Me conta." + **conversa de bom dia** estilo chat (dreamz "digitando…"): pergunta marca → nome →
  o que precisa (chips) → prazo (chips) → o sonho em 1 frase (pode pular) → botão "Enviar pelo WhatsApp" com a mensagem montada. E-mail/Instagram/WhatsApp ao lado.
  Reprovado: formulário com campos e prévia da mensagem ("não curti").
- **Sons da madrugada, sem botão** (pedido do dono): chuva fina + grilos à noite, passarinhos no amanhecer, gerados com Web Audio; começam no 1º clique/toque/tecla
  (o navegador não deixa tocar antes) e pausam quando a aba sai de foco.
- **Easter egg**: 3 cliques rápidos no menino (logo da entrada, símbolo do topo ou da seção da logo) → ele pula, toca um "plim" e as estrelas saem voando (o aviso "ele acordou!" foi removido a pedido do dono).
- **Bocejo**: 20 s sem mexer → tela escurece, pálpebras pesam e piscam devagar, "z z z" e "mexa pra acordar"; qualquer movimento desfaz.
- Faróis passando no teto: feitos e **removidos** ("não curti").
- Chuva no vidro: feita 2 vezes (canvas e gotas com refração) e **removida** ("gotinhas muito feias"); ficou só o som da chuva.
- **Relâmpago distante**: a cada 25–60 s (só à noite) um clarão duplo no céu + trovão grave baixinho se o som estiver ligado.
- **Modo sonho lúcido** (easter egg): tecla **L** ou **5 toques no relógio LCD** → 9 s de cores girando, véu furta-cor, página ondulando e um som subindo.
- Adesivos soltos arrastáveis: feitos e **removidos** a pedido do dono.
- **Cursor = nuvenzinha** (escolhida no mostruário https://claude.ai/artifact/8GC9PGW52ACU9YXTLtibX1, `cursores.html`): nuvem fofa que segue o mouse com atraso,
  flutua, cresce em cima de coisas clicáveis e aperta no clique; cor acompanha a hora (creme à noite, marinho no amanhecer) + pontinho exato. Só com mouse.
  Substituiu o cursor de estrela com rastro.
- Detalhes: contador "há mm:ss perdendo o sono com a gente" (canto, desktop) e no rodapé.
- WhatsApp: **+55 17 99108-9367** (constante `WHATSAPP = "5517991089367"` no script).
- Imagens do acervo: `assets/obras/<projeto>/NN.webp` (01 = capa, 02 = aparece no hover). Originais no Drive "PROJETOS DREAMZ 2026".
- Ideias guardadas: mesa de luz com peças arrastáveis.
