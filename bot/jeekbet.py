

def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    if lowered == 'ajuda':
        return '!ranking               - Ver o ranking de todos que tem jeekpoints\n!pegar-pontos   - 10 pontos diários para apostar\n!apostar              - Aposta em uma aposta aberta\n!premios             - Lista completa de prêmios em jeekpoints'

    elif 'ola' in lowered:
        return 'Salve salve'
