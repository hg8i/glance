#!/bin/env python3
import os

def loadTable():
    global thisPath
    nx = 5
    ny = 5
    table = ""
    table+= "<table>\n"
    for y in range(ny):
        table+="<tr>"
        for x in range(nx):
            p = f"{thisPath}/cells/c{x}x{y}.html"
            if os.path.exists(p):
                content = open(p,"r").read()
            else:
                content = f"""<div id="content" style="text-align: center;color:#888;"> {y}, {x}</div>"""
                # content = f"{y}, {x}"
            table+=f"<td>{content}</td>\n"
        table+="</tr>"
    table+= "</table>\n"
    return table

def generate(oPath,templatePath):
    template = open(templatePath,"r").read()
    table = loadTable()
    page = template.replace("TABLE",table)
    o = open(oPath,"w")
    print("Saved to",oPath)
    o.write(page)
    o.close()

if __name__=="__main__":
    thisPath = os.path.dirname(os.path.realpath(__file__))
    oPath = os.path.join(thisPath,"index.html")
    templatePath = os.path.join(thisPath,"template.html")
    generate(oPath,templatePath)
