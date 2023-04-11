import justpy as jp
import api
import documentation

jp.Route('/', documentation.Doc.serve)
jp.Route('/api', api.Api.serve)
jp.justpy()
