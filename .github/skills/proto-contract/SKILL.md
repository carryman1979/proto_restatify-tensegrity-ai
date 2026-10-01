---
name: proto-contract
description: "Use when adding or changing Tensegrity AI protobuf contracts (tensegrity.v1 inference, feedback, federation, release, admin, exchange), checking breaking changes with buf, or regenerating Rust/Python/C# code. Keywords: proto, protobuf, contract, schnittstelle, buf, grpc, breaking change, codegen."
---
# Proto-Contract ändern

1. Änderung begründen (REQ-/ADR-ID); bei neuem Datenfluss nach außen Security & Privacy Officer einbinden.
2. Datei unter `proto/tensegrity/v1/<paket>.proto` bearbeiten.
   - Neue Felder mit neuen Nummern; entfernte Felder als `reserved`.
   - Nachrichten mit Gerätedaten: `ConfidentialityLevel level` Pflicht.
   - Streng geheim: nur `category_id`, keine Freitexte, keine Gewichte.
3. `buf lint` und `buf breaking --against '.git#branch=main'` ausführen.
4. Code generieren (`buf generate`) und Konsumenten-Repos (core, hive, cloud, app) anpassen.
5. Contract-Tests in den Konsumenten (Integrationsstufe) ergänzen.
6. Version taggen (Release Manager) – erst nach Freigabe pushen.
