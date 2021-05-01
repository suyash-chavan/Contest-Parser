
import re
# contestPage = """
# <div>
#           <aside class="breadcrumbs">
#             <a href="/">Home</a>&nbsp;»&nbsp;<a href="/contests/">Compete</a>&nbsp;»&nbsp;Spider AlgoCup
#           </aside>
#         </div>
# """
# contest_name = re.findall(r"\/contests\/\"\>Compete\<\/a.*\<\/aside\>", contestPage, re.DOTALL)[0]
# print(contest_name)

a = """<code class=" mathjax-support">2
1
5
5
2 0 0 5 0
</code>"""

a = a.split(">")[1].split("<")[0]
print(a)