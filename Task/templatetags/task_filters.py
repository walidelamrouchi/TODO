from django import template
from django.utils.safestring import mark_safe

register = template.Library()

# ===== DATA DICTIONARIES =====
PRIORITY_DATA = {
    1: {
        'label': 'Priority 1',
        'color': '#d1453b',
        'icon': '<svg width="14" height="14" viewBox="0 0 24 24" fill="#d1453b" stroke="none"><path d="M4 15s1-1 4-1 5 2 8 2 4-1 4-1V3s-1 1-4 1-5-2-8-2-4 1-4 1z"/><line x1="4" y1="22" x2="4" y2="15" stroke="#d1453b" stroke-width="2"/></svg>'
    },
    2: {
        'label': 'Priority 2',
        'color': '#eb8909',
        'icon': '<svg width="14" height="14" viewBox="0 0 24 24" fill="#eb8909" stroke="none"><path d="M4 15s1-1 4-1 5 2 8 2 4-1 4-1V3s-1 1-4 1-5-2-8-2-4 1-4 1z"/><line x1="4" y1="22" x2="4" y2="15" stroke="#eb8909" stroke-width="2"/></svg>'
    },
    3: {
        'label': 'Priority 3',
        'color': '#246fe0',
        'icon': '<svg width="14" height="14" viewBox="0 0 24 24" fill="#246fe0" stroke="none"><path d="M4 15s1-1 4-1 5 2 8 2 4-1 4-1V3s-1 1-4 1-5-2-8-2-4 1-4 1z"/><line x1="4" y1="22" x2="4" y2="15" stroke="#246fe0" stroke-width="2"/></svg>'
    },
    4: {
        'label': 'Priority 4',
        'color': '#666',
        'icon': '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#666" stroke-width="2"><path d="M4 15s1-1 4-1 5 2 8 2 4-1 4-1V3s-1 1-4 1-5-2-8-2-4 1-4 1z"/><line x1="4" y1="22" x2="4" y2="15"/></svg>'
    },
}

CATEGORY_DATA = {
    1: {
        'label': 'Work',
        'color': '#555',
        'icon': '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#555" stroke-width="2"><rect x="2" y="7" width="20" height="14" rx="2"/><path d="M16 7V5a2 2 0 00-2-2h-4a2 2 0 00-2 2v2"/></svg>'
    },
    2: {
        'label': 'Personal',
        'color': '#555',
        'icon': '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#555" stroke-width="2"><path d="M20 21v-2a4 4 0 00-4-4H8a4 4 0 00-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>'
    },
    3: {
        'label': 'Home Improvement',
        'color': '#555',
        'icon': '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#555" stroke-width="2"><path d="M3 9l9-7 9 7v11a2 2 0 01-2 2H5a2 2 0 01-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg>'
    },
}

# ===== FILTERS =====
@register.filter
def priority_icon(value):
    data = PRIORITY_DATA.get(value, {})
    return mark_safe(data.get('icon', ''))

@register.filter
def priority_label(value):
    data = PRIORITY_DATA.get(value, {})
    return data.get('label', '')

@register.filter
def priority_color(value):
    data = PRIORITY_DATA.get(value, {})
    return data.get('color', '#666')

@register.filter
def category_icon(value):
    data = CATEGORY_DATA.get(value, {})
    return mark_safe(data.get('icon', ''))

@register.filter
def category_label(value):
    data = CATEGORY_DATA.get(value, {})
    return data.get('label', '')