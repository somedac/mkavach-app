#!/usr/bin/env python3
"""Regenerate assets/qr.svg for the page URL.  Usage: python3 make-qr.py https://example.com/
Needs: pip install segno"""
import sys, segno
url = sys.argv[1]
segno.make(url, error="q").save("assets/qr.svg", scale=10, border=2, dark="#000", light="#fff")
print("wrote assets/qr.svg for", url)
