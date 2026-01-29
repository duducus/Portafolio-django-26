from django.shortcuts import render, HttpResponse

html_base = """
<h1> Mi web personal </h1>
<ul>
	<li><a href="/">Portada</a></li>
	<li><a href="/about-me/">Acerca de</a></li>
</ul>

"""

# Create your views here.
def home(request):
	return HttpResponse( html_base + """
		<h2>Portada</h2>
		<p>Esto es la portada</p>
	""")

def about(request):
	return HttpResponse("""
		<h2>Acerca de mi</h2>
		<p>Me llamo Cerón y soy el mejor en lo que hago</p>

		""")