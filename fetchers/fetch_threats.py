import os
import json
import yaml
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
import time
import sys
import io

# Force UTF-8 for Windows compatibility
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

def load_competitors(filepath):
    with open(filepath, 'r') as f:
        data = yaml.safe_load(f)
    return data.get('competitors', [])

def fetch_threat_papers():
    yaml_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'competitors.yaml')
    competitors = load_competitors(yaml_path)
    
    threat_papers = []
    base_url = "http://export.arxiv.org/api/query"
    
    for comp in competitors:
        print(f"Fetching papers for competitor: {comp}")
        query = f'all:"{comp}"'
        url = f"{base_url}?search_query={urllib.parse.quote(query)}&sortBy=submittedDate&sortOrder=descending&max_results=5"
        
        try:
            response = urllib.request.urlopen(url)
            xml_data = response.read()
            root = ET.fromstring(xml_data)
            ns = {'atom': 'http://www.w3.org/2005/Atom'}
            
            for entry in root.findall('atom:entry', ns):
                title = entry.find('atom:title', ns).text.strip().replace('\n', ' ')
                summary_elem = entry.find('atom:summary', ns)
                summary = summary_elem.text.strip().replace('\n', ' ') if summary_elem is not None else ""
                link = entry.find('atom:id', ns).text
                
                threat_papers.append({
                    "title": title,
                    "abstract": summary,
                    "url": link,
                    "authors": [a.find('atom:name', ns).text for a in entry.findall('atom:author', ns)],
                    "source": "ArXiv",
                    "competitor": comp
                })
        except Exception as e:
            print(f"Error fetching for {comp}: {e}")
        
        time.sleep(1)
    
    # Write to contract
    contract_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'contracts', 'threat_papers.json')
    os.makedirs(os.path.dirname(contract_path), exist_ok=True)
    
    with open(contract_path, 'w', encoding='utf-8') as f:
        json.dump(threat_papers, f, indent=4)
    print(f"Saved {len(threat_papers)} verified threat papers to {contract_path}")

if __name__ == "__main__":
    fetch_threat_papers()
