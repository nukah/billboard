# -*- coding: utf-8 -*-
import feedparser, time

testfeed = "http://www.glinka.museum/ezg_calendar/calendar.php?action=rss&target=_blank&linktype=1&urltitle=&"
def form_element(entry):
    element = {}
    element['title'] = entry.title
    element['date'] = time.strftime('%d/%m/%Y %H:%M', entry.updated_parsed)
    element['description'] = entry.summary
    element['link'] = entry.link
    return element

def attain_feed(url):
    result = []
    feed = feedparser.parse(url)
    for entry in feed.entries:
            element = form_element(entry)
            result.append(element)
    return result
