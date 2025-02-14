# projekt_lab
Projekti i lendes LAB i integruar
Blockchain Project
Ky është një projekt për krijimin e një blockchain të thjeshtë duke përdorur Python. Ky projekt ka për qëllim të ndihmojë përdoruesit të kuptojnë konceptet bazë të teknologjisë Blockchain, si dhe të implementojnë një shembull të thjeshtë të tij.

Përmbajtja e Projektit
Ky projekt përmban:

Blockchain: Një zinxhir blloqesh që ruan të dhënat e transaksioneve.
Proof of Work: Një mekanizëm konsensusi për minimin e blloqeve.
Validimi i Zinxhirit: Kontrolli i integritetit të zinxhirit të blloqeve.
Server Flask: Një server i thjeshtë për të menaxhuar kërkesa HTTP (GET, POST).
Struktura e Dosjeve
blockchain.py: Ky skedar përmban implementimin e blockchain-it dhe logjikës për minimin e blloqeve.
README.md: Ky dokument që shpjegon përdorimin e projektit.
requirements.txt: Ky skedar përmban të gjitha bibliotekat e nevojshme për të ekzekutuar projektin.
Hapat për Të Përdorur Projektin
Kërkesat
Ky projekt kërkon Python 3.6+ dhe bibliotekën Flask për të krijuar API-në. Për të instaluar Flask, mund të përdorni komandën:


pip install flask
Për të instaluar të gjitha kërkesat e tjera, mund të përdorni:


pip install -r requirements.txt
Ekzekutimi i Serverit
Pasi të keni instaluar të gjitha kërkesat, mund ta filloni serverin Flask me këtë komandë:


python blockchain.py
Kjo do të nisë serverin lokal në http://127.0.0.1:5000/, i cili do të pranojë kërkesa HTTP.

API
GET /chain: Kjo kërkesë do të kthejë zinxhirin e të gjitha blloqeve të krijuara.


curl -X GET "http://127.0.0.1:5000/chain"
POST /mine: Kjo kërkesë do të minojë një bllok të ri dhe do të shtojë një transaksion të ri në blockchain.


curl -X POST http://127.0.0.1:5000/mine -H "Content-Type: application/json" -d '{"data": "Transaksioni i par"}'
GET /validate: Kjo kërkesë kontrollon nëse zinxhiri është valid.


curl -X GET "http://127.0.0.1:5000/validate"
Përdorimi i API-së me CURL
Për të parë zinxhirin:


curl -X GET "http://127.0.0.1:5000/chain"
Për të minuar një bllok të ri:


curl -X POST http://127.0.0.1:5000/mine -H "Content-Type: application/json" -d '{ "data": "Transaksioni i par" }'
Për të validuar zinxhirin:

curl -X GET "http://127.0.0.1:5000/validate"
Skedari requirements.txt
Për të instaluar të gjitha kërkesat, sigurohuni që të keni skedarin requirements.txt me përmbajtjen e mëposhtme:


flask
Testimi dhe Përdorimi
Pas ekzekutimit të serverit dhe përdorimit të komandave të sipërpërmendura, mund të testoni krijimin e blloqeve të reja, validimin e zinxhirit, dhe të mësoni si blockchain funksionon në një mjedis të thjeshtë.

Konceptet e Blockchain
Blockchain është një teknologji që ruan të dhënat në forma të blloqeve të lidhura njëri me tjetrin. Secili bllok përmban një hash, transaksionet dhe një hash të mëparshëm, që e lidh atë me bllokun e mëparshëm.

Proof of Work
Proof of Work (PoW) është një mekanizëm konsensusi që përdoret për të validuar dhe për të minuar blloqe të reja në blockchain. Ky mekanizëm kërkon që të bëhet një llogaritje e vështirë për të krijuar një hash që i përmbahet një kriteri të caktuar (p.sh., një numër i caktuar zero-sh në fillim të hash-it).

Konkluzion
Ky projekt është një shembull i thjeshtë për të kuptuar bazat e teknologjisë Blockchain.                                                                            
