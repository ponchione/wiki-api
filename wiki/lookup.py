import wikipedia


def find_page(name):
    suggestion = suggest(name)
    search_term = suggestion if suggestion is not None else name
    results = page(search_term)
    return results.summary


def suggest(name):
    return wikipedia.suggest(name)


def page_results(term):
    return wikipedia.search(term)


def page(query):
    return wikipedia.page(query, auto_suggest=True)


if __name__ == '__main__':
    find_page("twiter")
