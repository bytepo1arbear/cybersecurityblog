#!/usr/bin/env python3
"""Fetch threat feeds listed in _data/threat_sources.yml and write combined summary to _data/threats.yml
This script is intended to run in CI (GitHub Actions) daily.
"""
import os
import time
import yaml
import feedparser
from html import unescape


ROOT = os.path.dirname(os.path.dirname(__file__))
DATA_DIR = os.path.join(ROOT, "_data")
SOURCES_FILE = os.path.join(DATA_DIR, "threat_sources.yml")
OUT_FILE = os.path.join(DATA_DIR, "threats.yml")


def safe_text(text):
    if not text:
        return ""
    return unescape(' '.join(text.split()))


def parse_feed(source):
    url = source.get("url")
    name = source.get("name") or url
    if not url:
        return []
    print(f"Fetching: {name} -> {url}")
    feed = feedparser.parse(url)
    items = []
    for entry in feed.entries:
        published = None
        if getattr(entry, 'published', None):
            published = entry.published
        elif getattr(entry, 'updated', None):
            published = entry.updated
        elif getattr(entry, 'created', None):
            published = entry.created

        summary = safe_text(getattr(entry, 'summary', '') or getattr(entry, 'description', '') or '')

        items.append({
            'title': safe_text(getattr(entry, 'title', '')),
            'link': getattr(entry, 'link', ''),
            'published': published,
            'summary': summary,
            'source': name,
        })
    return items


def main():
    if not os.path.exists(SOURCES_FILE):
        print('No threat_sources.yml found; aborting.')
        return

    with open(SOURCES_FILE, 'r', encoding='utf-8') as fh:
        sources = yaml.safe_load(fh) or []

    all_items = []
    for source in sources:
        try:
            items = parse_feed(source)
            for it in items:
                all_items.append(it)
        except Exception as e:
            print(f"Error fetching {source.get('name')}: {e}")

    # sort by published if available, fallback to insertion order
    def key_fn(it):
        return it.get('published') or ''

    all_items_sorted = sorted(all_items, key=key_fn, reverse=True)
    # limit to most recent 100
    top_items = all_items_sorted[:100]

    out = {
        'last_updated': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
        'count': len(top_items),
        'items': top_items,
    }

    os.makedirs(DATA_DIR, exist_ok=True)
    with open(OUT_FILE, 'w', encoding='utf-8') as fh:
        yaml.safe_dump(out, fh, sort_keys=False, allow_unicode=True)

    print(f'Wrote {OUT_FILE} with {len(top_items)} items')


if __name__ == '__main__':
    main()
