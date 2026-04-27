from ddgs import DDGS
from colorama import Fore, init
import json

init(autoreset=True)


def formatar_descricoes(descricao_input):
    grupos = [grupo.strip() for grupo in descricao_input.split("**") if grupo.strip()]
    resultado = []

    for grupo in grupos:
        descricoes = [d.strip() for d in grupo.split("//") if d.strip()]
        resultado.append(descricoes)

    return resultado


def gerar_site(plataforma):
    if not plataforma:
        return ""

    plataforma = plataforma.lower().strip()

    if "site:" in plataforma:
        return plataforma

    if "." in plataforma:
        return f"site:{plataforma}"

    return f"site:{plataforma}.com"


def montar_query(hashtag, desc, local, modo, tipo, bio, plataforma):
    base = plataforma if plataforma else ""

    # 🔥 HASHTAG OPCIONAL
    partes = [base]

    if hashtag:
        partes.append(f"#{hashtag}")

    partes.append(desc)

    query = " ".join(filter(None, partes))

    if bio:
        query += f" {bio}"

    if local:
        query += f" {local}"

    if modo == "recente":
        query += " new recent 2026"

    site = gerar_site(plataforma)
    if site:
        query += f" {site}"

    return query


def buscar(hashtag, descricoes, local="", limit=5, modo="relevante", tipo="perfil", bio="", plataforma=""):
    resultados = []

    with DDGS() as ddgs:
        for desc in descricoes:
            query = montar_query(hashtag, desc, local, modo, tipo, bio, plataforma)

            for r in ddgs.text(query, max_results=40):
                href = r.get("href", "").lower()

                # filtro básico por plataforma
                if plataforma:
                    dominio = plataforma.replace("site:", "").replace("www.", "").lower()
                    if dominio not in href:
                        continue

                resultados.append({
                    "title": r.get("title", "Sem título"),
                    "url": href,
                    "desc": r.get("body", "Sem descrição."),
                    "query": query
                })

                if len(resultados) >= limit:
                    return resultados

    return resultados


def print_header():
    print(Fore.CYAN + "=" * 60)
    print(Fore.MAGENTA + "🔥 BUSCADOR SOCIAL FLEX 🔥".center(60))
    print(Fore.CYAN + "=" * 60)


def print_result(i, r):
    print(Fore.YELLOW + f"\n[{i}] {r['title']}")
    print(Fore.GREEN + f"🔗 URL: {r['url']}")
    print(Fore.BLUE + f"🔎 Query: {r['query']}")
    print(Fore.WHITE + f"📝 SEO: {r['desc']}")
    print(Fore.CYAN + "-" * 60)


def main():
    print_header()

    plataforma = input(Fore.CYAN + "Plataforma/site (ex: instagram, tiktok, youtube.com): ").strip()

    # 🔥 HASHTAG OPCIONAL
    hashtags_input = input(Fore.CYAN + "Hashtags (opcional, sem #): ").strip()
    if hashtags_input:
        hashtags = [h.strip() for h in hashtags_input.split(",") if h.strip()]
    else:
        hashtags = [""]  # mantém o loop funcionando

    descricao_input = input(Fore.CYAN + "Descrição SEO (// e **): ")
    grupos_descricoes = formatar_descricoes(descricao_input)

    bio = input(Fore.CYAN + "BIO (opcional): ").strip()
    cidade = input(Fore.CYAN + "Cidade/Bairro: ").strip()

    modo = input(Fore.CYAN + "Modo (recente/relevante): ").strip().lower()
    if modo not in ["recente", "relevante"]:
        modo = "relevante"

    try:
        limit = int(input(Fore.CYAN + "Resultados por hashtag: "))
    except:
        limit = 5
        print(Fore.RED + "⚠️ Valor inválido, usando padrão: 5")

    salvar_json = input(Fore.CYAN + "Gerar JSON? (sim/nao): ").strip().lower() == "sim"

    total_infos = sum(len(grupo) for grupo in grupos_descricoes)
    json_data = []

    for hashtag in hashtags:
        label = f"#{hashtag}" if hashtag else "(sem hashtag)"
        print(Fore.MAGENTA + f"\n🚀 Buscando para {label}...\n")

        for idx, grupo in enumerate(grupos_descricoes, start=1):
            print(Fore.YELLOW + f"\n📂 Grupo {idx}:")
            print(Fore.WHITE + " | ".join(grupo))

            resultados = buscar(
                hashtag,
                grupo,
                cidade,
                limit,
                modo,
                bio=bio,
                plataforma=plataforma
            )

            print(Fore.CYAN + f"\n📊 Informações geradas: {len(grupo)}")

            if resultados:
                print(Fore.GREEN + f"✅ Resultados encontrados: {len(resultados)}\n")

                for i, r in enumerate(resultados, start=1):
                    print_result(i, r)

                    if salvar_json:
                        json_data.append({
                            "plataforma": plataforma,
                            "hashtag": hashtag if hashtag else None,
                            "grupo": idx,
                            "resultado": r
                        })
            else:
                print(Fore.RED + "⚠️ Nenhum resultado encontrado.")

    print(Fore.CYAN + f"\n📦 TOTAL DE INFORMAÇÕES GERADAS: {total_infos}")

    if salvar_json:
        with open("resultados_social.json", "w", encoding="utf-8") as f:
            json.dump(json_data, f, indent=4, ensure_ascii=False)

        print(Fore.GREEN + "\n💾 JSON salvo como: resultados_social.json")


if __name__ == "__main__":
    main()