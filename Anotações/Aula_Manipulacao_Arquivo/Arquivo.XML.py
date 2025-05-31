import xml.etree.ElementTree as ET#Cria uma árvore de XML
from os import times_result

#Cria a raiz do XML
root = ET.Element("root")

#Cria o elemento filho de root
filho = ET.SubElement(root, "filho")

#Seta os atributos do filho
filho.set("attribute","value")
filho.text ="Esse é o meu primeiro texto em XML"

segundo_filho = ET.SubElement(root,"segundo_filho")
segundo_filho.text =" Diretos de Letícia Alves Roth"

#Cria um elemento dentro do outro
neto_do_root = ET.SubElement(segundo_filho,"neto_do_root")
neto_do_root.text = "2025"

arvore_xml = ET.ElementTree(root)
arvore_xml.write("outout.xml", encoding="utf-8")

print("XML escrito com sucesso total!")