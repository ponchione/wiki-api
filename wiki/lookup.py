import wikipedia


def find_page(name):
    search_term = suggest(name) if suggest(name) is not None else name
    results = page(search_term)
    # print(results.summary)
    return results.summary


def suggest(name):
    return wikipedia.suggest(name)


def page_results(term):
    return wikipedia.search(term)


def page(query):
    return wikipedia.page(query, auto_suggest=True)


if __name__ == '__main__':
    find_page("twiter")
