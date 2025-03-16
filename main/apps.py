from django.apps import AppConfig

import os
port = int(os.getenv("PORT", 5000))  
app.run(host="0.0.0.0", port=port)

class MainConfig(AppConfig):
    name = 'main'
    verbose_name = verbose_name_plural = r''
