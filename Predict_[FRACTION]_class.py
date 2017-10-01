minifractions = [u'¼', u'½', u'¾', u'⅔', u'⅓']

def is_fraction(token):
    if any(c.isalpha() for c in token):
        return False
    if token.count(u'/') > 1 or u'.' in token:
        return False
    if token[0] != u'-' and u'-' in token:
        return False
    for minifraction in minifractions:
        if minifraction in token:
            return True
    if u'/' in token and any(c.isdigit() for c in token):
        return True
    return False
