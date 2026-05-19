import zipfile
import xml.etree.ElementTree as ET
import sys
import os

def read_docx(path):
    try:
        document = zipfile.ZipFile(path)
        xml_content = document.read('word/document.xml')
        document.close()
        tree = ET.XML(xml_content)
        
        NAMESPACE = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
        TEXT = NAMESPACE + 't'
        P = NAMESPACE + 'p'
        
        paragraphs = []
        for p in tree.iter(P):
            texts = [node.text for node in p.iter(TEXT) if node.text]
            if texts:
                paragraphs.append(''.join(texts))
            
        return '\n'.join(paragraphs)
    except Exception as e:
        return f"Error reading {path}: {e}"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        text = read_docx(sys.argv[1])
        with open("docx_text.txt", "w", encoding="utf-8") as f:
            f.write(text)
