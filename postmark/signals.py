from django.dispatch import Signal

try:
    post_send = Signal(providing_args=["message", "response"])
except:
    post_send = Signal()