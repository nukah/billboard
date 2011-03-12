# -*- coding: utf-8 -*-
import feedparser

testfeed = "http://www.glinka.museum/ezg_calendar/calendar.php?action=rss&target=_blank&linktype=1&urltitle=&"
mapping = {
            "title" : "title",
            "place" : "Gnesinka",
            "description" : "description",
            "filter" : u"Концерт"
}
place = mapping['place']
filter = mapping['filter'] if mapping['filter'] else None
feed = feedparser.parse(testfeed)

for entry in feed.entries:
    if filter and filter in entry.title:
        print "%s %s @ %s" % (entry.title, entry.updated, place)
        if entry.title_detail:
            print entry.title_detail
