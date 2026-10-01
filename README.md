# proto_restatify-tensegrity-ai

Protobuf-Contracts **`tensegrity.v1`** für Tensegrity AI – die einzige Quelle der Wahrheit für alle Schnittstellen
zwischen Core, Hive, Cloud-Backend und App.

| Paket | Zweck | Anbieter → Nutzer |
|---|---|---|
| `tensegrity.v1.inference` | Generierung, Streaming, Experten-Auswahl | Cloud → App (WASM) |
| `tensegrity.v1.feedback` | Daumen hoch/runter, Korrektur mit Beleg, positive Rückmeldung | App/Cloud → Hive |
| `tensegrity.v1.federation` | Einreichung gefalteter Deltas und Strukturmeldungen | Core → Hive |
| `tensegrity.v1.release` | Update-Request, Delta-Pakete, TUF-Metadaten | Hive/Peer → Core |
| `tensegrity.v1.admin` | Trust, Blacklist, Richtlinien, Slot-Registry | Admin → Hive |
| `tensegrity.v1.exchange` | Import/Export zwischen Hives (online, Datenträger) | Hive ↔ Hive-Klon |

Die `.proto`-Dateien entstehen in Phase 1 (siehe Roadmap im Docs-Repo).

## Werkzeuge

- [buf](https://buf.build/) für Lint, Breaking-Change-Prüfung und Codegenerierung (Rust/prost, Python, C#).
- Regeln: keine Feldnummern wiederverwenden, nur additive Änderungen in `v1`, Breaking Changes → `v2`.

## Dokumentation

Siehe [docs_restatify-tensegrity-ai](https://github.com/carryman1979/docs_restatify-tensegrity-ai).

## Lizenz

Apache License 2.0 – siehe [LICENSE](LICENSE).
