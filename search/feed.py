import feedparser
import html2text

_CACHED_FEED = dict()

def _feed(url):
    if url not in _CACHED_FEED:
        _CACHED_FEED[url] = feedparser.parse(url)
    return _CACHED_FEED[url]