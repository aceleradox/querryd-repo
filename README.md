# 🔥 Querryd — Social SEO Finder

**Querryd** é uma ferramenta em Python para buscar perfis, posts e conteúdos em redes sociais usando técnicas de SEO (via DuckDuckGo).

Ideal para quem quer **analisar concorrência, encontrar perfis e otimizar conteúdo**.

---

## 🚀 Funcionalidades

* 🔎 Busca em qualquer plataforma (Instagram, TikTok, YouTube, etc.)
* 🧠 Múltiplas descrições inteligentes:

  * `//` → variações no mesmo grupo
  * `**` → separa grupos diferentes
* 🏷️ Hashtags **opcionais**
* 👤 Uso de BIO para refinar busca
* 📍 Filtro por cidade/bairro
* ⏱️ Modo:

  * `recente`
  * `relevante`
* 💾 Exportação para JSON
* 🎨 Interface de console com cores

---

## 💻 Exemplo de uso

```bash id="exq1"
Plataforma/site: instagram
Hashtags: funk, rave
Descrição SEO: baile pesado // som automotivo ** dj set // rave noturna
BIO: produtor musical independente
Cidade/Bairro: sao paulo
Modo: recente
Resultados por hashtag: 5
Gerar JSON? sim
```

---

## 🧠 Como funciona

O Querryd gera queries otimizadas como:

```bash id="exq2"
instagram #funk baile pesado produtor musical sao paulo site:instagram.com
```

E busca resultados usando a biblioteca `ddgs`.

---

## 📦 Estrutura das descrições

### ➤ Múltiplas variações:

```bash id="exq3"
descricao1 // descricao2
```

### ➤ Grupos separados:

```bash id="exq4"
grupo1 ** grupo2
```

---

## 📁 Saída JSON

```json id="exq5"
[
  {
    "plataforma": "instagram",
    "hashtag": "funk",
    "grupo": 1,
    "resultado": {
      "title": "...",
      "url": "...",
      "desc": "...",
      "query": "..."
    }
  }
]
```

---

## ⚙️ Instalação

```bash id="exq6"
git clone https://github.com/aceleradox/querryd-repo.git
cd querryd
pip install ddgs colorama
```

---

## ▶️ Executar

```bash id="exq7"
python main.py
```

---

## ⚠️ Observações

* Não utiliza API oficial das redes sociais
* Depende da indexação do DuckDuckGo
* Resultados podem variar conforme SEO
* Algumas plataformas têm limitação de indexação

---

## 🧩 Roadmap

* 📊 Score SEO automático
* 🧹 Remoção de duplicados
* 🤖 Sugestão automática de hashtags
* 🌐 API / painel web
* 📈 Ranking de resultados

---

## 📄 Licença

MIT License

---

## ✨ Sobre

Querryd foi criado como uma ferramenta de exploração SEO para redes sociais, focada em descoberta de conteúdo e análise de nicho.
