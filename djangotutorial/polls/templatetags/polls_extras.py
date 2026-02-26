from django import template

register = template.Library()


@register.filter
def vote_percent(votes, total):
    """Return the vote percentage as an integer (0-100)."""
    try:
        if total == 0:
            return 0
        return int((votes / total) * 100)
    except (ValueError, ZeroDivisionError, TypeError):
        return 0
