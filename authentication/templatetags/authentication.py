from django import template

register = template.Library()

PROVIDER_ICONS = dict(Google='google plus', Facebook='facebook')


@register.filter
def get_provider_icon_name(provider):
    """
    Returns a list of social authentication providers.

    Usage: `{% get_providers as socialaccount_providers %}`.

    """
    return PROVIDER_ICONS[provider.name]
