import json
from urllib import request, parse

def link_to_title(link):
    return link["title"]

def clean_if_key(page,key):
    if key in page.keys():
        return map(link_to_title,page[key])
    else: return []

def get_wiki_links(pageTitle):
    safe_title = parse.quote(pageTitle)
    url = ("https://en.wikipedia.org/w/api.php?action=query"
           "&prop=links|linkshere&pllimit=500&lhlimit=500"
           "&titles={}&format=json&formatversion=2").format(safe_title)
    page = request.urlopen(url).read()
    j = json.loads(page)
    jpage = j["query"]["pages"][0]
    inbound = clean_if_key(jpage,"links")
    outbound = clean_if_key(jpage,"linkshere")

    return {"title": pageTitle,
            "in-links":list(inbound),
            "out-links":list(outbound)}

