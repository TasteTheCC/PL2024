import re
import sys


def cabecalhos(markdown):
    #cabeçalhos
    markdown = re.sub(r'^#\s(.*)', r'<h1>\1</h1>', markdown, flags=re.MULTILINE)
    return markdown


def negrito(markdown):
    markdown = re.sub(r'\*\*(.+)\*\*', r'<b>{\1}</b>', markdown)
    return markdown

def italico(markdown):
    markdown = re.sub(r'\*(.+)\*', r'<i>{\1}</i>', markdown)
    return markdown

def listanumerada(markdown):
    markdown = re.sub(r'^(\d+\.\s.+)$',r'<ol>\n<li>{\1}</li>\n</ol>', markdown)
    return markdown

def link(markdown):
    markdown = re.sub(r'\[(.+)\]\((.+)\)',r'<a href="{\2}">{\1}</a>', markdown)
    return markdown

def imagem(markdown):
    markdown = re.sub(r'!\[(.+)\]\((.+)\)',r'<img src="{\2}" alt="{\1}"/>', markdown)
    return markdown