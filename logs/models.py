from django.db import models

LOG_LEVEL_INFO = "i"
LOG_LEVEL_WARNING = "w"
LOG_LEVEL_ERROR = "e"

LOG_LEVELS = [
    (LOG_LEVEL_INFO, "Info"),
    (LOG_LEVEL_WARNING, "Warning"),
    (LOG_LEVEL_ERROR, "Error"),
]


class Log(models.Model):
    level = models.CharField(max_length=1, choices=LOG_LEVELS, default=LOG_LEVEL_INFO)
    message = models.TextField(max_length=256, blank=False, null=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def level_to_string(self):
        if self.level == LOG_LEVEL_INFO:
            return "Info"
        elif self.level == LOG_LEVEL_WARNING:
            return "Warning"
        elif self.level == LOG_LEVEL_ERROR:
            return "Error"
        else:
            return "Unknown"

    def to_json(self):
        return {
            "id": self.id,
            "level": self.level,
            "level_str": self.level_to_string(),
            "message": self.message,
            "timestamp": self.timestamp,
        }

    def __str__(self):
        return f"Log #{self.id}"
