# CLAUDE.md – proto_restatify-tensegrity-ai

Protobuf-Contracts `tensegrity.v1`. Fachliche Referenz: Docs-Repo (Whitepaper V1.0.26, ADRs).

## Regeln
- Jede Änderung mit dem Skill `proto-contract`; `buf lint` und `buf breaking` müssen grün sein.
- Vertraulichkeitsstufe ist in jeder Nachricht, die Gerätedaten transportiert, ein Pflichtfeld.
- Keine Freitext-Felder für Streng-geheim-Strukturmeldungen – nur Kategorie-IDs aus der Hive-Liste.
- Kommentare in den `.proto`-Dateien auf Englisch, knapp.
- Kein `git push` ohne Freigabe.
