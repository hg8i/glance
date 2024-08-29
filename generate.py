#!/bin/env python3
import os

def loadTable():
    nx = 5
    ny = 5
    table = ""
    table+= "<table>"
    for y in range(ny):
        table+="<tr>"
        for x in range(nx):
            p = f"cells/c{x}x{y}.html"
            if os.path.exists(p):
                content = open(p,"r").read()
            else:
                content = f"""<div id="content" style="text-align: center;color:#888;"> {y}, {x}</div>"""
                # content = f"{y}, {x}"
            table+=f"<td>{content}</td>"
        table+="</tr>"
    table+= "</table>"
    return table

def generate(oPath,templatePath):
    template = open(templatePath,"r").read()
    table = loadTable()
    page = template.replace("TABLE",table)
    o = open(oPath,"w")
    o.write(page)
    o.close()

if __name__=="__main__":
    oPath = "index.html"
    templatePath = "template.html"
    generate(oPath,templatePath)
