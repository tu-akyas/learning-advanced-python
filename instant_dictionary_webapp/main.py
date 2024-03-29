import justpy as jp
import inspect
from webapp.about import About
from webapp.home import Home
from webapp.dictionary import Dictionary
from instant_dictionary_webapp.webapp import page

imports = list(globals().values())

for obj in imports:
    if inspect.isclass(obj):
        if hasattr(obj, 'path') and issubclass(obj, page.Page) and obj is not page.Page:
            jp.Route(obj.path, obj.serve)

# jp.Route(Home.path, Home.serve)
# jp.Route(About.path, About.serve)
# jp.Route(Dictionary.path, Dictionary.serve)

jp.justpy(port=8001)

