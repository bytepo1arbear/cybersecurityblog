#!/usr/bin/env python3
"""Fetch threat feeds and write a clean threat intelligence summary to _data/threats.yml."""
import os
import re
import time
from email.utils import parsedate_to_datetime
from html import unescape

import feedparser
import yaml

ROOT = os.path.dirname(os.path.dirname(__file__))
DATA_DIR = os.path.join(ROOT, "_data")
SOURCES_FILE = os.path.join(DATA_DIR, "threat_sources.yml")
OUT_FILE = os.path.join(DATA_DIR, "threats.yml")


def safe_text(text):
    if text is None:
        return ""
    return unescape(' '.join(str(text).split())).strip()


def normalize_published(raw_value):
    if not raw_value:
        return ""
    if isinstance(raw_value, str):
        text = raw_value.strip()
        if not text:
            return ""
        try:
            dt = parsedate_to_datetime(text)
            return dt.strftime('%Y-%m-%dT%H:%M:%SZ')
        except (TypeError, ValueError, IndexError):
            return text
    try:
        return raw_value.strftime('%Y-%m-%dT%H:%M:%SZ')
    except Exception:
        return str(raw_value)


def clean_item(entry):
    title = safe_text(entry.get('title'))
    link = safe_text(entry.get('link'))
    source = safe_text(entry.get('source'))
    summary = safe_text(entry.get('summary'))
    published = normalize_published(entry.get('published'))

    if not title or not link or not source:
        return None

    if not summary:
        summary = "Threat intelligence update from this source."

    return {
        'title': title,
        'link': link,
        'published': published,
        'summary': summary,
        'source': source,
    }


def dedupe_items(items):
    seen = set()
    unique = []
    for item in items:
        key = (item.get('title', '').lower().strip(), item.get('link', '').strip())
        if not key[0] or not key[1]:
            continue
        if key in seen:
            continue
        seen.add(key)
        unique.append(item)
    return unique


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

        summary = getattr(entry, 'summary', '') or getattr(entry, 'description', '') or ''
        item = clean_item({
            'title': getattr(entry, 'title', ''),
            'link': getattr(entry, 'link', ''),
            'published': published,
            'summary': summary,
            'source': name,
        })
        if item is not None:
            items.append(item)
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

    deduped = dedupe_items(all_items)

    def key_fn(it):
        return it.get('published') or ''

    all_items_sorted = sorted(deduped, key=key_fn, reverse=True)
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
